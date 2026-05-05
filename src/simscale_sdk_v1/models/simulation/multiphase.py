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
from simscale_sdk_v1.models.simulation.one_of__multiphase_boundary_conditions import OneOf_MultiphaseBoundaryConditions


class Multiphase(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="MULTIPHASE", description="Schema name: Multiphase"
    )
    use_local_time_stepping: bool | None = Field(
        validation_alias="useLocalTimeStepping",
        serialization_alias="useLocalTimeStepping",
        default=False,
        description="With the Local time stepping option enabled, it’s possible to accelerate the simulation towards a steady-state. As a result, faster computing times and smaller result data size. Commonly used in ship hull resistance analysis.",
    )
    turbulence_model: Literal["SMAGORINSKY", "SPALARTALLMARAS", "NONE", "KEPSILON", "KOMEGA", "KOMEGASST"] | None = (
        Field(
            validation_alias="turbulenceModel",
            serialization_alias="turbulenceModel",
            default="KOMEGASST",
            description="Choose a turbulence model for your CFD analysis:No turbulence: LaminarRANS: k-epsilon, Realizable k-epsilon, k-omega and k-omega SSTLES: Smagorinsky, Spalart-AllmarasLearn more.",
        )
    )
    model: FluidModel | None = Field(default=None)
    materials: IncompressibleFluidMaterials | None = Field(default=None)
    initial_conditions: FluidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_MultiphaseBoundaryConditions] | None = Field(
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
