from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.first_layer_growth import FirstLayerGrowth
from simscale_sdk_v1.models.meshing.fractional_height1 import FractionalHeight1
from simscale_sdk_v1.models.meshing.fractional_height2 import FractionalHeight2
from simscale_sdk_v1.models.meshing.geometric_growth import GeometricGrowth

_ONE_OF__AUTOMATIC_LAYER_ON_LAYER_TYPE_VARIANTS: dict[str, type] = {
    "FRACTIONAL_HEIGHT_1": FractionalHeight1,
    "FRACTIONAL_HEIGHT_2": FractionalHeight2,
    "GEOMETRIC_GROWTH": GeometricGrowth,
    "FIRST_LAYER_GROWTH": FirstLayerGrowth,
}

OneOf_AutomaticLayerOnLayerType = Annotated[
    Union[FractionalHeight1, FractionalHeight2, GeometricGrowth, FirstLayerGrowth],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__AUTOMATIC_LAYER_ON_LAYER_TYPE_VARIANTS,
        )
    ),
]
