from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class JsonNode(SimScaleModel):
    array: bool | None = Field(default=None)
    big_decimal: bool | None = Field(validation_alias="bigDecimal", serialization_alias="bigDecimal", default=None)
    big_integer: bool | None = Field(validation_alias="bigInteger", serialization_alias="bigInteger", default=None)
    binary: bool | None = Field(default=None)
    boolean: bool | None = Field(default=None)
    container: bool | None = Field(default=None)
    double: bool | None = Field(default=None)
    embedded_value: bool | None = Field(
        validation_alias="embeddedValue", serialization_alias="embeddedValue", default=None
    )
    empty: bool | None = Field(default=None)
    float: bool | None = Field(default=None)
    floating_point_number: bool | None = Field(
        validation_alias="floatingPointNumber", serialization_alias="floatingPointNumber", default=None
    )
    int: bool | None = Field(default=None)
    integral_number: bool | None = Field(
        validation_alias="integralNumber", serialization_alias="integralNumber", default=None
    )
    long: bool | None = Field(default=None)
    missing_node: bool | None = Field(validation_alias="missingNode", serialization_alias="missingNode", default=None)
    node_type: Literal["ARRAY", "BINARY", "BOOLEAN", "MISSING", "NULL", "NUMBER", "OBJECT", "POJO", "STRING"] | None = (
        Field(validation_alias="nodeType", serialization_alias="nodeType", default=None)
    )
    null: bool | None = Field(default=None)
    number: bool | None = Field(default=None)
    object: bool | None = Field(default=None)
    pojo: bool | None = Field(default=None)
    short: bool | None = Field(default=None)
    string: bool | None = Field(default=None)
    textual: bool | None = Field(default=None)
    value_node: bool | None = Field(validation_alias="valueNode", serialization_alias="valueNode", default=None)
