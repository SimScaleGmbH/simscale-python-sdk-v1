from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.automatic_curvature import AutomaticCurvature
from simscale_sdk_v1.models.meshing.relative_curvature import RelativeCurvature

# The Curvature setting allows the user to specify the mesh refinement on curved features. By default, this is Automatic. Alternatively, the user can specify the curvature in terms of number of mesh nodes in a circle using Relative. Curvature refinement is not supported for Geometry primitive region refinement.
_ONE_OF__REGION_REFINEMENT_WITH_LENGTH_CURVATURE_VARIANTS: dict[str, type] = {
    "AUTOMATIC_CURVATURE": AutomaticCurvature,
    "RELATIVE_CURVATURE": RelativeCurvature,
}

OneOf_RegionRefinementWithLengthCurvature = Annotated[
    Union[AutomaticCurvature, RelativeCurvature],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__REGION_REFINEMENT_WITH_LENGTH_CURVATURE_VARIANTS,
        )
    ),
]
