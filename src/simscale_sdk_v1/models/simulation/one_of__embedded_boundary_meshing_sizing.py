from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_embedded_boundary_mesh_sizing import (
    AutomaticEmbeddedBoundaryMeshSizing,
)
from simscale_sdk_v1.models.simulation.custom_embedded_boundary_mesh_sizing import CustomEmbeddedBoundaryMeshSizing
from simscale_sdk_v1.models.simulation.manual_embedded_boundary_mesh_sizing import ManualEmbeddedBoundaryMeshSizing

# Define how to control the global mesh sizing: Automatic: Element sizing is controlled by automatic fineness levels that take the geometrical properties into account. Manual: Element sizing is controlled by maximum and minimum edge length.  Custom: Element sizing is controlled by the specified number of cells in the three spatial directions and the number refinement levels applied on the surfaces.
_ONE_OF__EMBEDDED_BOUNDARY_MESHING_SIZING_VARIANTS: dict[str, type] = {
    "AUTOMATIC_EBM_MESH_SIZING": AutomaticEmbeddedBoundaryMeshSizing,
    "MANUAL_EBM_MESH_SIZING": ManualEmbeddedBoundaryMeshSizing,
    "CUSTOM_EBM_MESH_SIZING": CustomEmbeddedBoundaryMeshSizing,
}

OneOf_EmbeddedBoundaryMeshingSizing = Annotated[
    Union[AutomaticEmbeddedBoundaryMeshSizing, ManualEmbeddedBoundaryMeshSizing, CustomEmbeddedBoundaryMeshSizing],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__EMBEDDED_BOUNDARY_MESHING_SIZING_VARIANTS,
        )
    ),
]
