from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AutomaticMeshGrading(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC",
        description="Schema name: AutomaticMeshGrading",
    )
    fineness: Literal["VERY_COARSE", "COARSE", "MODERATE", "FINE", "VERY_FINE"] | None = Field(
        default="COARSE",
        description="The mesh grading specifies how fine details of the geometry are resolved and also influences the quality of the resulting elements.If you select the automatic grading, you can specify how fine your mesh should be (ranging from 1 - very coarse to 5 - very fine) and all additional parameters will be set automatically.For full control over the underlying parameters number of segements per edge, number of segements per radius and growth rate you can choose the manual mesh grading option. The figure shows meshes for grading 1 - very coarse (left) and 5 - very fine (right).",
    )
