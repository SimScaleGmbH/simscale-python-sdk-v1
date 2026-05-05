from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_power_source import AbsolutePowerSource
from simscale_sdk_v1.models.simulation.heat_exchanger_source import HeatExchangerSource
from simscale_sdk_v1.models.simulation.specific_power_source import SpecificPowerSource
from simscale_sdk_v1.models.simulation.tr_absolute_power_source import TrAbsolutePowerSource
from simscale_sdk_v1.models.simulation.tr_specific_power_source import TrSpecificPowerSource

_ONE_OF__ADVANCED_CONCEPTS_POWER_SOURCES_VARIANTS: dict[str, type] = {
    "ABSOLUTE_V23": AbsolutePowerSource,
    "SPECIFIC_V23": SpecificPowerSource,
    "HEAT_EXCHANGER_SOURCE": HeatExchangerSource,
    "TR_ABSOLUTE_POWER_SOURCE": TrAbsolutePowerSource,
    "TR_SPECIFIC_POWER_SOURCE": TrSpecificPowerSource,
}

OneOf_AdvancedConceptsPowerSources = Annotated[
    Union[AbsolutePowerSource, SpecificPowerSource, HeatExchangerSource, TrAbsolutePowerSource, TrSpecificPowerSource],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_POWER_SOURCES_VARIANTS,
        )
    ),
]
