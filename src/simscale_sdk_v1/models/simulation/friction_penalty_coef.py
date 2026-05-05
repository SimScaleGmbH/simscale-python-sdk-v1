from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FrictionPenaltyCoef(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FRICTION_PENALTY_COEF",
        description="Schema name: FrictionPenaltyCoef",
    )
    friction_penalty_coefficient: float | None = Field(
        validation_alias="frictionPenaltyCoefficient", serialization_alias="frictionPenaltyCoefficient", default=100000
    )
    coulomb_coefficient: float | None = Field(
        validation_alias="coulombCoefficient", serialization_alias="coulombCoefficient", default=0.1
    )
