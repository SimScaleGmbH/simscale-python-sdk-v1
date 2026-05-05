from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.center_frequency import CenterFrequency
from simscale_sdk_v1.models.simulation.first_mode import FirstMode
from simscale_sdk_v1.models.simulation.frequency_range import FrequencyRange
from simscale_sdk_v1.models.simulation.twice_max_loading_frequency import TwiceMaxLoadingFrequency

# Select the method to build the modal base, by controlling the search of the natural frequencies: Twice the maximum loading frequency: From zero to twice the maximum excitation frequency defined under Harmonic response.First modes: The first Number of modes will be searched and computed in the order of low to high frequency.Frequency range: All the modes within the specified frequency range will be searched and computed. The frequency range is defined by a Start frequency and an End frequency.Center frequency: Compute the Number of modes closest to the frequency defined by the Center frequency.
_ONE_OF__MODAL_BASE_CONTROL_EIGENFREQUENCY_SCOPE_VARIANTS: dict[str, type] = {
    "TWICE_MAX_LOADING_FREQUENCY": TwiceMaxLoadingFrequency,
    "FIRSTMODE": FirstMode,
    "RANGE": FrequencyRange,
    "CENTER": CenterFrequency,
}

OneOf_ModalBaseControlEigenfrequencyScope = Annotated[
    Union[TwiceMaxLoadingFrequency, FirstMode, FrequencyRange, CenterFrequency],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MODAL_BASE_CONTROL_EIGENFREQUENCY_SCOPE_VARIANTS,
        )
    ),
]
