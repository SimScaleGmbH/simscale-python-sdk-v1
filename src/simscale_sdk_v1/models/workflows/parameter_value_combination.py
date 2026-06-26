from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.json_node import JsonNode


class ParameterValueCombination(SimScaleModel):
    parameter_values: dict[str, JsonNode] | None = Field(
        validation_alias="parameterValues", serialization_alias="parameterValues", default=None
    )
