from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.component_registry.parameter_description import ParameterDescription


class DataDescription(SimScaleModel):
    """Description of a single data."""

    data_provider_type: Literal["INTERNAL", "EXTERNAL"] | None = Field(
        validation_alias="dataProviderType",
        serialization_alias="dataProviderType",
        default=None,
        description="Identifies if a data is - `INTERNAL`: data is stored and managed by `data-repository` service or - `EXTERNAL`: data is stored and managed by an external service. Only a reference for it is stored in `data-repository` service.",
    )
    data_type_filter: Any | None = Field(
        validation_alias="dataTypeFilter", serialization_alias="dataTypeFilter", default=None
    )
    doc: str | None = Field(default=None)
    label: str | None = Field(default=None)
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
    multi_language_label: dict[str, str] | None = Field(
        validation_alias="multiLanguageLabel", serialization_alias="multiLanguageLabel", default=None
    )
    name: str | None = Field(default=None)
    optional: bool | None = Field(default=None)
    parameters: list[ParameterDescription] | None = Field(default=None)
    type_: str | None = Field(validation_alias="type", serialization_alias="type", default=None)
