from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ThetaMethodTimeIntegrationType(SimScaleModel):
    """Choose the time integration scheme type"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="THETA_METHOD",
        description="Choose the time integration scheme type  Schema name: ThetaMethodTimeIntegrationType",
    )
    theta: float | None = Field(
        default=0.57,
        description="The parameter &theta; must be ranging between 0.0 (explicit method) and 1.0 (completely implicit method). The standard value of &theta; = 0.57 is chosen a little higher than &theta; = 0.5 which would lead to the Crank-Nicolson scheme of order 2.",
    )
