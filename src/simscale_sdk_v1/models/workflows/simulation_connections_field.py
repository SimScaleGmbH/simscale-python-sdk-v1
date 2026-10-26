from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.schema_element import SchemaElement


class SimulationConnectionsField(SimScaleModel):
    cad_input: str | None = Field(validation_alias="cadInput", serialization_alias="cadInput", default=None)
    default_subtype: bool | None = Field(
        validation_alias="defaultSubtype", serialization_alias="defaultSubtype", default=None
    )
    doc: str | None = Field(default=None)
    expert: bool | None = Field(default=None)
    fields: dict[str, SchemaElement] | None = Field(default=None)
    grouping: Literal["BODY_PAIR", "FACE_PAIR"] | None = Field(
        default="", description="How detected face pairs are grouped into simulation connections."
    )
    label: str | None = Field(default=None)
    list_: bool | None = Field(validation_alias="list", serialization_alias="list", default=None)
    model_field_name: str | None = Field(
        validation_alias="modelFieldName", serialization_alias="modelFieldName", default=None
    )
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
    multi_language_label: dict[str, str] | None = Field(
        validation_alias="multiLanguageLabel", serialization_alias="multiLanguageLabel", default=None
    )
    name: str | None = Field(default=None)
    non_empty: bool | None = Field(validation_alias="nonEmpty", serialization_alias="nonEmpty", default=None)
    optional: bool | None = Field(default=None)
    polymorphic: bool | None = Field(default=None)
    schema_definition_field_index: int | None = Field(
        validation_alias="schemaDefinitionFieldIndex", serialization_alias="schemaDefinitionFieldIndex", default=None
    )
    subtypes: list[Any] | None = Field(default=None)
    supertype: Any | None = Field(
        default=None, description="Abstract compound field denotes a schema element which has nested schema elements."
    )
    type_name: str | None = Field(validation_alias="typeName", serialization_alias="typeName", default=None)
    ui_field_index: int | None = Field(
        validation_alias="uiFieldIndex", serialization_alias="uiFieldIndex", default=None
    )
    schema_element_type: str
