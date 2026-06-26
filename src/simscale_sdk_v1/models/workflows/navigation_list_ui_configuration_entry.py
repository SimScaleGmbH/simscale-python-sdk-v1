from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class NavigationListUiConfigurationEntry(SimScaleModel):
    configuration_entry_type: str
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    icon: Any | None = Field(default=None, description="Value model for a string value. Resolves to a text JSON node.")
    initially_open: Any | None = Field(
        validation_alias="initiallyOpen",
        serialization_alias="initiallyOpen",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
    show_item_count_if_collapsed: Any | None = Field(
        validation_alias="showItemCountIfCollapsed",
        serialization_alias="showItemCountIfCollapsed",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
