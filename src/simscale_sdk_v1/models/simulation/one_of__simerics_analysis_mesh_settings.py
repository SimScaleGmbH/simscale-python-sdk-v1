from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_simerics_mesh_settings import AutomaticSimericsMeshSettings
from simscale_sdk_v1.models.simulation.manual_simerics_mesh_settings import ManualSimericsMeshSettings

_ONE_OF__SIMERICS_ANALYSIS_MESH_SETTINGS_VARIANTS: dict[str, type] = {
    "AUTOMATIC_SETTINGS": AutomaticSimericsMeshSettings,
    "MANUAL_SETTINGS": ManualSimericsMeshSettings,
}

OneOf_SimericsAnalysisMeshSettings = Annotated[
    Union[AutomaticSimericsMeshSettings, ManualSimericsMeshSettings],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMERICS_ANALYSIS_MESH_SETTINGS_VARIANTS,
        )
    ),
]
