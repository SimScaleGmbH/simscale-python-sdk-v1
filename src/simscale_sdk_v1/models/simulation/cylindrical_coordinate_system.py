from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class CylindricalCoordinateSystem(SimScaleModel):
    """Cylindrical — Defines positions using an Origin, a Polar direction vector (radial reference axis) and an Axial direction vector (z-axis). Positions are expressed as a radial distance (r), an angle (Φ) measured from the polar axis, and a height (z) along the axial axis. Best suited for:Rotationally symmetric or tubular geometriesRotating machinery, pipes, or circular boundariesSetups where distances from a central axis are of primary interest"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CYLINDRICAL_COORDINATE_SYSTEM",
        description="Cylindrical — Defines positions using an Origin, a Polar direction vector (radial reference axis) and an Axial direction vector (z-axis). Positions are expressed as a radial distance (r), an angle (Φ) measured from the polar axis, and a height (z) along the axial axis. Best suited for:Rotationally symmetric or tubular geometriesRotating machinery, pipes, or circular boundariesSetups where distances from a central axis are of primary interest  Schema name: CylindricalCoordinateSystem",
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    origin: DimensionalVector_Length | None = Field(default=None)
    polar: DimensionalVector_Dimensionless | None = Field(default=None)
    axial: DimensionalVector_Dimensionless | None = Field(default=None)
