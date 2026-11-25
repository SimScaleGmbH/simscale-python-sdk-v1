from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__speed import Dimensional_Speed
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless
from simscale_sdk_v1.models.simulation.one_of__motion_axis_travel_limit import OneOf_MotionAxisTravelLimit


class MotionAxis(SimScaleModel):
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system the direction below is written in. Leave it empty to use the global Cartesian system.Only Cartesian systems can be selected, because the motion follows a single fixed axis.",
    )
    direction: DimensionalVector_Dimensionless | None = Field(default=None)
    initial_velocity: Dimensional_Speed | None = Field(
        validation_alias="initialVelocity", serialization_alias="initialVelocity", default=None
    )
    travel_limit: OneOf_MotionAxisTravelLimit | None = Field(
        validation_alias="travelLimit", serialization_alias="travelLimit", default=None
    )
