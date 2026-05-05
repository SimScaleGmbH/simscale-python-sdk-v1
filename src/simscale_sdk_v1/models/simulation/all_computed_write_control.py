from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AllComputedWriteControl(SimScaleModel):
    """Define how frequently intermediate results should be saved. With the selection of initial time steps only the user defined time steps are stored in the result and by selecting all computed time steps also intermediate results that were created by the automatic time stepping are saved. With the selection of write interval a specific write frequency can be chosen which reduces the result size. Finally using user defined time steps there can either be a constant time increment for result storage given or a table with varying time intervals analogous to the time step length definition."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ALL_COMPUTED",
        description="Define how frequently intermediate results should be saved. With the selection of initial time steps only the user defined time steps are stored in the result and by selecting all computed time steps also intermediate results that were created by the automatic time stepping are saved. With the selection of write interval a specific write frequency can be chosen which reduces the result size. Finally using user defined time steps there can either be a constant time increment for result storage given or a table with varying time intervals analogous to the time step length definition.  Schema name: AllComputedWriteControl",
    )
