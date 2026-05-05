from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__elastic_support_bc_spring_stiffness import (
    OneOf_ElasticSupportBCSpringStiffness,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ElasticSupportBC(SimScaleModel):
    """The elastic support constraint can be used to model an elastic foundation between the assigned surfaces and the rigid ground. Additionally it can be used to prevent rigid body motions in a nonlinear analysis. The constraint acts on tension and compression forces and all stiffness values are expressed in the global coordinate system.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ELASTIC_SUPPORT",
        description="The elastic support constraint can be used to model an elastic foundation between the assigned surfaces and the rigid ground. Additionally it can be used to prevent rigid body motions in a nonlinear analysis. The constraint acts on tension and compression forces and all stiffness values are expressed in the global coordinate system.Learn more.  Schema name: ElasticSupportBC",
    )
    name: str | None = Field(default=None)
    spring_stiffness: OneOf_ElasticSupportBCSpringStiffness | None = Field(
        validation_alias="springStiffness", serialization_alias="springStiffness", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
