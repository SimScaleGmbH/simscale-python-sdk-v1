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
from simscale_sdk_v1.models.simulation.one_of__simerics_analysis_boundary_conditions import (
    OneOf_SimericsAnalysisBoundaryConditions,
)
from simscale_sdk_v1.models.simulation.one_of__simerics_analysis_mesh_settings import OneOf_SimericsAnalysisMeshSettings
from simscale_sdk_v1.models.simulation.one_of__simerics_analysis_time_dependency import (
    OneOf_SimericsAnalysisTimeDependency,
)
from simscale_sdk_v1.models.simulation.simerics_materials import SimericsMaterials


class SimericsAnalysis(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMERICS_ANALYSIS",
        description="Schema name: SimericsAnalysis",
    )
    is_compressible: bool | None = Field(
        validation_alias="isCompressible", serialization_alias="isCompressible", default=False
    )
    is_multicomponent: bool | None = Field(
        validation_alias="isMulticomponent", serialization_alias="isMulticomponent", default=False
    )
    is_multiphase: bool | None = Field(
        validation_alias="isMultiphase", serialization_alias="isMultiphase", default=False
    )
    is_cht: bool | None = Field(validation_alias="isCHT", serialization_alias="isCHT", default=False)
    number_of_phases: int | None = Field(
        validation_alias="numberOfPhases", serialization_alias="numberOfPhases", default=2
    )
    cavitation_model: Literal["CONSTANT_GAS_MASS_FRACTION", "NONE"] | None = Field(
        validation_alias="cavitationModel", serialization_alias="cavitationModel", default="NONE"
    )
    turbulence_model: Literal["NONE", "KEPSILON"] | None = Field(
        validation_alias="turbulenceModel",
        serialization_alias="turbulenceModel",
        default="KEPSILON",
        description="Choose a turbulence model for your CFD analysis:No turbulence: LaminarRANS: k-epsilonLearn more.",
    )
    time_dependency: OneOf_SimericsAnalysisTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
    model: FluidModel | None = Field(default=None)
    materials: SimericsMaterials | None = Field(default=None)
    initial_conditions: FluidInitialConditions | None = Field(
        validation_alias="initialConditions", serialization_alias="initialConditions", default=None
    )
    boundary_conditions: list[OneOf_SimericsAnalysisBoundaryConditions] | None = Field(
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
    mesh_settings: OneOf_SimericsAnalysisMeshSettings | None = Field(
        validation_alias="meshSettings", serialization_alias="meshSettings", default=None
    )
