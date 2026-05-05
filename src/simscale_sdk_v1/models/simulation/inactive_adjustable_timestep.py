from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class InactiveAdjustableTimestep(SimScaleModel):
    """This option activates an adjustable time step. The time step is being modified according to the Courant number."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INACTIVE_TIMESTEP",
        description="This option activates an adjustable time step. The time step is being modified according to the Courant number.  Schema name: InactiveAdjustableTimestep",
    )
