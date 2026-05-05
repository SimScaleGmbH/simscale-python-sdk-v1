from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.ami_rotating_zone import AMIRotatingZone
from simscale_sdk_v1.models.simulation.mrf_rotating_zone import MRFRotatingZone

_ONE_OF__ADVANCED_CONCEPTS_ROTATING_ZONES_VARIANTS: dict[str, type] = {
    "ARBITRARY_MESH_INTERFACE": AMIRotatingZone,
    "MULTI_REFERENCE_FRAME": MRFRotatingZone,
}

OneOf_AdvancedConceptsRotatingZones = Annotated[
    Union[AMIRotatingZone, MRFRotatingZone],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_ROTATING_ZONES_VARIANTS,
        )
    ),
]
