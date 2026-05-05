from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.turbulence_intensity_tibc import TurbulenceIntensityTIBC
from simscale_sdk_v1.models.simulation.turbulence_kinetic_energy_tibc import TurbulenceKineticEnergyTIBC

_ONE_OF__VELOCITY_INLET_BC_TURBULENCE_INTENSITY_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": TurbulenceIntensityTIBC,
    "TURBULENCE_KINETIC_ENERGY": TurbulenceKineticEnergyTIBC,
}

OneOf_VelocityInletBCTurbulenceIntensity = Annotated[
    Union[TurbulenceIntensityTIBC, TurbulenceKineticEnergyTIBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VELOCITY_INLET_BC_TURBULENCE_INTENSITY_VARIANTS,
        )
    ),
]
