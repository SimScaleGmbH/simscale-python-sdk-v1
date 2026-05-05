from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.function_parameter import FunctionParameter


class ExpressionFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="EXPRESSION",
        description="Schema name: ExpressionFunction",
    )
    expression: str | None = Field(default=None)
    available_variables: list[FunctionParameter] | None = Field(
        validation_alias="availableVariables", serialization_alias="availableVariables", default=None
    )
