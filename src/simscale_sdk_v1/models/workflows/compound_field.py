from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.schema_element import SchemaElement


class CompoundField(SimScaleModel):
    associated_data_type: str | None = Field(
        validation_alias="associatedDataType", serialization_alias="associatedDataType", default=None
    )
    default_subtype: bool | None = Field(
        validation_alias="defaultSubtype", serialization_alias="defaultSubtype", default=None
    )
    doc: str | None = Field(default=None)
    expert: bool | None = Field(default=None)
    fields: dict[str, SchemaElement] | None = Field(default=None)
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
    optional: bool | None = Field(default=None)
    polymorphic: bool | None = Field(default=None)
    schema_definition_field_index: int | None = Field(
        validation_alias="schemaDefinitionFieldIndex", serialization_alias="schemaDefinitionFieldIndex", default=None
    )
    subtypes: list[Any] | None = Field(default=None)
    type_name: str | None = Field(validation_alias="typeName", serialization_alias="typeName", default=None)
    ui_field_index: int | None = Field(
        validation_alias="uiFieldIndex", serialization_alias="uiFieldIndex", default=None
    )
