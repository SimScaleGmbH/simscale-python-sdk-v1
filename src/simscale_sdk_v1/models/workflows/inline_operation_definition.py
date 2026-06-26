from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.data_mapping_entry import DataMappingEntry
from simscale_sdk_v1.models.workflows.data_reference import DataReference
from simscale_sdk_v1.models.workflows.value import Value


class InlineOperationDefinition(SimScaleModel):
    configuration_data_sources: list[DataReference] | None = Field(
        validation_alias="configurationDataSources", serialization_alias="configurationDataSources", default=None
    )
    configuration_value_model: Any | None = Field(
        validation_alias="configurationValueModel",
        serialization_alias="configurationValueModel",
        default=None,
        description="Value model for a concrete compound value. Resolves to an object JSON node.  Note that the serialized representation of this value model contains the nested value models in a field map. This is necessary to make this class sufficient for deserializing and processing compound values in the workflow engine in the absence of the original generated value models. When the developer is accessing fields of the generated value models then the generated getter and setter functions are storing values in this field map, there's no backing field behind the properties in the generated value models. This architecture makes the value model definition type-safe meanwhile there's no need for the generated classes at runtime.",
    )
    doc: str | None = Field(default=None)
    input_mapping: list[DataMappingEntry] | None = Field(
        validation_alias="inputMapping", serialization_alias="inputMapping", default=None
    )
    label: str | None = Field(default=None)
    metadata: dict[str, dict[str, Any]] | None = Field(default=None)
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
    multi_language_label: dict[str, str] | None = Field(
        validation_alias="multiLanguageLabel", serialization_alias="multiLanguageLabel", default=None
    )
    name: str | None = Field(default=None)
    output_data_value_models: dict[str, Value] | None = Field(
        validation_alias="outputDataValueModels", serialization_alias="outputDataValueModels", default=None
    )
    output_mapping: list[DataMappingEntry] | None = Field(
        validation_alias="outputMapping", serialization_alias="outputMapping", default=None
    )
    operation_definition_type: str
