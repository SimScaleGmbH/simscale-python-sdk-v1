from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__component_vector_function_x import OneOf_ComponentVectorFunctionX
from simscale_sdk_v1.models.simulation.one_of__component_vector_function_y import OneOf_ComponentVectorFunctionY
from simscale_sdk_v1.models.simulation.one_of__component_vector_function_z import OneOf_ComponentVectorFunctionZ


class ComponentVectorFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COMPONENT",
        description="Schema name: ComponentVectorFunction",
    )
    x: OneOf_ComponentVectorFunctionX | None = Field(default=None)
    y: OneOf_ComponentVectorFunctionY | None = Field(default=None)
    z: OneOf_ComponentVectorFunctionZ | None = Field(default=None)
