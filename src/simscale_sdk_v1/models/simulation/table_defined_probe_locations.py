from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TableDefinedProbeLocations(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TABULAR",
        description="Schema name: TableDefinedProbeLocations",
    )
    table_id: str | None = Field(
        validation_alias="tableId",
        serialization_alias="tableId",
        default=None,
        description="The ID of the imported table.",
    )
