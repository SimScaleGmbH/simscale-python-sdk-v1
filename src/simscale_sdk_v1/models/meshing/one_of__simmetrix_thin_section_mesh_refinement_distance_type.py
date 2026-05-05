from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.absolute_distance import AbsoluteDistance
from simscale_sdk_v1.models.meshing.relative_distance import RelativeDistance

_ONE_OF__SIMMETRIX_THIN_SECTION_MESH_REFINEMENT_DISTANCE_TYPE_VARIANTS: dict[str, type] = {
    "ABSOLUTE": AbsoluteDistance,
    "RELATIVE": RelativeDistance,
}

OneOf_SimmetrixThinSectionMeshRefinementDistanceType = Annotated[
    Union[AbsoluteDistance, RelativeDistance],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_THIN_SECTION_MESH_REFINEMENT_DISTANCE_TYPE_VARIANTS,
        )
    ),
]
