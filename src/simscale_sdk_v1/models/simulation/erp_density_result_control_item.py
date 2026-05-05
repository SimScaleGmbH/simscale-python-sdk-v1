from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.equivalent_radiated_power_density_type import EquivalentRadiatedPowerDensityType


class ERPDensityResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ERP_DENSITY",
        description="Schema name: ERPDensityResultControlItem",
    )
    name: str | None = Field(default=None)
    density_type: EquivalentRadiatedPowerDensityType | None = Field(
        validation_alias="densityType", serialization_alias="densityType", default=None
    )
