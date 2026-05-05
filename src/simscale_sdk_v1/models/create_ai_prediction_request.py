from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateAiPredictionRequest(SimScaleModel):
    ai_model_id: str = Field(validation_alias="aiModelId", serialization_alias="aiModelId")
    project_id: str = Field(validation_alias="projectId", serialization_alias="projectId")
    simulation_id: str = Field(validation_alias="simulationId", serialization_alias="simulationId")
