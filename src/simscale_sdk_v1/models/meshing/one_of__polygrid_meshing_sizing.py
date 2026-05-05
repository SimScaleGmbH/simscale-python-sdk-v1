from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.automatic_polygrid_mesh_sizing import AutomaticPolygridMeshSizing
from simscale_sdk_v1.models.meshing.custom_polygrid_mesh_sizing import CustomPolygridMeshSizing
from simscale_sdk_v1.models.meshing.manual_polygrid_mesh_sizing import ManualPolygridMeshSizing

# Define how to control the global mesh sizing: Automatic: Element sizing is controlled by automatic fineness levels that take the geometrical properties into account. Manual: Element sizing is controlled by maximum and minimum edge length.  Custom: Element sizing is controlled by the specified number of cells in the three spatial directions and the number refinement levels applied on the surfaces.
_ONE_OF__POLYGRID_MESHING_SIZING_VARIANTS: dict[str, type] = {
    "AUTOMATIC_POLYGRID_MESH_SIZING": AutomaticPolygridMeshSizing,
    "MANUAL_POLYGRID_MESH_SIZING": ManualPolygridMeshSizing,
    "CUSTOM_POLYGRID_MESH_SIZING": CustomPolygridMeshSizing,
}

OneOf_PolygridMeshingSizing = Annotated[
    Union[AutomaticPolygridMeshSizing, ManualPolygridMeshSizing, CustomPolygridMeshSizing],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__POLYGRID_MESHING_SIZING_VARIANTS,
        )
    ),
]
