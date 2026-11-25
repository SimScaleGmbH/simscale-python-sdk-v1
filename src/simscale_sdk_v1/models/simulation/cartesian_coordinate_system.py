from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class CartesianCoordinateSystem(SimScaleModel):
    """Cartesian — Defines positions using three mutually perpendicular axes derived from an Origin, a first direction vector e1 (local x-axis), and a second direction vector e2 (local y-axis). The third axis (z) is computed automatically as the cross product of e1 and e2. Best suited for:Rectangular or box-shaped geometriesLinear motion or straight boundariesSetups where dimensions are naturally expressed as width, height, and depth"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CARTESIAN_COORDINATE_SYSTEM",
        description="Cartesian — Defines positions using three mutually perpendicular axes derived from an Origin, a first direction vector e1 (local x-axis), and a second direction vector e2 (local y-axis). The third axis (z) is computed automatically as the cross product of e1 and e2. Best suited for:Rectangular or box-shaped geometriesLinear motion or straight boundariesSetups where dimensions are naturally expressed as width, height, and depth  Schema name: CartesianCoordinateSystem",
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    origin: DimensionalVector_Length | None = Field(default=None)
    e1: DimensionalVector_Dimensionless | None = Field(default=None)
    e2: DimensionalVector_Dimensionless | None = Field(default=None)
