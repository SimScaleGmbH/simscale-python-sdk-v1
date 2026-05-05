from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__true_semi_implicit_solver import OneOf_TrueSemiImplicitSolver


class TrueSemiImplicit(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TRUE_SEMI_IMPLICIT",
        description="Schema name: TrueSemiImplicit",
    )
    limiter_iterations: int | None = Field(
        validation_alias="limiterIterations", serialization_alias="limiterIterations", default=8
    )
    compression_correction: bool | None = Field(
        validation_alias="compressionCorrection", serialization_alias="compressionCorrection", default=True
    )
    solver: OneOf_TrueSemiImplicitSolver | None = Field(default=None)
