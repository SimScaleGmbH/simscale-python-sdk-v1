from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.area_average_result_control import AreaAverageResultControl
from simscale_sdk_v1.models.simulation.area_integral_result_control import AreaIntegralResultControl
from simscale_sdk_v1.models.simulation.pressure_difference_result_control import PressureDifferenceResultControl

_ONE_OF__FLUID_RESULT_CONTROLS_SURFACE_DATA_VARIANTS: dict[str, type] = {
    "AREA_AVERAGE": AreaAverageResultControl,
    "AREA_INTEGRAL": AreaIntegralResultControl,
    "PRESSURE_DIFFERENCE": PressureDifferenceResultControl,
}

OneOf_FluidResultControlsSurfaceData = Annotated[
    Union[AreaAverageResultControl, AreaIntegralResultControl, PressureDifferenceResultControl],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_RESULT_CONTROLS_SURFACE_DATA_VARIANTS,
        )
    ),
]
