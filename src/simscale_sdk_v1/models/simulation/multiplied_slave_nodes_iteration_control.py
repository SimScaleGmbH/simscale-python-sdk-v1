from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MultipliedSlaveNodesIterationControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MULTIPLIED_SLAVE_NODE",
        description="Schema name: MultipliedSlaveNodesIterationControl",
    )
    multiple_value: int | None = Field(validation_alias="multipleValue", serialization_alias="multipleValue", default=4)
