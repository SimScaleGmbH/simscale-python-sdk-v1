from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DataValueReference(SimScaleModel):
    value_reference_type: str
    data_name: str | None = Field(validation_alias="dataName", serialization_alias="dataName", default=None)
    value_path: str | None = Field(validation_alias="valuePath", serialization_alias="valuePath", default=None)
