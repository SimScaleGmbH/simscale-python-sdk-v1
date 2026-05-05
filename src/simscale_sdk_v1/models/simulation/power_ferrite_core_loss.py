from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class PowerFerriteCoreLoss(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="POWER_FERRITE",
        description="Schema name: PowerFerriteCoreLoss",
    )
    steinmetz_constant: float | None = Field(
        validation_alias="steinmetzConstant", serialization_alias="steinmetzConstant", default=0.0
    )
    frequency_exponent: float | None = Field(
        validation_alias="frequencyExponent", serialization_alias="frequencyExponent", default=0.0
    )
    flux_density_exponent: float | None = Field(
        validation_alias="fluxDensityExponent", serialization_alias="fluxDensityExponent", default=0.0
    )
