from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.automatic_mesh_sizing_simmetrix import AutomaticMeshSizingSimmetrix
from simscale_sdk_v1.models.meshing.manual_mesh_sizing_simmetrix import ManualMeshSizingSimmetrix

# Define how to control the overall mesh sizing: Automatic: Element sizing is controlled by automatic fineness levels that take the geometrical properties into account. Manual: Element sizing is controlled by default and minimum size.
_ONE_OF__SIMMETRIX_MESHING_ELECTROMAGNETICS_SIZING_VARIANTS: dict[str, type] = {
    "AUTOMATIC_V9": AutomaticMeshSizingSimmetrix,
    "MANUAL": ManualMeshSizingSimmetrix,
}

OneOf_SimmetrixMeshingElectromagneticsSizing = Annotated[
    Union[AutomaticMeshSizingSimmetrix, ManualMeshSizingSimmetrix],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_MESHING_ELECTROMAGNETICS_SIZING_VARIANTS,
        )
    ),
]
