from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class AdvancedSimmetrixFluidSettings(SimScaleModel):
    small_feature_tolerance: Dimensional_Length | None = Field(
        validation_alias="smallFeatureTolerance", serialization_alias="smallFeatureTolerance", default=None
    )
    gap_elements: float | None = Field(
        validation_alias="gapElements",
        serialization_alias="gapElements",
        default=0.05,
        description="Define a target number of elements across thin gaps. The Gap refinement factor is the ratio between gap thickness and the cell longest edge in that gap. Learn more.Example of gap refinements applied with a target of 4 elements across the thickness",
    )
    global_gradation_rate: float | None = Field(
        validation_alias="globalGradationRate",
        serialization_alias="globalGradationRate",
        default=1.22,
        description="Adjust the transition from small to large cells. This value is the ratio between the size of two adjacent cells. The allowed range is 1.0 - 3.0. 1.0 would produce a uniform mesh with the smallest size everywhere. This is generally not recommended, as it may produce very large meshes.",
    )
