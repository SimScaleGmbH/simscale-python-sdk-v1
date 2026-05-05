from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.automatic_mesh_sizing import AutomaticMeshSizing
from simscale_sdk_v1.models.meshing.manual_mesh_sizing import ManualMeshSizing

# Choose how your mesh element sizes should be defined:If you select the Automatic sizing, you can specify how fine your mesh should be (ranging from Very coarse to Very fine) and all additional parameters will be set automatically according to the chosen fineness and the geometry features.For full control over the mesh sizing, select the Manual option. Here you can define the Minimum edge length and Maximum edge length. The figure shows meshes with fineness Very coarse (left) and Very fine (right).
_ONE_OF__SUBMESH_REFINEMENT_SIZING_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticMeshSizing,
    "MANUAL": ManualMeshSizing,
}

OneOf_SubmeshRefinementSizing = Annotated[
    Union[AutomaticMeshSizing, ManualMeshSizing],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SUBMESH_REFINEMENT_SIZING_VARIANTS,
        )
    ),
]
