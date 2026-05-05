from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.greybody_diffusive_ray_bc import GreybodyDiffusiveRayBC
from simscale_sdk_v1.models.simulation.open_boundary_ray_bc import OpenBoundaryRayBC
from simscale_sdk_v1.models.simulation.semi_open_boundary_ray_bc import SemiOpenBoundaryRayBC

# Radiative behaviour of the wall. The Kirchhoff's law of thermal radiation is applied in all options. This means that the absorptivity of the surface is equal to its emissivity.  Opaque is applied to surfaces with transmissivity equal to 0. The radiation that hits the surface will be absorbed and reflected, but not transmitted, e.g.: brick or concrete walls.Transparent is applied to surfaces with transmissivity equal to 1. The radiation that hits the surface will be fully transmitted to the other side, e.g.: inlets, outlets or regular windows.Semi-transparent is applied to non-fully transparent surfaces. The radiation that hits the surface will be absorbed, reflected and transmitted, e.g. some stained glass windows.
_ONE_OF__WALL_BC_RADIATIVE_INTENSITY_RAY_VARIANTS: dict[str, type] = {
    "GREYBODY_DIFFUSIVE_RAY": GreybodyDiffusiveRayBC,
    "OPEN_BOUNDARY_RAY": OpenBoundaryRayBC,
    "SEMI_OPEN_BOUNDARY_RAY": SemiOpenBoundaryRayBC,
}

OneOf_WallBCRadiativeIntensityRay = Annotated[
    Union[GreybodyDiffusiveRayBC, OpenBoundaryRayBC, SemiOpenBoundaryRayBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WALL_BC_RADIATIVE_INTENSITY_RAY_VARIANTS,
        )
    ),
]
