from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SubspaceDimension(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SUBSPACE_DIMENSION",
        description="Schema name: SubspaceDimension",
    )
    subspace_dimension: int | None = Field(
        validation_alias="subspaceDimension",
        serialization_alias="subspaceDimension",
        default=0,
        description="Specify the subspace dimension. It is recommended to check the error log to get a hint for how to select it. It must be larger than the number of computed frequencies, it is ignored otherwise.",
    )
