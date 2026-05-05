#!/usr/bin/env python
"""Incompressible CFD example using the SimScale SDK v1."""

import zipfile
from pathlib import Path

from simscale_sdk_v1 import SimScaleOperationError, SimScaleSDK, models
from simscale_sdk_v1.models import geometry_primitive as geo
from simscale_sdk_v1.models import meshing as mesh
from simscale_sdk_v1.models import reporting as rpt
from simscale_sdk_v1.models import simulation as sim

EXAMPLE_DIR = Path(__file__).resolve().parent

sdk = SimScaleSDK()

# Create project
project = sdk.projects.create_project(
    models.Project(
        name="Incompressible via Python SDK",
        description="Incompressible via Python SDK",
        measurement_system="SI",
    ),
)
project_id = project.project_id
print(f"project_id: {project_id}")

# Upload and import CAD
storage = sdk.upload(EXAMPLE_DIR / "fixtures/pipe_junction_model_tutorial.x_t")
cad_import = sdk.cad_imports.import_cad(
    project_id,
    models.CadImportRequest(
        name="CAD-pipe-junction_v1",
        location=models.CadImportRequestLocation(storage_id=storage.storage_id),
        format="PARASOLID",
        input_unit="m",
        options=models.CadImportRequestOptions(
            facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=False
        ),
    ),
)
cad_id = cad_import.cad_id
cad_import = sdk.wait_until_done(lambda: sdk.cad_imports.get_imported_cad(project_id, cad_id), timeout=900, interval=10)
cad_state_id = cad_import.cad_state_id
print(f"cad_id: {cad_id}, cad_state_id: {cad_state_id}")


# Get CAD topology mappings
def get_single_entity_name(cad_id, cad_state_id, **kwargs):
    entities = sdk.cads.get_cad_topology(cad_id, cad_state_id, **kwargs).embedded
    if len(entities) == 1:
        return entities[0].name
    else:
        raise ValueError(f"Found {len(entities)} entities instead of 1: {entities}")


material_entity = get_single_entity_name(cad_id, cad_state_id, attributes=["SDL/TYSA_NAME"], values=["Fluid Region"])
inlet1_entity = get_single_entity_name(cad_id, cad_state_id, attributes=["SDL/TYSA_NAME"], values=["Face ZMAX"])
inlet2_entity = get_single_entity_name(cad_id, cad_state_id, attributes=["SDL/TYSA_NAME"], values=["Face Junction"])
outlet_entity = get_single_entity_name(cad_id, cad_state_id, attributes=["SDL/TYSA_NAME"], values=["Face YMAX"])

# Create geometry primitive (probe point)
geometry_primitive = sdk.simulations.create_geometry_primitive(
    project_id,
    geo.Point(
        name="Point 1",
        center=geo.DimensionalVector_Length(
            value=geo.DecimalVector(x=0.0035744310360600745, y=0.4499999880790711, z=-0.4507558972231502),
            unit="m",
        ),
    ),
)
geometry_primitive_uuid = geometry_primitive.geometry_primitive_id

