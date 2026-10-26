from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class ThreeBackstressTerms(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="THREE_TERMS",
        description="Schema name: ThreeBackstressTerms",
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
    hardening_modulus2: Dimensional_Pressure | None = Field(
        validation_alias="hardeningModulus2", serialization_alias="hardeningModulus2", default=None
    )
    dynamic_recovery_rate2: float | None = Field(
        validation_alias="dynamicRecoveryRate2",
        serialization_alias="dynamicRecoveryRate2",
        default=0.0,
        description="The dynamic recovery rate of this backstress term, controlling how quickly it saturates with accumulated plastic strain. A value of 0 makes this term purely linear (no saturation).",
    )
    hardening_modulus3: Dimensional_Pressure | None = Field(
        validation_alias="hardeningModulus3", serialization_alias="hardeningModulus3", default=None
    )
    dynamic_recovery_rate3: float | None = Field(
        validation_alias="dynamicRecoveryRate3",
        serialization_alias="dynamicRecoveryRate3",
        default=0.0,
        description="The dynamic recovery rate of this backstress term, controlling how quickly it saturates with accumulated plastic strain. A value of 0 makes this term purely linear (no saturation).",
    )
