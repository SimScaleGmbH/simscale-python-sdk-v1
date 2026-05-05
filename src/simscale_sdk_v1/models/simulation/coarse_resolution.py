from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CoarseResolution(SimScaleModel):
    """Output will be written every 8 time steps."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COARSE_RESOLUTION",
        description="Output will be written every 8 time steps.  Schema name: CoarseResolution",
    )
