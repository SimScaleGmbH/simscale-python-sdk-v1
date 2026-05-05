from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.distributed_orthotropic_stiffness_definition import (
    DistributedOrthotropicStiffnessDefinition,
)
from simscale_sdk_v1.models.simulation.total_orthotropic_stiffness_definition import TotalOrthotropicStiffnessDefinition

# The resulting stiffness of the elastic support can be defined either via the total stiffness expressed as force per length or the distributed stiffness expressed as force per length per area.
_ONE_OF__ORTHOTROPIC_SPRING_STIFFNESS_STIFFNESS_DEFINITION_VARIANTS: dict[str, type] = {
    "TOTAL_ORTHOTROPIC": TotalOrthotropicStiffnessDefinition,
    "DISTRIBUTED_ORTHOTROPIC": DistributedOrthotropicStiffnessDefinition,
}

OneOf_OrthotropicSpringStiffnessStiffnessDefinition = Annotated[
    Union[TotalOrthotropicStiffnessDefinition, DistributedOrthotropicStiffnessDefinition],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ORTHOTROPIC_SPRING_STIFFNESS_STIFFNESS_DEFINITION_VARIANTS,
        )
    ),
]
