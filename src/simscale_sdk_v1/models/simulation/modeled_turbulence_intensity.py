from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ModeledTurbulenceIntensity(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MODELED_TURBULENCE_INTENSITY",
        description="Schema name: ModeledTurbulenceIntensity",
    )
