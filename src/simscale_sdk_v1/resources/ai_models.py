from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class AiModels:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_prediction(
        self,
        body: models.CreateAiPredictionRequest,
    ) -> models.CreateAiPredictionResponse:
        """Generate an AI prediction for a simulation based on an AI model"""
        return self._client.request(
            "POST",
            "/ai/predict",
            json_body=body,
            response_type=models.CreateAiPredictionResponse,
        )

    def get_ai_model(
        self,
        ai_model_id: str,
    ) -> models.AiUserModel:
        """Get specific AI model belonging to the user"""
        return self._client.request(
            "GET",
            f"/ai/models/{ai_model_id}",
            response_type=models.AiUserModel,
        )

    def get_ai_models(self) -> models.GetAiModelsResponse:
        """Get all AI models belonging to the user"""
        return self._client.request(
            "GET",
            "/ai/models",
            response_type=models.GetAiModelsResponse,
        )

    def get_available_ai_model(
        self,
        *,
        simulation_id: str | None = None,
        project_id: str | None = None,
    ) -> models.GetAvailableAiModelsResponse:
        """Get all AI model belonging to the user that can be used to run a specific simulation"""
        return self._client.request(
            "GET",
            "/ai/available-models",
            query_params={"simulationId": simulation_id, "projectId": project_id},
            response_type=models.GetAvailableAiModelsResponse,
        )
