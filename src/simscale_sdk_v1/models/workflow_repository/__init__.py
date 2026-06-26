"""Generated WorkflowRepository models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.workflow_repository.create_workflow_request import CreateWorkflowRequest
    from simscale_sdk_v1.models.workflow_repository.read_workflow_response import ReadWorkflowResponse
    from simscale_sdk_v1.models.workflow_repository.update_workflow_request import UpdateWorkflowRequest
    from simscale_sdk_v1.models.workflow_repository.workflow_overview import WorkflowOverview
    from simscale_sdk_v1.models.workflow_repository.workflow_version_overview import WorkflowVersionOverview

_NAMES: dict[str, tuple[str, str]] = {
    "CreateWorkflowRequest": (
        "simscale_sdk_v1.models.workflow_repository.create_workflow_request",
        "CreateWorkflowRequest",
    ),
    "ReadWorkflowResponse": (
        "simscale_sdk_v1.models.workflow_repository.read_workflow_response",
        "ReadWorkflowResponse",
    ),
    "UpdateWorkflowRequest": (
        "simscale_sdk_v1.models.workflow_repository.update_workflow_request",
        "UpdateWorkflowRequest",
    ),
    "WorkflowOverview": ("simscale_sdk_v1.models.workflow_repository.workflow_overview", "WorkflowOverview"),
    "WorkflowVersionOverview": (
        "simscale_sdk_v1.models.workflow_repository.workflow_version_overview",
        "WorkflowVersionOverview",
    ),
}


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys())
