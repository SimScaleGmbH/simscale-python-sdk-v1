from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fluid_type_gas import FluidTypeGas
from simscale_sdk_v1.models.simulation.fluid_type_liquid import FluidTypeLiquid

_ONE_OF__INCOMPRESSIBLE_MATERIAL_FLUID_TYPE_VARIANTS: dict[str, type] = {
    "LIQUID": FluidTypeLiquid,
    "GAS": FluidTypeGas,
}

OneOf_IncompressibleMaterialFluidType = Annotated[
    Union[FluidTypeLiquid, FluidTypeGas],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__INCOMPRESSIBLE_MATERIAL_FLUID_TYPE_VARIANTS,
        )
    ),
]
