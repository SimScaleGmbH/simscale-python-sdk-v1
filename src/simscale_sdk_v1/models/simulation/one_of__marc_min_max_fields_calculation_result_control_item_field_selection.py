from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_contact_field_selection import MarcContactFieldSelection
from simscale_sdk_v1.models.simulation.marc_displacement_field_selection import MarcDisplacementFieldSelection
from simscale_sdk_v1.models.simulation.marc_pressure_field_selection import MarcPressureFieldSelection
from simscale_sdk_v1.models.simulation.marc_strain_field_selection import MarcStrainFieldSelection
from simscale_sdk_v1.models.simulation.marc_stress_field_selection import MarcStressFieldSelection

_ONE_OF__MARC_MIN_MAX_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "DISPLACEMENT": MarcDisplacementFieldSelection,
    "PRESSURE": MarcPressureFieldSelection,
    "STRESS": MarcStressFieldSelection,
    "STRAIN": MarcStrainFieldSelection,
    "CONTACT": MarcContactFieldSelection,
}

OneOf_MarcMinMaxFieldsCalculationResultControlItemFieldSelection = Annotated[
    Union[
        MarcDisplacementFieldSelection,
        MarcPressureFieldSelection,
        MarcStressFieldSelection,
        MarcStrainFieldSelection,
        MarcContactFieldSelection,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_MIN_MAX_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS,
        )
    ),
]
