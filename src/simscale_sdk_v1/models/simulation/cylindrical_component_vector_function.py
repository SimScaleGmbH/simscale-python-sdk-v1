from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__cylindrical_component_vector_function_axial import (
    OneOf_CylindricalComponentVectorFunctionAxial,
)
from simscale_sdk_v1.models.simulation.one_of__cylindrical_component_vector_function_radial import (
    OneOf_CylindricalComponentVectorFunctionRadial,
)
from simscale_sdk_v1.models.simulation.one_of__cylindrical_component_vector_function_tangential import (
    OneOf_CylindricalComponentVectorFunctionTangential,
)


class CylindricalComponentVectorFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CYLINDRICAL_COMPONENTS",
        description="Schema name: CylindricalComponentVectorFunction",
    )
    radial: OneOf_CylindricalComponentVectorFunctionRadial | None = Field(default=None)
    tangential: OneOf_CylindricalComponentVectorFunctionTangential | None = Field(default=None)
    axial: OneOf_CylindricalComponentVectorFunctionAxial | None = Field(default=None)
