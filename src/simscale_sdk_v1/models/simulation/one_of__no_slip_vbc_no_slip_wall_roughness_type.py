from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.no_slip_wall_aerodynamic_roughness import NoSlipWallAerodynamicRoughness
from simscale_sdk_v1.models.simulation.no_slip_wall_equivalent_sand_roughness import NoSlipWallEquivalentSandRoughness

# Define a surface roughness on the wall of the virtual wind tunnel. The roughness value can be defined in two ways: Equivalent sand grain roughness ks. This method is used to represent the actual roughness of specific materials that influence the flow close to the surface. Typical values reach from 0.00005 m for steel to 0.003 m for concrete.Aerodynamic roughness z0. Here, the roughness value is used to model the larger scale effects of non-modeled obstacles (such as vegetation, buildings etc.) on the atmospheric boundary layer flow. Typical values range from 0.0002 m for open sea to 1 m for dense urban areas. The roughness value will only be applied to the floor of the wind tunnel and not to potential terrain surfaces. Learn more.
_ONE_OF__NO_SLIP_VBC_NO_SLIP_WALL_ROUGHNESS_TYPE_VARIANTS: dict[str, type] = {
    "NO_SLIP_WALL_EQUIVALENT_SAND_ROUGHNESS": NoSlipWallEquivalentSandRoughness,
    "NO_SLIP_WALL_AERODYNAMIC_ROUGHNESS": NoSlipWallAerodynamicRoughness,
}

OneOf_NoSlipVBCNoSlipWallRoughnessType = Annotated[
    Union[NoSlipWallEquivalentSandRoughness, NoSlipWallAerodynamicRoughness],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__NO_SLIP_VBC_NO_SLIP_WALL_ROUGHNESS_TYPE_VARIANTS,
        )
    ),
]
