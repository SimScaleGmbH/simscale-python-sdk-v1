from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_electric_conductivity_method import IsotropicElectricConductivityMethod

_ONE_OF__ELECTROMAGNETIC_MATERIAL_ELECTRIC_CONDUCTIVITY_TYPE_VARIANTS: dict[str, type] = {
    "ISOTROPIC_ELECTRIC_CONDUCTIVITY": IsotropicElectricConductivityMethod,
}

OneOf_ElectromagneticMaterialElectricConductivityType = Annotated[
    Union[IsotropicElectricConductivityMethod],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_MATERIAL_ELECTRIC_CONDUCTIVITY_TYPE_VARIANTS,
        )
    ),
]
