from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MultifrontalSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MULTIFRONT",
        description="Schema name: MultifrontalSolver",
    )
    renumbering_method: Literal["MDA", "MD"] | None = Field(
        validation_alias="renumberingMethod",
        serialization_alias="renumberingMethod",
        default="MDA",
        description="Choose a renumbering method for the solution process.For large models around and above 50000 degrees of freedom you should consider using MDA.",
    )
    force_symmetric: bool | None = Field(
        validation_alias="forceSymmetric",
        serialization_alias="forceSymmetric",
        default=False,
        description="Choose if you want to enforce a symmetric matrix.",
    )
    precision_singularity_detection: int | None = Field(
        validation_alias="precisionSingularityDetection",
        serialization_alias="precisionSingularityDetection",
        default=8,
        description="Define the precision value for the detection of a singular matrix. Positive values enable the check, with 9 being a good starting point. Smaller values make the check more strict. This is an advanced option that should only be used to debug a model.",
    )
    stop_if_singular: bool | None = Field(
        validation_alias="stopIfSingular",
        serialization_alias="stopIfSingular",
        default=True,
        description="Choose if the calculation should be stopped if the problem turns out to be singular.",
    )
    eliminate_lagrange_multipliers: bool | None = Field(
        validation_alias="eliminateLagrangeMultipliers",
        serialization_alias="eliminateLagrangeMultipliers",
        default=False,
        description="This option makes it possible to eliminate the Lagrange Multipliers which are introduced by generalized boundary conditions like bonded contact, remote boundary conditions and symmetry conditions. If activated, this option removes the Lagrange Multipliers which leads to a reduction of the total number of unknowns and can increase the robustness of iterative solvers.",
    )
