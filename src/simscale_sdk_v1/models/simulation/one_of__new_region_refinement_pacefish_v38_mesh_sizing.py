from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_mesh_sizing import AutomaticMeshSizing
from simscale_sdk_v1.models.simulation.manual_region_sizing_pacefish import ManualRegionSizingPacefish

_ONE_OF__NEW_REGION_REFINEMENT_PACEFISH_V38_MESH_SIZING_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticMeshSizing,
    "MANUAL_REGION_PACEFISH": ManualRegionSizingPacefish,
}

OneOf_NewRegionRefinementPacefishV38MeshSizing = Annotated[
    Union[AutomaticMeshSizing, ManualRegionSizingPacefish],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__NEW_REGION_REFINEMENT_PACEFISH_V38_MESH_SIZING_VARIANTS,
        )
    ),
]
