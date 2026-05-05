from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CadImportRequestLocation(SimScaleModel):
    storage_id: str = Field(
        validation_alias="storageId",
        serialization_alias="storageId",
        description="The storage ID of the temporary storage location where the CAD file has been uploaded.",
    )
