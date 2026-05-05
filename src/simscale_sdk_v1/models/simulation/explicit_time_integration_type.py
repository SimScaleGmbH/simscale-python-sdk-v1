from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__explicit_time_integration_type_scheme import (
    OneOf_ExplicitTimeIntegrationTypeScheme,
)


class ExplicitTimeIntegrationType(SimScaleModel):
    """Choose the time integration scheme typeImportant remarks:Choose implicit if the problem is static or dynamic but not so complex. Implicit analysis takes more solution time but can solve the problem easily with larger timesteps. Therefore, it is always recommended to use implicit time integration scheme. Choose explicit if the problem is only dynamic and highly complex. Explicit analysis takes less solution time but also needs more refined (small) timesteps to solve the problem. Therefore, in most of the cases it's not recommended due to convergence problems."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="EXPLICIT",
        description="Choose the time integration scheme typeImportant remarks:Choose implicit if the problem is static or dynamic but not so complex. Implicit analysis takes more solution time but can solve the problem easily with larger timesteps. Therefore, it is always recommended to use implicit time integration scheme. Choose explicit if the problem is only dynamic and highly complex. Explicit analysis takes less solution time but also needs more refined (small) timesteps to solve the problem. Therefore, in most of the cases it's not recommended due to convergence problems.    Schema name: ExplicitTimeIntegrationType",
    )
    scheme: OneOf_ExplicitTimeIntegrationTypeScheme | None = Field(default=None)
    scheme_formulation: Literal["ACCELERATION"] | None = Field(
        validation_alias="schemeFormulation",
        serialization_alias="schemeFormulation",
        default="ACCELERATION",
        description="Choose the primary variable for the time integration scheme.",
    )
    stop_on_cfl_criterion: bool | None = Field(
        validation_alias="stopOnCFLCriterion",
        serialization_alias="stopOnCFLCriterion",
        default=True,
        description="If activated the simulation run is stopped when at some point the Courant-Friedrichs-Lewy (CFL) condition is violated.",
    )
    mass_matrix_shift: float | None = Field(
        validation_alias="massMatrixShift",
        serialization_alias="massMatrixShift",
        default=0,
        description="This parameter cK allows the shifting of the mass matrix with the stiffness matrix multiplied by cK: M'=M + cK*K. This makes it possible to strongly improve convergence in dynamics with implicit time scheme by imposing a cut-off frequency inversely proportional to the value of cK (at the cost of a light distortion of all the eigen frequencies of the system).",
    )
