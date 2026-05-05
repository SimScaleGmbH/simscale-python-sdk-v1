from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AbsoluteHarmonicVelocityFieldType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ABSOLUTE",
        description="Schema name: AbsoluteHarmonicVelocityFieldType",
    )
