from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class UserSignupResponse(SimScaleModel):
    email: str
    user_id: str = Field(validation_alias="userId", serialization_alias="userId")
