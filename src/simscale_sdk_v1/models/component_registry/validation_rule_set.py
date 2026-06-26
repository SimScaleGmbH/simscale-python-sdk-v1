from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.component_registry.validation_rule import ValidationRule


class ValidationRuleSet(SimScaleModel):
    """Set of validation rules.  It can be associated to for example a workflow type configuration schema or a method configuration schema."""

    rules: list[ValidationRule] | None = Field(default=None)
