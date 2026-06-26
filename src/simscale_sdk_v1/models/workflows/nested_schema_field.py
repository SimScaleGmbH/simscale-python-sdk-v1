from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NestedSchemaField(SimScaleModel):
    doc: str | None = Field(default=None)
    expert: bool | None = Field(default=None)
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
    schema_definition_field_index: int | None = Field(
        validation_alias="schemaDefinitionFieldIndex", serialization_alias="schemaDefinitionFieldIndex", default=None
    )
    schema_element_type: str
    ui_field_index: int | None = Field(
        validation_alias="uiFieldIndex", serialization_alias="uiFieldIndex", default=None
    )
    nested_data_type_reference: str | None = Field(
        validation_alias="nestedDataTypeReference", serialization_alias="nestedDataTypeReference", default=None
    )
    nested_schema_data_model_class_name: str | None = Field(
        validation_alias="nestedSchemaDataModelClassName",
        serialization_alias="nestedSchemaDataModelClassName",
        default=None,
    )
    nested_schema_package: str | None = Field(
        validation_alias="nestedSchemaPackage", serialization_alias="nestedSchemaPackage", default=None
    )
    nested_schema_value_model_class_name: str | None = Field(
        validation_alias="nestedSchemaValueModelClassName",
        serialization_alias="nestedSchemaValueModelClassName",
        default=None,
    )
