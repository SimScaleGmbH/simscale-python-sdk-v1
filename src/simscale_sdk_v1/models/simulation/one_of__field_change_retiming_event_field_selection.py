from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cauchy_stress_tensor_field import CauchyStressTensorField
from simscale_sdk_v1.models.simulation.displacement_field import DisplacementField
from simscale_sdk_v1.models.simulation.intern_variables_field import InternVariablesField

_ONE_OF__FIELD_CHANGE_RETIMING_EVENT_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "DISPLACEMENT": DisplacementField,
    "CAUCHY_STRESS_TENSOR": CauchyStressTensorField,
    "INTERN_VARIABLES": InternVariablesField,
}

OneOf_FieldChangeRetimingEventFieldSelection = Annotated[
    Union[DisplacementField, CauchyStressTensorField, InternVariablesField],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIELD_CHANGE_RETIMING_EVENT_FIELD_SELECTION_VARIANTS,
        )
    ),
]
