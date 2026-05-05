from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.distributed_isotropic_stiffness_definition import (
    DistributedIsotropicStiffnessDefinition,
)
from simscale_sdk_v1.models.simulation.total_isotropic_stiffness_definition import TotalIsotropicStiffnessDefinition

# The resulting stiffness of the elastic support can be defined either via the total stiffness expressed as force per length or the distributed stiffness expressed as force per length per area.
_ONE_OF__ISOTROPIC_SPRING_STIFFNESS_STIFFNESS_DEFINITION_VARIANTS: dict[str, type] = {
    "TOTAL_ISOTROPIC": TotalIsotropicStiffnessDefinition,
    "DISTRIBUTED_ISOTROPIC": DistributedIsotropicStiffnessDefinition,
}

OneOf_IsotropicSpringStiffnessStiffnessDefinition = Annotated[
    Union[TotalIsotropicStiffnessDefinition, DistributedIsotropicStiffnessDefinition],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ISOTROPIC_SPRING_STIFFNESS_STIFFNESS_DEFINITION_VARIANTS,
        )
    ),
]
