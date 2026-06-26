from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ParameterDescription(SimScaleModel):
    """Description of a single parameter for parametric data."""

    data_type: str | None = Field(validation_alias="dataType", serialization_alias="dataType", default=None)
    doc: str | None = Field(default=None)
    label: str | None = Field(default=None)
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
    multi_language_label: dict[str, str] | None = Field(
        validation_alias="multiLanguageLabel", serialization_alias="multiLanguageLabel", default=None
    )
    name: str | None = Field(default=None)
