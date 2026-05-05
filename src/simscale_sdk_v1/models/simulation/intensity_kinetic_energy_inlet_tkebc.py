from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class IntensityKineticEnergyInletTKEBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TURBULENT_INTENSITY_KINETIC_ENERGY_INLET",
        description="Schema name: IntensityKineticEnergyInletTKEBC",
    )
    intensity: float | None = Field(default=0.05)