# Create simulation spec
model = sim.Incompressible(
    turbulence_model="KOMEGASST",
    algorithm="SIMPLE",
    num_of_passive_species=0,
    model=sim.FluidModel(),
    initial_conditions=sim.FluidInitialConditions(),
    advanced_concepts=sim.AdvancedConcepts(),
    materials=sim.IncompressibleFluidMaterials(),
    numerics=sim.FluidNumerics(
        relaxation_factor=sim.RelaxationFactor(),
        pressure_reference_value=sim.Dimensional_Pressure(value=0, unit="Pa"),
        residual_controls=sim.ResidualControls(
            velocity=sim.Tolerance(),
            pressure=sim.Tolerance(),
            turbulent_kinetic_energy=sim.Tolerance(),
            omega_dissipation_rate=sim.Tolerance(),
        ),
        solvers=sim.FluidSolvers(),
        schemes=sim.Schemes(
            time_differentiation=sim.TimeDifferentiationSchemes(),
            gradient=sim.GradientSchemes(),
            divergence=sim.DivergenceSchemes(),
            laplacian=sim.LaplacianSchemes(),
            interpolation=sim.InterpolationSchemes(),
            surface_normal_gradient=sim.SurfaceNormalGradientSchemes(),
        ),
    ),
    boundary_conditions=[
        sim.VelocityInletBC(
            name="Velocity inlet 1",
            velocity=sim.FixedValueVBC(
                value=sim.DimensionalVectorFunction_Speed(
                    unit="m/s",
                    value=sim.ComponentVectorFunction(
                        x=sim.ConstantFunction(value=0),
                        y=sim.ConstantFunction(value=0),
                        z=sim.ConstantFunction(value=-1.5),
                    ),
                )
            ),
            topological_reference=sim.TopologicalReference(entities=[inlet1_entity]),
        ),
        sim.VelocityInletBC(
            name="Velocity inlet 2",
            velocity=sim.FixedValueVBC(
                value=sim.DimensionalVectorFunction_Speed(
                    unit="m/s",
                    value=sim.ComponentVectorFunction(
                        x=sim.ConstantFunction(value=0),
                        y=sim.ConstantFunction(value=-1),
                        z=sim.ConstantFunction(value=0),
                    ),
                )
            ),
            topological_reference=sim.TopologicalReference(entities=[inlet2_entity]),
        ),
        sim.PressureOutletBC(
            name="Pressure outlet 3",
            gauge_pressure=sim.FixedValuePBC(
                value=sim.DimensionalFunction_Pressure(value=sim.ConstantFunction(value=0), unit="Pa")
            ),
            topological_reference=sim.TopologicalReference(entities=[outlet_entity]),
        ),
    ],
    simulation_control=sim.FluidSimulationControl(
        end_time=sim.Dimensional_Time(value=100, unit="s"),
        delta_t=sim.Dimensional_Time(value=1, unit="s"),
        write_control=sim.TimeStepWriteControl(write_interval=20),
        max_run_time=sim.Dimensional_Time(value=10000, unit="s"),
        decompose_algorithm=sim.ScotchDecomposeAlgorithm(),
    ),
    result_control=sim.FluidResultControls(
        probe_points=[
            sim.ProbePointsResultControl(
                name="Probe point 1",
                write_control=sim.TimeStepWriteControl(write_interval=1),
                geometry_primitive_uuids=[geometry_primitive_uuid],
            )
        ]
    ),
)

simulation = sdk.simulations.create_simulation(
    project_id,
    models.SimulationSpec(
        name="Incompressible via Python SDK",
        cad_id=cad_id,
        state_id=cad_state_id,
        model=model,
    ),
)
simulation_id = simulation.simulation_id
print(f"simulation_id: {simulation_id}")

# Add material and assign to fluid region
material_data = sdk.get_material("Water")
sdk.simulations.update_simulation_materials(
    project_id,
    simulation_id,
    models.MaterialUpdateRequest(
        operations=[
            models.MaterialUpdateOperation(
                path="/materials/fluids",
                material_data=material_data,
            )
        ]
    ),
)
simulation_spec = sdk.simulations.get_simulation(project_id, simulation_id)
simulation_spec.model.materials.fluids[0].topological_reference = sim.TopologicalReference(entities=[material_entity])
sdk.simulations.update_simulation(project_id, simulation_id, simulation_spec)

# Create, check, and run mesh operation
mesh_operation = sdk.mesh_operations.create_mesh_operation(
    project_id,
    models.MeshOperation(
        name="Pipe junction mesh",
        cad_id=cad_id,
        state_id=cad_state_id,
        model=mesh.SimmetrixMeshingFluid(
            physics_based_meshing=True,
            automatic_layer_settings=mesh.AutomaticLayerOn(),
        ),
    ),
)
mesh_operation_id = mesh_operation.mesh_operation_id
print(f"mesh_operation_id: {mesh_operation_id}")
mesh_check = sdk.mesh_operations.check_mesh_operation_setup(project_id, mesh_operation_id, simulation_id=simulation_id)
if any(e.severity == "ERROR" for e in mesh_check.entries):
    raise SimScaleOperationError(mesh_check, "Mesh setup check failed")
