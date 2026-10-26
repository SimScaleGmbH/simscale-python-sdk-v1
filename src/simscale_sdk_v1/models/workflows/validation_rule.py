from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.list_element_scope import ListElementScope
from simscale_sdk_v1.models.workflows.validation_rule_case import ValidationRuleCase
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class ValidationRule(SimScaleModel):
    """Validation rule defined on top of a value model.  Each rule consists of one or more cases."""

    cases: list[ValidationRuleCase] | None = Field(default=None)
    code: str | None = Field(default=None)
    description: str | None = Field(default=None)
    element_scope: ListElementScope | None = Field(
        validation_alias="elementScope", serialization_alias="elementScope", default=None
    )
    multi_language_description: dict[str, str] | None = Field(
        validation_alias="multiLanguageDescription", serialization_alias="multiLanguageDescription", default=None
    )
    multi_language_name: dict[str, str] | None = Field(
        validation_alias="multiLanguageName", serialization_alias="multiLanguageName", default=None
    )
    name: str | None = Field(default=None)
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
