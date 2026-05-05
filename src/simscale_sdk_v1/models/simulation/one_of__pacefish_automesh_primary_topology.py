from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.buildings_of_interest import BuildingsOfInterest
from simscale_sdk_v1.models.simulation.region import Region

_ONE_OF__PACEFISH_AUTOMESH_PRIMARY_TOPOLOGY_VARIANTS: dict[str, type] = {
    "BUILDINGS_OF_INTEREST": BuildingsOfInterest,
    "REGION": Region,
}

OneOf_PacefishAutomeshPrimaryTopology = Annotated[
    Union[BuildingsOfInterest, Region],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PACEFISH_AUTOMESH_PRIMARY_TOPOLOGY_VARIANTS,
        )
    ),
]
