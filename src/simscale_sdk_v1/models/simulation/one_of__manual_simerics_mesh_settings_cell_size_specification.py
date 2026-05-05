from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_to_all_cad_surfaces_settings import AbsoluteToAllCadSurfacesSettings
from simscale_sdk_v1.models.simulation.relative_to_all_cad_surfaces_settings import RelativeToAllCadSurfacesSettings

_ONE_OF__MANUAL_SIMERICS_MESH_SETTINGS_CELL_SIZE_SPECIFICATION_VARIANTS: dict[str, type] = {
    "RELATIVE_TO_ALL_CAD_SURFACES": RelativeToAllCadSurfacesSettings,
    "ABSOLUTE_TO_ALL_CAD_SURFACES": AbsoluteToAllCadSurfacesSettings,
}

OneOf_ManualSimericsMeshSettingsCellSizeSpecification = Annotated[
    Union[RelativeToAllCadSurfacesSettings, AbsoluteToAllCadSurfacesSettings],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MANUAL_SIMERICS_MESH_SETTINGS_CELL_SIZE_SPECIFICATION_VARIANTS,
        )
    ),
]
