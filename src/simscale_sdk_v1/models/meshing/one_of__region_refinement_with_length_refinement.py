from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.distance_region_refinement_with_length import DistanceRegionRefinementWithLength
from simscale_sdk_v1.models.meshing.inside_region_refinement_with_length import InsideRegionRefinementWithLength
from simscale_sdk_v1.models.meshing.outside_region_refinement_with_length import OutsideRegionRefinementWithLength

# Choose between the following refinement modes:Inside: Refines all volume mesh cells inside the selected volumes up to the specified cell edge length.Outside: Refines the mesh cells outside of the specified area up to the specified cell edge length.Distance: Refines mesh cells according to the distance to the surface of the assigned volume(s). The Distance mode can accommodate different refinement levels at multiple distances.
_ONE_OF__REGION_REFINEMENT_WITH_LENGTH_REFINEMENT_VARIANTS: dict[str, type] = {
    "INSIDE": InsideRegionRefinementWithLength,
    "DISTANCE": DistanceRegionRefinementWithLength,
    "OUTSIDE": OutsideRegionRefinementWithLength,
}

OneOf_RegionRefinementWithLengthRefinement = Annotated[
    Union[InsideRegionRefinementWithLength, DistanceRegionRefinementWithLength, OutsideRegionRefinementWithLength],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__REGION_REFINEMENT_WITH_LENGTH_REFINEMENT_VARIANTS,
        )
    ),
]
