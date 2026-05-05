from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__acceleration_field_selection_acceleration_type import (
    OneOf_AccelerationFieldSelectionAccelerationType,
)


class AccelerationFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ACCELERATION",
        description="Schema name: AccelerationFieldSelection",
    )
    acceleration_type: OneOf_AccelerationFieldSelectionAccelerationType | None = Field(
        validation_alias="accelerationType", serialization_alias="accelerationType", default=None
    )
    component_selection: Literal["X", "Y", "Z", "ALL"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="ALL"
    )
    output_method: Literal["POST_SIMULATION", "LIVE"] | None = Field(
        validation_alias="outputMethod",
        serialization_alias="outputMethod",
        default="POST_SIMULATION",
        description="This option allows to control the output frequency and accuracy:Post simulation: Point data output is synchronised with global solution fields. Data is interpolated from nodes surrounding the geometry primitive.Live: Point data is output continuously during the simulation at all computed timesteps. Data is taken directly from the nearest mesh node and no interpolation is performed.",
    )
