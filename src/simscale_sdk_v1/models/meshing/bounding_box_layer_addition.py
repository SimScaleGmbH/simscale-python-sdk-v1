from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class BoundingBoxLayerAddition(SimScaleModel):
    """This option enables layer refinement on the faces of the bounding box. This refinement is useful if the bounding box itself provides walls of the flow domain. It is often used for external aerodynamic cases where the floor is considered as a wall and hence the mesh should be refined with layers in the vicinity."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BOUNDING_BOX_LAYER_ADDITION",
        description="This option enables layer refinement on the faces of the bounding box. This refinement is useful if the bounding box itself provides walls of the flow domain. It is often used for external aerodynamic cases where the floor is considered as a wall and hence the mesh should be refined with layers in the vicinity.  Schema name: BoundingBoxLayerAddition",
    )
    name: str | None = Field(default="Bounding box layer addition")
    face: Literal["XMIN", "XMAX", "YMIN", "YMAX", "ZMIN", "ZMAX"] | None = Field(
        default="XMIN",
        description="This option selects the face of the bounding box on which layers will be added. A face is selected by its normal (denoted by the respective coordinate system axis) and its position (denoted by min or max).",
    )
    layers: int | None = Field(
        default=5, description="The number of layers defines how many boundary layers should be created."
    )
    expansion_ratio: float | None = Field(
        validation_alias="expansionRatio",
        serialization_alias="expansionRatio",
        default=1.3,
        description="The Expansion ratio determines how the boundary layers grow in thickness from the wall to the internal mesh. The larger the ratio, the larger each cell layer will be in comparison to the neighbouring layer closer to the wall. The figure shows a ratio of 1.3.",
    )
    min_thickness: Dimensional_Length | None = Field(
        validation_alias="minThickness", serialization_alias="minThickness", default=None
    )
    final_thickness: Dimensional_Length | None = Field(
        validation_alias="finalThickness", serialization_alias="finalThickness", default=None
    )
