from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class VisibilityUiConfigurationEntry(SimScaleModel):
    configuration_entry_type: str
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    visible_when: Any | None = Field(
        validation_alias="visibleWhen",
        serialization_alias="visibleWhen",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
