from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity


class InletOutletNBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_OUTLET",
        description="Schema name: InletOutletNBC",
    )
    value: Dimensional_KinematicViscosity | None = Field(default=None)
