from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateExportRequest(SimScaleModel):
    result_id: str = Field(
        validation_alias="resultId", serialization_alias="resultId", description="The result to be exported"
    )
    format: str = Field(description="The format to export to")
