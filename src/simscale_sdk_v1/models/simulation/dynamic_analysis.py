from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_boundary_conditions import (
    OneOf_DynamicAnalysisBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_connection_groups import (
    OneOf_DynamicAnalysisConnectionGroups,
)
from simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_connectors import OneOf_DynamicAnalysisConnectors
from simscale_sdk_v1.models.simulation.solid_element_technology import SolidElementTechnology
from simscale_sdk_v1.models.simulation.solid_initial_conditions import SolidInitialConditions
from simscale_sdk_v1.models.simulation.solid_material import SolidMaterial
from simscale_sdk_v1.models.simulation.solid_model import SolidModel
from simscale_sdk_v1.models.simulation.solid_numerics import SolidNumerics
from simscale_sdk_v1.models.simulation.solid_result_control import SolidResultControl
from simscale_sdk_v1.models.simulation.solid_simulation_control import SolidSimulationControl


class DynamicAnalysis(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DYNAMIC_ANALYSIS",
        description="Schema name: DynamicAnalysis",
    )
    connection_groups: list[OneOf_DynamicAnalysisConnectionGroups] | None = Field(
        validation_alias="connectionGroups", serialization_alias="connectionGroups", default=None
    )
    connectors: list[OneOf_DynamicAnalysisConnectors] | None = Field(default=None)
    element_technology: SolidElementTechnology | None = Field(
        validation_alias="elementTechnology", serialization_alias="elementTechnology", default=None
    )
    model: SolidModel | None = Field(default=None)
    materials: list[SolidMaterial] | None = Field(default=None)
    initial_conditions: SolidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_DynamicAnalysisBoundaryConditions] | None = Field(
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
