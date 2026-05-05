from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class QZ(SimScaleModel):
    type_: str = Field(validation_alias="type", serialization_alias="type", default="QZ", description="Schema name: QZ")
    type_qz: Literal["QZ_SIMPLE", "QZ_EQUI", "QZ_QR"] | None = Field(
        validation_alias="typeQZ", serialization_alias="typeQZ", default="QZ_SIMPLE"
    )
