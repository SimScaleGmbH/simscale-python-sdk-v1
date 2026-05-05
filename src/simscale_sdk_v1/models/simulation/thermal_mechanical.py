from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_boundary_conditions import (
    OneOf_ThermalMechanicalBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_connection_groups import (
    OneOf_ThermalMechanicalConnectionGroups,
)
from simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_time_dependency import (
    OneOf_ThermalMechanicalTimeDependency,
)
from simscale_sdk_v1.models.simulation.pin_connector import PinConnector
from simscale_sdk_v1.models.simulation.solid_element_technology import SolidElementTechnology
from simscale_sdk_v1.models.simulation.solid_initial_conditions import SolidInitialConditions
from simscale_sdk_v1.models.simulation.solid_material import SolidMaterial
from simscale_sdk_v1.models.simulation.solid_model import SolidModel
from simscale_sdk_v1.models.simulation.solid_numerics import SolidNumerics
from simscale_sdk_v1.models.simulation.solid_result_control import SolidResultControl
from simscale_sdk_v1.models.simulation.solid_simulation_control import SolidSimulationControl


class ThermalMechanical(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="THERMAL_MECHANICAL",
        description="Schema name: ThermalMechanical",
    )
    time_dependency: OneOf_ThermalMechanicalTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
    inertia_effect: str | None = Field(
        validation_alias="inertiaEffect",
        serialization_alias="inertiaEffect",
        default="STATIC",
        description="Select if inertia effects should be considered in the analysis. If high loading accelerations or impacts are present then dynamic is the right choice for this parameter. If the dynamic effects are negligible, static should be selected.",
    )
    non_linear_analysis: bool | None = Field(
        validation_alias="nonLinearAnalysis",
        serialization_alias="nonLinearAnalysis",
        default=False,
        description="Choose if your analysis should feature any kind of nonlinearity like physical contacts, nonlinear materials as hyperelasticity or plasticity or large rotations and large deformations, temperature dependant material properties or temperature dependant boundary conditions. For a linear analysis none of those nonlinearities are available.",
    )
    connection_groups: list[OneOf_ThermalMechanicalConnectionGroups] | None = Field(
        validation_alias="connectionGroups", serialization_alias="connectionGroups", default=None
    )
    connectors: list[PinConnector] | None = Field(default=None)
    element_technology: SolidElementTechnology | None = Field(
        validation_alias="elementTechnology", serialization_alias="elementTechnology", default=None
    )
    model: SolidModel | None = Field(default=None)
    materials: list[SolidMaterial] | None = Field(default=None)
    initial_conditions: SolidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_ThermalMechanicalBoundaryConditions] | None = Field(
        validation_alias="boundaryConditions", serialization_alias="boundaryConditions", default=None
    )
    numerics: SolidNumerics | None = Field(default=None)
    simulation_control: SolidSimulationControl | None = Field(
        validation_alias="simulationControl", serialization_alias="simulationControl", default=None
    )
    result_control: SolidResultControl | None = Field(
        validation_alias="resultControl", serialization_alias="resultControl", default=None
    )
    mesh_order: Literal["FIRST", "SECOND", "NONE"] | None = Field(
        validation_alias="meshOrder", serialization_alias="meshOrder", default="NONE"
    )
