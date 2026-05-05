from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WriteIntervalWriteControl(SimScaleModel):
    """Define how frequently intermediate results should be saved. With the selection of initial time steps only the user defined time steps are stored in the result and by selecting all computed time steps also intermediate results that were created by the automatic time stepping are saved. With the selection of write interval a specific write frequency can be chosen which reduces the result size. Finally using user defined time steps there can either be a constant time increment for result storage given or a table with varying time intervals analogous to the time step length definition."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WRITE_INTERVAL",
        description="Define how frequently intermediate results should be saved. With the selection of initial time steps only the user defined time steps are stored in the result and by selecting all computed time steps also intermediate results that were created by the automatic time stepping are saved. With the selection of write interval a specific write frequency can be chosen which reduces the result size. Finally using user defined time steps there can either be a constant time increment for result storage given or a table with varying time intervals analogous to the time step length definition.  Schema name: WriteIntervalWriteControl",
    )
    write_interval: int | None = Field(
        validation_alias="writeInterval",
        serialization_alias="writeInterval",
        default=5,
        description="Define the write frequency of the intermediate results to the result file. Selecting a write interval of 2 means that every second computed time step is saved in the final result database, independently if it is a pre-defined user time step or an intermediate one that was added during automatic time stepping.",
    )
