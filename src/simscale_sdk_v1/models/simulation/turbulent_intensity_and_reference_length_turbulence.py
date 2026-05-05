from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class TurbulentIntensityAndReferenceLengthTurbulence(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TURBULENT_INTENSITY_AND_REFERENCE_LENGTH_TURBULENCE",
        description="Schema name: TurbulentIntensityAndReferenceLengthTurbulence",
    )
    turbulent_intensity: float | None = Field(
        validation_alias="turbulentIntensity",
        serialization_alias="turbulentIntensity",
        default=0.05,
        description="This provides a turbulent intensity boundary condition. The turbulent intensity is defined as the ratio of the root-mean-square of the velocity fluctuations to the mean flow velocity",
    )
    mixing_length: Dimensional_Length | None = Field(
        validation_alias="mixingLength", serialization_alias="mixingLength", default=None
    )
