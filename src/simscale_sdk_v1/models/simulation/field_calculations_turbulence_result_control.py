from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__field_calculations_turbulence_result_control_result_type import (
    OneOf_FieldCalculationsTurbulenceResultControlResultType,
)


class FieldCalculationsTurbulenceResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TURBULENCE",
        description="Schema name: FieldCalculationsTurbulenceResultControl",
    )
    name: str | None = Field(default=None)
    result_type: OneOf_FieldCalculationsTurbulenceResultControlResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
