from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateAiPredictionResponse(SimScaleModel):
    prediction_id: str | None = Field(validation_alias="predictionId", serialization_alias="predictionId", default=None)
    result_id: str | None = Field(validation_alias="resultId", serialization_alias="resultId", default=None)
    available_fields: list[Any] | None = Field(
        validation_alias="availableFields", serialization_alias="availableFields", default=None
    )
    confidence_score: float | None = Field(
        validation_alias="confidenceScore", serialization_alias="confidenceScore", default=None
    )
    global_outputs: list[Any] | None = Field(
        validation_alias="globalOutputs", serialization_alias="globalOutputs", default=None
    )
