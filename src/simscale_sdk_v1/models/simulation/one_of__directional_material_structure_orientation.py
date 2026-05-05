from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cartesian_orientation import CartesianOrientation
from simscale_sdk_v1.models.simulation.custom_orientation import CustomOrientation

_ONE_OF__DIRECTIONAL_MATERIAL_STRUCTURE_ORIENTATION_VARIANTS: dict[str, type] = {
    "CARTESIAN": CartesianOrientation,
    "CUSTOM": CustomOrientation,
}

OneOf_DirectionalMaterialStructureOrientation = Annotated[
    Union[CartesianOrientation, CustomOrientation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIRECTIONAL_MATERIAL_STRUCTURE_ORIENTATION_VARIANTS,
        )
    ),
]
