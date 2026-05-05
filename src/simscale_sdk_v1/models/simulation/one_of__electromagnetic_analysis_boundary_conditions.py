from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.charge_density import ChargeDensity
from simscale_sdk_v1.models.simulation.convective_heat_flux import ConvectiveHeatFlux
from simscale_sdk_v1.models.simulation.fixed_potential import FixedPotential
from simscale_sdk_v1.models.simulation.fixed_temperature import FixedTemperature
from simscale_sdk_v1.models.simulation.floating_potential import FloatingPotential
from simscale_sdk_v1.models.simulation.magnetic_field_normal import MagneticFieldNormal
from simscale_sdk_v1.models.simulation.magnetic_flux_tangential import MagneticFluxTangential
from simscale_sdk_v1.models.simulation.radiation_heat_flux import RadiationHeatFlux
from simscale_sdk_v1.models.simulation.surface_heat_flux import SurfaceHeatFlux
from simscale_sdk_v1.models.simulation.total_charge import TotalCharge
from simscale_sdk_v1.models.simulation.volume_heat_flux import VolumeHeatFlux

_ONE_OF__ELECTROMAGNETIC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS: dict[str, type] = {
    "MAGNETIC_FIELD_NORMAL": MagneticFieldNormal,
    "MAGNETIC_FLUX_TANGENTIAL": MagneticFluxTangential,
    "FIXED_POTENTIAL": FixedPotential,
    "FLOATING_POTENTIAL": FloatingPotential,
    "CHARGE_DENSITY": ChargeDensity,
    "TOTAL_CHARGE": TotalCharge,
    "FIXED_TEMPERATURE": FixedTemperature,
    "SURFACE_HEAT_FLUX": SurfaceHeatFlux,
    "VOLUME_HEAT_FLUX": VolumeHeatFlux,
    "CONVECTIVE_HEAT_FLUX": ConvectiveHeatFlux,
    "RADIATION_HEAT_FLUX": RadiationHeatFlux,
}

OneOf_ElectromagneticAnalysisBoundaryConditions = Annotated[
    Union[
        MagneticFieldNormal,
        MagneticFluxTangential,
        FixedPotential,
        FloatingPotential,
        ChargeDensity,
        TotalCharge,
        FixedTemperature,
        SurfaceHeatFlux,
        VolumeHeatFlux,
        ConvectiveHeatFlux,
        RadiationHeatFlux,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS,
        )
    ),
]
