from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__volumetric_flow_rate import (
    DimensionalFunction_VolumetricFlowRate,
)


class VolumetricFlow(SimScaleModel):
    """Defines the volumetric flow rate per each face of the assignment."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLUMETRIC",
        description="Defines the volumetric flow rate per each face of the assignment.  Schema name: VolumetricFlow",
    )
    value: DimensionalFunction_VolumetricFlowRate | None = Field(default=None)
