from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TableRow(SimScaleModel):
    elements: list[str] = Field(
        description="Values of the current row. These values are in the order specified by the `columnLabels` field."
    )
