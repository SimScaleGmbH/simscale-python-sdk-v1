from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.distance_region_refinement_with_levels import DistanceRegionRefinementWithLevels
from simscale_sdk_v1.models.meshing.inside_region_refinement_with_levels import InsideRegionRefinementWithLevels
from simscale_sdk_v1.models.meshing.outside_region_refinement_with_levels import OutsideRegionRefinementWithLevels

_ONE_OF__REGION_REFINEMENT_WITH_LEVELS_REFINEMENT_VARIANTS: dict[str, type] = {
    "INSIDE": InsideRegionRefinementWithLevels,
    "DISTANCE": DistanceRegionRefinementWithLevels,
    "OUTSIDE": OutsideRegionRefinementWithLevels,
}

OneOf_RegionRefinementWithLevelsRefinement = Annotated[
    Union[InsideRegionRefinementWithLevels, DistanceRegionRefinementWithLevels, OutsideRegionRefinementWithLevels],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__REGION_REFINEMENT_WITH_LEVELS_REFINEMENT_VARIANTS,
        )
    ),
]
