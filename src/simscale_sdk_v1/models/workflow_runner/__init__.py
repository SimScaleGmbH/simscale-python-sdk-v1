"""Generated WorkflowRunner models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.workflow_runner.initialize_workflow_run_request import InitializeWorkflowRunRequest
    from simscale_sdk_v1.models.workflow_runner.method_checkpoint_progress import MethodCheckpointProgress
    from simscale_sdk_v1.models.workflow_runner.method_percentage_progress import MethodPercentageProgress
    from simscale_sdk_v1.models.workflow_runner.method_progress_entry import MethodProgressEntry
    from simscale_sdk_v1.models.workflow_runner.method_resource_usage_report import MethodResourceUsageReport
    from simscale_sdk_v1.models.workflow_runner.operation_run import OperationRun
    from simscale_sdk_v1.models.workflow_runner.operation_run_progress import OperationRunProgress
    from simscale_sdk_v1.models.workflow_runner.operation_run_state_history_item import OperationRunStateHistoryItem
    from simscale_sdk_v1.models.workflow_runner.operation_run_state_history_statistical_summary import (
        OperationRunStateHistoryStatisticalSummary,
    )
    from simscale_sdk_v1.models.workflow_runner.public_workflow_run_overview import PublicWorkflowRunOverview
    from simscale_sdk_v1.models.workflow_runner.resource_usage import ResourceUsage
    from simscale_sdk_v1.models.workflow_runner.resource_usage_summary import ResourceUsageSummary
    from simscale_sdk_v1.models.workflow_runner.workflow_run_error import WorkflowRunError
    from simscale_sdk_v1.models.workflow_runner.workflow_run_progress import WorkflowRunProgress

_NAMES: dict[str, tuple[str, str]] = {
    "InitializeWorkflowRunRequest": (
        "simscale_sdk_v1.models.workflow_runner.initialize_workflow_run_request",
        "InitializeWorkflowRunRequest",
    ),
    "MethodCheckpointProgress": (
        "simscale_sdk_v1.models.workflow_runner.method_checkpoint_progress",
        "MethodCheckpointProgress",
    ),
    "MethodPercentageProgress": (
        "simscale_sdk_v1.models.workflow_runner.method_percentage_progress",
        "MethodPercentageProgress",
    ),
    "MethodProgressEntry": ("simscale_sdk_v1.models.workflow_runner.method_progress_entry", "MethodProgressEntry"),
    "MethodResourceUsageReport": (
        "simscale_sdk_v1.models.workflow_runner.method_resource_usage_report",
        "MethodResourceUsageReport",
    ),
    "OperationRun": ("simscale_sdk_v1.models.workflow_runner.operation_run", "OperationRun"),
    "OperationRunProgress": ("simscale_sdk_v1.models.workflow_runner.operation_run_progress", "OperationRunProgress"),
    "OperationRunStateHistoryItem": (
        "simscale_sdk_v1.models.workflow_runner.operation_run_state_history_item",
        "OperationRunStateHistoryItem",
    ),
    "OperationRunStateHistoryStatisticalSummary": (
        "simscale_sdk_v1.models.workflow_runner.operation_run_state_history_statistical_summary",
        "OperationRunStateHistoryStatisticalSummary",
    ),
    "PublicWorkflowRunOverview": (
        "simscale_sdk_v1.models.workflow_runner.public_workflow_run_overview",
        "PublicWorkflowRunOverview",
    ),
    "ResourceUsage": ("simscale_sdk_v1.models.workflow_runner.resource_usage", "ResourceUsage"),
    "ResourceUsageSummary": ("simscale_sdk_v1.models.workflow_runner.resource_usage_summary", "ResourceUsageSummary"),
    "WorkflowRunError": ("simscale_sdk_v1.models.workflow_runner.workflow_run_error", "WorkflowRunError"),
    "WorkflowRunProgress": ("simscale_sdk_v1.models.workflow_runner.workflow_run_progress", "WorkflowRunProgress"),
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
