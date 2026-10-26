from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__electric_current import Dimensional_ElectricCurrent
from simscale_sdk_v1.models.simulation.one_of__current_excitation_current_type import OneOf_CurrentExcitationCurrentType


class CurrentExcitation(SimScaleModel):
    """The current in a single turn of the coil. For Stranded and Litz wire coils, the solver multiplies it by the Number of turns to obtain the ampere-turns.The current is shared over all entry (or internal) port faces of the coil, which are treated as parallel current paths. To model coils that are connected in series, create one coil per physical coil, each with a single port face, and assign the full current to every coil."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CURRENT_EXCITATION",
        description="The current in a single turn of the coil. For Stranded and Litz wire coils, the solver multiplies it by the Number of turns to obtain the ampere-turns.The current is shared over all entry (or internal) port faces of the coil, which are treated as parallel current paths. To model coils that are connected in series, create one coil per physical coil, each with a single port face, and assign the full current to every coil.  Schema name: CurrentExcitation",
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
