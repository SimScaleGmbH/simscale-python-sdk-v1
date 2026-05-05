from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__orthotropic_spring_stiffness_stiffness_definition import (
    OneOf_OrthotropicSpringStiffnessStiffnessDefinition,
)


class OrthotropicSpringStiffness(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ORTHOTROPIC",
        description="Schema name: OrthotropicSpringStiffness",
    )
    stiffness_definition: OneOf_OrthotropicSpringStiffnessStiffnessDefinition | None = Field(
        validation_alias="stiffnessDefinition", serialization_alias="stiffnessDefinition", default=None
    )
