from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__magnetic_flux_density import Dimensional_MagneticFluxDensity
from simscale_sdk_v1.models.simulation.one_of__permanent_magnet_material_magnetization_direction_type import (
    OneOf_PermanentMagnetMaterialMagnetizationDirectionType,
)


class PermanentMagnetMaterial(SimScaleModel):
    """A permanent magnet retains a significant portion of its magnetization indefinitely, even without an external magnetic field."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PERMANENT_MAGNET",
        description="A permanent magnet retains a significant portion of its magnetization indefinitely, even without an external magnetic field.  Schema name: PermanentMagnetMaterial",
    )
    remanence: Dimensional_MagneticFluxDensity | None = Field(default=None)
    magnetization_direction_type: OneOf_PermanentMagnetMaterialMagnetizationDirectionType | None = Field(
        validation_alias="magnetizationDirectionType", serialization_alias="magnetizationDirectionType", default=None
    )
