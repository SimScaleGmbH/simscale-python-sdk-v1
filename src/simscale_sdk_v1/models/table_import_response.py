from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TableImportResponse(SimScaleModel):
    table_id: str = Field(
        validation_alias="tableId", serialization_alias="tableId", description="The ID of the imported table."
    )
