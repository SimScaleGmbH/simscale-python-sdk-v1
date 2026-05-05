from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_concepts import AdvancedConcepts
from simscale_sdk_v1.models.simulation.coupled_conjugate_heat_transfer_materials import (
    CoupledConjugateHeatTransferMaterials,
)
from simscale_sdk_v1.models.simulation.embedded_boundary_meshing import EmbeddedBoundaryMeshing
from simscale_sdk_v1.models.simulation.fluid_initial_conditions import FluidInitialConditions
from simscale_sdk_v1.models.simulation.fluid_model import FluidModel
from simscale_sdk_v1.models.simulation.fluid_numerics import FluidNumerics
from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
from simscale_sdk_v1.models.simulation.fluid_simulation_control import FluidSimulationControl
from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_boundary_conditions import (
    OneOf_EmbeddedBoundaryBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_external_flow_boundary_condition import (
    OneOf_EmbeddedBoundaryExternalFlowBoundaryCondition,
)
from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_time_dependency import (
    OneOf_EmbeddedBoundaryTimeDependency,
)
from simscale_sdk_v1.models.simulation.solar_calculator import SolarCalculator


class EmbeddedBoundary(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="EMBEDDED_BOUNDARY",
        description="Schema name: EmbeddedBoundary",
    )
    allow_external_flow: bool | None = Field(
        validation_alias="allowExternalFlow",
        serialization_alias="allowExternalFlow",
        default=False,
        description="This toggle allows you to create an additional external fluid domain via a Cartesian box. Enable this toggle if you want to simulate for example natural convection around your system and the external flow domain is not represented in your CAD model as a solid body.",
    )
    model: FluidModel | None = Field(default=None)
    solar_calculator: SolarCalculator | None = Field(
        validation_alias="solarCalculator", serialization_alias="solarCalculator", default=None
    )
    materials: CoupledConjugateHeatTransferMaterials | None = Field(default=None)
    initial_conditions: FluidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    external_flow_boundary_condition: OneOf_EmbeddedBoundaryExternalFlowBoundaryCondition | None = Field(
        validation_alias="externalFlowBoundaryCondition",
        serialization_alias="externalFlowBoundaryCondition",
        default=None,
    )
    boundary_conditions: list[OneOf_EmbeddedBoundaryBoundaryConditions] | None = Field(
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
    embedded_boundary_meshing: EmbeddedBoundaryMeshing | None = Field(
        validation_alias="embeddedBoundaryMeshing", serialization_alias="embeddedBoundaryMeshing", default=None
    )
    is_compressible: bool | None = Field(
        validation_alias="isCompressible",
        serialization_alias="isCompressible",
        default=False,
        description="Toggle off Compressible for small temperature variations within the domain, for example, in natural convection simulations (Boussinesq approximation). Use Gauge pressure (0 Pa). Toggle on Compressible to calculate resulting density variations within the domain based on pressure and temperature. Use Absolute pressure (for example, 101325 Pa at sea level)",
    )
    enable_radiation: bool | None = Field(
        validation_alias="enableRadiation",
        serialization_alias="enableRadiation",
        default=False,
        description="Heat transfer through radiation takes place in the form of electromagnetic waves and it can be calculated in the simulation. This phenomenon becomes more important when the temperature differences in the simulation domain are large. Learn more.",
    )
    enable_solar_load: bool | None = Field(
        validation_alias="enableSolarLoad",
        serialization_alias="enableSolarLoad",
        default=False,
        description="Enables the solar load model in the simulation. Diffuse and/or directional solar load contributions are specified in the solar calculator. The solar load terms will heat the external faces of the simulation domain. Moreover, if transparent and/or semi-transparent boundaries are present, internal surfaces of the domain might also be heated. All internal solids will be considered opaque. Learn more.",
    )
    enable_humidity_model: bool | None = Field(
        validation_alias="enableHumidityModel",
        serialization_alias="enableHumidityModel",
        default=False,
        description="Humidity model to simulate wet air. First turn on the compressible toggle to enable it. The simulation will take the effect of humid air on the flow field into account. Dry air is heavier than wet air and hence sinks. The model does not account for condensation and evaporation and is not applicable in cases where this is of concern, for example dehumidifiers. It is suitable for HVAC analysis and for temperature ranges of 0° to 100°C. Learn more.",
    )
    enable_joule_heating: bool | None = Field(
        validation_alias="enableJouleHeating",
        serialization_alias="enableJouleHeating",
        default=False,
        description="Enabling Joule heating gives you the possibility to solve a coupled electric conduction and conjugate heat transfer problem in a single simulation.",
    )
    turbulence_model: Literal["NONE", "KOMEGASST"] | None = Field(
        validation_alias="turbulenceModel",
        serialization_alias="turbulenceModel",
        default="KOMEGASST",
        description="Choose a turbulence model for your CFD analysis:No turbulence: LaminarRANS: k-omega SST ,k-epsilon",
    )
    time_dependency: OneOf_EmbeddedBoundaryTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
    num_of_passive_species: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] | None = Field(
        validation_alias="numOfPassiveSpecies",
        serialization_alias="numOfPassiveSpecies",
        default=0,
        description="Select the number of passive species involved in the simulation. Passive species allow you to simulate the transport of a scalar quantity within a fluid flow without affecting it. Learn more.",
    )
