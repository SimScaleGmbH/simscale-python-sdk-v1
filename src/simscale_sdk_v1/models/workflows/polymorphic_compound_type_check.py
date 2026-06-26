from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class PolymorphicCompoundTypeCheck(SimScaleModel):
    compound_value: Any | None = Field(
        validation_alias="compoundValue",
        serialization_alias="compoundValue",
        default=None,
        description="Value model for a concrete compound value. Resolves to an object JSON node.  Note that the serialized representation of this value model contains the nested value models in a field map. This is necessary to make this class sufficient for deserializing and processing compound values in the workflow engine in the absence of the original generated value models. When the developer is accessing fields of the generated value models then the generated getter and setter functions are storing values in this field map, there's no backing field behind the properties in the generated value models. This architecture makes the value model definition type-safe meanwhile there's no need for the generated classes at runtime.",
    )
    target_type_value: Any | None = Field(
        validation_alias="targetTypeValue",
        serialization_alias="targetTypeValue",
        default=None,
        description="Value model for a string value. Resolves to a text JSON node.",
    )
    value_model_type: str
