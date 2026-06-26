from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.boolean_value import BooleanValue
from simscale_sdk_v1.models.workflows.string_value import StringValue


class ValidationRuleCase(SimScaleModel):
    """One particular case of a validation rule to be checked during validation."""

    code: str | None = Field(default=None)
    condition: BooleanValue | None = Field(default=None)
    details: dict[str, Any] | None = Field(default=None)
    message: StringValue | None = Field(default=None)
    multi_language_message: dict[str, StringValue] | None = Field(
        validation_alias="multiLanguageMessage", serialization_alias="multiLanguageMessage", default=None
    )
    severity_level: Literal["ERROR", "WARNING"] | None = Field(
        validation_alias="severityLevel",
        serialization_alias="severityLevel",
        default=None,
        description="Severity levels for reporting validation results.",
    )
