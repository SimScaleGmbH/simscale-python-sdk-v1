from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.displacements_convergence_method import DisplacementsConvergenceMethod
from simscale_sdk_v1.models.simulation.residuals_convergence_method import ResidualsConvergenceMethod
from simscale_sdk_v1.models.simulation.residuals_or_displacements_convergence_method import (
    ResidualsOrDisplacementsConvergenceMethod,
)
from simscale_sdk_v1.models.simulation.strain_energy_convergence_method import StrainEnergyConvergenceMethod

# Selects the physical quantity used to determine if the simulation has converged. The force residual or the displacement changes must satisfy their respective tolerances.Displacement: Monitors the change in nodal displacements between iterations; convergence is achieved when displacements stabilize.Force: Monitors the force residuals; convergence is achieved when the out-of-balance force residuals become small enough relative to the applied loads.Both: Both the force residual and displacement changes must satisfy their respective tolerances.
_ONE_OF__MARC_NONLINEAR_SOLVER_SETTINGS_CONVERGENCE_METHOD_VARIANTS: dict[str, type] = {
    "RESIDUALS": ResidualsConvergenceMethod,
    "DISPLACEMENTS": DisplacementsConvergenceMethod,
    "STRAIN_ENERGY": StrainEnergyConvergenceMethod,
    "RESIDUALS_OR_DISPLACEMENTS": ResidualsOrDisplacementsConvergenceMethod,
}

OneOf_MarcNonlinearSolverSettingsConvergenceMethod = Annotated[
    Union[
        ResidualsConvergenceMethod,
        DisplacementsConvergenceMethod,
        StrainEnergyConvergenceMethod,
        ResidualsOrDisplacementsConvergenceMethod,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_NONLINEAR_SOLVER_SETTINGS_CONVERGENCE_METHOD_VARIANTS,
        )
    ),
]
