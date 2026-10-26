from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DocumentationPage(SimScaleModel):
    content: str | None = Field(default=None)
    id: str | None = Field(default=None)
    multi_language_content: dict[str, str] | None = Field(
        validation_alias="multiLanguageContent", serialization_alias="multiLanguageContent", default=None
    )
    multi_language_title: dict[str, str] | None = Field(
        validation_alias="multiLanguageTitle", serialization_alias="multiLanguageTitle", default=None
    )
    title: str | None = Field(default=None)
