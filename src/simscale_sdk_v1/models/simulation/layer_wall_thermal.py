from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.conductivity_thickness_pair import ConductivityThicknessPair


class LayerWallThermal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONTACT_INTERFACE_MATERIAL",
        description="Schema name: LayerWallThermal",
    )
    conductivity_thickness_pairs: list[ConductivityThicknessPair] | None = Field(
        validation_alias="conductivityThicknessPairs", serialization_alias="conductivityThicknessPairs", default=None
    )
