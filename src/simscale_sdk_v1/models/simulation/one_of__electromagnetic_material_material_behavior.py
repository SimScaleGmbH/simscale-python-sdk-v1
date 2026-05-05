from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.permanent_magnet_material import PermanentMagnetMaterial
from simscale_sdk_v1.models.simulation.soft_magnetic_material import SoftMagneticMaterial

_ONE_OF__ELECTROMAGNETIC_MATERIAL_MATERIAL_BEHAVIOR_VARIANTS: dict[str, type] = {
    "SOFT_MAGNETIC": SoftMagneticMaterial,
    "PERMANENT_MAGNET": PermanentMagnetMaterial,
}

OneOf_ElectromagneticMaterialMaterialBehavior = Annotated[
    Union[SoftMagneticMaterial, PermanentMagnetMaterial],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_MATERIAL_MATERIAL_BEHAVIOR_VARIANTS,
        )
    ),
]
