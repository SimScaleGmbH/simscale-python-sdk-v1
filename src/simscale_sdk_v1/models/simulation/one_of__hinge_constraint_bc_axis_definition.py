from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_axis_definition import AutomaticAxisDefinition
from simscale_sdk_v1.models.simulation.custom_axis_definition import CustomAxisDefinition

_ONE_OF__HINGE_CONSTRAINT_BC_AXIS_DEFINITION_VARIANTS: dict[str, type] = {
    "CUSTOM": CustomAxisDefinition,
    "AUTOMATIC": AutomaticAxisDefinition,
}

OneOf_HingeConstraintBCAxisDefinition = Annotated[
    Union[CustomAxisDefinition, AutomaticAxisDefinition],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HINGE_CONSTRAINT_BC_AXIS_DEFINITION_VARIANTS,
        )
    ),
]
