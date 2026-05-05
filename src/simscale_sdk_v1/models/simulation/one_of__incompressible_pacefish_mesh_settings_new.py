from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.pacefish_automesh import PacefishAutomesh
from simscale_sdk_v1.models.simulation.pacefish_mesh_legacy import PacefishMeshLegacy

_ONE_OF__INCOMPRESSIBLE_PACEFISH_MESH_SETTINGS_NEW_VARIANTS: dict[str, type] = {
    "PACEFISH_MESH_LEGACY": PacefishMeshLegacy,
    "PACEFISH_AUTOMESH": PacefishAutomesh,
}

OneOf_IncompressiblePacefishMeshSettingsNew = Annotated[
    Union[PacefishMeshLegacy, PacefishAutomesh],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__INCOMPRESSIBLE_PACEFISH_MESH_SETTINGS_NEW_VARIANTS,
        )
    ),
]
