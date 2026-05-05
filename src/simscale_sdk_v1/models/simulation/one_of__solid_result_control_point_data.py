from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.harmonic_response_result_control_item import HarmonicResponseResultControlItem
from simscale_sdk_v1.models.simulation.temporal_response_result_control_item import TemporalResponseResultControlItem

_ONE_OF__SOLID_RESULT_CONTROL_POINT_DATA_VARIANTS: dict[str, type] = {
    "TEMPORAL_RESPONSE": TemporalResponseResultControlItem,
    "HARMONIC_RESPONSE": HarmonicResponseResultControlItem,
}

OneOf_SolidResultControlPointData = Annotated[
    Union[TemporalResponseResultControlItem, HarmonicResponseResultControlItem],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_RESULT_CONTROL_POINT_DATA_VARIANTS,
        )
    ),
]
