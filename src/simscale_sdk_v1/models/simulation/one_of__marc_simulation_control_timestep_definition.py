from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_time_step_defintion import AutomaticTimeStepDefintion
from simscale_sdk_v1.models.simulation.manual_time_step_defintion import ManualTimeStepDefintion

# Choose between an automatic and a manual method to define the time increments during the simulation.Automatic: The solver dynamically adjusts the time step size based on convergence behavior and error tolerances. This is recommended for most nonlinear simulations to ensure stability during complex events like contact changes or material yielding.Manual: Specifies a fixed time step size for the duration of the simulation or specific intervals defined via a table. Use this option when the loading rate is constant and well-understood, or when a specific temporal resolution is required regardless of convergence ease. Cut-backs of the time steps are still allowed in case of non-convergence, up to the max number set by the user.
_ONE_OF__MARC_SIMULATION_CONTROL_TIMESTEP_DEFINITION_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticTimeStepDefintion,
    "MANUAL": ManualTimeStepDefintion,
}

OneOf_MarcSimulationControlTimestepDefinition = Annotated[
    Union[AutomaticTimeStepDefintion, ManualTimeStepDefintion],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_SIMULATION_CONTROL_TIMESTEP_DEFINITION_VARIANTS,
        )
    ),
]
