from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class LocalElementSizeEBM(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LOCAL_SIZING_EBM",
        description="Schema name: LocalElementSizeEBM",
    )
    name: str | None = Field(default="Local element size")
    max_element_size: Dimensional_Length | None = Field(
        validation_alias="maxElementSize", serialization_alias="maxElementSize", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
