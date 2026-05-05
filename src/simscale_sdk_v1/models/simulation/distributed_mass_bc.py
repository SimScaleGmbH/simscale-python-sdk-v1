from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__distributed_mass_bc_mass_definition import (
    OneOf_DistributedMassBCMassDefinition,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class DistributedMassBC(SimScaleModel):
    """Define a Distributed mass boundary condition in order to insert an additional mass on a specific face of the active model."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISTRIBUTED_MASS",
        description="Define a Distributed mass boundary condition in order to insert an additional mass on a specific face of the active model.  Schema name: DistributedMassBC",
    )
    name: str | None = Field(default=None)
    mass_definition: OneOf_DistributedMassBCMassDefinition | None = Field(
        validation_alias="massDefinition", serialization_alias="massDefinition", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
