from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__directional_dependency_darcy_forchheimer_type import (
    OneOf_DirectionalDependencyDarcyForchheimerType,
)


class DirectionalDependency(SimScaleModel):
    darcy_forchheimer_type: OneOf_DirectionalDependencyDarcyForchheimerType | None = Field(
        validation_alias="darcyForchheimerType", serialization_alias="darcyForchheimerType", default=None
    )
