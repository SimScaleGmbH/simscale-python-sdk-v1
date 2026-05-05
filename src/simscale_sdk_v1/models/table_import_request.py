from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.table_import_request_location import TableImportRequestLocation


class TableImportRequest(SimScaleModel):
    location: TableImportRequestLocation
