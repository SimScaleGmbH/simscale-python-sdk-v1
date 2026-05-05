from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.convective_heat_flux_bc import ConvectiveHeatFluxBC
from simscale_sdk_v1.models.simulation.cyclic_symmetry_bc import CyclicSymmetryBC
from simscale_sdk_v1.models.simulation.fixed_temperature_value_bc import FixedTemperatureValueBC
from simscale_sdk_v1.models.simulation.surface_heat_flux_bc import SurfaceHeatFluxBC
from simscale_sdk_v1.models.simulation.volume_heat_flux_bc import VolumeHeatFluxBC

_ONE_OF__HEAT_TRANSFER_BOUNDARY_CONDITIONS_VARIANTS: dict[str, type] = {
    "FIXED_TEMPERATURE_VALUE": FixedTemperatureValueBC,
    "CYCLIC_SYMMETRY": CyclicSymmetryBC,
    "SURFACE_HEAT_FLUX": SurfaceHeatFluxBC,
    "CONVECTIVE_HEAT_FLUX": ConvectiveHeatFluxBC,
    "VOLUME_HEAT_FLUX": VolumeHeatFluxBC,
}

OneOf_HeatTransferBoundaryConditions = Annotated[
    Union[FixedTemperatureValueBC, CyclicSymmetryBC, SurfaceHeatFluxBC, ConvectiveHeatFluxBC, VolumeHeatFluxBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HEAT_TRANSFER_BOUNDARY_CONDITIONS_VARIANTS,
        )
    ),
]
