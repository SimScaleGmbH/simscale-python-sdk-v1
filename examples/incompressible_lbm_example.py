#!/usr/bin/env python
"""Incompressible LBM (Pacefish) example using the SimScale SDK v1."""

import zipfile
from pathlib import Path

from simscale_sdk_v1 import SimScaleOperationError, SimScaleSDK, models
from simscale_sdk_v1.models import geometry_primitive as geo
from simscale_sdk_v1.models import reporting as rpt
from simscale_sdk_v1.models import simulation as sim

EXAMPLE_DIR = Path(__file__).resolve().parent

sdk = SimScaleSDK()

# Create project
project = sdk.projects.create_project(
    models.Project(
        name="Incompressible LBM via Python SDK",
        description="Incompressible LBM via Python SDK",
        measurement_system="SI",
    ),
)
project_id = project.project_id
print(f"project_id: {project_id}")

# Upload and import CAD
storage = sdk.upload(EXAMPLE_DIR / "fixtures/Shapes.stl")
cad_import = sdk.cad_imports.import_cad(
    project_id,
    models.CadImportRequest(
        name="Shapes",
        location=models.CadImportRequestLocation(storage_id=storage.storage_id),
        format="STL",
        input_unit="m",
        options=models.CadImportRequestOptions(
            facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=True
        ),
    ),
)
cad_id = cad_import.cad_id
cad_import = sdk.wait_until_done(lambda: sdk.cad_imports.get_imported_cad(project_id, cad_id), timeout=900, interval=10)
cad_state_id = cad_import.cad_state_id
print(f"cad_id: {cad_id}, cad_state_id: {cad_state_id}")

# Get CAD topology mappings for faces
topology = sdk.cads.get_cad_topology(cad_id, cad_state_id, class_="face", entities=["Cylinder", "Cube 2", "Sphere"])
entities = [entity.name for entity in topology.embedded]
print(f"entities: {entities}")

# Upload and import table: Probe Points
probe_points_storage = sdk.upload(EXAMPLE_DIR / "fixtures/ProbePoints.csv")
probe_points_table = sdk.table_imports.import_table(
    project_id,
    models.TableImportRequest(location=models.TableImportRequestLocation(storage_id=probe_points_storage.storage_id)),
)
probe_points_table_id = probe_points_table.table_id

# Upload and import table: Inlet Profile
inlet_profile_storage = sdk.upload(EXAMPLE_DIR / "fixtures/InletProfile.csv")
inlet_profile_table = sdk.table_imports.import_table(
    project_id,
    models.TableImportRequest(location=models.TableImportRequestLocation(storage_id=inlet_profile_storage.storage_id)),
)
inlet_profile_table_id = inlet_profile_table.table_id

# Create geometry primitives
external_flow_domain = sdk.simulations.create_geometry_primitive(
    project_id,
    geo.RotatableCartesianBox(
        name="External Flow Domain",
        min=geo.DimensionalVector_Length(value=geo.DecimalVector(x=-350, y=-100, z=0), unit="m"),
        max=geo.DimensionalVector_Length(value=geo.DecimalVector(x=650, y=100, z=300), unit="m"),
        rotation_point=geo.DimensionalVector_Length(value=geo.DecimalVector(x=0, y=0, z=0), unit="m"),
        rotation_angles=geo.DimensionalVector_Angle(value=geo.DecimalVector(x=0, y=0, z=0), unit="°"),
    ),
)
external_flow_domain_uuid = external_flow_domain.geometry_primitive_id

mesh_region = sdk.simulations.create_geometry_primitive(
    project_id,
    geo.LocalCartesianBox(
        name="Mesh Region",
        orientation_reference="GEOMETRY",
        min=geo.DimensionalVector_Length(value=geo.DecimalVector(x=-30, y=-30, z=0), unit="m"),
        max=geo.DimensionalVector_Length(value=geo.DecimalVector(x=30, y=30, z=120), unit="m"),
    ),
)
mesh_region_uuid = mesh_region.geometry_primitive_id

