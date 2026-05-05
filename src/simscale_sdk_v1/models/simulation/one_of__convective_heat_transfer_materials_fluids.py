from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fluid_compressible_material import FluidCompressibleMaterial
from simscale_sdk_v1.models.simulation.incompressible_material import IncompressibleMaterial

_ONE_OF__CONVECTIVE_HEAT_TRANSFER_MATERIALS_FLUIDS_VARIANTS: dict[str, type] = {
    "INCOMPRESSIBLE": IncompressibleMaterial,
    "COMPRESSIBLE": FluidCompressibleMaterial,
}

OneOf_ConvectiveHeatTransferMaterialsFluids = Annotated[
    Union[IncompressibleMaterial, FluidCompressibleMaterial],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONVECTIVE_HEAT_TRANSFER_MATERIALS_FLUIDS_VARIANTS,
        )
    ),
]
