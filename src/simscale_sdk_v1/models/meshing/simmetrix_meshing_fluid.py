from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.advanced_simmetrix_fluid_settings import AdvancedSimmetrixFluidSettings
from simscale_sdk_v1.models.meshing.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_automatic_layer_settings import (
    OneOf_SimmetrixMeshingFluidAutomaticLayerSettings,
)
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_automatic_sweep_parameters import (
    OneOf_SimmetrixMeshingFluidAutomaticSweepParameters,
)
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_refinements import (
    OneOf_SimmetrixMeshingFluidRefinements,
)
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_sizing import OneOf_SimmetrixMeshingFluidSizing
from simscale_sdk_v1.models.meshing.simmetrix_cell_zones import SimmetrixCellZones


class SimmetrixMeshingFluid(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMMETRIX_MESHING_FLUID_V16",
        description="Schema name: SimmetrixMeshingFluid",
    )
    sizing: OneOf_SimmetrixMeshingFluidSizing | None = Field(default=None)
    refinements: list[OneOf_SimmetrixMeshingFluidRefinements] | None = Field(default=None)
    cell_zones: list[SimmetrixCellZones] | None = Field(
        validation_alias="cellZones", serialization_alias="cellZones", default=None
    )
    automatic_layer_settings: OneOf_SimmetrixMeshingFluidAutomaticLayerSettings | None = Field(
        validation_alias="automaticLayerSettings", serialization_alias="automaticLayerSettings", default=None
    )
    physics_based_meshing: bool | None = Field(
        validation_alias="physicsBasedMeshing",
        serialization_alias="physicsBasedMeshing",
        default=True,
        description="Physics-based meshing takes setup information like materials, boundary conditions, and source terms into account to size the mesh accordingly. When enabled, the following adaptations will be made:Refinements on inlets and outletsDifferent sizing for solid and fluid regions in CHT simulations When toggled on users don’t have to worry about creating a separate cell zone.",
    )
    hex_core: bool | None = Field(
        validation_alias="hexCore",
        serialization_alias="hexCore",
        default=True,
        description="If Hex element core is activated, the interior of the mesh gets covered by hexahedral elements. The transition to the triangulated surface mesh is covered by tetrahedral and pyramid elements.Meshclip through a hex-core mesh.",
    )
    automatic_sweep_parameters: OneOf_SimmetrixMeshingFluidAutomaticSweepParameters | None = Field(
        validation_alias="automaticSweepParameters", serialization_alias="automaticSweepParameters", default=None
    )
    num_of_processors: Literal[-1, 4, 8, 16, 32, 48, 64, 96] | None = Field(
        validation_alias="numOfProcessors",
        serialization_alias="numOfProcessors",
        default=-1,
        description="Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    max_meshing_run_time: Dimensional_Time | None = Field(
        validation_alias="maxMeshingRunTime", serialization_alias="maxMeshingRunTime", default=None
    )
    advanced_simmetrix_settings: AdvancedSimmetrixFluidSettings | None = Field(
        validation_alias="advancedSimmetrixSettings", serialization_alias="advancedSimmetrixSettings", default=None
    )
