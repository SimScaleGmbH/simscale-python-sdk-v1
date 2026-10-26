from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class OneBackstressTerm(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ONE_TERM",
        description="Schema name: OneBackstressTerm",
    )
    hardening_modulus1: Dimensional_Pressure | None = Field(
        validation_alias="hardeningModulus1", serialization_alias="hardeningModulus1", default=None
    )
    dynamic_recovery_rate1: float | None = Field(
        validation_alias="dynamicRecoveryRate1",
        serialization_alias="dynamicRecoveryRate1",
        default=0.0,
        description="The dynamic recovery rate of this backstress term, controlling how quickly it saturates with accumulated plastic strain. A value of 0 makes this term purely linear (no saturation).",
    )
