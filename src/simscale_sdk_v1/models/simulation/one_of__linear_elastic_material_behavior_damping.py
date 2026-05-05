from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.global_damping_value import GlobalDampingValue
from simscale_sdk_v1.models.simulation.hysteretic_damping import HystereticDamping
from simscale_sdk_v1.models.simulation.none_damping import NoneDamping
from simscale_sdk_v1.models.simulation.rayleigh_damping import RayleighDamping

_ONE_OF__LINEAR_ELASTIC_MATERIAL_BEHAVIOR_DAMPING_VARIANTS: dict[str, type] = {
    "NONE": NoneDamping,
    "RAYLEIGH": RayleighDamping,
    "HYSTERETIC": HystereticDamping,
    "GLOBAL_DAMPING_VALUE": GlobalDampingValue,
}

OneOf_LinearElasticMaterialBehaviorDamping = Annotated[
    Union[NoneDamping, RayleighDamping, HystereticDamping, GlobalDampingValue],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__LINEAR_ELASTIC_MATERIAL_BEHAVIOR_DAMPING_VARIANTS,
        )
    ),
]