# Define simulation spec
model = sim.IncompressiblePacefish(
    bounding_box_uuid=external_flow_domain_uuid,
    flow_domain_boundaries=sim.FlowDomainBoundaries(
        xmin=sim.VelocityInletBC(
            name="Velocity inlet (A)",
            velocity=sim.FixedMagnitudeVBC(
                value=sim.DimensionalFunction_Speed(
                    value=sim.TableDefinedFunction(
                        table_id=inlet_profile_table_id,
                        result_index=[2],
                        independent_variables=[sim.TableFunctionParameter(reference=1, parameter="HEIGHT", unit="m")],
                    ),
                    unit="m/s",
                )
            ),
            turbulence_intensity=sim.TurbulenceIntensityTIBC(
                value=sim.DimensionalFunction_Dimensionless(value=sim.ConstantFunction(value=0.015), unit="")
            ),
            dissipation_type=sim.CustomOmegaDissipation(
                value=sim.DimensionalFunction_SpecificTurbulenceDissipationRate(
                    value=sim.TableDefinedFunction(
                        table_id=inlet_profile_table_id,
                        result_index=[3],
                        independent_variables=[sim.TableFunctionParameter(reference=1, parameter="HEIGHT", unit="m")],
                    ),
                    unit="1/s",
                )
            ),
        ),
        xmax=sim.PressureOutletBC(name="Pressure outlet (B)"),
        ymin=sim.WallBC(name="Side (C)", velocity=sim.SlipVBC()),
        ymax=sim.WallBC(name="Side (D)", velocity=sim.SlipVBC()),
        zmin=sim.WallBC(
            name="Ground (E)",
            velocity=sim.NoSlipVBC(
                no_slip_wall_roughness_type=sim.NoSlipWallEquivalentSandRoughness(
                    surface_roughness=sim.Dimensional_Length(value=0, unit="m")
                )
            ),
        ),
        zmax=sim.WallBC(name="Top (F)", velocity=sim.SlipVBC()),
    ),
    simulation_control=sim.FluidSimulationControl(
        end_time=sim.Dimensional_Time(value=5, unit="s"),
    ),
    advanced_modelling=sim.AdvancedModelling(),
    result_control=sim.FluidResultControls(
        forces_moments=[
            sim.ForcesMomentsResultControl(
                name="Forces and moments 1",
                center_of_rotation=sim.DimensionalVector_Length(value=sim.DecimalVector(x=0, y=0, z=0), unit="m"),
                write_control=sim.HighResolution(),
                export_statistics=False,
                group_assignments=False,
                topological_reference=sim.TopologicalReference(entities=entities),
            ),
            sim.ForcesMomentsResultControl(
                name="Forces and moments 2",
                center_of_rotation=sim.DimensionalVector_Length(value=sim.DecimalVector(x=0, y=0, z=0), unit="m"),
                write_control=sim.HighResolution(),
                fraction_from_end=0.3,
                topological_reference=sim.TopologicalReference(entities=entities),
            ),
        ],
        probe_points=[
            sim.ProbePointsResultControl(
                name="Probe point 1",
                write_control=sim.ModerateResolution(),
                probe_locations=sim.TableDefinedProbeLocations(table_id=probe_points_table_id),
            )
        ],
        transient_result_control=sim.TransientResultControl(
            write_control=sim.CoarseResolution(),
            export_fluid=True,
            geometry_primitive_uuids=[external_flow_domain_uuid],
        ),
        statistical_averaging_result_control=sim.StatisticalAveragingResultControlV2(
            sampling_interval=sim.CoarseResolution(),
            export_fluid=True,
            geometry_primitive_uuids=[external_flow_domain_uuid],
            export_surface=True,
            topological_reference=sim.TopologicalReference(entities=entities),
        ),
        snapshot_result_control=sim.SnapshotResultControl(
            export_fluid=True,
            geometry_primitive_uuids=[external_flow_domain_uuid],
        ),
    ),
    mesh_settings_new=sim.PacefishAutomesh(
        new_fineness=sim.PacefishFinenessCoarse(),
        reference_length_computation=sim.AutomaticReferenceLength(),
        primary_topology=sim.Region(geometry_primitive_uuids=[mesh_region_uuid]),
    ),
)

simulation = sdk.simulations.create_simulation(
    project_id,
    models.SimulationSpec(
        name="Incompressible LBM via Python SDK",
        cad_id=cad_id,
        state_id=cad_state_id,
        model=model,
    ),
)
simulation_id = simulation.simulation_id
print(f"simulation_id: {simulation_id}")

