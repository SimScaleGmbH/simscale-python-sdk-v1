from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.table_data import TableData


class Table(SimScaleModel):
    id: str
    data: TableData
