"""Generated ComponentRegistry models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.component_registry.component_group_metadata import ComponentGroupMetadata
    from simscale_sdk_v1.models.component_registry.component_overview import ComponentOverview
    from simscale_sdk_v1.models.component_registry.component_version_dependencies import ComponentVersionDependencies
    from simscale_sdk_v1.models.component_registry.component_version_dependents import ComponentVersionDependents
    from simscale_sdk_v1.models.component_registry.component_version_metadata import ComponentVersionMetadata
    from simscale_sdk_v1.models.component_registry.data_description import DataDescription
    from simscale_sdk_v1.models.component_registry.data_interface import DataInterface
    from simscale_sdk_v1.models.component_registry.data_type_file_operations_description import (
        DataTypeFileOperationsDescription,
    )
    from simscale_sdk_v1.models.component_registry.file_format import FileFormat
    from simscale_sdk_v1.models.component_registry.file_format_group import FileFormatGroup
    from simscale_sdk_v1.models.component_registry.organization_component_group_metadata import (
        OrganizationComponentGroupMetadata,
    )
    from simscale_sdk_v1.models.component_registry.parameter_description import ParameterDescription
    from simscale_sdk_v1.models.component_registry.ui_configuration import UiConfiguration
    from simscale_sdk_v1.models.component_registry.validation_rule import ValidationRule
    from simscale_sdk_v1.models.component_registry.validation_rule_case import ValidationRuleCase
    from simscale_sdk_v1.models.component_registry.validation_rule_set import ValidationRuleSet
    from simscale_sdk_v1.models.component_registry.workflow_definition import WorkflowDefinition

_NAMES: dict[str, tuple[str, str]] = {
    "ComponentGroupMetadata": (
        "simscale_sdk_v1.models.component_registry.component_group_metadata",
        "ComponentGroupMetadata",
    ),
    "ComponentOverview": ("simscale_sdk_v1.models.component_registry.component_overview", "ComponentOverview"),
    "ComponentVersionDependencies": (
        "simscale_sdk_v1.models.component_registry.component_version_dependencies",
        "ComponentVersionDependencies",
    ),
    "ComponentVersionDependents": (
        "simscale_sdk_v1.models.component_registry.component_version_dependents",
        "ComponentVersionDependents",
    ),
    "ComponentVersionMetadata": (
        "simscale_sdk_v1.models.component_registry.component_version_metadata",
        "ComponentVersionMetadata",
    ),
    "DataDescription": ("simscale_sdk_v1.models.component_registry.data_description", "DataDescription"),
    "DataInterface": ("simscale_sdk_v1.models.component_registry.data_interface", "DataInterface"),
    "DataTypeFileOperationsDescription": (
        "simscale_sdk_v1.models.component_registry.data_type_file_operations_description",
        "DataTypeFileOperationsDescription",
    ),
    "FileFormat": ("simscale_sdk_v1.models.component_registry.file_format", "FileFormat"),
    "FileFormatGroup": ("simscale_sdk_v1.models.component_registry.file_format_group", "FileFormatGroup"),
    "OrganizationComponentGroupMetadata": (
        "simscale_sdk_v1.models.component_registry.organization_component_group_metadata",
        "OrganizationComponentGroupMetadata",
    ),
    "ParameterDescription": ("simscale_sdk_v1.models.component_registry.parameter_description", "ParameterDescription"),
    "UiConfiguration": ("simscale_sdk_v1.models.component_registry.ui_configuration", "UiConfiguration"),
    "ValidationRule": ("simscale_sdk_v1.models.component_registry.validation_rule", "ValidationRule"),
    "ValidationRuleCase": ("simscale_sdk_v1.models.component_registry.validation_rule_case", "ValidationRuleCase"),
    "ValidationRuleSet": ("simscale_sdk_v1.models.component_registry.validation_rule_set", "ValidationRuleSet"),
    "WorkflowDefinition": ("simscale_sdk_v1.models.component_registry.workflow_definition", "WorkflowDefinition"),
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
