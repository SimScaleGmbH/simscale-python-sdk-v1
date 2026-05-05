from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_reactualization import AutomaticReactualization
from simscale_sdk_v1.models.simulation.manual_reactualization import ManualReactualization
from simscale_sdk_v1.models.simulation.none_reactualization import NoneReactualization

_ONE_OF__FIXED_POINT_NON_LINEARITY_RESOLUTION_GEOMETRY_REACTUALIZATION_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticReactualization,
    "MANUAL": ManualReactualization,
    "NONE": NoneReactualization,
}

OneOf_FixedPointNonLinearityResolutionGeometryReactualization = Annotated[
    Union[AutomaticReactualization, ManualReactualization, NoneReactualization],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIXED_POINT_NON_LINEARITY_RESOLUTION_GEOMETRY_REACTUALIZATION_VARIANTS,
        )
    ),
]
