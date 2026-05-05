from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class LayerAdditionHexDominantSnappy(SimScaleModel):
    """Inflated boundary layers are used to resolve the boundary layer near walls (no-slip) which are in contact with the fluid. Using boundary layers is generally recommended for turbulent simulations."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LAYER_ADDITION_HEX_DOMINANT_SNAPPY",
        description="Inflated boundary layers are used to resolve the boundary layer near walls (no-slip) which are in contact with the fluid. Using boundary layers is generally recommended for turbulent simulations.  Schema name: LayerAdditionHexDominantSnappy",
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
        default=0.0,
        description="Specifies the overall minimum thickness of all layers combined. In case the overall thickness falls below this minimum thickness, no layers will be added for the affected areas.",
    )
    first_layer_thickness: float | None = Field(
        validation_alias="firstLayerThickness",
        serialization_alias="firstLayerThickness",
        default=0.055,
        description="Specifies the height (thickness) of the first layer that is closest to the surface. The first layer thickness is specified relative to the neighboring volume cell size after refinements.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
