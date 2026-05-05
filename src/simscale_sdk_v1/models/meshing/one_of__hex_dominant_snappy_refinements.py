from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.feature_refinement_hex_dominant_snappy import FeatureRefinementHexDominantSnappy
from simscale_sdk_v1.models.meshing.layer_addition_hex_dominant_snappy import LayerAdditionHexDominantSnappy
from simscale_sdk_v1.models.meshing.region_refinement_with_length import RegionRefinementWithLength
from simscale_sdk_v1.models.meshing.surface_refinement_hex_dominant_snappy import SurfaceRefinementHexDominantSnappy

_ONE_OF__HEX_DOMINANT_SNAPPY_REFINEMENTS_VARIANTS: dict[str, type] = {
    "REGION_LENGTH": RegionRefinementWithLength,
    "SURFACE_HEX_DOMINANT_SNAPPY_V3": SurfaceRefinementHexDominantSnappy,
    "FEATURE_HEX_DOMINANT_SNAPPY": FeatureRefinementHexDominantSnappy,
    "LAYER_ADDITION_HEX_DOMINANT_SNAPPY": LayerAdditionHexDominantSnappy,
}

OneOf_HexDominantSnappyRefinements = Annotated[
    Union[
        RegionRefinementWithLength,
        SurfaceRefinementHexDominantSnappy,
        FeatureRefinementHexDominantSnappy,
        LayerAdditionHexDominantSnappy,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HEX_DOMINANT_SNAPPY_REFINEMENTS_VARIANTS,
        )
    ),
]
