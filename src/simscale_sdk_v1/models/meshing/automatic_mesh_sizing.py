from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AutomaticMeshSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC",
        description="Schema name: AutomaticMeshSizing",
    )
    fineness: Literal["VERY_COARSE", "COARSE", "MODERATE", "FINE", "VERY_FINE"] | None = Field(
        default="COARSE",
        description="Choose between Automatic and Manual mesh settings. Learn more.Note: Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.",
    )
