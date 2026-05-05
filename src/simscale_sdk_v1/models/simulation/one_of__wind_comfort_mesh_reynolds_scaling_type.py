from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_reynolds_scaling import AutomaticReynoldsScaling
from simscale_sdk_v1.models.simulation.manual_reynolds_scaling import ManualReynoldsScaling

# Use this factor to scale the Reynolds number of your simulation. For example, to change the Reynolds number from 108 to 106, set this factor to 0.01. Learn more.
_ONE_OF__WIND_COMFORT_MESH_REYNOLDS_SCALING_TYPE_VARIANTS: dict[str, type] = {
    "AUTOMATIC_REYNOLDS_SCALING": AutomaticReynoldsScaling,
    "MANUAL_REYNOLDS_SCALING": ManualReynoldsScaling,
}

OneOf_WindComfortMeshReynoldsScalingType = Annotated[
    Union[AutomaticReynoldsScaling, ManualReynoldsScaling],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WIND_COMFORT_MESH_REYNOLDS_SCALING_TYPE_VARIANTS,
        )
    ),
]
