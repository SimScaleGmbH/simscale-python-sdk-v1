from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.no_travel_limit import NoTravelLimit
from simscale_sdk_v1.models.simulation.travel_distance import TravelDistance

# Whether the body is stopped once it has moved a certain distance, the way a real actuator hits an end stop.None &mdash; the motion is unbounded. A body with no spring holding it back will keep accelerating until it leaves the simulated region.Distance &mdash; set how far the body may travel in each direction.
_ONE_OF__MOTION_AXIS_TRAVEL_LIMIT_VARIANTS: dict[str, type] = {
    "NO_TRAVEL_LIMIT": NoTravelLimit,
    "TRAVEL_DISTANCE": TravelDistance,
}

OneOf_MotionAxisTravelLimit = Annotated[
    Union[NoTravelLimit, TravelDistance],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MOTION_AXIS_TRAVEL_LIMIT_VARIANTS,
        )
    ),
]
