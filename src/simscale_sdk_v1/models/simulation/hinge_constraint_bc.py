from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__hinge_constraint_bc_axis_definition import (
    OneOf_HingeConstraintBCAxisDefinition,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class HingeConstraintBC(SimScaleModel):
    """Replicate the behaviour of a freely rotating hinge fixed to the ground. Note that only a single face assignment is allowed. The assigned surface is constrained such that only rotational motion around the hinge axis is free. SimScale can automatically detect the axis of the hinge based on an assigned cylindrical surface, but the boundary condition also allows for a user-defined input."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HINGE_CONSTRAINT",
        description="Replicate the behaviour of a freely rotating hinge fixed to the ground. Note that only a single face assignment is allowed. The assigned surface is constrained such that only rotational motion around the hinge axis is free. SimScale can automatically detect the axis of the hinge based on an assigned cylindrical surface, but the boundary condition also allows for a user-defined input.  Schema name: HingeConstraintBC",
    )
    name: str | None = Field(default=None)
    axis_definition: OneOf_HingeConstraintBCAxisDefinition | None = Field(
        validation_alias="axisDefinition", serialization_alias="axisDefinition", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
