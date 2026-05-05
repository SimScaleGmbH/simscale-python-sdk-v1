from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StrainEnergyConvergenceMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRAIN_ENERGY",
        description="Schema name: StrainEnergyConvergenceMethod",
    )
    strain_energy_tolerance: float | None = Field(
        validation_alias="strainEnergyTolerance",
        serialization_alias="strainEnergyTolerance",
        default=0.1,
        description="The ratio of the incremental strain energy to the total strain energy. Because energy is a scalar, this criterion is often smoother and less sensitive to local numerical noise than force or displacement checks.",
    )
