from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.component_registry.file_format import FileFormat


class FileFormatGroup(SimScaleModel):
    """A group of related file formats."""

    file_formats: list[FileFormat] | None = Field(
        validation_alias="fileFormats", serialization_alias="fileFormats", default=None
    )
    multi_language_name: dict[str, str] | None = Field(
        validation_alias="multiLanguageName", serialization_alias="multiLanguageName", default=None
    )
    name: str | None = Field(default=None)
