from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class PolynomialFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="POLYNOMIAL",
        description="Schema name: PolynomialFunction",
    )
    coefficients: list[float] | None = Field(default=None)
    parameter_base_unit: str = Field(validation_alias="parameterBaseUnit", serialization_alias="parameterBaseUnit")
