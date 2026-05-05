from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of_mules_solver_semi_implicit import OneOf_MULESSolverSemiImplicit


class MULESSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="MULES_V7", description="Schema name: MULESSolver"
    )
    alpha_correctors: int | None = Field(
        validation_alias="alphaCorrectors", serialization_alias="alphaCorrectors", default=2
    )
    alpha_sub_cycles: int | None = Field(
        validation_alias="alphaSubCycles", serialization_alias="alphaSubCycles", default=2
    )
    compression_coefficient: float | None = Field(
        validation_alias="compressionCoefficient", serialization_alias="compressionCoefficient", default=1
    )
    isotropic_compression_coefficient: float | None = Field(
        validation_alias="isotropicCompressionCoefficient",
        serialization_alias="isotropicCompressionCoefficient",
        default=0.25,
    )
    semi_implicit: OneOf_MULESSolverSemiImplicit | None = Field(
        validation_alias="semiImplicit", serialization_alias="semiImplicit", default=None
    )
