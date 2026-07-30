from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bolt_preload_bc_marc import BoltPreloadBCMarc
from simscale_sdk_v1.models.simulation.convection_radiation_bc_marc import ConvectionRadiationBCMarc
from simscale_sdk_v1.models.simulation.fixed_value_bc_marc import FixedValueBCMarc
from simscale_sdk_v1.models.simulation.point_displacement_bc_marc import PointDisplacementBCMarc
from simscale_sdk_v1.models.simulation.point_load_bc_marc import PointLoadBCMarc
from simscale_sdk_v1.models.simulation.pressure_bc_marc import PressureBCMarc
from simscale_sdk_v1.models.simulation.surface_heat_flux_bc_marc import SurfaceHeatFluxBCMarc
from simscale_sdk_v1.models.simulation.symmetry_bc_marc import SymmetryBCMarc
from simscale_sdk_v1.models.simulation.temperature_bc_marc import TemperatureBCMarc
from simscale_sdk_v1.models.simulation.volume_heat_flux_bc_marc import VolumeHeatFluxBCMarc

_ONE_OF__MARC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValueBCMarc,
    "PRESSURE": PressureBCMarc,
    "SYMMETRY": SymmetryBCMarc,
    "POINT_DISPLACEMENT": PointDisplacementBCMarc,
    "POINT_LOAD": PointLoadBCMarc,
    "TEMPERATURE": TemperatureBCMarc,
    "CONVECTION_RADIATION": ConvectionRadiationBCMarc,
    "SURFACE_HEAT_FLUX": SurfaceHeatFluxBCMarc,
    "VOLUME_HEAT_FLUX": VolumeHeatFluxBCMarc,
    "BOLT_PRELOAD": BoltPreloadBCMarc,
}

OneOf_MarcAnalysisBoundaryConditions = Annotated[
    Union[
        FixedValueBCMarc,
        PressureBCMarc,
        SymmetryBCMarc,
        PointDisplacementBCMarc,
        PointLoadBCMarc,
        TemperatureBCMarc,
        ConvectionRadiationBCMarc,
        SurfaceHeatFluxBCMarc,
        VolumeHeatFluxBCMarc,
        BoltPreloadBCMarc,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS,
        )
    ),
]
