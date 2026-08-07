"""Generated models — lazy-loaded to avoid importing all files on startup."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.ai_user_model import AiUserModel
    from simscale_sdk_v1.models.available_ai_model import AvailableAiModel
    from simscale_sdk_v1.models.body_path import BodyPath
    from simscale_sdk_v1.models.cad._root import Cad
    from simscale_sdk_v1.models.cad_feature import CadFeature
    from simscale_sdk_v1.models.cad_feature_response import CadFeatureResponse
    from simscale_sdk_v1.models.cad_import_request import CadImportRequest
    from simscale_sdk_v1.models.cad_import_request_location import CadImportRequestLocation
    from simscale_sdk_v1.models.cad_import_request_options import CadImportRequestOptions
    from simscale_sdk_v1.models.cad_import_response import CadImportResponse
    from simscale_sdk_v1.models.cad_internal_format import CadInternalFormat
    from simscale_sdk_v1.models.cad_query_response import CadQueryResponse
    from simscale_sdk_v1.models.cad_state import CadState
    from simscale_sdk_v1.models.cad_topology import CadTopology
    from simscale_sdk_v1.models.cad_unit import CadUnit
    from simscale_sdk_v1.models.cads import Cads
    from simscale_sdk_v1.models.cell_count import CellCount
    from simscale_sdk_v1.models.check_response import CheckResponse
    from simscale_sdk_v1.models.collection_links import CollectionLinks
    from simscale_sdk_v1.models.collection_meta import CollectionMeta
    from simscale_sdk_v1.models.compute_resource import ComputeResource
    from simscale_sdk_v1.models.compute_resource_type import ComputeResourceType
    from simscale_sdk_v1.models.create_ai_prediction_request import CreateAiPredictionRequest
    from simscale_sdk_v1.models.create_ai_prediction_response import CreateAiPredictionResponse
    from simscale_sdk_v1.models.create_async_ai_prediction_response import CreateAsyncAiPredictionResponse
    from simscale_sdk_v1.models.create_export_request import CreateExportRequest
    from simscale_sdk_v1.models.create_export_response import CreateExportResponse
    from simscale_sdk_v1.models.create_saved_selection_request import CreateSavedSelectionRequest
    from simscale_sdk_v1.models.create_saved_selection_response import CreateSavedSelectionResponse
    from simscale_sdk_v1.models.data_id import DataId
    from simscale_sdk_v1.models.download_original_cad_response import DownloadOriginalCadResponse
    from simscale_sdk_v1.models.duration import Duration
    from simscale_sdk_v1.models.entity_attribute import EntityAttribute
    from simscale_sdk_v1.models.entity_description import EntityDescription
    from simscale_sdk_v1.models.error_response import ErrorResponse
    from simscale_sdk_v1.models.estimation import Estimation
    from simscale_sdk_v1.models.event_log_response import EventLogResponse
    from simscale_sdk_v1.models.folder import Folder
    from simscale_sdk_v1.models.geometry import Geometry
    from simscale_sdk_v1.models.geometry_import_request import GeometryImportRequest
    from simscale_sdk_v1.models.geometry_import_response import GeometryImportResponse
    from simscale_sdk_v1.models.geometry_primitive_response import GeometryPrimitiveResponse
    from simscale_sdk_v1.models.geometry_unit import GeometryUnit
    from simscale_sdk_v1.models.get_ai_models_response import GetAiModelsResponse
    from simscale_sdk_v1.models.get_ai_prediction_response import GetAiPredictionResponse
    from simscale_sdk_v1.models.get_available_ai_models_response import GetAvailableAiModelsResponse
    from simscale_sdk_v1.models.get_export_response import GetExportResponse
    from simscale_sdk_v1.models.interpolation_parameters import InterpolationParameters
    from simscale_sdk_v1.models.log_entry import LogEntry
    from simscale_sdk_v1.models.log_severity import LogSeverity
    from simscale_sdk_v1.models.material_update_operation import MaterialUpdateOperation
    from simscale_sdk_v1.models.material_update_operation_reference import MaterialUpdateOperationReference
    from simscale_sdk_v1.models.material_update_request import MaterialUpdateRequest
    from simscale_sdk_v1.models.material_update_response import MaterialUpdateResponse
    from simscale_sdk_v1.models.mesh import Mesh
    from simscale_sdk_v1.models.mesh_operation import MeshOperation
    from simscale_sdk_v1.models.mesh_operation_compute_resource import MeshOperationComputeResource
    from simscale_sdk_v1.models.move_content_request import MoveContentRequest
    from simscale_sdk_v1.models.one_of_simulation_run_result import OneOfSimulationRunResult
    from simscale_sdk_v1.models.original_entity_reference import OriginalEntityReference
    from simscale_sdk_v1.models.permission import Permission
    from simscale_sdk_v1.models.permission_level import PermissionLevel
    from simscale_sdk_v1.models.permission_scope import PermissionScope
    from simscale_sdk_v1.models.permissions import Permissions
    from simscale_sdk_v1.models.project import Project
    from simscale_sdk_v1.models.project_copy_request import ProjectCopyRequest
    from simscale_sdk_v1.models.project_permissions import ProjectPermissions
    from simscale_sdk_v1.models.rename_cad_request import RenameCadRequest
    from simscale_sdk_v1.models.rename_cad_response import RenameCadResponse
    from simscale_sdk_v1.models.report_download import ReportDownload
    from simscale_sdk_v1.models.resource_location import ResourceLocation
    from simscale_sdk_v1.models.resource_to_move import ResourceToMove
    from simscale_sdk_v1.models.saved_selection import SavedSelection
    from simscale_sdk_v1.models.saved_selection_type import SavedSelectionType
    from simscale_sdk_v1.models.sharing_control import SharingControl
    from simscale_sdk_v1.models.simulation._root import Simulation
    from simscale_sdk_v1.models.simulation_run import SimulationRun
    from simscale_sdk_v1.models.simulation_run_compute_resource import SimulationRunComputeResource
    from simscale_sdk_v1.models.simulation_run_result_category import SimulationRunResultCategory
    from simscale_sdk_v1.models.simulation_run_result_convergence_plot import SimulationRunResultConvergencePlot
    from simscale_sdk_v1.models.simulation_run_result_direction import SimulationRunResultDirection
    from simscale_sdk_v1.models.simulation_run_result_name import SimulationRunResultName
    from simscale_sdk_v1.models.simulation_run_result_plot import SimulationRunResultPlot
    from simscale_sdk_v1.models.simulation_run_result_quantity import SimulationRunResultQuantity
    from simscale_sdk_v1.models.simulation_run_result_solution import SimulationRunResultSolution
    from simscale_sdk_v1.models.simulation_run_result_table import SimulationRunResultTable
    from simscale_sdk_v1.models.simulation_run_result_type import SimulationRunResultType
    from simscale_sdk_v1.models.simulation_spec import SimulationSpec
    from simscale_sdk_v1.models.slim_mesh_operation import SlimMeshOperation
    from simscale_sdk_v1.models.space import Space
    from simscale_sdk_v1.models.space_permissions import SpacePermissions
    from simscale_sdk_v1.models.space_settings import SpaceSettings
    from simscale_sdk_v1.models.spaces import Spaces
    from simscale_sdk_v1.models.status import Status
    from simscale_sdk_v1.models.storage import Storage
    from simscale_sdk_v1.models.swap_cad_report import SwapCadReport
    from simscale_sdk_v1.models.swap_cad_request import SwapCadRequest
    from simscale_sdk_v1.models.table import Table
    from simscale_sdk_v1.models.table_data import TableData
    from simscale_sdk_v1.models.table_import_request import TableImportRequest
    from simscale_sdk_v1.models.table_import_request_location import TableImportRequestLocation
    from simscale_sdk_v1.models.table_import_response import TableImportResponse
    from simscale_sdk_v1.models.table_row import TableRow
    from simscale_sdk_v1.models.tables import Tables
    from simscale_sdk_v1.models.user import User
    from simscale_sdk_v1.models.user_signup_request import UserSignupRequest
    from simscale_sdk_v1.models.user_signup_response import UserSignupResponse
    from simscale_sdk_v1.models.wind_data import WindData
    from simscale_sdk_v1.models.wind_rose_response import WindRoseResponse
    from simscale_sdk_v1.models.workflow_id import WorkflowId
    from simscale_sdk_v1.models.workflow_run_id import WorkflowRunId
    from simscale_sdk_v1.models.workflow_version_id import WorkflowVersionId
    from simscale_sdk_v1._base import SimScaleModel

_NAMES: dict[str, tuple[str, str]] = {
    "AiUserModel": ("simscale_sdk_v1.models.ai_user_model", "AiUserModel"),
    "AvailableAiModel": ("simscale_sdk_v1.models.available_ai_model", "AvailableAiModel"),
    "BodyPath": ("simscale_sdk_v1.models.body_path", "BodyPath"),
    "Cad": ("simscale_sdk_v1.models.cad._root", "Cad"),
    "CadFeature": ("simscale_sdk_v1.models.cad_feature", "CadFeature"),
    "CadFeatureResponse": ("simscale_sdk_v1.models.cad_feature_response", "CadFeatureResponse"),
    "CadImportRequest": ("simscale_sdk_v1.models.cad_import_request", "CadImportRequest"),
    "CadImportRequestLocation": ("simscale_sdk_v1.models.cad_import_request_location", "CadImportRequestLocation"),
    "CadImportRequestOptions": ("simscale_sdk_v1.models.cad_import_request_options", "CadImportRequestOptions"),
    "CadImportResponse": ("simscale_sdk_v1.models.cad_import_response", "CadImportResponse"),
    "CadInternalFormat": ("simscale_sdk_v1.models.cad_internal_format", "CadInternalFormat"),
    "CadQueryResponse": ("simscale_sdk_v1.models.cad_query_response", "CadQueryResponse"),
    "CadState": ("simscale_sdk_v1.models.cad_state", "CadState"),
    "CadTopology": ("simscale_sdk_v1.models.cad_topology", "CadTopology"),
    "CadUnit": ("simscale_sdk_v1.models.cad_unit", "CadUnit"),
    "Cads": ("simscale_sdk_v1.models.cads", "Cads"),
    "CellCount": ("simscale_sdk_v1.models.cell_count", "CellCount"),
    "CheckResponse": ("simscale_sdk_v1.models.check_response", "CheckResponse"),
    "CollectionLinks": ("simscale_sdk_v1.models.collection_links", "CollectionLinks"),
    "CollectionMeta": ("simscale_sdk_v1.models.collection_meta", "CollectionMeta"),
    "ComputeResource": ("simscale_sdk_v1.models.compute_resource", "ComputeResource"),
    "ComputeResourceType": ("simscale_sdk_v1.models.compute_resource_type", "ComputeResourceType"),
    "CreateAiPredictionRequest": ("simscale_sdk_v1.models.create_ai_prediction_request", "CreateAiPredictionRequest"),
    "CreateAiPredictionResponse": (
        "simscale_sdk_v1.models.create_ai_prediction_response",
        "CreateAiPredictionResponse",
    ),
    "CreateAsyncAiPredictionResponse": (
        "simscale_sdk_v1.models.create_async_ai_prediction_response",
        "CreateAsyncAiPredictionResponse",
    ),
    "CreateExportRequest": ("simscale_sdk_v1.models.create_export_request", "CreateExportRequest"),
    "CreateExportResponse": ("simscale_sdk_v1.models.create_export_response", "CreateExportResponse"),
    "CreateSavedSelectionRequest": (
        "simscale_sdk_v1.models.create_saved_selection_request",
        "CreateSavedSelectionRequest",
    ),
    "CreateSavedSelectionResponse": (
        "simscale_sdk_v1.models.create_saved_selection_response",
        "CreateSavedSelectionResponse",
    ),
    "DataId": ("simscale_sdk_v1.models.data_id", "DataId"),
    "DownloadOriginalCadResponse": (
        "simscale_sdk_v1.models.download_original_cad_response",
        "DownloadOriginalCadResponse",
    ),
    "Duration": ("simscale_sdk_v1.models.duration", "Duration"),
    "EntityAttribute": ("simscale_sdk_v1.models.entity_attribute", "EntityAttribute"),
    "EntityDescription": ("simscale_sdk_v1.models.entity_description", "EntityDescription"),
    "ErrorResponse": ("simscale_sdk_v1.models.error_response", "ErrorResponse"),
    "Estimation": ("simscale_sdk_v1.models.estimation", "Estimation"),
    "EventLogResponse": ("simscale_sdk_v1.models.event_log_response", "EventLogResponse"),
    "Folder": ("simscale_sdk_v1.models.folder", "Folder"),
    "Geometry": ("simscale_sdk_v1.models.geometry", "Geometry"),
    "GeometryImportRequest": ("simscale_sdk_v1.models.geometry_import_request", "GeometryImportRequest"),
    "GeometryImportResponse": ("simscale_sdk_v1.models.geometry_import_response", "GeometryImportResponse"),
    "GeometryPrimitiveResponse": ("simscale_sdk_v1.models.geometry_primitive_response", "GeometryPrimitiveResponse"),
    "GeometryUnit": ("simscale_sdk_v1.models.geometry_unit", "GeometryUnit"),
    "GetAiModelsResponse": ("simscale_sdk_v1.models.get_ai_models_response", "GetAiModelsResponse"),
    "GetAiPredictionResponse": ("simscale_sdk_v1.models.get_ai_prediction_response", "GetAiPredictionResponse"),
    "GetAvailableAiModelsResponse": (
        "simscale_sdk_v1.models.get_available_ai_models_response",
        "GetAvailableAiModelsResponse",
    ),
    "GetExportResponse": ("simscale_sdk_v1.models.get_export_response", "GetExportResponse"),
    "InterpolationParameters": ("simscale_sdk_v1.models.interpolation_parameters", "InterpolationParameters"),
    "LogEntry": ("simscale_sdk_v1.models.log_entry", "LogEntry"),
    "LogSeverity": ("simscale_sdk_v1.models.log_severity", "LogSeverity"),
    "MaterialUpdateOperation": ("simscale_sdk_v1.models.material_update_operation", "MaterialUpdateOperation"),
    "MaterialUpdateOperationReference": (
        "simscale_sdk_v1.models.material_update_operation_reference",
        "MaterialUpdateOperationReference",
    ),
    "MaterialUpdateRequest": ("simscale_sdk_v1.models.material_update_request", "MaterialUpdateRequest"),
    "MaterialUpdateResponse": ("simscale_sdk_v1.models.material_update_response", "MaterialUpdateResponse"),
    "Mesh": ("simscale_sdk_v1.models.mesh", "Mesh"),
    "MeshOperation": ("simscale_sdk_v1.models.mesh_operation", "MeshOperation"),
    "MeshOperationComputeResource": (
        "simscale_sdk_v1.models.mesh_operation_compute_resource",
        "MeshOperationComputeResource",
    ),
    "MoveContentRequest": ("simscale_sdk_v1.models.move_content_request", "MoveContentRequest"),
    "OneOfSimulationRunResult": ("simscale_sdk_v1.models.one_of_simulation_run_result", "OneOfSimulationRunResult"),
    "OriginalEntityReference": ("simscale_sdk_v1.models.original_entity_reference", "OriginalEntityReference"),
    "Permission": ("simscale_sdk_v1.models.permission", "Permission"),
    "PermissionLevel": ("simscale_sdk_v1.models.permission_level", "PermissionLevel"),
    "PermissionScope": ("simscale_sdk_v1.models.permission_scope", "PermissionScope"),
    "Permissions": ("simscale_sdk_v1.models.permissions", "Permissions"),
    "Project": ("simscale_sdk_v1.models.project", "Project"),
    "ProjectCopyRequest": ("simscale_sdk_v1.models.project_copy_request", "ProjectCopyRequest"),
    "ProjectPermissions": ("simscale_sdk_v1.models.project_permissions", "ProjectPermissions"),
    "RenameCadRequest": ("simscale_sdk_v1.models.rename_cad_request", "RenameCadRequest"),
    "RenameCadResponse": ("simscale_sdk_v1.models.rename_cad_response", "RenameCadResponse"),
    "ReportDownload": ("simscale_sdk_v1.models.report_download", "ReportDownload"),
    "ResourceLocation": ("simscale_sdk_v1.models.resource_location", "ResourceLocation"),
    "ResourceToMove": ("simscale_sdk_v1.models.resource_to_move", "ResourceToMove"),
    "SavedSelection": ("simscale_sdk_v1.models.saved_selection", "SavedSelection"),
    "SavedSelectionType": ("simscale_sdk_v1.models.saved_selection_type", "SavedSelectionType"),
    "SharingControl": ("simscale_sdk_v1.models.sharing_control", "SharingControl"),
    "Simulation": ("simscale_sdk_v1.models.simulation._root", "Simulation"),
    "SimulationRun": ("simscale_sdk_v1.models.simulation_run", "SimulationRun"),
    "SimulationRunComputeResource": (
        "simscale_sdk_v1.models.simulation_run_compute_resource",
        "SimulationRunComputeResource",
    ),
    "SimulationRunResultCategory": (
        "simscale_sdk_v1.models.simulation_run_result_category",
        "SimulationRunResultCategory",
    ),
    "SimulationRunResultConvergencePlot": (
        "simscale_sdk_v1.models.simulation_run_result_convergence_plot",
        "SimulationRunResultConvergencePlot",
    ),
    "SimulationRunResultDirection": (
        "simscale_sdk_v1.models.simulation_run_result_direction",
        "SimulationRunResultDirection",
    ),
    "SimulationRunResultName": ("simscale_sdk_v1.models.simulation_run_result_name", "SimulationRunResultName"),
    "SimulationRunResultPlot": ("simscale_sdk_v1.models.simulation_run_result_plot", "SimulationRunResultPlot"),
    "SimulationRunResultQuantity": (
        "simscale_sdk_v1.models.simulation_run_result_quantity",
        "SimulationRunResultQuantity",
    ),
    "SimulationRunResultSolution": (
        "simscale_sdk_v1.models.simulation_run_result_solution",
        "SimulationRunResultSolution",
    ),
    "SimulationRunResultTable": ("simscale_sdk_v1.models.simulation_run_result_table", "SimulationRunResultTable"),
    "SimulationRunResultType": ("simscale_sdk_v1.models.simulation_run_result_type", "SimulationRunResultType"),
    "SimulationSpec": ("simscale_sdk_v1.models.simulation_spec", "SimulationSpec"),
    "SlimMeshOperation": ("simscale_sdk_v1.models.slim_mesh_operation", "SlimMeshOperation"),
    "Space": ("simscale_sdk_v1.models.space", "Space"),
    "SpacePermissions": ("simscale_sdk_v1.models.space_permissions", "SpacePermissions"),
    "SpaceSettings": ("simscale_sdk_v1.models.space_settings", "SpaceSettings"),
    "Spaces": ("simscale_sdk_v1.models.spaces", "Spaces"),
    "Status": ("simscale_sdk_v1.models.status", "Status"),
    "Storage": ("simscale_sdk_v1.models.storage", "Storage"),
    "SwapCadReport": ("simscale_sdk_v1.models.swap_cad_report", "SwapCadReport"),
    "SwapCadRequest": ("simscale_sdk_v1.models.swap_cad_request", "SwapCadRequest"),
    "Table": ("simscale_sdk_v1.models.table", "Table"),
    "TableData": ("simscale_sdk_v1.models.table_data", "TableData"),
    "TableImportRequest": ("simscale_sdk_v1.models.table_import_request", "TableImportRequest"),
    "TableImportRequestLocation": (
        "simscale_sdk_v1.models.table_import_request_location",
        "TableImportRequestLocation",
    ),
    "TableImportResponse": ("simscale_sdk_v1.models.table_import_response", "TableImportResponse"),
    "TableRow": ("simscale_sdk_v1.models.table_row", "TableRow"),
    "Tables": ("simscale_sdk_v1.models.tables", "Tables"),
    "User": ("simscale_sdk_v1.models.user", "User"),
    "UserSignupRequest": ("simscale_sdk_v1.models.user_signup_request", "UserSignupRequest"),
    "UserSignupResponse": ("simscale_sdk_v1.models.user_signup_response", "UserSignupResponse"),
    "WindData": ("simscale_sdk_v1.models.wind_data", "WindData"),
    "WindRoseResponse": ("simscale_sdk_v1.models.wind_rose_response", "WindRoseResponse"),
    "WorkflowId": ("simscale_sdk_v1.models.workflow_id", "WorkflowId"),
    "WorkflowRunId": ("simscale_sdk_v1.models.workflow_run_id", "WorkflowRunId"),
    "WorkflowVersionId": ("simscale_sdk_v1.models.workflow_version_id", "WorkflowVersionId"),
    "SimScaleModel": ("simscale_sdk_v1._base", "SimScaleModel"),
}

# Namespace submodules
# models.cad
# models.component_registry
# models.data_repository
# models.geometry_primitive
# models.material
# models.meshing
# models.parametric
# models.postprocessing
# models.reporting
# models.simulation
# models.workflow_repository
# models.workflow_runner
# models.workflows


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    if name == "cad":
        mod = importlib.import_module("simscale_sdk_v1.models.cad")
        globals()[name] = mod
        return mod
    if name == "component_registry":
        mod = importlib.import_module("simscale_sdk_v1.models.component_registry")
        globals()[name] = mod
        return mod
    if name == "data_repository":
        mod = importlib.import_module("simscale_sdk_v1.models.data_repository")
        globals()[name] = mod
        return mod
    if name == "geometry_primitive":
        mod = importlib.import_module("simscale_sdk_v1.models.geometry_primitive")
        globals()[name] = mod
        return mod
    if name == "material":
        mod = importlib.import_module("simscale_sdk_v1.models.material")
        globals()[name] = mod
        return mod
    if name == "meshing":
        mod = importlib.import_module("simscale_sdk_v1.models.meshing")
        globals()[name] = mod
        return mod
    if name == "parametric":
        mod = importlib.import_module("simscale_sdk_v1.models.parametric")
        globals()[name] = mod
        return mod
    if name == "postprocessing":
        mod = importlib.import_module("simscale_sdk_v1.models.postprocessing")
        globals()[name] = mod
        return mod
    if name == "reporting":
        mod = importlib.import_module("simscale_sdk_v1.models.reporting")
        globals()[name] = mod
        return mod
    if name == "simulation":
        mod = importlib.import_module("simscale_sdk_v1.models.simulation")
        globals()[name] = mod
        return mod
    if name == "workflow_repository":
        mod = importlib.import_module("simscale_sdk_v1.models.workflow_repository")
        globals()[name] = mod
        return mod
    if name == "workflow_runner":
        mod = importlib.import_module("simscale_sdk_v1.models.workflow_runner")
        globals()[name] = mod
        return mod
    if name == "workflows":
        mod = importlib.import_module("simscale_sdk_v1.models.workflows")
        globals()[name] = mod
        return mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys()) + [
        "cad",
        "component_registry",
        "data_repository",
        "geometry_primitive",
        "material",
        "meshing",
        "parametric",
        "postprocessing",
        "reporting",
        "simulation",
        "workflow_repository",
        "workflow_runner",
        "workflows",
    ]
