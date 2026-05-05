from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional__speed import Dimensional_Speed
from simscale_sdk_v1.models.simulation.fluid_solvers import FluidSolvers
from simscale_sdk_v1.models.simulation.relaxation_factor import RelaxationFactor
from simscale_sdk_v1.models.simulation.residual_controls import ResidualControls
from simscale_sdk_v1.models.simulation.schemes import Schemes
from simscale_sdk_v1.models.simulation.stabilization import Stabilization


class FluidNumerics(SimScaleModel):
    relaxation_type: str | None = Field(
        validation_alias="relaxationType", serialization_alias="relaxationType", default="MANUAL"
    )
    relaxation_factor: RelaxationFactor | None = Field(
        validation_alias="relaxationFactor", serialization_alias="relaxationFactor", default=None
    )
    diagonal_relaxation_factor: RelaxationFactor | None = Field(
        validation_alias="diagonalRelaxationFactor", serialization_alias="diagonalRelaxationFactor", default=None
    )
    viscous_work_included: bool | None = Field(
        validation_alias="viscousWorkIncluded",
        serialization_alias="viscousWorkIncluded",
        default=False,
        description="Enabling this option makes the viscous work terms included everywhere in the domain.",
    )
    radiation_resolution: Literal["COARSE", "MODERATE", "FINE"] | None = Field(
        validation_alias="radiationResolution", serialization_alias="radiationResolution", default="MODERATE"
    )
    momentum_predictor: bool | None = Field(
        validation_alias="momentumPredictor", serialization_alias="momentumPredictor", default=None
    )
    transonic: bool | None = Field(default=False)
    num_outer_correctors: int | None = Field(
        validation_alias="numOuterCorrectors", serialization_alias="numOuterCorrectors", default=3
    )
    num_correctors: int | None = Field(validation_alias="numCorrectors", serialization_alias="numCorrectors", default=4)
    num_non_orthogonal_correctors: int | None = Field(
        validation_alias="numNonOrthogonalCorrectors",
        serialization_alias="numNonOrthogonalCorrectors",
        default=1,
        description="The pressure equation is repeatedly solved based on the value of non-orthogonal correctors in the PISO/SIMPLE/PIMPLE algorithm. This may reduce the effect of bad mesh.",
    )
    smoothing_parameter: float | None = Field(
        validation_alias="smoothingParameter", serialization_alias="smoothingParameter", default=0.05
    )
    damping_coefficient: float | None = Field(
        validation_alias="dampingCoefficient", serialization_alias="dampingCoefficient", default=0.5
    )
    num_alpha_spread_iterations: int | None = Field(
        validation_alias="numAlphaSpreadIterations", serialization_alias="numAlphaSpreadIterations", default=0
    )
    num_alpha_sweep_iterations: int | None = Field(
        validation_alias="numAlphaSweepIterations", serialization_alias="numAlphaSweepIterations", default=0
    )
    evaluate_turbulence_only_on_final_iteration: bool | None = Field(
        validation_alias="evaluateTurbulenceOnlyOnFinalIteration",
        serialization_alias="evaluateTurbulenceOnlyOnFinalIteration",
        default=False,
    )
    pressure_reference_cell: int | None = Field(
        validation_alias="pressureReferenceCell",
        serialization_alias="pressureReferenceCell",
        default=0,
        description="Enter the cell where you want to define reference pressure in the PISO/SIMPLE/PIMPLE algorithm.",
    )
    pressure_reference_value: Dimensional_Pressure | None = Field(
        validation_alias="pressureReferenceValue", serialization_alias="pressureReferenceValue", default=None
    )
    velocity_limit: Dimensional_Speed | None = Field(
        validation_alias="velocityLimit", serialization_alias="velocityLimit", default=None
    )
    max_voltage_initial_iterations: float | None = Field(
        validation_alias="maxVoltageInitialIterations", serialization_alias="maxVoltageInitialIterations", default=200
    )
    voltage_initial_tolerance: float | None = Field(
        validation_alias="voltageInitialTolerance", serialization_alias="voltageInitialTolerance", default=1e-08
    )
    residual_controls: ResidualControls | None = Field(
        validation_alias="residualControls", serialization_alias="residualControls", default=None
    )
    solvers: FluidSolvers | None = Field(default=None)
    schemes: Schemes | None = Field(default=None)
    stabilization: Stabilization | None = Field(default=None)
