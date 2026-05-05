from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class PacefishFinenessModerate(SimScaleModel):
    """This parameter determines the fineness of the mesh and affects the overall number of cells. It is recommended to start with the coarse setting. Find out more.Note: This setting will impact the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MODERATE",
        description="This parameter determines the fineness of the mesh and affects the overall number of cells. It is recommended to start with the coarse setting. Find out more.Note: This setting will impact the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.  Schema name: PacefishFinenessModerate",
    )
