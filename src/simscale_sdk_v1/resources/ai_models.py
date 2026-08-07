from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class AiModels:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_async_prediction(
        self,
        body: models.CreateAiPredictionRequest,
    ) -> models.CreateAsyncAiPredictionResponse:
        """Start an AI prediction for a simulation based on an AI model



        Starts the prediction and returns immediately, without waiting for the results. Poll

        GET /ai/predictions/{predictionId} for the status and the results.
        """
        return self._client.request(
            "POST",
            "/ai/predictions",
            json_body=body,
            response_type=models.CreateAsyncAiPredictionResponse,
        )

    def create_prediction(
        self,
        body: models.CreateAiPredictionRequest,
    ) -> models.CreateAiPredictionResponse:
        """Generate an AI prediction for a simulation based on an AI model



        Waits for the prediction to finish and returns the results. Predictions that take longer

        than 50 seconds time out, use POST /v1/ai/predictions for those.
        """
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

    def get_prediction(
        self,
        prediction_id: str,
    ) -> models.GetAiPredictionResponse:
        """Get the status of an AI prediction, and its results if it is done"""
        return self._client.request(
            "GET",
            f"/ai/predictions/{prediction_id}",
            response_type=models.GetAiPredictionResponse,
        )
