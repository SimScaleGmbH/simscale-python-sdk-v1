from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_concepts import AdvancedConcepts
from simscale_sdk_v1.models.simulation.compressible_fluid_materials import CompressibleFluidMaterials
from simscale_sdk_v1.models.simulation.fluid_initial_conditions import FluidInitialConditions
from simscale_sdk_v1.models.simulation.fluid_model import FluidModel
from simscale_sdk_v1.models.simulation.fluid_numerics import FluidNumerics
from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
from simscale_sdk_v1.models.simulation.fluid_simulation_control import FluidSimulationControl
from simscale_sdk_v1.models.simulation.one_of__compressible_boundary_conditions import (
    OneOf_CompressibleBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__compressible_time_dependency import OneOf_CompressibleTimeDependency


class Compressible(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COMPRESSIBLE",
        description="Schema name: Compressible",
    )
    turbulence_model: Literal["SMAGORINSKY", "SPALARTALLMARAS", "NONE", "KEPSILON", "KOMEGASST"] | None = Field(
        validation_alias="turbulenceModel",
        serialization_alias="turbulenceModel",
        default="KOMEGASST",
        description="Choose a turbulence model for your CFD analysis:No turbulence: LaminarRANS: k-epsilon, Realizable k-epsilon, k-omega and k-omega SSTLES: Smagorinsky, Spalart-AllmarasLearn more.",
    )
    time_dependency: OneOf_CompressibleTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
    model: FluidModel | None = Field(default=None)
    materials: CompressibleFluidMaterials | None = Field(default=None)
    initial_conditions: FluidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_CompressibleBoundaryConditions] | None = Field(
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
