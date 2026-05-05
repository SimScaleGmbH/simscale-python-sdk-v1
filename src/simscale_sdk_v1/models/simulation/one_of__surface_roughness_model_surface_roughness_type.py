from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.aerodynamic_roughness import AerodynamicRoughness
from simscale_sdk_v1.models.simulation.equivalent_sand_grain_roughness import EquivalentSandGrainRoughness
from simscale_sdk_v1.models.simulation.wind_exposure_roughness import WindExposureRoughness

# Add a surface roughness to the selected surfaces. Three different options are available: Equivalent sand grain roughness ks. This method is used to represent the actual roughness of specific materials that influence the flow close to the surface. Typical values reach from 0.00005 m for steel to 0.003 m for concrete.Aerodynamic roughness z0. Here, the roughness value is used to model the larger scale effects of non-modeled obstacles (such as vegetation, buildings etc.) on the Atmospheric Boundary Layer (ABL) flow. Typical values range from 0.0002 m for open sea to 1 m for dense urban areas.From wind exposure (only PWC). Here, the aerodynamic roughness value is automatically selected based on the selected wind exposure category for each wind direction individually. For the exact values of the aerodynamic roughness used, depending on the wind engineering standard, you can refer to this documentation page. This method is preferred in order to achieve horizontal homogeneity for the incoming ABL flow.. Learn more.
_ONE_OF__SURFACE_ROUGHNESS_MODEL_SURFACE_ROUGHNESS_TYPE_VARIANTS: dict[str, type] = {
    "EQUIVALENT_SAND_GRAIN_ROUGHNESS": EquivalentSandGrainRoughness,
    "AERODYNAMIC_ROUGHNESS": AerodynamicRoughness,
    "WIND_EXPOSURE_ROUGHNESS": WindExposureRoughness,
}

OneOf_SurfaceRoughnessModelSurfaceRoughnessType = Annotated[
    Union[EquivalentSandGrainRoughness, AerodynamicRoughness, WindExposureRoughness],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SURFACE_ROUGHNESS_MODEL_SURFACE_ROUGHNESS_TYPE_VARIANTS,
        )
    ),
]
