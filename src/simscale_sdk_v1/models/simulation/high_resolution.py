from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class HighResolution(SimScaleModel):
    """Output will be written every 2 time steps."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HIGH_RESOLUTION",
        description="Output will be written every 2 time steps.  Schema name: HighResolution",
    )
