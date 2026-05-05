from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__rotational_stiffness import Dimensional_RotationalStiffness


class TorsionalAxialRotation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TORSIONAL",
        description="Schema name: TorsionalAxialRotation",
    )
    torsional_stiffness: Dimensional_RotationalStiffness | None = Field(
        validation_alias="torsionalStiffness", serialization_alias="torsionalStiffness", default=None
    )
