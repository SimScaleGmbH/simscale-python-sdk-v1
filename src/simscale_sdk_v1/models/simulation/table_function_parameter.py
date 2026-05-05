from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TableFunctionParameter(SimScaleModel):
    reference: int = Field(
        description="Indicates which column of the table contains the values of this independent variable. One-based indexing must be used. For example, set this property to '1' if the first column of the table contains the values of this independent variable."
    )
    parameter: str | None = Field(
        default=None,
        description="The name of the independent variable. Possible values: 'X', 'Y', 'Z', 'HEIGHT', 'Temperature', 'T' (time), 'Q' (mass flow rate), 'V_DOT' (volumetric flow rate), 'F' (frequency), 'E' (strain)",
    )
    unit: str
