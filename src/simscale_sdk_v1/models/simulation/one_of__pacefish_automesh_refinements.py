from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.new_region_refinement_pacefish_v38 import NewRegionRefinementPacefishV38
from simscale_sdk_v1.models.simulation.new_surface_refinement_pacefish_v38 import NewSurfaceRefinementPacefishV38

_ONE_OF__PACEFISH_AUTOMESH_REFINEMENTS_VARIANTS: dict[str, type] = {
    "REGION_PACEFISH_V38": NewRegionRefinementPacefishV38,
    "SURFACE_PACEFISH_V38": NewSurfaceRefinementPacefishV38,
}

OneOf_PacefishAutomeshRefinements = Annotated[
    Union[NewRegionRefinementPacefishV38, NewSurfaceRefinementPacefishV38],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PACEFISH_AUTOMESH_REFINEMENTS_VARIANTS,
        )
    ),
]
