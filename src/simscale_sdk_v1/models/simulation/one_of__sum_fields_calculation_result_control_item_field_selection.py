from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.force_field_selection import ForceFieldSelection
from simscale_sdk_v1.models.simulation.moment_field_selection import MomentFieldSelection

_ONE_OF__SUM_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "FORCE": ForceFieldSelection,
    "MOMENT": MomentFieldSelection,
}

OneOf_SumFieldsCalculationResultControlItemFieldSelection = Annotated[
    Union[ForceFieldSelection, MomentFieldSelection],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SUM_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS,
        )
    ),
]
