from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__prescribed_optional_function_value import (
    OneOf_PrescribedOptionalFunctionValue,
)


class PrescribedOptionalFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESCRIBED",
        description="Schema name: PrescribedOptionalFunction",
    )
    value: OneOf_PrescribedOptionalFunctionValue | None = Field(default=None)
