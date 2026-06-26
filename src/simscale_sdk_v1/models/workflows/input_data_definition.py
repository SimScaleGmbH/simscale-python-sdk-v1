from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class InputDataDefinition(SimScaleModel):
    data_type_reference: str | None = Field(
        validation_alias="dataTypeReference", serialization_alias="dataTypeReference", default=None
    )
    data_definition_type: str
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
    optional: bool | None = Field(default=None)
