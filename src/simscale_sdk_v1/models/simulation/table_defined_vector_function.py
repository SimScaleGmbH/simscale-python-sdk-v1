from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.table_function_parameter import TableFunctionParameter


class TableDefinedVectorFunction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TABLE_DEFINED",
        description="Schema name: TableDefinedVectorFunction",
    )
    label: str | None = Field(default="Table")
    table_id: str | None = Field(
        validation_alias="tableId",
        serialization_alias="tableId",
        default=None,
        description="The ID of the imported table.",
    )
    result_index: list[int] | None = Field(
        validation_alias="resultIndex",
        serialization_alias="resultIndex",
        default=None,
        description="Indicates which column(s) of the table contains the result values. One-based indexing must be used. For example, set this field to '[2]' if the second column of the table contains the dependent variable values.",
    )
    independent_variables: list[TableFunctionParameter] | None = Field(
        validation_alias="independentVariables", serialization_alias="independentVariables", default=None
    )
    separator: str | None = Field(
        default=",", description="Values in each row are separated by this character. Also known as a delimiter."
    )
    out_of_bounds: Literal["CLAMP"] | None = Field(
        validation_alias="outOfBounds", serialization_alias="outOfBounds", default="CLAMP"
    )
