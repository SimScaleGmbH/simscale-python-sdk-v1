from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__mrt_solar_parameters_fraction_body_surface import (
    OneOf_MrtSolarParametersFractionBodySurface,
)


class MrtSolarParameters(SimScaleModel):
    fraction_body_surface: OneOf_MrtSolarParametersFractionBodySurface | None = Field(
        validation_alias="fractionBodySurface", serialization_alias="fractionBodySurface", default=None
    )
    projected_area_factor: float | None = Field(
        validation_alias="projectedAreaFactor",
        serialization_alias="projectedAreaFactor",
        default=0.7,
        description="The projected area of a standard person exposed to direct beam sunlight in the range [0, 1]. This projection depends on the time of day and year usually in the range [0, 0.7]. This parameter is not a necessary input if the solar load is computed from time and place since it can be computed.",
    )
    short_wave_absorptivity: float | None = Field(
        validation_alias="shortWaveAbsorptivity",
        serialization_alias="shortWaveAbsorptivity",
        default=0.67,
        description="The radiation wavelength of a source depends on its temperature. Since the sun is much hotter than surfaces in a typical room, the amount of sun heat absorbed by a person is different than the amount it is able to emit back to its surroundings. Typical values are:  0.2 : White clothing.  0.57 : Khaki clothing  0.57 : White skin  0.65 : Brown skin  0.84 : Black skin.  0.88 : Black clothing.",
    )
