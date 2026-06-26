from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class NavigationUiConfigurationEntry(SimScaleModel):
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
    multi_language_new_element_name: dict[str, Any] | None = Field(
        validation_alias="multiLanguageNewElementName", serialization_alias="multiLanguageNewElementName", default=None
    )
    name_field: Any | None = Field(
        validation_alias="nameField",
        serialization_alias="nameField",
        default=None,
        description="Value model for a string value. Resolves to a text JSON node.",
    )
    new_element_name: Any | None = Field(
        validation_alias="newElementName",
        serialization_alias="newElementName",
        default=None,
        description="Value model for a string value. Resolves to a text JSON node.",
    )
