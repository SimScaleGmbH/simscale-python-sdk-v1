from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_temperature_heat_transfer_coefficient_result_type import (
    FixedTemperatureHeatTransferCoefficientResultType,
)
from simscale_sdk_v1.models.simulation.wall_next_cell_heat_transfer_coefficient_result_type import (
    WallNextCellHeatTransferCoefficientResultType,
)

_ONE_OF__FIELD_CALCULATIONS_WALL_HEAT_FLUX_RESULT_CONTROL_REFERENCE_TEMPERATURE_RESULT_TYPE_VARIANTS: dict[
    str, type
] = {
    "WALL_NEXT_CELL_HEAT_TRANSFER_COEFFICIENT": WallNextCellHeatTransferCoefficientResultType,
    "REFERENCE_TEMPERATURE_HEAT_TRANSFER_COEFFICIENT": FixedTemperatureHeatTransferCoefficientResultType,
}

OneOf_FieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType = Annotated[
    Union[WallNextCellHeatTransferCoefficientResultType, FixedTemperatureHeatTransferCoefficientResultType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIELD_CALCULATIONS_WALL_HEAT_FLUX_RESULT_CONTROL_REFERENCE_TEMPERATURE_RESULT_TYPE_VARIANTS,
        )
    ),
]
