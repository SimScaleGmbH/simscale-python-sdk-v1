from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.automatic_layer_off import AutomaticLayerOff
from simscale_sdk_v1.models.meshing.automatic_layer_on import AutomaticLayerOn

# This toggle enables the automatic creation of boundary layers at no-slip walls. When toggled on, the meshing is started together with the simulation run.
_ONE_OF__SIMMETRIX_MESHING_FLUID_AUTOMATIC_LAYER_SETTINGS_VARIANTS: dict[str, type] = {
    "AUTOMATIC_LAYER_ON": AutomaticLayerOn,
    "AUTOMATIC_LAYER_OFF": AutomaticLayerOff,
}

OneOf_SimmetrixMeshingFluidAutomaticLayerSettings = Annotated[
    Union[AutomaticLayerOn, AutomaticLayerOff],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_MESHING_FLUID_AUTOMATIC_LAYER_SETTINGS_VARIANTS,
        )
    ),
]
