from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WorkflowRunError(SimScaleModel):
    """Error information for a failed workflow run. Present only when the run is in the FAILED state."""

    code: str | None = Field(default=None)
    details: dict[str, str] | None = Field(default=None)
    message: str | None = Field(default=None)
