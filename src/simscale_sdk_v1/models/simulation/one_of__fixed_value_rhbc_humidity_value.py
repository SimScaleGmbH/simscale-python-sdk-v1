from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_humidity_value import AbsoluteHumidityValue
from simscale_sdk_v1.models.simulation.relative_humidity_value import RelativeHumidityValue
from simscale_sdk_v1.models.simulation.specific_humidity_value import SpecificHumidityValue

_ONE_OF__FIXED_VALUE_RHBC_HUMIDITY_VALUE_VARIANTS: dict[str, type] = {
    "RELATIVE_HUMIDITY_VALUE": RelativeHumidityValue,
    "SPECIFIC_HUMIDITY_VALUE": SpecificHumidityValue,
    "ABSOLUTE_HUMIDITY_VALUE": AbsoluteHumidityValue,
}

OneOf_FixedValueRHBCHumidityValue = Annotated[
    Union[RelativeHumidityValue, SpecificHumidityValue, AbsoluteHumidityValue],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIXED_VALUE_RHBC_HUMIDITY_VALUE_VARIANTS,
        )
    ),
]
