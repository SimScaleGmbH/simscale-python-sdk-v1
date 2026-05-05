from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.sweep_meshing_absolute_size import SweepMeshingAbsoluteSize
from simscale_sdk_v1.models.meshing.sweep_meshing_number_of_elements import SweepMeshingNumberOfElements

# Sweep sizing type allows you to specify either the number of elements or the element thickness along the direction of the sweep. The actual absolute thickness will match the desired value as close as possible, given the length of the sweep region as a constraint.
_ONE_OF__SIMMETRIX_SWEPT_MESH_REFINEMENT_SIZING_TYPE_VARIANTS: dict[str, type] = {
    "SWEEP_MESHING_ABSOLUTE_SIZE": SweepMeshingAbsoluteSize,
    "SWEEP_MESHING_NUMBER_OF_ELEMENTS": SweepMeshingNumberOfElements,
}

OneOf_SimmetrixSweptMeshRefinementSizingType = Annotated[
    Union[SweepMeshingAbsoluteSize, SweepMeshingNumberOfElements],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_SWEPT_MESH_REFINEMENT_SIZING_TYPE_VARIANTS,
        )
    ),
]
