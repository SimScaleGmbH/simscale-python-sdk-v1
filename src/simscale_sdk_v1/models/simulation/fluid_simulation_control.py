from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.dimensional_function__time import DimensionalFunction_Time
from simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_adjustable_timestep import (
    OneOf_FluidSimulationControlAdjustableTimestep,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_decompose_algorithm import (
    OneOf_FluidSimulationControlDecomposeAlgorithm,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_write_control import (
    OneOf_FluidSimulationControlWriteControl,
)


class FluidSimulationControl(SimScaleModel):
    end_time: Dimensional_Time | None = Field(validation_alias="endTime", serialization_alias="endTime", default=None)
    adjoint_end_time: Dimensional_Time | None = Field(
        validation_alias="adjointEndTime", serialization_alias="adjointEndTime", default=None
    )
    number_of_iterations: int | None = Field(
        validation_alias="numberOfIterations",
        serialization_alias="numberOfIterations",
        default=None,
        description="This represents the total number of iterations at which the simulation will terminate. No further iterations will be performed beyond this point. Learn more.",
    )
    delta_t: Dimensional_Time | None = Field(validation_alias="deltaT", serialization_alias="deltaT", default=None)
    variable_delta_t: DimensionalFunction_Time | None = Field(
        validation_alias="variableDeltaT", serialization_alias="variableDeltaT", default=None
    )
    adjustable_timestep: OneOf_FluidSimulationControlAdjustableTimestep | None = Field(
        validation_alias="adjustableTimestep", serialization_alias="adjustableTimestep", default=None
    )
    write_control: OneOf_FluidSimulationControlWriteControl | None = Field(
        validation_alias="writeControl", serialization_alias="writeControl", default=None
    )
    relative_convergence_criteria: float | None = Field(
        validation_alias="relativeConvergenceCriteria",
        serialization_alias="relativeConvergenceCriteria",
        default=None,
        description="Steady-state simulation: This represents the relative error residuals that once attained by the solver the simulation is considered to be converged and will stop. The recommended value is 0.001. Transient simulation: This represents the relative error residuals that once attained by the solver the simulation will move to the next time-step regardless of the Number of iterations. The recommended value is 0.1.  Please note: Relative residual is defined as the residual in the current iteration divided by the maximum value of residual calculated up to that point.  Please note: Lower convergence criterion is demanded for Steady-state simulations because the initial guess is typically farther from the correct solution.",
    )
    num_processors: int | None = Field(
        validation_alias="numProcessors",
        serialization_alias="numProcessors",
        default=-1,
        description="Selecting more processor cores will speed up the simulation process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    max_run_time: Dimensional_Time | None = Field(
        validation_alias="maxRunTime", serialization_alias="maxRunTime", default=None
    )
    velocity_scaling: float | None = Field(
        validation_alias="velocityScaling",
        serialization_alias="velocityScaling",
        default=0.1,
        description="It affects the stability of the simulation. The default value of 0.1 is a good compromise between accuracy and computational requirements. Lower values of this parameter might increase the stability of the simulation at the cost of higher computational time.",
    )
    potential_foam_initialization: bool | None = Field(
        validation_alias="potentialFoamInitialization",
        serialization_alias="potentialFoamInitialization",
        default=False,
        description="This setting activates the solution of a potential flow field. The potential flow is used as initial condition for the actual simulation. This can accelerate convergence and improve stability during the first time steps. If you experience stability problems, this setting may bring some improvement.",
    )
    decompose_algorithm: OneOf_FluidSimulationControlDecomposeAlgorithm | None = Field(
        validation_alias="decomposeAlgorithm", serialization_alias="decomposeAlgorithm", default=None
    )
