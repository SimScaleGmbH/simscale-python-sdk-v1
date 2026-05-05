from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Simulation(SimScaleModel):
    simulation_id: str | None = Field(validation_alias="simulationId", serialization_alias="simulationId", default=None)
    name: str | None = Field(default=None, description="The name of the simulation.")
