from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__coulomb_friction_nonlinearity_resolution import (
    OneOf_CoulombFrictionNonlinearityResolution,
)


class CoulombFriction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COULOMB_FRICTION",
        description="Schema name: CoulombFriction",
    )
    nonlinearity_resolution: OneOf_CoulombFrictionNonlinearityResolution | None = Field(
        validation_alias="nonlinearityResolution", serialization_alias="nonlinearityResolution", default=None
    )
