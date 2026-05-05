from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_nonlinear_solver_settings_convergence_method import (
    OneOf_MarcNonlinearSolverSettingsConvergenceMethod,
)


class MarcNonlinearSolverSettings(SimScaleModel):
    iterative_procedure: (
        Literal["FULL_NEWTON_RAPHSON", "MODIFIED_NEWTON_RAPHSON", "NEWTON_RAPHSON_STRAIN_CORRECTION"] | None
    ) = Field(
        validation_alias="iterativeProcedure",
        serialization_alias="iterativeProcedure",
        default="FULL_NEWTON_RAPHSON",
        description="Determines how the global stiffness matrix is updated during the nonlinear equilibrium search. This choice balances the speed of convergence against the computational cost per iteration.Full Newton-Raphson: Recomputes and factorizes the stiffness matrix at every single iteration. It provides the most robust convergence for highly nonlinear problems.Modified Newton-Raphson: Updates the stiffness matrix only at the beginning of each increment, reusing it for all subsequent iterations. This reduces the cost per iteration but may require more iterations or smaller time steps to converge in nonlinear cases.Newton-Raphson with strain correction: A variation of the Newton-Raphson method that applies a correction based on the strain increment to improve stability. It is particularly useful in material nonlinearities where plastic flow or creep is dominant.",
    )
    initial_stress_stiffness_contribution: (
        Literal[
            "FULL_CONTRIBUTION",
            "NO_CONTRIBUTION",
            "TENSILE_STRESS",
            "DEVIATORIC_STRESS",
            "BEGIN_INCREMENT_STRESS",
            "PRINCIPAL_TENSILE_STRESS",
        ]
        | None
    ) = Field(
        validation_alias="initialStressStiffnessContribution",
        serialization_alias="initialStressStiffnessContribution",
        default="FULL_CONTRIBUTION",
        description="Controls how the current state of stress in the material (geometric stiffness) influences the overall stiffness matrix. This is critical for capturing effects like &quot;stress stiffening&quot; in thin membranes or stability in buckled structures.Full contribution: Includes the complete geometric stiffness matrix based on the current stress state. Use this for standard large displacement or buckling analyses to ensure all physical stiffening/softening effects are captured.No initial stress stiffness: Ignores the geometric stiffness component, relying solely on the material stiffness. This can be used to improve stability in specific cases where stress-induced numerical fluctuations prevent convergence, though it may reduce physical accuracy.Only positive stress: Includes the geometric stiffness only for regions under tension, neglecting the destabilizing effects of compression. This is sometimes used to stabilize membranes or cables that cannot support compressive loads.Reduce proportional to hydrostatic pressure: Modifies the geometric stiffness based on the pressure component of the stress tensor. This is typically used in specialized rubber or foam applications to prevent numerical instabilities under high confinement.Stress at beginning of increment: Uses the stress state from the end of the previous increment to form the geometric stiffness for the current one. This can speed up calculation but may lead to &quot;lagging&quot; errors in highly dynamic or rapidly changing nonlinear cases.",
    )
    max_number_of_recycles: int | None = Field(
        validation_alias="maxNumberOfRecycles",
        serialization_alias="maxNumberOfRecycles",
        default=20,
        description="Defines the upper limit for the number of additional equilibrium iterations (recycles) within a single increment. If Marc cannot converge within this many recycles, the increment is reduced or the simulation stops.",
    )
    min_number_of_recycles: int | None = Field(
        validation_alias="minNumberOfRecycles",
        serialization_alias="minNumberOfRecycles",
        default=0,
        description="Defines the lower limit of the number of equilibrium recycles within a single increment. Setting this above 1 ensures that Marc always performs multiple iterations, which can help to avoid false convergence due to numerical noise.",
    )
    convergence_method: OneOf_MarcNonlinearSolverSettingsConvergenceMethod | None = Field(
        validation_alias="convergenceMethod", serialization_alias="convergenceMethod", default=None
    )
