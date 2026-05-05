from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_concepts import AdvancedConcepts
from simscale_sdk_v1.models.simulation.conjugate_heat_transfer_materials import ConjugateHeatTransferMaterials
from simscale_sdk_v1.models.simulation.fluid_initial_conditions import FluidInitialConditions
from simscale_sdk_v1.models.simulation.fluid_interface import FluidInterface
from simscale_sdk_v1.models.simulation.fluid_model import FluidModel
from simscale_sdk_v1.models.simulation.fluid_numerics import FluidNumerics
from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
from simscale_sdk_v1.models.simulation.fluid_simulation_control import FluidSimulationControl
from simscale_sdk_v1.models.simulation.one_of__conjugate_heat_transfer_boundary_conditions import (
    OneOf_ConjugateHeatTransferBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__conjugate_heat_transfer_time_dependency import (
    OneOf_ConjugateHeatTransferTimeDependency,
)


class ConjugateHeatTransfer(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONJUGATE_HEAT_TRANSFER",
        description="Schema name: ConjugateHeatTransfer",
    )
    turbulence_model: Literal["SMAGORINSKY", "NONE", "KEPSILON", "KOMEGASST"] | None = Field(
        validation_alias="turbulenceModel",
        serialization_alias="turbulenceModel",
        default="KOMEGASST",
        description="Choose a turbulence model for your CFD analysis:No turbulence: LaminarRANS: k-epsilon, Realizable k-epsilon, k-omega and k-omega SSTLES: Smagorinsky, Spalart-AllmarasLearn more.",
    )
    time_dependency: OneOf_ConjugateHeatTransferTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
    enable_radiation: bool | None = Field(
        validation_alias="enableRadiation",
        serialization_alias="enableRadiation",
        default=False,
        description="Heat transfer through radiation takes place in the form of electromagnetic waves and it can be calculated in the simulation. This phenomenon becomes more important when the temperature differences in the simulation domain are large. Learn more.",
    )
    connection_groups: list[FluidInterface] | None = Field(
        validation_alias="connectionGroups", serialization_alias="connectionGroups", default=None
    )
    model: FluidModel | None = Field(default=None)
    materials: ConjugateHeatTransferMaterials | None = Field(default=None)
    initial_conditions: FluidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_ConjugateHeatTransferBoundaryConditions] | None = Field(
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
    contact_handling_mode: Literal["MANUAL", "AUTO"] | None = Field(
        validation_alias="contactHandlingMode", serialization_alias="contactHandlingMode", default="MANUAL"
    )
