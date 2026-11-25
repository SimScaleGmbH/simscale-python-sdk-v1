from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__three_terms_exponent1_function import OneOf_ThreeTermsExponent1Function
from simscale_sdk_v1.models.simulation.one_of__three_terms_exponent2_function import OneOf_ThreeTermsExponent2Function
from simscale_sdk_v1.models.simulation.one_of__three_terms_exponent3_function import OneOf_ThreeTermsExponent3Function


class ThreeTerms(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="THREE_TERMS",
        description="Schema name: ThreeTerms",
    )
    modulus1_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="modulus1Function", serialization_alias="modulus1Function", default=None
    )
    exponent1_function: OneOf_ThreeTermsExponent1Function | None = Field(
        validation_alias="exponent1Function", serialization_alias="exponent1Function", default=None
    )
    modulus2_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="modulus2Function", serialization_alias="modulus2Function", default=None
    )
    exponent2_function: OneOf_ThreeTermsExponent2Function | None = Field(
        validation_alias="exponent2Function", serialization_alias="exponent2Function", default=None
    )
    modulus3_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="modulus3Function", serialization_alias="modulus3Function", default=None
    )
    exponent3_function: OneOf_ThreeTermsExponent3Function | None = Field(
        validation_alias="exponent3Function", serialization_alias="exponent3Function", default=None
    )