sdk.mesh_operations.start_mesh_operation(project_id, mesh_operation_id, simulation_id=simulation_id)
mesh_operation = sdk.wait_until_done(
    lambda: sdk.mesh_operations.get_mesh_operation(project_id, mesh_operation_id),
)
print(f"Meshing finished. mesh_id: {mesh_operation.mesh_id}")

# Assign mesh to simulation
simulation_spec = sdk.simulations.get_simulation(project_id, simulation_id)
simulation_spec.mesh_id = mesh_operation.mesh_id
sdk.simulations.update_simulation(project_id, simulation_id, simulation_spec)

# Check simulation setup and run
check = sdk.simulations.check_simulation_setup(project_id, simulation_id)
if any(e.severity == "ERROR" for e in check.entries):
    raise SimScaleOperationError(check, "Simulation setup check failed")
simulation_run = sdk.simulation_runs.create_simulation_run(
    project_id, simulation_id, models.SimulationRun(name="Run 1")
)
run_id = simulation_run.run_id
print(f"run_id: {run_id}")
sdk.simulation_runs.start_simulation_run(project_id, simulation_id, run_id)
simulation_run = sdk.wait_until_done(
    lambda: sdk.simulation_runs.get_simulation_run(project_id, simulation_id, run_id),
)

# Export and download probe point results
probe_point_results = sdk.simulation_runs.get_simulation_run_results(
    project_id, simulation_id, run_id, category="PROBE_POINT_PLOT"
)
export = sdk.export.create_export(
    project_id, models.CreateExportRequest(result_id=probe_point_results.embedded[0].result_id, format="CSV")
)
export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, export.export_id), interval=5)
probe_csv = EXAMPLE_DIR / "probe_points.csv"
sdk.download(export.url, probe_csv)
print(f"Downloaded {probe_csv} ({probe_csv.stat().st_size} bytes)")

# Export and download solution fields
solution_results = sdk.simulation_runs.get_simulation_run_results(
    project_id, simulation_id, run_id, category="SOLUTION"
)
solution_result = solution_results.embedded[0]
export = sdk.export.create_export(
    project_id, models.CreateExportRequest(result_id=solution_result.result_id, format="OPEN_FOAM")
)
export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, export.export_id), interval=5)
solution_zip = EXAMPLE_DIR / "solution.zip"
sdk.download(export.url, solution_zip)
print(f"Solution ZIP content: {zipfile.ZipFile(solution_zip).namelist()}")

# Generate and download animation report
report = sdk.reports.create_report(
    project_id,
    rpt.ReportRequest(
        name="Report 1",
        description="Simulation report",
        result_ids=[solution_result.result_id],
        report_properties=rpt.AnimationReportProperties(
            model_settings=rpt.ModelSettings(
                parts=[],
                scalar_field=rpt.ScalarField(field_name="Velocity", component="Magnitude", data_type="CELL"),
            ),
            filters=rpt.Filters(
                cutting_planes=[
                    rpt.CuttingPlane(
                        name="velocity-plane",
                        scalar_field=rpt.ScalarField(field_name="Velocity", component="Magnitude", data_type="CELL"),
                        center=rpt.Vector3D(x=0, y=0, z=0),
                        normal=rpt.Vector3D(x=1, y=0, z=0),
                        opacity=1,
                        clipping=True,
                        render_mode="SURFACES",
                    )
                ]
            ),
            camera_settings=rpt.TopViewPredefinedCameraSettings(
                projection_type="ORTHOGONAL",
                direction_specifier="X_POSITIVE",
            ),
            output_settings=rpt.TimeStepAnimationOutputSettings(
                name="Output 1",
                format="MP4",
                resolution=rpt.ResolutionInfo(x=1440, y=1080),
                from_frame_index=0,
                to_frame_index=5,
                skip_frames=0,
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
