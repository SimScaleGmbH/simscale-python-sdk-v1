from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__molar_mass import Dimensional_MolarMass


class SpecieDefault(SimScaleModel):
    """Specie: defines the molecular composition of the fluid material. Currently a single specie is available."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIE",
        description="Specie: defines the molecular composition of the fluid material. Currently a single specie is available.  Schema name: SpecieDefault",
    )
    molar_weight: Dimensional_MolarMass | None = Field(
        validation_alias="molarWeight", serialization_alias="molarWeight", default=None
    )
