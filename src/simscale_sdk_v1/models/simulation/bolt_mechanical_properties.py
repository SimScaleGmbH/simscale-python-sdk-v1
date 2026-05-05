from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class BoltMechanicalProperties(SimScaleModel):
    youngs_modulus: Dimensional_Pressure | None = Field(
        validation_alias="youngsModulus", serialization_alias="youngsModulus", default=None
    )
    poissons_ratio: float | None = Field(
        validation_alias="poissonsRatio",
        serialization_alias="poissonsRatio",
        default=0.28,
        description="Provide the Poisson's ratio value which describes the compression or elongation of the bolt material transverse to axial strain. Poisson's ratio can have a value within range from -1 to 0.5.",
    )
    density: Dimensional_Density | None = Field(default=None)
