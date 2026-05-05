from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__scalar_transport_result_control_write_control import (
    OneOf_ScalarTransportResultControlWriteControl,
)


class ScalarTransportResultControl(SimScaleModel):
    name: str | None = Field(default=None)
    diffusion_coefficient: float | None = Field(
        validation_alias="diffusionCoefficient", serialization_alias="diffusionCoefficient", default=0
    )
    volume_mode: Literal["SPECIFIC", "ABSOLUTE"] | None = Field(
        validation_alias="volumeMode", serialization_alias="volumeMode", default="SPECIFIC"
    )
    su: float | None = Field(default=1)
    sp: float | None = Field(default=0)
    write_control: OneOf_ScalarTransportResultControlWriteControl | None = Field(
        validation_alias="writeControl", serialization_alias="writeControl", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
