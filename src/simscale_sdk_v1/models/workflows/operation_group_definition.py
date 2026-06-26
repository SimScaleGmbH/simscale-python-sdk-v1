from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.abstract_operation_definition import AbstractOperationDefinition
from simscale_sdk_v1.models.workflows.breakpoint import Breakpoint


class OperationGroupDefinition(SimScaleModel):
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
    operations: list[AbstractOperationDefinition] | None = Field(default=None)
