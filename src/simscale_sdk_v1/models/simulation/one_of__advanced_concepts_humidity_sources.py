from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.species_humidity_source import SpeciesHumiditySource
from simscale_sdk_v1.models.simulation.volumetric_species_humidity_source import VolumetricSpeciesHumiditySource

_ONE_OF__ADVANCED_CONCEPTS_HUMIDITY_SOURCES_VARIANTS: dict[str, type] = {
    "SPECIES_MASS_FLOW_RATE": SpeciesHumiditySource,
    "VOLUMETRIC_SPECIES_MASS_FLOW_RATE": VolumetricSpeciesHumiditySource,
}

OneOf_AdvancedConceptsHumiditySources = Annotated[
    Union[SpeciesHumiditySource, VolumetricSpeciesHumiditySource],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_HUMIDITY_SOURCES_VARIANTS,
        )
    ),
]
