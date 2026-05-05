from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.automatic_mesh_grading import AutomaticMeshGrading
from simscale_sdk_v1.models.meshing.manual_mesh_grading import ManualMeshGrading

# The mesh grading specifies how fine details of the geometry are resolved and also influences the quality of the resulting elements.If you select the automatic grading, you can specify how fine your mesh should be (ranging from 1 - very coarse to 5 - very fine) and all additional parameters will be set automatically.For full control over the underlying parameters number of segements per edge, number of segements per radius and growth rate you can choose the manual mesh grading option. The figure shows meshes for grading 1 - very coarse (left) and 5 - very fine (right).
_ONE_OF__MANUAL_MESH_SIZING_GRADING_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticMeshGrading,
    "MANUAL": ManualMeshGrading,
}

OneOf_ManualMeshSizingGrading = Annotated[
    Union[AutomaticMeshGrading, ManualMeshGrading],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MANUAL_MESH_SIZING_GRADING_VARIANTS,
        )
    ),
]
