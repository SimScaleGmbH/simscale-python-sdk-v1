from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.component_registry.validation_rule_case import ValidationRuleCase


class ValidationRule(SimScaleModel):
    """Validation rule defined on top of a value model.  Each rule consists of one or more cases."""

    cases: list[ValidationRuleCase] | None = Field(default=None)
    code: str | None = Field(default=None)
    description: str | None = Field(default=None)
    multi_language_description: dict[str, str] | None = Field(
        validation_alias="multiLanguageDescription", serialization_alias="multiLanguageDescription", default=None
    )
    multi_language_name: dict[str, str] | None = Field(
        validation_alias="multiLanguageName", serialization_alias="multiLanguageName", default=None
    )
    name: str | None = Field(default=None)
    value_reference: Any | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
