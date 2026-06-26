from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DimensionalProfileObjectDimension(SimScaleModel):
    """Encapsulates a default unit, additional units, and an optional default value for a dimensional quantity."""

    additional_units: list[str] | None = Field(
        validation_alias="additionalUnits", serialization_alias="additionalUnits", default=None
    )
    default_unit: str | None = Field(validation_alias="defaultUnit", serialization_alias="defaultUnit", default=None)
    default_value: dict[str, Any] | None = Field(
        validation_alias="defaultValue", serialization_alias="defaultValue", default=None
    )
