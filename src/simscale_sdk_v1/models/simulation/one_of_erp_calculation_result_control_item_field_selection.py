from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_erp_field_selection import AbsoluteERPFieldSelection
from simscale_sdk_v1.models.simulation.relative_erp_field_selection import RelativeERPFieldSelection

_ONE_OF_ERP_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "ABSOLUTE_ERP": AbsoluteERPFieldSelection,
    "RELATIVE_ERP": RelativeERPFieldSelection,
}

OneOf_ERPCalculationResultControlItemFieldSelection = Annotated[
    Union[AbsoluteERPFieldSelection, RelativeERPFieldSelection],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_ERP_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS,
        )
    ),
]
