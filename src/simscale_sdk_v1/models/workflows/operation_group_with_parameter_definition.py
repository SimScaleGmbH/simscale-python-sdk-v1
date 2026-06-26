from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.breakpoint import Breakpoint


class OperationGroupWithParameterDefinition(SimScaleModel):
    doc: str | None = Field(default=None)
    label: str | None = Field(default=None)
    metadata: dict[str, dict[str, Any]] | None = Field(default=None)
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
    multi_language_label: dict[str, str] | None = Field(
        validation_alias="multiLanguageLabel", serialization_alias="multiLanguageLabel", default=None
    )
    name: str | None = Field(default=None)
    operation_definition_type: str
    breakpoints: list[Breakpoint] | None = Field(default=None)
    iterator_reference: Any | None = Field(
        validation_alias="iteratorReference",
        serialization_alias="iteratorReference",
        default=None,
        description="Iterator reference for processing collections.",
    )
    parameter_doc: str | None = Field(validation_alias="parameterDoc", serialization_alias="parameterDoc", default=None)
    parameter_label: str | None = Field(
        validation_alias="parameterLabel", serialization_alias="parameterLabel", default=None
    )
    parameter_multi_language_doc: dict[str, str] | None = Field(
        validation_alias="parameterMultiLanguageDoc", serialization_alias="parameterMultiLanguageDoc", default=None
    )
    parameter_multi_language_label: dict[str, str] | None = Field(
        validation_alias="parameterMultiLanguageLabel", serialization_alias="parameterMultiLanguageLabel", default=None
    )
    parameter_name: str | None = Field(
        validation_alias="parameterName", serialization_alias="parameterName", default=None
    )
    value_list: Any | None = Field(
        validation_alias="valueList",
        serialization_alias="valueList",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
