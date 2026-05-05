from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_contact_force_field_selection import MarcContactForceFieldSelection
from simscale_sdk_v1.models.simulation.marc_force_field_selection import MarcForceFieldSelection

_ONE_OF__MARC_SUM_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "FORCE": MarcForceFieldSelection,
    "CONTACT_FORCE": MarcContactForceFieldSelection,
}

OneOf_MarcSumFieldsCalculationResultControlItemFieldSelection = Annotated[
    Union[MarcForceFieldSelection, MarcContactForceFieldSelection],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_SUM_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS,
        )
    ),
]
