from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class LayerAddition(SimScaleModel):
    """Inflated boundary layers are used to resolve the boundary layer near walls (no-slip) which are in contact with the fluid. Using boundary layers is generally recommended for turbulent simulations."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LAYER_ADDITION",
        description="Inflated boundary layers are used to resolve the boundary layer near walls (no-slip) which are in contact with the fluid. Using boundary layers is generally recommended for turbulent simulations.  Schema name: LayerAddition",
    )
    name: str | None = Field(default="Inflate boundary layer")
    layers: int | None = Field(
        default=5, description="The number of layers defines how many boundary layers should be created."
    )
    expansion_ratio: float | None = Field(
        validation_alias="expansionRatio",
        serialization_alias="expansionRatio",
        default=1.3,
        description="The Expansion ratio determines how the boundary layers grow in thickness from the wall to the internal mesh. The larger the ratio, the larger each cell layer will be in comparison to the neighbouring layer closer to the wall. The figure shows a ratio of 1.3.",
    )
    min_thickness: float | None = Field(
        validation_alias="minThickness",
        serialization_alias="minThickness",
        default=0.01,
        description="This is the overall minimum thickness of all added layers. If for any case the overall layer thickness is smaller than this value, the layer addition process is stopped and no layers are added. In case the 'Use relative size for layers?' option in the global settings is set to 'true', this thickness is relative to the undistorted size of the cells in the internal mesh directly next to the boundary layer.",
    )
    final_layer_thickness: float | None = Field(
        validation_alias="finalLayerThickness",
        serialization_alias="finalLayerThickness",
        default=0.3,
        description="Specify the desired final layer thickness farthest away from the wall on which the boundary layer is grown. If the 'Layer Size' toggle in the hex-parametric global settings is turned on, this thickness is relative to the undistorted size of the cells in the internal mesh directly next to the boundary layer.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
