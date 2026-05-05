from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ActiveAdjustableTimestep(SimScaleModel):
    """This option activates an adjustable time step. The time step is being modified according to the Courant number."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ACTIVE_TIMESTEP",
        description="This option activates an adjustable time step. The time step is being modified according to the Courant number.  Schema name: ActiveAdjustableTimestep",
    )
    maximal_courant_number: float | None = Field(
        validation_alias="maximalCourantNumber",
        serialization_alias="maximalCourantNumber",
        default=0.5,
        description="This option defines a maximum Courant number. The resulting time step should resolve relevant transient effects with at least 100 steps. Transient multiphase simulations: Maximum Courant number may not be greater than 1. Values of 0.5-0.7 are recommended for many cases.",
    )
    maximal_step: float | None = Field(
        validation_alias="maximalStep",
        serialization_alias="maximalStep",
        default=1,
        description="This option defines a maximum time step length which may not be exceeded when the time step is adapted during runtime.",
    )
    max_alpha_co: float | None = Field(
        validation_alias="maxAlphaCo",
        serialization_alias="maxAlphaCo",
        default=0.5,
        description="Define a maximum Courant number based on the interface velocity.",
    )
