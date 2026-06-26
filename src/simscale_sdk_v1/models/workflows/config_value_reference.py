from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ConfigValueReference(SimScaleModel):
    value_reference_type: str
    value_path: str | None = Field(validation_alias="valuePath", serialization_alias="valuePath", default=None)
