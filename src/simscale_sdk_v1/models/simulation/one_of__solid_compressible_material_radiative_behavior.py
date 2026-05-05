from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.opaque_material import OpaqueMaterial
from simscale_sdk_v1.models.simulation.semi_transparent_material import SemiTransparentMaterial
from simscale_sdk_v1.models.simulation.transparent_material import TransparentMaterial

_ONE_OF__SOLID_COMPRESSIBLE_MATERIAL_RADIATIVE_BEHAVIOR_VARIANTS: dict[str, type] = {
    "TRANSPARENT_MATERIAL": TransparentMaterial,
    "SEMI_TRANSPARENT_MATERIAL": SemiTransparentMaterial,
    "OPAQUE_MATERIAL": OpaqueMaterial,
}

OneOf_SolidCompressibleMaterialRadiativeBehavior = Annotated[
    Union[TransparentMaterial, SemiTransparentMaterial, OpaqueMaterial],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_COMPRESSIBLE_MATERIAL_RADIATIVE_BEHAVIOR_VARIANTS,
        )
    ),
]
