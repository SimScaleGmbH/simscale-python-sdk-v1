from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.one_processor_estimation_value_model import OneProcessorEstimationValueModel
from simscale_sdk_v1.models.workflows.scaling_estimation_value_model import ScalingEstimationValueModel


class MethodResourceEstimationValueModel(SimScaleModel):
    one_processor_estimation: OneProcessorEstimationValueModel | None = Field(
        validation_alias="oneProcessorEstimation", serialization_alias="oneProcessorEstimation", default=None
    )
    scaling_estimation: ScalingEstimationValueModel | None = Field(
        validation_alias="scalingEstimation", serialization_alias="scalingEstimation", default=None
    )
