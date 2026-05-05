from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.local_element_size_ebm import LocalElementSizeEBM
from simscale_sdk_v1.models.meshing.region_refinement_ebm import RegionRefinementEBM

_ONE_OF__POLYGRID_MESHING_REFINEMENTS_VARIANTS: dict[str, type] = {
    "REGION_REFINEMENT_EBM": RegionRefinementEBM,
    "LOCAL_SIZING_EBM": LocalElementSizeEBM,
}

OneOf_PolygridMeshingRefinements = Annotated[
    Union[RegionRefinementEBM, LocalElementSizeEBM],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__POLYGRID_MESHING_REFINEMENTS_VARIANTS,
        )
    ),
]
