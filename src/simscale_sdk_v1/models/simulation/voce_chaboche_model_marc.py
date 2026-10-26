from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.one_of__voce_chaboche_model_marc_hardening_rule import (
    OneOf_VoceChabocheModelMarcHardeningRule,
)


class VoceChabocheModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOCE_CHABOCHE",
        description="Schema name: VoceChabocheModelMarc",
    )
    initial_yield_stress: Dimensional_Pressure | None = Field(
        validation_alias="initialYieldStress", serialization_alias="initialYieldStress", default=None
    )
    hardening_rule: OneOf_VoceChabocheModelMarcHardeningRule | None = Field(
        validation_alias="hardeningRule", serialization_alias="hardeningRule", default=None
    )
