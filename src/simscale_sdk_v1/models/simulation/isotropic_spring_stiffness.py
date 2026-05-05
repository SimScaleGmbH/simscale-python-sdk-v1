from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__isotropic_spring_stiffness_stiffness_definition import (
    OneOf_IsotropicSpringStiffnessStiffnessDefinition,
)


class IsotropicSpringStiffness(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Schema name: IsotropicSpringStiffness",
    )
    stiffness_definition: OneOf_IsotropicSpringStiffnessStiffnessDefinition | None = Field(
        validation_alias="stiffnessDefinition", serialization_alias="stiffnessDefinition", default=None
    )
