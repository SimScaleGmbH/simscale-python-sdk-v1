from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.meshing.one_of__hex_dominant_snappy_refinements import OneOf_HexDominantSnappyRefinements
from simscale_sdk_v1.models.meshing.one_of__hex_dominant_snappy_sizing import OneOf_HexDominantSnappySizing


class HexDominantSnappy(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HEX_DOMINANT_SNAPPY_V5",
        description="Schema name: HexDominantSnappy",
    )
    meshing_mode: Literal["INTERNAL"] | None = Field(
        validation_alias="meshingMode",
        serialization_alias="meshingMode",
        default="INTERNAL",
        description="The meshing mode defines how the mesher should generate the mesh.The Internal mode will create the mesh inside of the geometry body. If the CAD consists of multiple solids, the mesher will attempt to create a multiregion mesh which is suitable for conjugate heat transfer analyses. Use this mode if the CAD model already represents the final fluid domain.External meshing will create the mesh outside of the bodies. The absolute dimensions of the mesh are determined by the Background Mesh Box. Use this mode in case you want to extract the fluid domain around your model.The option Material point allows you to define a point inside the domain where the mesh will be placed. It can be used to select which part (or enclosed volume) of the model or should be meshed. The mesh will surround the material point and extend until the boundaries of the body. The location of the material point is defined by the Material Point geometry primitive.",
    )
    sizing: OneOf_HexDominantSnappySizing | None = Field(default=None)
    physics_based_meshing: bool | None = Field(
        validation_alias="physicsBasedMeshing",
        serialization_alias="physicsBasedMeshing",
        default=True,
        description="This toggle enables the automatic creation of boundary layers at no-slip walls. When toggled on, the meshing is started together with the simulation run.",
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
    refinements: list[OneOf_HexDominantSnappyRefinements] | None = Field(default=None)
