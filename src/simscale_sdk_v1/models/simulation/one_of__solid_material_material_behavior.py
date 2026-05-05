from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.hyper_elastic_material_behavior import HyperElasticMaterialBehavior
from simscale_sdk_v1.models.simulation.linear_elastic_material_behavior import LinearElasticMaterialBehavior
from simscale_sdk_v1.models.simulation.plastic_material_behavior import PlasticMaterialBehavior

_ONE_OF__SOLID_MATERIAL_MATERIAL_BEHAVIOR_VARIANTS: dict[str, type] = {
    "LINEAR_ELASTIC": LinearElasticMaterialBehavior,
    "HYPER_ELASTIC": HyperElasticMaterialBehavior,
    "PLASTIC": PlasticMaterialBehavior,
}

OneOf_SolidMaterialMaterialBehavior = Annotated[
    Union[LinearElasticMaterialBehavior, HyperElasticMaterialBehavior, PlasticMaterialBehavior],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_MATERIAL_MATERIAL_BEHAVIOR_VARIANTS,
        )
    ),
]
