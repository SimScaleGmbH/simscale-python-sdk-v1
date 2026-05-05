from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelativeHarmonicAccelerationFieldType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE",
        description="Schema name: RelativeHarmonicAccelerationFieldType",
    )
