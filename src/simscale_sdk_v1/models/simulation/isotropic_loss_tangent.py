from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless


class IsotropicLossTangent(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC_LOSS_TANGENT",
        description="Schema name: IsotropicLossTangent",
    )
    dielectric_loss_tangent: DimensionalFunction_Dimensionless | None = Field(
        validation_alias="dielectricLossTangent", serialization_alias="dielectricLossTangent", default=None
    )
