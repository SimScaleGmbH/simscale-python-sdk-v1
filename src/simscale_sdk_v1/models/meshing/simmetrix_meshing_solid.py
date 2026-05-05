from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.advanced_simmetrix_solid_settings import AdvancedSimmetrixSolidSettings
from simscale_sdk_v1.models.meshing.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_automatic_sweep_parameters import (
    OneOf_SimmetrixMeshingSolidAutomaticSweepParameters,
)
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_refinements import (
    OneOf_SimmetrixMeshingSolidRefinements,
)
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_sizing import OneOf_SimmetrixMeshingSolidSizing


class SimmetrixMeshingSolid(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMMETRIX_MESHING_SOLID",
        description="Schema name: SimmetrixMeshingSolid",
    )
    sizing: OneOf_SimmetrixMeshingSolidSizing | None = Field(default=None)
    refinements: list[OneOf_SimmetrixMeshingSolidRefinements] | None = Field(default=None)
    automatic_sweep_parameters: OneOf_SimmetrixMeshingSolidAutomaticSweepParameters | None = Field(
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
    advanced_simmetrix_settings: AdvancedSimmetrixSolidSettings | None = Field(
        validation_alias="advancedSimmetrixSettings", serialization_alias="advancedSimmetrixSettings", default=None
    )
