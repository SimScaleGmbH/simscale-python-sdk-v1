from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_dielectric_strength import IsotropicDielectricStrength
from simscale_sdk_v1.models.simulation.no_dielectric_strength import NoDielectricStrength

# Dielectric strength is the maximum electric field a dielectric material can withstand without electrical breakdown, beyond which it becomes conductive.
_ONE_OF__ELECTROMAGNETIC_MATERIAL_DIELECTRIC_STRENGTH_TYPE_VARIANTS: dict[str, type] = {
    "NONE": NoDielectricStrength,
    "ISOTROPIC": IsotropicDielectricStrength,
}

OneOf_ElectromagneticMaterialDielectricStrengthType = Annotated[
    Union[NoDielectricStrength, IsotropicDielectricStrength],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_MATERIAL_DIELECTRIC_STRENGTH_TYPE_VARIANTS,
        )
    ),
]
