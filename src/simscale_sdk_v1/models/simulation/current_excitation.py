from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__electric_current import Dimensional_ElectricCurrent
from simscale_sdk_v1.models.simulation.one_of__current_excitation_current_type import OneOf_CurrentExcitationCurrentType


class CurrentExcitation(SimScaleModel):
    """The total current over all faces"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CURRENT_EXCITATION",
        description="The total current over all faces  Schema name: CurrentExcitation",
    )
    current_type: OneOf_CurrentExcitationCurrentType | None = Field(
        validation_alias="currentType", serialization_alias="currentType", default=None
    )
    current_rms: Dimensional_ElectricCurrent | None = Field(
        validation_alias="currentRMS", serialization_alias="currentRMS", default=None
    )
    current_phase: Dimensional_Angle | None = Field(
        validation_alias="currentPhase", serialization_alias="currentPhase", default=None
    )
