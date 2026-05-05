from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__harmonic_response_control_excitation_frequencies import (
    OneOf_HarmonicResponseControlExcitationFrequencies,
)


class HarmonicResponseControl(SimScaleModel):
    excitation_frequencies: OneOf_HarmonicResponseControlExcitationFrequencies | None = Field(
        validation_alias="excitationFrequencies", serialization_alias="excitationFrequencies", default=None
    )
