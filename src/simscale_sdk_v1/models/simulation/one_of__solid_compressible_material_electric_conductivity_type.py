from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.dielectric import Dielectric
from simscale_sdk_v1.models.simulation.isotropic_electric_conductivity import IsotropicElectricConductivity
from simscale_sdk_v1.models.simulation.orthotropic_electric_conductivity import OrthotropicElectricConductivity

_ONE_OF__SOLID_COMPRESSIBLE_MATERIAL_ELECTRIC_CONDUCTIVITY_TYPE_VARIANTS: dict[str, type] = {
    "DIELECTRIC": Dielectric,
    "ISOTROPIC_ELECTRIC_CONDUCTIVITY": IsotropicElectricConductivity,
    "ORTHOTROPIC_ELECTRIC_CONDUCTIVITY": OrthotropicElectricConductivity,
}

OneOf_SolidCompressibleMaterialElectricConductivityType = Annotated[
    Union[Dielectric, IsotropicElectricConductivity, OrthotropicElectricConductivity],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_COMPRESSIBLE_MATERIAL_ELECTRIC_CONDUCTIVITY_TYPE_VARIANTS,
        )
    ),
]
