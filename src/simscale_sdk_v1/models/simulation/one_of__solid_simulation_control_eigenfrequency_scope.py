from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.center_frequency import CenterFrequency
from simscale_sdk_v1.models.simulation.first_mode import FirstMode
from simscale_sdk_v1.models.simulation.frequency_range import FrequencyRange

# Select how you want to control natural frequencies to be computed: First modes: The first Number of modes will be searched and computed, in the order of low to high frequency.Frequency range: All the modes within the range of frequencies will be searched and computed. The frequency range is specified by a Start frequency and an End frequency.Center frequency: Compute the Number of modes closest to the frequency defined by Center frequency.
_ONE_OF__SOLID_SIMULATION_CONTROL_EIGENFREQUENCY_SCOPE_VARIANTS: dict[str, type] = {
    "FIRSTMODE": FirstMode,
    "RANGE": FrequencyRange,
    "CENTER": CenterFrequency,
}

OneOf_SolidSimulationControlEigenfrequencyScope = Annotated[
    Union[FirstMode, FrequencyRange, CenterFrequency],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_SIMULATION_CONTROL_EIGENFREQUENCY_SCOPE_VARIANTS,
        )
    ),
]
