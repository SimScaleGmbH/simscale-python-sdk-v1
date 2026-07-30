from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.filters_override import FiltersOverride
from simscale_sdk_v1.models.reporting.model_settings_override import ModelSettingsOverride


class StateOverrides(SimScaleModel):
    """Render-time overrides applied on top of the fetched post-processor state, mirroring the report's own model/filter structure so each override is unambiguous. Additive - further sections (filters, ...) can be added over time without changing the report-from-state contract."""

    model_settings: ModelSettingsOverride | None = Field(
        validation_alias="modelSettings", serialization_alias="modelSettings", default=None
    )
    filters: FiltersOverride | None = Field(default=None)
