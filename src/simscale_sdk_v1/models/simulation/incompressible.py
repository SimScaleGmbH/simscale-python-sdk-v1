from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_concepts import AdvancedConcepts
from simscale_sdk_v1.models.simulation.fluid_initial_conditions import FluidInitialConditions
from simscale_sdk_v1.models.simulation.fluid_model import FluidModel
from simscale_sdk_v1.models.simulation.fluid_numerics import FluidNumerics
from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
from simscale_sdk_v1.models.simulation.fluid_simulation_control import FluidSimulationControl
from simscale_sdk_v1.models.simulation.incompressible_fluid_materials import IncompressibleFluidMaterials
from simscale_sdk_v1.models.simulation.one_of__incompressible_boundary_conditions import (
    OneOf_IncompressibleBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__incompressible_time_dependency import OneOf_IncompressibleTimeDependency


class Incompressible(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INCOMPRESSIBLE",
        description="Schema name: Incompressible",
    )
    turbulence_model: (
        Literal["SMAGORINSKY", "SPALARTALLMARAS", "NONE", "KEPSILON", "REALIZABLEKE", "KOMEGA", "KOMEGASST"] | None
    ) = Field(
        validation_alias="turbulenceModel",
        serialization_alias="turbulenceModel",
        default="KOMEGASST",
        description="Choose a turbulence model for your CFD analysis:No turbulence: LaminarRANS: k-epsilon, Realizable k-epsilon, k-omega and k-omega SSTLES: Smagorinsky, Spalart-AllmarasLearn more.",
    )
    adjoint_turbulence_model: Literal["ADJOINT_NONE", "ADJOINT_KOMEGASST"] | None = Field(
        validation_alias="adjointTurbulenceModel",
        serialization_alias="adjointTurbulenceModel",
        default="ADJOINT_KOMEGASST",
    )
    time_dependency: OneOf_IncompressibleTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
    algorithm: str | None = Field(default="SIMPLE")
    num_of_passive_species: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | None = Field(
        validation_alias="numOfPassiveSpecies",
        serialization_alias="numOfPassiveSpecies",
        default=0,
        description="Select the number of passive species involved in the simulation. Passive species allow you to simulate the transport of a scalar quantity within a fluid flow without affecting it. Learn more.",
    )
    enable_adjoint_optimization: bool | None = Field(
        validation_alias="enableAdjointOptimization", serialization_alias="enableAdjointOptimization", default=False
    )
    model: FluidModel | None = Field(default=None)
    materials: IncompressibleFluidMaterials | None = Field(default=None)
    initial_conditions: FluidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_IncompressibleBoundaryConditions] | None = Field(
        validation_alias="boundaryConditions", serialization_alias="boundaryConditions", default=None
    )
    advanced_concepts: AdvancedConcepts | None = Field(
        validation_alias="advancedConcepts", serialization_alias="advancedConcepts", default=None
    )
    numerics: FluidNumerics | None = Field(default=None)
    simulation_control: FluidSimulationControl | None = Field(
        validation_alias="simulationControl", serialization_alias="simulationControl", default=None
    )
    result_control: FluidResultControls | None = Field(
        validation_alias="resultControl", serialization_alias="resultControl", default=None
    )
