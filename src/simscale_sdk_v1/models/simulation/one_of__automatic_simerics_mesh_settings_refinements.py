from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.region_refinement_simerics import RegionRefinementSimerics
from simscale_sdk_v1.models.simulation.surface_refinement_simerics import SurfaceRefinementSimerics

_ONE_OF__AUTOMATIC_SIMERICS_MESH_SETTINGS_REFINEMENTS_VARIANTS: dict[str, type] = {
    "REGION_REFINEMENT_SIMERICS": RegionRefinementSimerics,
    "SURFACE_REFINEMENT_SIMERICS": SurfaceRefinementSimerics,
}

OneOf_AutomaticSimericsMeshSettingsRefinements = Annotated[
    Union[RegionRefinementSimerics, SurfaceRefinementSimerics],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__AUTOMATIC_SIMERICS_MESH_SETTINGS_REFINEMENTS_VARIANTS,
        )
    ),
]
