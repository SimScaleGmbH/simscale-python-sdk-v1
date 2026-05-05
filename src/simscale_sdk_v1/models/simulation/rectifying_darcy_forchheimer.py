from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class RectifyingDarcyForchheimer(SimScaleModel):
    """Directional porous object where the permeability and friction form coefficient are applied only in the specified direction. For directions orthogonal to the specified direction, the permeability is set to zero, i.e. there is no flow in the orthogonal directions."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RECTIFYING",
        description="Directional porous object where the permeability and friction form coefficient are applied only in the specified direction. For directions orthogonal to the specified direction, the permeability is set to zero, i.e. there is no flow in the orthogonal directions.  Schema name: RectifyingDarcyForchheimer",
    )
    direction: DimensionalVector_Length | None = Field(default=None)
