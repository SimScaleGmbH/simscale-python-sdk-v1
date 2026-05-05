from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.box_with_unit import BoxWithUnit


class FlowVolumeExtractionExternalParameters(SimScaleModel):
    flow_box: BoxWithUnit
    seed_face: str | None = Field(
        default=None,
        description="Seed face indicating an area adjacent to the flow. A seed face is needed only when the flow is unclear and could correspond to multiple solid regions.",
    )
    excluded_parts: list[str] | None = Field(
        default=None, description="List of solid regions and/or sheet bodies to exclude from the flow volume."
    )
