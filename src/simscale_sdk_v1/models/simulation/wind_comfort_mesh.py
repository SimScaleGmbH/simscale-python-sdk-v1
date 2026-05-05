from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_automatic_gap_closing import (
    OneOf_WindComfortMeshAutomaticGapClosing,
)
from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_refinements import OneOf_WindComfortMeshRefinements
from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_reynolds_scaling_type import (
    OneOf_WindComfortMeshReynoldsScalingType,
)
from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_wind_comfort_fineness import (
    OneOf_WindComfortMeshWindComfortFineness,
)
from simscale_sdk_v1.models.simulation.progressive_refinement import ProgressiveRefinement


class WindComfortMesh(SimScaleModel):
    wind_comfort_fineness: OneOf_WindComfortMeshWindComfortFineness | None = Field(
        validation_alias="windComfortFineness", serialization_alias="windComfortFineness", default=None
    )
    automatic_gap_closing: OneOf_WindComfortMeshAutomaticGapClosing | None = Field(
        validation_alias="automaticGapClosing", serialization_alias="automaticGapClosing", default=None
    )
    progressive_refinement: ProgressiveRefinement | None = Field(
        validation_alias="progressiveRefinement", serialization_alias="progressiveRefinement", default=None
    )
    reynolds_scaling_type: OneOf_WindComfortMeshReynoldsScalingType | None = Field(
        validation_alias="reynoldsScalingType", serialization_alias="reynoldsScalingType", default=None
    )
    refinements: list[OneOf_WindComfortMeshRefinements] | None = Field(default=None)
