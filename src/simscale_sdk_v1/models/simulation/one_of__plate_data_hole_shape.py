from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.circular_hole_shape import CircularHoleShape
from simscale_sdk_v1.models.simulation.general_hole_shape import GeneralHoleShape

# Shape of holes in perforated plate.
_ONE_OF__PLATE_DATA_HOLE_SHAPE_VARIANTS: dict[str, type] = {
    "GENERAL": GeneralHoleShape,
    "CIRCULAR": CircularHoleShape,
}

OneOf_PlateDataHoleShape = Annotated[
    Union[GeneralHoleShape, CircularHoleShape],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PLATE_DATA_HOLE_SHAPE_VARIANTS,
        )
    ),
]
