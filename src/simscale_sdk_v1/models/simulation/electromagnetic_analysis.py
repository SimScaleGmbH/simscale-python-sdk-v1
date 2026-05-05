from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.coil import Coil
from simscale_sdk_v1.models.simulation.electromagnetic_advanced_concepts import ElectromagneticAdvancedConcepts
from simscale_sdk_v1.models.simulation.electromagnetic_initial_conditions import ElectromagneticInitialConditions
from simscale_sdk_v1.models.simulation.electromagnetic_material import ElectromagneticMaterial
from simscale_sdk_v1.models.simulation.electromagnetic_numerics import ElectromagneticNumerics
from simscale_sdk_v1.models.simulation.electromagnetic_result_control import ElectromagneticResultControl
from simscale_sdk_v1.models.simulation.electromagnetic_simulation_control import ElectromagneticSimulationControl
from simscale_sdk_v1.models.simulation.one_of__electromagnetic_analysis_boundary_conditions import (
    OneOf_ElectromagneticAnalysisBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__electromagnetic_analysis_model import OneOf_ElectromagneticAnalysisModel


class ElectromagneticAnalysis(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ELECTROMAGNETIC_ANALYSIS",
        description="Schema name: ElectromagneticAnalysis",
    )
    model: OneOf_ElectromagneticAnalysisModel | None = Field(default=None)
    materials: list[ElectromagneticMaterial] | None = Field(default=None)
    initial_conditions: ElectromagneticInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    coils: list[Coil] | None = Field(default=None)
    boundary_conditions: list[OneOf_ElectromagneticAnalysisBoundaryConditions] | None = Field(
        validation_alias="boundaryConditions", serialization_alias="boundaryConditions", default=None
    )
    advanced_concepts: ElectromagneticAdvancedConcepts | None = Field(
        validation_alias="advancedConcepts", serialization_alias="advancedConcepts", default=None
    )
    result_control: ElectromagneticResultControl | None = Field(
        validation_alias="resultControl", serialization_alias="resultControl", default=None
    )
    numerics: ElectromagneticNumerics | None = Field(default=None)
    simulation_control: ElectromagneticSimulationControl | None = Field(
        validation_alias="simulationControl", serialization_alias="simulationControl", default=None
    )
