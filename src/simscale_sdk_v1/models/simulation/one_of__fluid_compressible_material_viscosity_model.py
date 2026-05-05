from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.newtonian_viscosity_model import NewtonianViscosityModel
from simscale_sdk_v1.models.simulation.sutherland_viscosity import SutherlandViscosity

_ONE_OF__FLUID_COMPRESSIBLE_MATERIAL_VISCOSITY_MODEL_VARIANTS: dict[str, type] = {
    "NEWTONIAN": NewtonianViscosityModel,
    "SUTHERLAND_VISCOSITY": SutherlandViscosity,
}

OneOf_FluidCompressibleMaterialViscosityModel = Annotated[
    Union[NewtonianViscosityModel, SutherlandViscosity],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_COMPRESSIBLE_MATERIAL_VISCOSITY_MODEL_VARIANTS,
        )
    ),
]
