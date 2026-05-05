from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__field_calculations_pressure_result_control_pressure_type import (
    OneOf_FieldCalculationsPressureResultControlPressureType,
)
from simscale_sdk_v1.models.simulation.one_of__field_calculations_pressure_result_control_result_type import (
    OneOf_FieldCalculationsPressureResultControlResultType,
)


class FieldCalculationsPressureResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE",
        description="Schema name: FieldCalculationsPressureResultControl",
    )
    name: str | None = Field(default=None)
    pressure_type: OneOf_FieldCalculationsPressureResultControlPressureType | None = Field(
        validation_alias="pressureType", serialization_alias="pressureType", default=None
    )
    result_type: OneOf_FieldCalculationsPressureResultControlResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
