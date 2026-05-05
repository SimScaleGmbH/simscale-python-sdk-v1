from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.augmented_lagrange_method import AugmentedLagrangeMethod
from simscale_sdk_v1.models.simulation.penalty_method import PenaltyMethod

_ONE_OF__FRICTION_CONTACT_CONTACT_SOLUTION_METHOD_VARIANTS: dict[str, type] = {
    "AUGMENTED_LAGRANGE": AugmentedLagrangeMethod,
    "PENALTY_METHOD": PenaltyMethod,
}

OneOf_FrictionContactContactSolutionMethod = Annotated[
    Union[AugmentedLagrangeMethod, PenaltyMethod],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FRICTION_CONTACT_CONTACT_SOLUTION_METHOD_VARIANTS,
        )
    ),
]
