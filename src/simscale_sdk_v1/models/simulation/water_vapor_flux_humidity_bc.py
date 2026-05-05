from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__mass_flow_rate import Dimensional_MassFlowRate


class WaterVaporFluxHumidityBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WATER_VAPOR_FLUX",
        description="Schema name: WaterVaporFluxHumidityBC",
    )
    water_vapor_flux: Dimensional_MassFlowRate | None = Field(
        validation_alias="waterVaporFlux", serialization_alias="waterVaporFlux", default=None
    )
