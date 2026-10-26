from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value import Value


class ValidationRuleCase(SimScaleModel):
    """One particular case of a validation rule to be checked during validation."""

    code: str | None = Field(default=None)
    condition: Any | None = Field(
        default=None, description="Value model of a boolean value. Resolves to a JSON boolean or null node."
    )
    details: dict[str, Value] | None = Field(default=None)
    message: Any | None = Field(
        default=None, description="Value model for a string value. Resolves to a text JSON node."
    )
    multi_language_message: dict[str, Any] | None = Field(
        validation_alias="multiLanguageMessage", serialization_alias="multiLanguageMessage", default=None
    )
    severity_level: Literal["ERROR", "WARNING"] | None = Field(
        validation_alias="severityLevel",
        serialization_alias="severityLevel",
        default="",
        description="Severity levels for reporting validation results.",
    )
