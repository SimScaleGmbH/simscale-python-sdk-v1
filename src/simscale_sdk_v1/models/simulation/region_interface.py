from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__region_interface_interface_thermal import (
    OneOf_RegionInterfaceInterfaceThermal,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class RegionInterface(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_INTERFACE",
        description="Schema name: RegionInterface",
    )
    name: str | None = Field(default=None)
    interface_thermal: OneOf_RegionInterfaceInterfaceThermal | None = Field(
        validation_alias="interfaceThermal", serialization_alias="interfaceThermal", default=None
    )
    master_topological_reference: TopologicalReference | None = Field(
        validation_alias="masterTopologicalReference", serialization_alias="masterTopologicalReference", default=None
    )
    slave_topological_reference: TopologicalReference | None = Field(
        validation_alias="slaveTopologicalReference", serialization_alias="slaveTopologicalReference", default=None
    )
    is_partial: bool | None = Field(validation_alias="isPartial", serialization_alias="isPartial", default=False)
    custom_modified: bool | None = Field(
        validation_alias="customModified", serialization_alias="customModified", default=False
    )