# Check simulation setup
check = sdk.simulations.check_simulation_setup(project_id, simulation_id)
warnings = [entry for entry in check.entries if entry.severity == "WARNING"]
print(f"Simulation check warnings: {len(warnings)}")
if any(e.severity == "ERROR" for e in check.entries):
    raise SimScaleOperationError(check, "Simulation setup check failed")

# Estimate simulation
max_runtime = 36000
estimation = sdk.simulations.estimate_simulation_setup(project_id, simulation_id)
print(f"Simulation estimation: {estimation}")
if estimation.compute_resource is not None and estimation.compute_resource.value > 10.0:
    raise Exception("Too expensive", estimation)

# Create simulation run, start, and wait
simulation_run = sdk.simulation_runs.create_simulation_run(
    project_id, simulation_id, models.SimulationRun(name="Run 1")
)
run_id = simulation_run.run_id
print(f"run_id: {run_id}")
sdk.simulation_runs.start_simulation_run(project_id, simulation_id, run_id)
simulation_run = sdk.wait_until_done(
    lambda: sdk.simulation_runs.get_simulation_run(project_id, simulation_id, run_id),
    timeout=max_runtime,
)

# Export and download probe point statistical data
probe_points_results = sdk.simulation_runs.get_simulation_run_results(
    project_id, simulation_id, run_id, category="PROBE_POINT_PLOT_STATISTICAL_DATA"
)
probe_result = probe_points_results.embedded[0]
export = sdk.export.create_export(
    project_id, models.CreateExportRequest(result_id=probe_result.result_id, format="CSV")
)
export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, export.export_id), interval=5)
probe_csv = EXAMPLE_DIR / "probe_points.csv"
sdk.download(export.url, probe_csv)
print(f"Downloaded {probe_csv} ({probe_csv.stat().st_size} bytes)")

# Export and download averaged solution fields
averaged_solution_results = sdk.simulation_runs.get_simulation_run_results(
    project_id, simulation_id, run_id, category="AVERAGED_SOLUTION"
)
averaged_solution = averaged_solution_results.embedded[0]
export_format = averaged_solution.available_export_formats[0]
export = sdk.export.create_export(
    project_id, models.CreateExportRequest(result_id=averaged_solution.result_id, format=export_format)
)
export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, export.export_id), interval=5)
averaged_solution_zip = EXAMPLE_DIR / "averaged_solution.zip"
sdk.download(export.url, averaged_solution_zip)
print(f"Averaged solution ZIP content: {zipfile.ZipFile(averaged_solution_zip).namelist()}")

# Generate and download screenshot report
report = sdk.reports.create_report(
    project_id,
    rpt.ReportRequest(
        name="Report 1",
        description="Simulation report",
        result_ids=[averaged_solution.result_id],
        report_properties=rpt.ScreenshotReportProperties(
            model_settings=rpt.ModelSettings(
                parts=[],
                scalar_field=rpt.ScalarField(field_name="Velocity", component="Magnitude", data_type="CELL"),
            ),
            filters=rpt.Filters(
                cutting_planes=[
                    rpt.CuttingPlane(
                        name="velocity-plane",
                        scalar_field=rpt.ScalarField(field_name="Velocity", component="Magnitude", data_type="CELL"),
                        center=rpt.Vector3D(x=150, y=0, z=150),
                        normal=rpt.Vector3D(x=0, y=1, z=0),
                        opacity=1,
                        clipping=True,
                        render_mode="SURFACES",
                    )
                ]
            ),
            camera_settings=rpt.TopViewPredefinedCameraSettings(
                projection_type="ORTHOGONAL",
                direction_specifier="Y_POSITIVE",
            ),
            output_settings=rpt.ScreenshotOutputSettings(
                name="Output 1",
                format="PNG",
                resolution=rpt.ResolutionInfo(x=1440, y=1080),
                frame_index=0,
                show_legend=True,
                show_cube=False,
            ),
        ),
    ),
)
report_id = report.report_id
print(f"Starting report with ID {report_id}")
sdk.reports.start_report_job(project_id, report_id)
report = sdk.wait_until_done(lambda: sdk.reports.get_report(project_id, report_id))
report_file = EXAMPLE_DIR / f"report.{report.download.format}"
sdk.download(report.download.url, report_file)
print(f"Downloaded report: {report_file}")

print("\nDone!")
