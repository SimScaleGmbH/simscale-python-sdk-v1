from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AdvancedComfortCriterionSettings(SimScaleModel):
    gust_factor: float | None = Field(
        validation_alias="gustFactor",
        serialization_alias="gustFactor",
        default=3.5,
        description="Value of the gust factor kg used in the computation of the gust wind speed from the mean wind speed Umean and the standard deviation of the wind speed &sigma;: Ugust = Umean + kg &sigma; Learn more.",
    )
    gem_correction: float | None = Field(
        validation_alias="gemCorrection",
        serialization_alias="gemCorrection",
        default=1.85,
        description="Value of the gust equivalent mean correction factor kGEM used in the computation of the gust equivalent mean wind speed UGEM from the gust wind speed Ugust: UGEM = Ugust / kGEM Learn more.",
    )
