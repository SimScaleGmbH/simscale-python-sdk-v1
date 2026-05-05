from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.ground_absolute import GroundAbsolute
from simscale_sdk_v1.models.simulation.ground_relative import GroundRelative

# Ground reference can be either absolute (uses bottom of region of interest as reference) or relative (uses each assignment as a reference) and elevates those by the height defined. Learn more.
_ONE_OF__PEDESTRIAN_COMFORT_SURFACE_GROUND_VARIANTS: dict[str, type] = {
    "GROUND_ABSOLUTE": GroundAbsolute,
    "GROUND_RELATIVE": GroundRelative,
}

OneOf_PedestrianComfortSurfaceGround = Annotated[
    Union[GroundAbsolute, GroundRelative],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PEDESTRIAN_COMFORT_SURFACE_GROUND_VARIANTS,
        )
    ),
]
