from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AbsoluteHarmonicDisplacementType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ABSOLUTE",
        description="Schema name: AbsoluteHarmonicDisplacementType",
    )
    complex_number: Literal["REAL_AND_IMAGINARY", "MAGNITUDE_AND_PHASE"] | None = Field(
        validation_alias="complexNumber", serialization_alias="complexNumber", default="MAGNITUDE_AND_PHASE"
    )
