from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_spring_stiffness import IsotropicSpringStiffness
from simscale_sdk_v1.models.simulation.orthotropic_spring_stiffness import OrthotropicSpringStiffness

# The stiffness can either be assumed equal in all directions by selecting isotropic or it can depend on the force direction by selecting orthotropic. For an orthotropic stiffness the stiffness value along each global coordinate direction can be given independently.
_ONE_OF__ELASTIC_SUPPORT_BC_SPRING_STIFFNESS_VARIANTS: dict[str, type] = {
    "ISOTROPIC": IsotropicSpringStiffness,
    "ORTHOTROPIC": OrthotropicSpringStiffness,
}

OneOf_ElasticSupportBCSpringStiffness = Annotated[
    Union[IsotropicSpringStiffness, OrthotropicSpringStiffness],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELASTIC_SUPPORT_BC_SPRING_STIFFNESS_VARIANTS,
        )
    ),
]
