from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.simmetrix_boundary_layer_refinement import SimmetrixBoundaryLayerRefinement
from simscale_sdk_v1.models.meshing.surface_custom_sizing import SurfaceCustomSizing
from simscale_sdk_v1.models.meshing.volume_custom_sizing import VolumeCustomSizing

_ONE_OF__SIMMETRIX_MESHING_ELECTROMAGNETICS_REFINEMENTS_VARIANTS: dict[str, type] = {
    "SURFACE_CUSTOM_SIZING": SurfaceCustomSizing,
    "VOLUME_CUSTOM_SIZING": VolumeCustomSizing,
    "SIMMETRIX_BOUNDARY_LAYER_V13": SimmetrixBoundaryLayerRefinement,
}

OneOf_SimmetrixMeshingElectromagneticsRefinements = Annotated[
    Union[SurfaceCustomSizing, VolumeCustomSizing, SimmetrixBoundaryLayerRefinement],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_MESHING_ELECTROMAGNETICS_REFINEMENTS_VARIANTS,
        )
    ),
]
