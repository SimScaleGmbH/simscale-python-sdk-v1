from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.manual_reynolds_scaling import ManualReynoldsScaling
from simscale_sdk_v1.models.simulation.one_of__pacefish_mesh_legacy_refinements import (
    OneOf_PacefishMeshLegacyRefinements,
)
from simscale_sdk_v1.models.simulation.progressive_refinement import ProgressiveRefinement


class PacefishMeshLegacy(SimScaleModel):
    """Choose between Automatic and Manual mesh settings. Learn more.Note: Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PACEFISH_MESH_LEGACY",
        description="Choose between Automatic and Manual mesh settings. Learn more.Note: Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.  Schema name: PacefishMeshLegacy",
    )
    fineness: Literal["VERY_COARSE", "COARSE", "MODERATE", "FINE", "VERY_FINE"] | None = Field(default="COARSE")
    progressive_refinement: ProgressiveRefinement | None = Field(
        validation_alias="progressiveRefinement", serialization_alias="progressiveRefinement", default=None
    )
    reference_length: Dimensional_Length | None = Field(
        validation_alias="referenceLength", serialization_alias="referenceLength", default=None
    )
    reynolds_scaling_type: ManualReynoldsScaling | None = Field(
        validation_alias="reynoldsScalingType", serialization_alias="reynoldsScalingType", default=None
    )
    refinements: list[OneOf_PacefishMeshLegacyRefinements] | None = Field(default=None)
