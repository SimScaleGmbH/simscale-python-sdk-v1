from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AbstractOperationDefinition(SimScaleModel):
    """Abstract workflow operation definition.  It can be either: * atomic method or nested workflow, * composition element: grouping operations, control structures etc."""

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
