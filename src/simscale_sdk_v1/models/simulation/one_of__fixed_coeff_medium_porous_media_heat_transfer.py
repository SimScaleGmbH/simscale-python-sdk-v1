from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.effective_conductivity_heat_transfer import EffectiveConductivityHeatTransfer
from simscale_sdk_v1.models.simulation.fluid_only_heat_transfer import FluidOnlyHeatTransfer

# The heat transfer modelling inside the porous media matrix:Fluid only: This model uses exclusively the fluid thermal properties in the porous media region. Effective conductivity: This model takes the effective thermal conductivity for the fluid-solid porous matrix as a constant value or a tabulated velocity function.
_ONE_OF__FIXED_COEFF_MEDIUM_POROUS_MEDIA_HEAT_TRANSFER_VARIANTS: dict[str, type] = {
    "FLUID_ONLY_HEAT_TRANSFER": FluidOnlyHeatTransfer,
    "EFFECTIVE_CONDUCTIVITY_HEAT_TRANSFER": EffectiveConductivityHeatTransfer,
}

OneOf_FixedCoeffMediumPorousMediaHeatTransfer = Annotated[
    Union[FluidOnlyHeatTransfer, EffectiveConductivityHeatTransfer],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIXED_COEFF_MEDIUM_POROUS_MEDIA_HEAT_TRANSFER_VARIANTS,
        )
    ),
]
