from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__partial_vector_function_x import OneOf_PartialVectorFunctionX
from simscale_sdk_v1.models.simulation.one_of__partial_vector_function_y import OneOf_PartialVectorFunctionY
from simscale_sdk_v1.models.simulation.one_of__partial_vector_function_z import OneOf_PartialVectorFunctionZ


class PartialVectorFunction(SimScaleModel):
    x: OneOf_PartialVectorFunctionX | None = Field(default=None)
    y: OneOf_PartialVectorFunctionY | None = Field(default=None)
    z: OneOf_PartialVectorFunctionZ | None = Field(default=None)
