from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FlowVolumeExtractionInternalParameters(SimScaleModel):
    seed_face: str | None = Field(default=None, description="Seed face indicating an area adjacent to the flow.")
    boundary_faces: list[str] | None = Field(
        default=None,
        description="List of faces representing the boundary of the internal flow region. Boundary faces are needed in case the internal flow is not bounded by the geometry.",
    )
    excluded_parts: list[str] | None = Field(
        default=None, description="List of solid regions and/or sheet bodies to exclude from the flow volume."
    )
