from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.table_row import TableRow


class TableData(SimScaleModel):
    """Table data"""

    column_labels: list[str] = Field(
        validation_alias="columnLabels", serialization_alias="columnLabels", description="List of the table's columns"
    )
    rows: list[TableRow] = Field(description="Array of table rows.")
