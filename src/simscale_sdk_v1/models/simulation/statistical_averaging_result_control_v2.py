from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__statistical_averaging_result_control_v2_sampling_interval import (
    OneOf_StatisticalAveragingResultControlV2SamplingInterval,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class StatisticalAveragingResultControlV2(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STATISTICAL_AVERAGING_V2",
        description="Schema name: StatisticalAveragingResultControlV2",
    )
    fraction_from_end: float | None = Field(
        validation_alias="fractionFromEnd",
        serialization_alias="fractionFromEnd",
        default=0.2,
        description="It defines the point in simulation where the result output data extraction starts. For instance, Fraction from end of 1 (100%) extracts all data from the beginning of the simulation while default 0.2 extracts 20% data from the end of the simulation.",
    )
    sampling_interval: OneOf_StatisticalAveragingResultControlV2SamplingInterval | None = Field(
        validation_alias="samplingInterval", serialization_alias="samplingInterval", default=None
    )
    export_fluid: bool | None = Field(
        validation_alias="exportFluid",
        serialization_alias="exportFluid",
        default=False,
        description="When this switch is activated, simulation data of the flow-field enclosed in the assignments will be exported",
    )
    export_surface: bool | None = Field(
        validation_alias="exportSurface",
        serialization_alias="exportSurface",
        default=False,
        description="When this switch is activated, simulation data on all surfaces enclosed in the assignments will be exported",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
