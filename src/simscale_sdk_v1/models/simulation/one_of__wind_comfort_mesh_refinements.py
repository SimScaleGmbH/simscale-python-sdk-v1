from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.region_refinement_wind_comfort import RegionRefinementWindComfort
from simscale_sdk_v1.models.simulation.surface_refinement_wind_comfort import SurfaceRefinementWindComfort

_ONE_OF__WIND_COMFORT_MESH_REFINEMENTS_VARIANTS: dict[str, type] = {
    "SURFACE_REFINEMENT_WIND_COMFORT": SurfaceRefinementWindComfort,
    "REGION_REFINEMENT_WIND_COMFORT": RegionRefinementWindComfort,
}

OneOf_WindComfortMeshRefinements = Annotated[
    Union[SurfaceRefinementWindComfort, RegionRefinementWindComfort],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WIND_COMFORT_MESH_REFINEMENTS_VARIANTS,
        )
    ),
]
