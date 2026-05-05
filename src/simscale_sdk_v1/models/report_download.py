from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ReportDownload(SimScaleModel):
    format: str | None = Field(
        default=None,
        description="The result format. Valid values include `OPEN_FOAM`, `ENSIGHT_GOLD`, `PVD`, `VTM`, `CSV`.",
    )
    uncompressed_size_in_bytes: int | None = Field(
        validation_alias="uncompressedSizeInBytes",
        serialization_alias="uncompressedSizeInBytes",
        default=None,
        description="The uncompressed size of the result content.",
    )
    url: str | None = Field(default=None, description="URL for downloading the result content.")
    compression: Literal["NONE", "ZIP64"] | None = Field(
        default=None, description="The compression used for the result download archive."
    )
