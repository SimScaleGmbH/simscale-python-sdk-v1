#!/usr/bin/env python
"""Pedestrian Wind Comfort (PWC) example using the SimScale SDK v1."""

import zipfile
from pathlib import Path

from simscale_sdk_v1 import SimScaleOperationError, SimScaleSDK, models
from simscale_sdk_v1.models import reporting as rpt
from simscale_sdk_v1.models import simulation as sim

EXAMPLE_DIR = Path(__file__).resolve().parent

sdk = SimScaleSDK()

# Create project
project = sdk.projects.create_project(
    models.Project(
        name="Pedestrian Wind Comfort via Python SDK",
        description="Pedestrian Wind Comfort via Python SDK",
        measurement_system="SI",
    ),
)
project_id = project.project_id
print(f"project_id: {project_id}")

# Upload and import CAD
storage = sdk.upload(EXAMPLE_DIR / "fixtures/Cylinder.stl")
cad_import = sdk.cad_imports.import_cad(
    project_id,
    models.CadImportRequest(
        name="Cylinder",
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

# The wind data can be user-defined or obtained from the Wind API, as shown in the following two examples:

# 1. User-defined wind data for simulation spec
wind_rose = sim.WindRose(
    num_directions=4,
    velocity_buckets=[
        sim.WindRoseVelocityBucket(from_=None, to=1.234, fractions=[0.1, 0.1, 0.1, 0.1]),
        sim.WindRoseVelocityBucket(from_=1.234, to=2.345, fractions=[0.0, 0.1, 0.1, 0.1]),
        sim.WindRoseVelocityBucket(from_=2.345, to=3.456, fractions=[0.0, 0.0, 0.1, 0.1]),
        sim.WindRoseVelocityBucket(from_=3.456, to=None, fractions=[0.0, 0.0, 0.0, 0.1]),
    ],
    velocity_unit="m/s",
    exposure_categories=["EC4", "EC4", "EC4", "EC4"],
    wind_engineering_standard="EU",
    wind_data_source="USER_UPLOAD",
    add_surface_roughness=False,
)

# 2. Get wind data from the Wind API for simulation spec
wind_rose_response = sdk.wind.get_wind_data(latitude="48.135125", longitude="11.581981")
wind_rose = wind_rose_response.wind_rose
wind_rose.num_directions = 4
wind_rose.exposure_categories = ["EC4"] * wind_rose.num_directions
wind_rose.wind_engineering_standard = "EU"
wind_rose.add_surface_roughness = False

# Create simulation spec
model = sim.WindComfort(
    region_of_interest=sim.RegionOfInterest(
        disc_radius=sim.Dimensional_Length(value=100, unit="m"),
        center_point=sim.DimensionalVector2d_Length(value=sim.DecimalVector2d(x=0, y=0), unit="m"),
        ground_height=sim.Dimensional_Length(value=0, unit="m"),
        north_angle=sim.Dimensional_Angle(value=0, unit="°"),
        advanced_settings=sim.AdvancedROISettings(wind_tunnel_size=sim.WindTunnelSizeModerate()),
    ),
    wind_conditions=sim.WindConditions(
        geographical_location=sim.GeographicalLocation(
            latitude=sim.Dimensional_Angle(value=48.135125, unit="°"),
            longitude=sim.Dimensional_Angle(value=11.581981, unit="°"),
        ),
        wind_rose=wind_rose,
    ),
    pedestrian_comfort_map=[
        sim.PedestrianComfortSurface(
            name="Pedestrian level 1",
            height_above_ground=sim.Dimensional_Length(value=1.5, unit="m"),
            ground=sim.GroundAbsolute(),
        )
    ],
    simulation_control=sim.WindComfortSimulationControl(
        max_direction_run_time=sim.Dimensional_Time(value=10000, unit="s"),
        number_of_fluid_passes=0.2,
    ),
    advanced_modelling=sim.AdvancedModelling(),
    additional_result_export=sim.FluidResultControls(
        transient_result_control=sim.TransientResultControl(
            write_control=sim.CoarseResolution(),
            fraction_from_end=0.1,
        ),
        statistical_averaging_result_control=sim.StatisticalAveragingResultControlV2(
            sampling_interval=sim.CoarseResolution(),
            fraction_from_end=0.1,
        ),
    ),
    mesh_settings=sim.WindComfortMesh(wind_comfort_fineness=sim.PacefishFinenessVeryCoarse()),
)

simulation = sdk.simulations.create_simulation(
    project_id,
    models.SimulationSpec(
        name="Pedestrian Wind Comfort via Python SDK",
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

# Export and download statistical surface solution results
results = sdk.simulation_runs.get_simulation_run_results(
    project_id, simulation_id, run_id, category="STATISTICAL_SURFACE_SOLUTION"
)
statistical_surface_solution = results.embedded[0]
export_format = statistical_surface_solution.available_export_formats[0]
export = sdk.export.create_export(
    project_id, models.CreateExportRequest(result_id=statistical_surface_solution.result_id, format=export_format)
)
export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, export.export_id), interval=5)
solution_zip = EXAMPLE_DIR / "statistical_surface_solution.zip"
sdk.download(export.url, solution_zip)
print(f"Statistical surface solution ZIP content: {zipfile.ZipFile(solution_zip).namelist()}")

# Generate and download screenshot report
report = sdk.reports.create_report(
    project_id,
    rpt.ReportRequest(
        name="Report 1",
        description="Simulation report",
        result_ids=[statistical_surface_solution.result_id],
        report_properties=rpt.ScreenshotReportProperties(
            model_settings=rpt.ModelSettings(
                parts=[
                    rpt.Part(part_identifier="solid 1 input - group-all-volumes"),
                    rpt.Part(part_identifier="Pedestrian level 1"),
                ],
            ),
            camera_settings=rpt.TopViewPredefinedCameraSettings(
                projection_type="ORTHOGONAL",
                direction_specifier="Z_NEGATIVE",
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

# Additional wind data: reuse directional results with updated simulation spec
# This is optional — useful when running the same simulation with different wind data.
# Only the statistical surface solution is re-calculated; directional results are reused.
simulation_spec = sdk.simulations.get_simulation(project_id, simulation_id)
simulation_spec.model.pedestrian_comfort_map[0].height_above_ground = sim.Dimensional_Length(value=1.8, unit="m")
simulation_spec.name = "Pedestrian Wind Comfort with additional data"
sdk.simulations.update_simulation(project_id, simulation_id, simulation_spec)

additional_run = sdk.simulation_runs.add_wind_data_to_simulation_run(
    project_id, simulation_id, run_id, models.WindData(name="Additional wind rose run")
)
additional_run_id = additional_run.run_id
additional_run = sdk.wait_until_done(
    lambda: sdk.simulation_runs.get_simulation_run(project_id, simulation_id, additional_run_id),
    timeout=max_runtime,
)

# Export and download updated statistical surface solution
updated_results = sdk.simulation_runs.get_simulation_run_results(
    project_id, simulation_id, additional_run_id, category="STATISTICAL_SURFACE_SOLUTION"
)
updated_solution = updated_results.embedded[0]
updated_export_format = updated_solution.available_export_formats[0]
updated_export = sdk.export.create_export(
    project_id, models.CreateExportRequest(result_id=updated_solution.result_id, format=updated_export_format)
)
updated_export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, updated_export.export_id), interval=5)
updated_zip = EXAMPLE_DIR / "statistical_surface_solution_2.zip"
sdk.download(updated_export.url, updated_zip)
print(f"Updated statistical surface solution ZIP content: {zipfile.ZipFile(updated_zip).namelist()}")

print("\nDone!")
