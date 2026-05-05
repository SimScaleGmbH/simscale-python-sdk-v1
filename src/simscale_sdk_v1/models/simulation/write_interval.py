from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WriteInterval(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WRITE_INTERVAL",
        description="Schema name: WriteInterval",
    )
    write_interval: int | None = Field(
        validation_alias="writeInterval",
        serialization_alias="writeInterval",
        default=1,
        description="Output results are saved every n time steps. Use a value larger than one to reduce the size of the output data and speed up the post-processing.",
    )
