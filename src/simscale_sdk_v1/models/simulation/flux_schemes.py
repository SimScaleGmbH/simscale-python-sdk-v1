from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__flux_schemes_for_default import OneOf_FluxSchemesForDefault


class FluxSchemes(SimScaleModel):
    for_default: OneOf_FluxSchemesForDefault | None = Field(
        validation_alias="forDefault", serialization_alias="forDefault", default=None
    )
