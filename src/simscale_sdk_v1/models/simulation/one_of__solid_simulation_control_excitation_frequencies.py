from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.frequency_list import FrequencyList
from simscale_sdk_v1.models.simulation.single_frequency import SingleFrequency

# Set the frequencies for the harmonic excitation. Setting it to single frequency will only compute harmonic excitation on that frequency. To have harmonic excitations on multiple frequencies, please choose frequency list.
_ONE_OF__SOLID_SIMULATION_CONTROL_EXCITATION_FREQUENCIES_VARIANTS: dict[str, type] = {
    "SINGLE": SingleFrequency,
    "LIST_V20": FrequencyList,
}

OneOf_SolidSimulationControlExcitationFrequencies = Annotated[
    Union[SingleFrequency, FrequencyList],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_SIMULATION_CONTROL_EXCITATION_FREQUENCIES_VARIANTS,
        )
    ),
]
