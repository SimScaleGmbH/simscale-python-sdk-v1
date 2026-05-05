from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GlobalVonMisesStressType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VON_MISES",
        description="Schema name: GlobalVonMisesStressType",
    )
    complex_number: Literal["REAL_AND_IMAGINARY"] | None = Field(
        validation_alias="complexNumber", serialization_alias="complexNumber", default="REAL_AND_IMAGINARY"
    )
