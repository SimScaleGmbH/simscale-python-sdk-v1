from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.region_refinement_pacefish import RegionRefinementPacefish
from simscale_sdk_v1.models.simulation.surface_refinement_pacefish import SurfaceRefinementPacefish

_ONE_OF__PACEFISH_MESH_LEGACY_REFINEMENTS_VARIANTS: dict[str, type] = {
    "REGION_PACEFISH": RegionRefinementPacefish,
    "SURFACE_PACEFISH": SurfaceRefinementPacefish,
}

OneOf_PacefishMeshLegacyRefinements = Annotated[
    Union[RegionRefinementPacefish, SurfaceRefinementPacefish],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PACEFISH_MESH_LEGACY_REFINEMENTS_VARIANTS,
        )
    ),
]
