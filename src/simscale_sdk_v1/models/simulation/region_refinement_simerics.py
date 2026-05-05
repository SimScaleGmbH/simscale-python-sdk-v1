from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class RegionRefinementSimerics(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_REFINEMENT_SIMERICS",
        description="Schema name: RegionRefinementSimerics",
    )
    name: str | None = Field(default="Region refinement")
    refinement_cell_size_absolute: Dimensional_Length | None = Field(
        validation_alias="refinementCellSizeAbsolute", serialization_alias="refinementCellSizeAbsolute", default=None
    )
    refinement_cell_size_relative: float | None = Field(
        validation_alias="refinementCellSizeRelative",
        serialization_alias="refinementCellSizeRelative",
        default=1,
        description="This parameter defines the length scale to which the entire region enclosed by the refinement zone needs to be resolved. Due to the binary-tree mesh generation approach applied, the actual cell size might be equal or smaller than the target cell size specified. Choosing a finer resolution will resolve the enclosed region to a greater level of detail, but will result in a larger mesh. This typically means longer runtimes and bigger sizes of results.",
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
