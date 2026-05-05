from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FanPressureDropMomentumSource(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FAN_PRESSURE_DROP",
        description="Schema name: FanPressureDropMomentumSource",
    )
    name: str | None = Field(default=None)
    fan_direction: DimensionalVector_Dimensionless | None = Field(
        validation_alias="fanDirection", serialization_alias="fanDirection", default=None
    )
    fan_pressure: DimensionalFunction_Pressure | None = Field(
        validation_alias="fanPressure", serialization_alias="fanPressure", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
