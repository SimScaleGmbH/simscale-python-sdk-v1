from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.load_step import LoadStep
from simscale_sdk_v1.models.simulation.marc_connection_group import MarcConnectionGroup
from simscale_sdk_v1.models.simulation.marc_element_technology import MarcElementTechnology
from simscale_sdk_v1.models.simulation.marc_material import MarcMaterial
from simscale_sdk_v1.models.simulation.marc_numerics import MarcNumerics
from simscale_sdk_v1.models.simulation.marc_result_control import MarcResultControl
from simscale_sdk_v1.models.simulation.marc_simulation_control import MarcSimulationControl
from simscale_sdk_v1.models.simulation.one_of__marc_analysis_boundary_conditions import (
    OneOf_MarcAnalysisBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.remote_point_connection_marc import RemotePointConnectionMarc


class MarcAnalysis(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MARC_ANALYSIS",
        description="Schema name: MarcAnalysis",
    )
    thermal_effects: bool | None = Field(
        validation_alias="thermalEffects",
        serialization_alias="thermalEffects",
        default=False,
        description="Choose whether thermal effects should be included in the analysis, such as heat conduction, thermal loads, temperature fields, thermal expansion, and temperature-dependent material properties. When thermal effects are disabled, the analysis is purely mechanical and assumes constant temperature.Note: Changing this setting will delete all existing material definitions.",
    )
    connection_groups: list[MarcConnectionGroup] | None = Field(
        validation_alias="connectionGroups", serialization_alias="connectionGroups", default=None
    )
    connectors: list[RemotePointConnectionMarc] | None = Field(default=None)
    element_technology: MarcElementTechnology | None = Field(
        validation_alias="elementTechnology", serialization_alias="elementTechnology", default=None
    )
    materials: list[MarcMaterial] | None = Field(default=None)
    boundary_conditions: list[OneOf_MarcAnalysisBoundaryConditions] | None = Field(
        validation_alias="boundaryConditions", serialization_alias="boundaryConditions", default=None
    )
    numerics: MarcNumerics | None = Field(default=None)
    load_steps: list[LoadStep] | None = Field(
        validation_alias="loadSteps", serialization_alias="loadSteps", default=None
    )
    simulation_control: MarcSimulationControl | None = Field(
        validation_alias="simulationControl", serialization_alias="simulationControl", default=None
    )
    result_control: MarcResultControl | None = Field(
        validation_alias="resultControl", serialization_alias="resultControl", default=None
    )
