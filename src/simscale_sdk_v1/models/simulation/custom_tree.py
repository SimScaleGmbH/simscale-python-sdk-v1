from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class CustomTree(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_TREE",
        description="Schema name: CustomTree",
    )
    leaf_area_index: float | None = Field(
        validation_alias="leafAreaIndex",
        serialization_alias="leafAreaIndex",
        default=5.28,
        description="Leaf Area Index (LAI) is a dimensionless quantity that is defined as the leaf area per unit ground surface area in broadle af canopies",
    )
    average_tree_height: Dimensional_Length | None = Field(
        validation_alias="averageTreeHeight", serialization_alias="averageTreeHeight", default=None
    )
    drag_coefficient: float | None = Field(
        validation_alias="dragCoefficient",
        serialization_alias="dragCoefficient",
        default=0.2,
        description="Drag coefficient of the tree canopy.",
    )
