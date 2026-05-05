from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.element_technology import ElementTechnology


class SolidElementTechnology(SimScaleModel):
    element_technology3_d: ElementTechnology | None = Field(
        validation_alias="elementTechnology3D", serialization_alias="elementTechnology3D", default=None
    )
