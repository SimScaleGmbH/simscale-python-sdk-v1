from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MUMPSPreconditoner(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MUMPS_LDLT",
        description="Schema name: MUMPSPreconditoner",
    )
    actualisation_rate: int | None = Field(
        validation_alias="actualisationRate",
        serialization_alias="actualisationRate",
        default=30,
        description="Set the reactualisation intervall for the preconditioner matrix P. If this value is set to 30 the preconditioner is recomputed just every 30th iteration. This preconditioner is computionally more expensive than the incomplete LDLT factorization but nearer to the exact solution. This setting makes it possible to save computation time by taking advantage of this fact.",
    )
    memory_percentage_for_pivoting: float | None = Field(
        validation_alias="memoryPercentageForPivoting",
        serialization_alias="memoryPercentageForPivoting",
        default=20,
        description="Define how much additional memory should be reserved for the pivoting operations. If MUMPS estimates that the necessary space for factorising the matrix would be 100, choosing a value of 20 would mean that MUMPS allocates a memory space of 120.",
    )
