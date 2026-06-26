from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.component_registry.file_format_group import FileFormatGroup


class DataTypeFileOperationsDescription(SimScaleModel):
    """Data type description in association to file operations"""

    downloadable: bool | None = Field(default=None)
    file_format_groups: list[FileFormatGroup] | None = Field(
        validation_alias="fileFormatGroups", serialization_alias="fileFormatGroups", default=None
    )
    uploadable: bool | None = Field(default=None)
