from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.distance_region_refinement_with_length import DistanceRegionRefinementWithLength
from simscale_sdk_v1.models.simulation.inside_region_refinement_with_length import InsideRegionRefinementWithLength

# Choose between the following refinement modes:Inside: Refines all the mesh cells inside the selected volumes up to the specified cell edge length.Distance:Refines the mesh cells according to the distance to the surface of the assigned volume(s). The Distance mode can accommodate different refinement levels at multiple distances.
_ONE_OF__REGION_REFINEMENT_EBM_REFINEMENT_VARIANTS: dict[str, type] = {
    "INSIDE": InsideRegionRefinementWithLength,
    "DISTANCE": DistanceRegionRefinementWithLength,
}

OneOf_RegionRefinementEBMRefinement = Annotated[
    Union[InsideRegionRefinementWithLength, DistanceRegionRefinementWithLength],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__REGION_REFINEMENT_EBM_REFINEMENT_VARIANTS,
        )
    ),
]
