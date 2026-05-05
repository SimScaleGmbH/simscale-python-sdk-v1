from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ModerateResolution(SimScaleModel):
    """Output will be written every 4 time steps."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MODERATE_RESOLUTION",
        description="Output will be written every 4 time steps.  Schema name: ModerateResolution",
    )
