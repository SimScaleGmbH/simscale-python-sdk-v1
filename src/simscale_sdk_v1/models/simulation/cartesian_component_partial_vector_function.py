from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__cartesian_component_partial_vector_function_x import (
    OneOf_CartesianComponentPartialVectorFunctionX,
)
from simscale_sdk_v1.models.simulation.one_of__cartesian_component_partial_vector_function_y import (
    OneOf_CartesianComponentPartialVectorFunctionY,
)
from simscale_sdk_v1.models.simulation.one_of__cartesian_component_partial_vector_function_z import (
    OneOf_CartesianComponentPartialVectorFunctionZ,
)


class CartesianComponentPartialVectorFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CARTESIAN_COMPONENTS",
        description="Schema name: CartesianComponentPartialVectorFunction",
    )
    x: OneOf_CartesianComponentPartialVectorFunctionX | None = Field(default=None)
    y: OneOf_CartesianComponentPartialVectorFunctionY | None = Field(default=None)
    z: OneOf_CartesianComponentPartialVectorFunctionZ | None = Field(default=None)
