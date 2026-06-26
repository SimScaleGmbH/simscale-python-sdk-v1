from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FileFormat(SimScaleModel):
    """High-level description of a file format which makes it suitable for dealing with files on user interfaces."""

    file_extensions: list[str] | None = Field(
        validation_alias="fileExtensions", serialization_alias="fileExtensions", default=None
    )
    mime_type: str | None = Field(validation_alias="mimeType", serialization_alias="mimeType", default=None)
    multi_language_name: dict[str, str] | None = Field(
        validation_alias="multiLanguageName", serialization_alias="multiLanguageName", default=None
    )
    name: str | None = Field(default=None)
