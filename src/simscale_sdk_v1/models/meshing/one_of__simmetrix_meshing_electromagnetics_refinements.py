from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.region_refinement_with_length import RegionRefinementWithLength
from simscale_sdk_v1.models.meshing.simmetrix_local_sizing_refinement import SimmetrixLocalSizingRefinement
from simscale_sdk_v1.models.meshing.surface_custom_sizing import SurfaceCustomSizing
from simscale_sdk_v1.models.meshing.volume_custom_sizing import VolumeCustomSizing

_ONE_OF__SIMMETRIX_MESHING_ELECTROMAGNETICS_REFINEMENTS_VARIANTS: dict[str, type] = {
    "REGION_LENGTH": RegionRefinementWithLength,
    "SURFACE_CUSTOM_SIZING": SurfaceCustomSizing,
    "VOLUME_CUSTOM_SIZING": VolumeCustomSizing,
    "SIMMETRIX_LOCAL_SIZING_V10": SimmetrixLocalSizingRefinement,
}

OneOf_SimmetrixMeshingElectromagneticsRefinements = Annotated[
    Union[RegionRefinementWithLength, SurfaceCustomSizing, VolumeCustomSizing, SimmetrixLocalSizingRefinement],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_MESHING_ELECTROMAGNETICS_REFINEMENTS_VARIANTS,
        )
    ),
]
