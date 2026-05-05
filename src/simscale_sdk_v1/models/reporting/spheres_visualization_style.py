from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SpheresVisualizationStyle(SimScaleModel):
    representation: str = Field(default="SPHERES", description="The representation to use for particle traces.")
    num_pulses: int = Field(
        validation_alias="numPulses",
        serialization_alias="numPulses",
        default=15,
        description="This value specifies how many pulses there should be in the model.",
    )
