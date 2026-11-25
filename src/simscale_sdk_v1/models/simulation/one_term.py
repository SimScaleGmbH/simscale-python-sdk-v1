from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__one_term_exponent1_function import OneOf_OneTermExponent1Function


class OneTerm(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="ONE_TERM", description="Schema name: OneTerm"
    )
    modulus1_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="modulus1Function", serialization_alias="modulus1Function", default=None
    )
    exponent1_function: OneOf_OneTermExponent1Function | None = Field(
        validation_alias="exponent1Function", serialization_alias="exponent1Function", default=None
    )
