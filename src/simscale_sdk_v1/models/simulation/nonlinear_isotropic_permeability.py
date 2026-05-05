from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__magnetic_flux_density import (
    DimensionalFunction_MagneticFluxDensity,
)


class NonlinearIsotropicPermeability(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NONLINEAR_ISOTROPIC",
        description="Schema name: NonlinearIsotropicPermeability",
    )
    bh_curve: DimensionalFunction_MagneticFluxDensity | None = Field(
        validation_alias="bhCurve", serialization_alias="bhCurve", default=None
    )
