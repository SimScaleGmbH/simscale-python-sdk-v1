from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class DebugMeshSizingSimmetrix(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DEBUG",
        description="Schema name: DebugMeshSizingSimmetrix",
    )
    maximum_edge_length: Dimensional_Length | None = Field(
        validation_alias="maximumEdgeLength", serialization_alias="maximumEdgeLength", default=None
    )
    minimum_edge_length: Dimensional_Length | None = Field(
        validation_alias="minimumEdgeLength", serialization_alias="minimumEdgeLength", default=None
    )
    chordal_error: float | None = Field(
        validation_alias="chordalError", serialization_alias="chordalError", default=0.4
    )
    min_curv_ref: float | None = Field(validation_alias="minCurvRef", serialization_alias="minCurvRef", default=0.0)
    gradation_rate: float | None = Field(
        validation_alias="gradationRate", serialization_alias="gradationRate", default=0.66
    )
    prox_ref_factor: float | None = Field(
        validation_alias="proxRefFactor", serialization_alias="proxRefFactor", default=0.0
    )
    min_prox_size: Dimensional_Length | None = Field(
        validation_alias="minProxSize", serialization_alias="minProxSize", default=None
    )
    small_feature_tol: float | None = Field(
        validation_alias="smallFeatureTol", serialization_alias="smallFeatureTol", default=0.0
    )
    layer_adjustment_behaviour: Literal["SHRINKING", "TRIMMING"] | None = Field(
        validation_alias="layerAdjustmentBehaviour", serialization_alias="layerAdjustmentBehaviour", default="SHRINKING"
    )
    layer_height_gradation_rate: float | None = Field(
        validation_alias="layerHeightGradationRate", serialization_alias="layerHeightGradationRate", default=0.66
    )
    surf_skewness: float | None = Field(
        validation_alias="surfSkewness", serialization_alias="surfSkewness", default=0.7
    )
    vol_len_ratio: float | None = Field(validation_alias="volLenRatio", serialization_alias="volLenRatio", default=0.15)
