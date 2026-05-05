from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_modelling import AdvancedModelling
from simscale_sdk_v1.models.simulation.flow_domain_boundaries import FlowDomainBoundaries
from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
from simscale_sdk_v1.models.simulation.fluid_simulation_control import FluidSimulationControl
from simscale_sdk_v1.models.simulation.incompressible_material import IncompressibleMaterial
from simscale_sdk_v1.models.simulation.one_of__incompressible_pacefish_mesh_settings_new import (
    OneOf_IncompressiblePacefishMeshSettingsNew,
)


class IncompressiblePacefish(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INCOMPRESSIBLE_PACEFISH",
        description="Schema name: IncompressiblePacefish",
    )
    bounding_box_uuid: str | None = Field(
        validation_alias="boundingBoxUuid", serialization_alias="boundingBoxUuid", default=None
    )
    turbulence_model: (
        Literal["SMAGORINSKY", "SMAGORINSKY_DIRECT", "NONE", "KOMEGASST", "KOMEGASST_DDES", "KOMEGASST_IDDES"] | None
    ) = Field(
        validation_alias="turbulenceModel",
        serialization_alias="turbulenceModel",
        default="KOMEGASST_DDES",
        description="Choose between RANS, LES, or DES turbulence models. Learn more.",
    )
    material: IncompressibleMaterial | None = Field(default=None)
    flow_domain_boundaries: FlowDomainBoundaries | None = Field(
        validation_alias="flowDomainBoundaries", serialization_alias="flowDomainBoundaries", default=None
    )
    simulation_control: FluidSimulationControl | None = Field(
        validation_alias="simulationControl", serialization_alias="simulationControl", default=None
    )
    advanced_modelling: AdvancedModelling | None = Field(
        validation_alias="advancedModelling", serialization_alias="advancedModelling", default=None
    )
    result_control: FluidResultControls | None = Field(
        validation_alias="resultControl", serialization_alias="resultControl", default=None
    )
    mesh_settings_new: OneOf_IncompressiblePacefishMeshSettingsNew | None = Field(
        validation_alias="meshSettingsNew", serialization_alias="meshSettingsNew", default=None
    )
