from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Users:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_current_user(self) -> models.User:
        """Get information about the currently authenticated user



        Get information about the currently authenticated user, such as name and email.
        """
        return self._client.request(
            "GET",
            "/users/me",
            response_type=models.User,
        )

    def signup_user(
        self,
        body: models.UserSignupRequest,
    ) -> models.UserSignupResponse:
        """Signup a user



        Signup a new user. The current requester user needs to be authenticated.
        """
        return self._client.request(
            "POST",
            "/users",
            json_body=body,
            response_type=models.UserSignupResponse,
        )
