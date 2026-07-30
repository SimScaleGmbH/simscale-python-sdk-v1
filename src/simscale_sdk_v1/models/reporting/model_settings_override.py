from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField


class ModelSettingsOverride(SimScaleModel):
    """Partial model settings applied as an override on top of the state's own model settings. All properties are optional; only those provided are overridden."""

    scalar_field: ScalarField | None = Field(
        validation_alias="scalarField", serialization_alias="scalarField", default=None
    )
