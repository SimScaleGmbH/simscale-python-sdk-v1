from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.advanced_simmetrix_em_settings import AdvancedSimmetrixEmSettings
from simscale_sdk_v1.models.meshing.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_electromagnetics_refinements import (
    OneOf_SimmetrixMeshingElectromagneticsRefinements,
)
from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_electromagnetics_sizing import (
    OneOf_SimmetrixMeshingElectromagneticsSizing,
)


class SimmetrixMeshingElectromagnetics(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMMETRIX_MESHING_ELECTROMAGNETICS",
        description="Schema name: SimmetrixMeshingElectromagnetics",
    )
    sizing: OneOf_SimmetrixMeshingElectromagneticsSizing | None = Field(default=None)
    refinements: list[OneOf_SimmetrixMeshingElectromagneticsRefinements] | None = Field(default=None)
    num_of_processors: Literal[-1, 4, 8, 16, 32, 48, 64, 96] | None = Field(
        validation_alias="numOfProcessors",
        serialization_alias="numOfProcessors",
        default=-1,
        description="Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    max_meshing_run_time: Dimensional_Time | None = Field(
        validation_alias="maxMeshingRunTime", serialization_alias="maxMeshingRunTime", default=None
    )
    advanced_simmetrix_settings: AdvancedSimmetrixEmSettings | None = Field(
        validation_alias="advancedSimmetrixSettings", serialization_alias="advancedSimmetrixSettings", default=None
    )
