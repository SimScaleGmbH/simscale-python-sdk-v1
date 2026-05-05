from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__friction_contact_contact_solution_method import (
    OneOf_FrictionContactContactSolutionMethod,
)
from simscale_sdk_v1.models.simulation.one_of__friction_contact_fictitious_clearance import (
    OneOf_FrictionContactFictitiousClearance,
)
from simscale_sdk_v1.models.simulation.one_of__friction_contact_friction_coefficient import (
    OneOf_FrictionContactFrictionCoefficient,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FrictionContact(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FRICTION_CONTACT",
        description="Schema name: FrictionContact",
    )
    name: str | None = Field(default=None)
    contact_solution_method: OneOf_FrictionContactContactSolutionMethod | None = Field(
        validation_alias="contactSolutionMethod", serialization_alias="contactSolutionMethod", default=None
    )
    friction_coefficient: OneOf_FrictionContactFrictionCoefficient | None = Field(
        validation_alias="frictionCoefficient", serialization_alias="frictionCoefficient", default=None
    )
    fictitious_clearance: OneOf_FrictionContactFictitiousClearance | None = Field(
        validation_alias="fictitiousClearance", serialization_alias="fictitiousClearance", default=None
    )
    master_topological_reference: TopologicalReference | None = Field(
        validation_alias="masterTopologicalReference", serialization_alias="masterTopologicalReference", default=None
    )
    slave_topological_reference: TopologicalReference | None = Field(
        validation_alias="slaveTopologicalReference", serialization_alias="slaveTopologicalReference", default=None
    )
