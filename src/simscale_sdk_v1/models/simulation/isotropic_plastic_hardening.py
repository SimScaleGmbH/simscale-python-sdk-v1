from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__isotropic_plastic_hardening_poissons_ratio import (
    OneOf_IsotropicPlasticHardeningPoissonsRatio,
)


class IsotropicPlasticHardening(SimScaleModel):
    """Define the plastic hardening type of the material."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Define the plastic hardening type of the material.  Schema name: IsotropicPlasticHardening",
    )
    youngs_modulus: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulus", serialization_alias="youngsModulus", default=None
    )
    poissons_ratio: OneOf_IsotropicPlasticHardeningPoissonsRatio | None = Field(
        validation_alias="poissonsRatio", serialization_alias="poissonsRatio", default=None
    )
    von_mises_stress: DimensionalFunction_Pressure | None = Field(
        validation_alias="vonMisesStress", serialization_alias="vonMisesStress", default=None
    )
