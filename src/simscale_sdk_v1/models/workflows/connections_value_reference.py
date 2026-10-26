from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ConnectionsValueReference(SimScaleModel):
    value_reference_type: str
    connections_path: str | None = Field(
        validation_alias="connectionsPath", serialization_alias="connectionsPath", default=None
    )
    value_path: str | None = Field(validation_alias="valuePath", serialization_alias="valuePath", default=None)
