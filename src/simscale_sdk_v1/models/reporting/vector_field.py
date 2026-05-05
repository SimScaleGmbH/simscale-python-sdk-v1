from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.data_type import DataType


class VectorField(SimScaleModel):
    field_name: str = Field(validation_alias="fieldName", serialization_alias="fieldName")
    data_type: DataType = Field(validation_alias="dataType", serialization_alias="dataType")
