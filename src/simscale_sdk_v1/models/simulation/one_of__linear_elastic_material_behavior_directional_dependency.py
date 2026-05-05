from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_directional_dependency import IsotropicDirectionalDependency
from simscale_sdk_v1.models.simulation.orthotropic_directional_dependency import OrthotropicDirectionalDependency

# Choose the directional dependency for this property:Isotropic material: all the material properties are the same in all directionsOrthotropic material: different material properties in different orthogonal directions (e.g. glass-reinforced plastic, or wood)
_ONE_OF__LINEAR_ELASTIC_MATERIAL_BEHAVIOR_DIRECTIONAL_DEPENDENCY_VARIANTS: dict[str, type] = {
    "ISOTROPIC": IsotropicDirectionalDependency,
    "ORTHOTROPIC": OrthotropicDirectionalDependency,
}

OneOf_LinearElasticMaterialBehaviorDirectionalDependency = Annotated[
    Union[IsotropicDirectionalDependency, OrthotropicDirectionalDependency],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__LINEAR_ELASTIC_MATERIAL_BEHAVIOR_DIRECTIONAL_DEPENDENCY_VARIANTS,
        )
    ),
]
