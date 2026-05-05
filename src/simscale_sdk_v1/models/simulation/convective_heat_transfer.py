from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_concepts import AdvancedConcepts
from simscale_sdk_v1.models.simulation.convective_heat_transfer_materials import ConvectiveHeatTransferMaterials
from simscale_sdk_v1.models.simulation.fluid_initial_conditions import FluidInitialConditions
from simscale_sdk_v1.models.simulation.fluid_model import FluidModel
from simscale_sdk_v1.models.simulation.fluid_numerics import FluidNumerics
from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
from simscale_sdk_v1.models.simulation.fluid_simulation_control import FluidSimulationControl
from simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_boundary_conditions import (
    OneOf_ConvectiveHeatTransferBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_time_dependency import (
    OneOf_ConvectiveHeatTransferTimeDependency,
)


class ConvectiveHeatTransfer(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONVECTIVE_HEAT_TRANSFER",
        description="Schema name: ConvectiveHeatTransfer",
    )
    is_compressible: bool | None = Field(
        validation_alias="isCompressible",
        serialization_alias="isCompressible",
        default=False,
        description="Toggle off Compressible for small temperature variations within the domain, for example, in natural convection simulations (Boussinesq approximation). Use Gauge pressure (0 Pa). Toggle on Compressible to calculate resulting density variations within the domain based on pressure and temperature. Use Absolute pressure (for example, 101325 Pa at sea level)",
    )
    turbulence_model: Literal["SMAGORINSKY", "SPALARTALLMARAS", "NONE", "KEPSILON", "KOMEGASST"] | None = Field(
        validation_alias="turbulenceModel",
        serialization_alias="turbulenceModel",
        default="KOMEGASST",
        description="Choose a turbulence model for your CFD analysis:No turbulence: LaminarRANS: k-epsilon, Realizable k-epsilon, k-omega and k-omega SSTLES: Smagorinsky, Spalart-AllmarasLearn more.",
    )
    time_dependency: OneOf_ConvectiveHeatTransferTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
    enable_radiation: bool | None = Field(
        validation_alias="enableRadiation",
        serialization_alias="enableRadiation",
        default=False,
        description="Heat transfer through radiation takes place in the form of electromagnetic waves and it can be calculated in the simulation. This phenomenon becomes more important when the temperature differences in the simulation domain are large. Learn more.",
    )
    num_of_passive_species: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | None = Field(
        validation_alias="numOfPassiveSpecies",
        serialization_alias="numOfPassiveSpecies",
        default=0,
        description="Select the number of passive species involved in the simulation. Passive species allow you to simulate the transport of a scalar quantity within a fluid flow without affecting it. Learn more.",
    )
    model: FluidModel | None = Field(default=None)
    materials: ConvectiveHeatTransferMaterials | None = Field(default=None)
    initial_conditions: FluidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_ConvectiveHeatTransferBoundaryConditions] | None = Field(
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
