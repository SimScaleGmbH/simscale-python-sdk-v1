from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AvailableAiModel(SimScaleModel):
    ai_model_label: str | None = Field(
        validation_alias="aiModelLabel", serialization_alias="aiModelLabel", default=None
    )
    ai_model_id: str | None = Field(validation_alias="aiModelId", serialization_alias="aiModelId", default=None)
