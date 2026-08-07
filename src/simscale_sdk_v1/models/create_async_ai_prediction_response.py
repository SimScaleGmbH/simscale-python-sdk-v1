from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateAsyncAiPredictionResponse(SimScaleModel):
    prediction_id: str | None = Field(validation_alias="predictionId", serialization_alias="predictionId", default=None)
    status: str | None = Field(
        default=None,
        description="RUNNING - Prediction is in progress, poll GET /ai/predictions/{predictionId} for the results",
    )
