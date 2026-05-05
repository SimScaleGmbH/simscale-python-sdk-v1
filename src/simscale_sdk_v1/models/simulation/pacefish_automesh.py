from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_automatic_gap_closing import (
    OneOf_PacefishAutomeshAutomaticGapClosing,
)
from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_new_fineness import OneOf_PacefishAutomeshNewFineness
from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_primary_topology import (
    OneOf_PacefishAutomeshPrimaryTopology,
)
from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_reference_length_computation import (
    OneOf_PacefishAutomeshReferenceLengthComputation,
)
from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_refinements import OneOf_PacefishAutomeshRefinements
from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_reynolds_scaling_type import (
    OneOf_PacefishAutomeshReynoldsScalingType,
)
from simscale_sdk_v1.models.simulation.progressive_refinement import ProgressiveRefinement


class PacefishAutomesh(SimScaleModel):
    """Choose between Automatic and Manual mesh settings. Learn more.Note: Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PACEFISH_AUTOMESH",
        description="Choose between Automatic and Manual mesh settings. Learn more.Note: Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.  Schema name: PacefishAutomesh",
    )
    new_fineness: OneOf_PacefishAutomeshNewFineness | None = Field(
        validation_alias="newFineness", serialization_alias="newFineness", default=None
    )
    automatic_gap_closing: OneOf_PacefishAutomeshAutomaticGapClosing | None = Field(
        validation_alias="automaticGapClosing", serialization_alias="automaticGapClosing", default=None
    )
    progressive_refinement: ProgressiveRefinement | None = Field(
        validation_alias="progressiveRefinement", serialization_alias="progressiveRefinement", default=None
    )
    reference_length_computation: OneOf_PacefishAutomeshReferenceLengthComputation | None = Field(
        validation_alias="referenceLengthComputation", serialization_alias="referenceLengthComputation", default=None
    )
    reynolds_scaling_type: OneOf_PacefishAutomeshReynoldsScalingType | None = Field(
        validation_alias="reynoldsScalingType", serialization_alias="reynoldsScalingType", default=None
    )
    primary_topology: OneOf_PacefishAutomeshPrimaryTopology | None = Field(
        validation_alias="primaryTopology", serialization_alias="primaryTopology", default=None
    )
    refinements: list[OneOf_PacefishAutomeshRefinements] | None = Field(default=None)
