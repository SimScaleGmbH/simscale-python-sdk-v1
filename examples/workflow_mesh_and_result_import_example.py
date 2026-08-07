#!/usr/bin/env python
"""Mesh and result import workflow example using the SimScale SDK v1."""

from pathlib import Path

from simscale_sdk_v1 import SimScaleSDK
from simscale_sdk_v1.models import CreateExportRequest, Project
from simscale_sdk_v1.models.data_repository import DomainSpecificMetadata
from simscale_sdk_v1.models.workflow_repository import CreateWorkflowRequest
from simscale_sdk_v1.models.workflow_runner import InitializeWorkflowRunRequest

EXAMPLE_DIR = Path(__file__).resolve().parent

INPUT_FILE = EXAMPLE_DIR / "fixtures/cube_with_results_ascii.vtu"
INPUT_CONTENT_TYPE = "application/octet-stream"
# Format of the uploaded data. VTK covers single-file VTU/VTM input; transient results
# assembled from a PVD collection use "PVD", MED-format meshes use "MED".
INPUT_FORMAT = "VTK"

WORKFLOW_TYPE = "simscale.ramps:mesh-and-result-import:1.3.1"
INPUT_DATA_TYPE = "simscale.ramps:general-mesh-and-fields:1.0.0"
INPUT_NAME = "generalMeshAndFields"
OUTPUT_NAME = "rampsMeshAndFields"

sdk = SimScaleSDK()

# Create project
project = sdk.projects.create_project(
    Project(
        name="Mesh and result import via Python SDK",
        description="Mesh and result import via Python SDK",
        measurement_system="SI",
    ),
)
project_id = project.project_id
print(f"project_id: {project_id}")

# Upload workflow input data
input_data_id = sdk.upload_to_data_repository(
    INPUT_FILE,
    project_id=project_id,
    data_type=INPUT_DATA_TYPE,
    content_type=INPUT_CONTENT_TYPE,
)
print(f"input_data_id: {input_data_id}")

# Declare the format of the uploaded data, so the conversion knows how to read it
sdk.data_repository.update_domain_specific_metadata(
    input_data_id,
    DomainSpecificMetadata(format=INPUT_FORMAT),
)

# Create workflow
workflow_id = sdk.workflow_repository.create_workflow(
    CreateWorkflowRequest(
        project_id=project_id,
        workflow_type_reference=WORKFLOW_TYPE,
        name="VTU mesh and result import",
        description="Import a VTU mesh and result field into SimScale.",
        input_data_map=sdk.create_non_parametric_workflow_data_map({INPUT_NAME: input_data_id}),
        configuration={},
    )
)
print(f"workflow_id: {workflow_id}")

# Initialize and start workflow run
workflow = sdk.workflow_repository.read_workflow(workflow_id)
workflow_version_id = workflow.workflow_version_id
print(f"workflow_version_id: {workflow_version_id}")

workflow_run_id = sdk.workflow_runner.initialize_workflow_run(
    InitializeWorkflowRunRequest(
        workflow_version_id=workflow_version_id,
        workflow_run_mode="REAL",
        workflow_run_name="VTU import",
    )
)
print(f"workflow_run_id: {workflow_run_id}")

sdk.workflow_runner.start_workflow_run(workflow_run_id)

workflow_run = sdk.wait_until_done(
    lambda: sdk.workflow_runner.get_workflow_run(workflow_run_id),
    interval=15,
    raise_on_failure=False,
    get_status=lambda run: run.state,
)
print(f"workflow_run_state: {workflow_run.state}")

if workflow_run.state != "SUCCEEDED":
    progress = sdk.workflow_runner.get_workflow_run_progress(workflow_run_id)
    raise RuntimeError(f"Workflow run did not succeed. State: {workflow_run.state}. Progress: {progress}")

# Resolve the workflow output data and export the RAMPS result
output_data_map = workflow_run.output_data_map
if not isinstance(output_data_map, dict):
    raise RuntimeError("Workflow run response did not contain output_data_map")

output_data_id = sdk.get_non_parametric_workflow_data_id(output_data_map, OUTPUT_NAME)
if output_data_id is None:
    raise RuntimeError(f"Output data ID for {OUTPUT_NAME} was not found")
print(f"output_data_id: {output_data_id}")

output_data_info = sdk.data_repository.get_data_info(output_data_id)
external_reference = getattr(output_data_info, "external_reference", None)
if external_reference is None:
    raise RuntimeError("Output data metadata did not contain external_reference")
print(f"ramps_result_id: {external_reference}")

export = sdk.export.create_export(
    project_id,
    CreateExportRequest(
        result_id=external_reference,
        format="VTK",
    ),
)

export = sdk.wait_until_done(lambda: sdk.export.get_export(project_id, export.export_id), interval=5)
if export.url is None:
    raise RuntimeError("Export completed without a download URL")

output_file = Path("workflow_mesh_and_result_import_result.zip")
sdk.download(export.url, output_file)
print(f"downloaded_result: {output_file}")

print("\nDone!")
