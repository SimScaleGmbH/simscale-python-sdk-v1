from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EntityAssignmentField(SimScaleModel):
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
    allowed_entity_types: (
        list[
            Literal[
                "SOLID",
                "SOLID_FACE",
                "SOLID_EDGE",
                "SOLID_VERTEX",
                "SHEET",
                "SHEET_FACE",
                "SHEET_EDGE",
                "SHEET_VERTEX",
                "WIRE",
                "WIRE_EDGE",
                "WIRE_VERTEX",
                "ACORN_VERTEX",
                "VERTEX",
                "EDGE",
                "FACE",
                "REGION",
            ]
        ]
        | None
    ) = Field(validation_alias="allowedEntityTypes", serialization_alias="allowedEntityTypes", default=None)
    allowed_source_types: list[Literal["CAD", "MESH"]] | None = Field(
        validation_alias="allowedSourceTypes", serialization_alias="allowedSourceTypes", default=None
    )
