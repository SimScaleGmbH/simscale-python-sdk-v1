from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.friction_augmented_lagrange_coef import FrictionAugmentedLagrangeCoef
from simscale_sdk_v1.models.simulation.friction_penalty_coef import FrictionPenaltyCoef

_ONE_OF__FRICTION_CONTACT_FRICTION_COEFFICIENT_VARIANTS: dict[str, type] = {
    "FRICTION_AUGMENTATION_COEF": FrictionAugmentedLagrangeCoef,
    "FRICTION_PENALTY_COEF": FrictionPenaltyCoef,
}

OneOf_FrictionContactFrictionCoefficient = Annotated[
    Union[FrictionAugmentedLagrangeCoef, FrictionPenaltyCoef],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FRICTION_CONTACT_FRICTION_COEFFICIENT_VARIANTS,
        )
    ),
]
