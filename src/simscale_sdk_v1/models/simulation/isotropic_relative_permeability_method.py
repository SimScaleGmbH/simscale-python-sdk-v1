from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless


class IsotropicRelativePermeabilityMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC_RELATIVE_MAGNETIC_PERMEABILITY",
        description="Schema name: IsotropicRelativePermeabilityMethod",
    )
    relative_magnetic_permeability: DimensionalFunction_Dimensionless | None = Field(
        validation_alias="relativeMagneticPermeability",
        serialization_alias="relativeMagneticPermeability",
        default=None,
    )
