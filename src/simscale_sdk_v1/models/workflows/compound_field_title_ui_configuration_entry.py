from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class CompoundFieldTitleUiConfigurationEntry(SimScaleModel):
    configuration_entry_type: str
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    title_type: Any | None = Field(
        validation_alias="titleType",
        serialization_alias="titleType",
        default=None,
        description="Value model for an enum value. Resolves to a text JSON node.",
    )
