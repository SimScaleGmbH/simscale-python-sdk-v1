from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__cylindrical_component_partial_vector_function_axial import (
    OneOf_CylindricalComponentPartialVectorFunctionAxial,
)
from simscale_sdk_v1.models.simulation.one_of__cylindrical_component_partial_vector_function_radial import (
    OneOf_CylindricalComponentPartialVectorFunctionRadial,
)
from simscale_sdk_v1.models.simulation.one_of__cylindrical_component_partial_vector_function_tangential import (
    OneOf_CylindricalComponentPartialVectorFunctionTangential,
)


class CylindricalComponentPartialVectorFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CYLINDRICAL_COMPONENTS",
        description="Schema name: CylindricalComponentPartialVectorFunction",
    )
    radial: OneOf_CylindricalComponentPartialVectorFunctionRadial | None = Field(default=None)
    tangential: OneOf_CylindricalComponentPartialVectorFunctionTangential | None = Field(default=None)
    axial: OneOf_CylindricalComponentPartialVectorFunctionAxial | None = Field(default=None)
