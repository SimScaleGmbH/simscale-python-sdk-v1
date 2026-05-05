from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cluster_around_modes import ClusterAroundModes
from simscale_sdk_v1.models.simulation.cover_spectrum import CoverSpectrum
from simscale_sdk_v1.models.simulation.frequency_list import FrequencyList
from simscale_sdk_v1.models.simulation.single_frequency import SingleFrequency

# Frequencies at which the harmonic loads are to be applied and results are to be computed. Define excitation frequencies using one of the following options: Single frequency : Harmonic loads are applied at one frequency only.Frequency list: Harmonic loads are applied across a range of frequencies with either a constant frequency stepping interval or a variable interval defined via a table.Cluster around modes: Harmonic loads are applied at frequencies clustered around eigenfrequencies.Cover spectrum: Harmonic loads are applied at frequencies clustered around and in between eigenfrequencies to fully capture the entire spectrum.
_ONE_OF__HARMONIC_RESPONSE_CONTROL_EXCITATION_FREQUENCIES_VARIANTS: dict[str, type] = {
    "SINGLE": SingleFrequency,
    "LIST_V20": FrequencyList,
    "CLUSTER_AROUND_MODES": ClusterAroundModes,
    "COVER_SPECTRUM": CoverSpectrum,
}

OneOf_HarmonicResponseControlExcitationFrequencies = Annotated[
    Union[SingleFrequency, FrequencyList, ClusterAroundModes, CoverSpectrum],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HARMONIC_RESPONSE_CONTROL_EXCITATION_FREQUENCIES_VARIANTS,
        )
    ),
]
