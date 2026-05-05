from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FixedTemperature(SimScaleModel):
    """Specify a fixed temperature at a volume or boundary. Used for parts maintained at a known temperature."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_TEMPERATURE",
        description="Specify a fixed temperature at a volume or boundary. Used for parts maintained at a known temperature.  Schema name: FixedTemperature",
    )
    name: str | None = Field(default=None)
    temperature: DimensionalFunction_Temperature | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
