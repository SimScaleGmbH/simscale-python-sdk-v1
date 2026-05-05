from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CometsVisualizationStyle(SimScaleModel):
    representation: str = Field(default="COMETS", description="The representation to use for particle traces.")
    num_pulses: int = Field(
        validation_alias="numPulses",
        serialization_alias="numPulses",
        default=15,
        description="This value specifies how many pulses there should be in the model.",
    )
    relative_comet_length: float = Field(
        validation_alias="relativeCometLength",
        serialization_alias="relativeCometLength",
        default=1e-05,
        description="The length of the tail of the comets. It is specified in time and is a fraction of the global total time range for all particles in this particle trace. For example, if the total trace time is 2, and the relativeCometLength is 0.01, then the length of the tail will be 0.02.",
    )
