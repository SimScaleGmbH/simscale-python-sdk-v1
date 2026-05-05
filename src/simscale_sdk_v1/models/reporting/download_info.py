from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DownloadInfo(SimScaleModel):
    format: str | None = Field(default=None, description="The result format.")
    uncompressed_size_in_bytes: int | None = Field(
        validation_alias="uncompressedSizeInBytes",
        serialization_alias="uncompressedSizeInBytes",
        default=None,
        description="The uncompressed size of the report result content.",
    )
    url: str | None = Field(default=None, description="URL for downloading the report result content.")
    compression: Literal["NONE", "ZIP64"] | None = Field(
        default=None, description="The compression used for the report result download archive."
    )
