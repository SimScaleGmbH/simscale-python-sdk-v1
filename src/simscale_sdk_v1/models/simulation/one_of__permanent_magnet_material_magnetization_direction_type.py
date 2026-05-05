from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.face_normal_magnetization_direction_method import (
    FaceNormalMagnetizationDirectionMethod,
)
from simscale_sdk_v1.models.simulation.global_cartesian_magnetization_direction_method import (
    GlobalCartesianMagnetizationDirectionMethod,
)

_ONE_OF__PERMANENT_MAGNET_MATERIAL_MAGNETIZATION_DIRECTION_TYPE_VARIANTS: dict[str, type] = {
    "GLOBAL_CARTESIAN": GlobalCartesianMagnetizationDirectionMethod,
    "FACE_NORMAL": FaceNormalMagnetizationDirectionMethod,
}

OneOf_PermanentMagnetMaterialMagnetizationDirectionType = Annotated[
    Union[GlobalCartesianMagnetizationDirectionMethod, FaceNormalMagnetizationDirectionMethod],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PERMANENT_MAGNET_MATERIAL_MAGNETIZATION_DIRECTION_TYPE_VARIANTS,
        )
    ),
]
