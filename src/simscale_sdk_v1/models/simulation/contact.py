from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__contact_connections import OneOf_ContactConnections


class Contact(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="CONTACT", description="Schema name: Contact"
    )
    node_merging_bonded: bool | None = Field(
        validation_alias="nodeMergingBonded",
        serialization_alias="nodeMergingBonded",
        default=False,
        description="Allow node merging for bonded contacts where possible to increase contact accuracy and solution efficiency. For contact pairs where nodes cannot be merged, linear relations will be used with the defined position tolerance.",
    )
    connections: list[OneOf_ContactConnections] | None = Field(default=None)
