from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.contact import Contact
from simscale_sdk_v1.models.simulation.one_of__harmonic_analysis_boundary_conditions import (
    OneOf_HarmonicAnalysisBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__harmonic_analysis_connectors import OneOf_HarmonicAnalysisConnectors
from simscale_sdk_v1.models.simulation.solid_element_technology import SolidElementTechnology
from simscale_sdk_v1.models.simulation.solid_global_physics import SolidGlobalPhysics
from simscale_sdk_v1.models.simulation.solid_initial_conditions import SolidInitialConditions
from simscale_sdk_v1.models.simulation.solid_material import SolidMaterial
from simscale_sdk_v1.models.simulation.solid_model import SolidModel
from simscale_sdk_v1.models.simulation.solid_numerics import SolidNumerics
from simscale_sdk_v1.models.simulation.solid_result_control import SolidResultControl
from simscale_sdk_v1.models.simulation.solid_simulation_control import SolidSimulationControl


class HarmonicAnalysis(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HARMONIC_ANALYSIS",
        description="Schema name: HarmonicAnalysis",
    )
    connection_groups: list[Contact] | None = Field(
        validation_alias="connectionGroups", serialization_alias="connectionGroups", default=None
    )
    connectors: list[OneOf_HarmonicAnalysisConnectors] | None = Field(default=None)
    element_technology: SolidElementTechnology | None = Field(
        validation_alias="elementTechnology", serialization_alias="elementTechnology", default=None
    )
    global_physics: SolidGlobalPhysics | None = Field(
        validation_alias="globalPhysics", serialization_alias="globalPhysics", default=None
    )
    model: SolidModel | None = Field(default=None)
    materials: list[SolidMaterial] | None = Field(default=None)
    initial_conditions: SolidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_HarmonicAnalysisBoundaryConditions] | None = Field(
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
