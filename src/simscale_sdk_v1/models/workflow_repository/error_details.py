from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflow_repository.error_parameter import ErrorParameter


class ErrorDetails(SimScaleModel):
    parameters: list[ErrorParameter] | None = Field(default=None)
