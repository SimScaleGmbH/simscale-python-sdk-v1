from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.connection_settings_v36 import ConnectionSettingsV36
from simscale_sdk_v1.models.simulation.one_of__physical_contact_connections import OneOf_PhysicalContactConnections


class PhysicalContact(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PHYSICAL_CONTACT_V36",
        description="Schema name: PhysicalContact",
    )
    settings: ConnectionSettingsV36 | None = Field(default=None)
    connections: list[OneOf_PhysicalContactConnections] | None = Field(default=None)
