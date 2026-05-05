from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_conductivity import IsotropicConductivity
from simscale_sdk_v1.models.simulation.orthotropic_conductivity import OrthotropicConductivity

_ONE_OF__SOLID_MATERIAL_CONDUCTIVITY_VARIANTS: dict[str, type] = {
    "ISOTROPIC": IsotropicConductivity,
    "ORTHOTROPIC": OrthotropicConductivity,
}

OneOf_SolidMaterialConductivity = Annotated[
    Union[IsotropicConductivity, OrthotropicConductivity],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_MATERIAL_CONDUCTIVITY_VARIANTS,
        )
    ),
]
