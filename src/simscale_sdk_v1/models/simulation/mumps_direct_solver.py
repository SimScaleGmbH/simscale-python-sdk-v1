from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MumpsDirectSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MUMPS_DIRECT",
        description="Schema name: MumpsDirectSolver",
    )
    auto_constrain: bool | None = Field(
        validation_alias="autoConstrain",
        serialization_alias="autoConstrain",
        default=False,
        description="Automatically applies small artificial stiffness to unconstrained bodies to prevent numerical singularities during the initial stages of a simulation. Use this when your setup has parts that are not fully fixed until contact is established.",
    )
