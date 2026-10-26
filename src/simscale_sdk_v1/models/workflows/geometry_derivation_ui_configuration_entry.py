from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class GeometryDerivationUiConfigurationEntry(SimScaleModel):
    configuration_entry_type: str
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    derivation: Literal["CENTER_OF_MASS"] | None = Field(
        default="", description="How a point is derived from the geometry of assigned entities."
    )
    source_value_reference: ValueReference | None = Field(
        validation_alias="sourceValueReference", serialization_alias="sourceValueReference", default=None
    )
