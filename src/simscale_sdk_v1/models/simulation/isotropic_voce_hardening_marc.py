from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class IsotropicVoceHardeningMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Schema name: IsotropicVoceHardeningMarc",
    )
    asymptotic_hardening_limit: Dimensional_Pressure | None = Field(
        validation_alias="asymptoticHardeningLimit", serialization_alias="asymptoticHardeningLimit", default=None
    )
    isotropic_saturation_rate: float | None = Field(
        validation_alias="isotropicSaturationRate",
        serialization_alias="isotropicSaturationRate",
        default=0.0,
        description="Controls how quickly the isotropic hardening approaches its asymptotic limit as plastic strain accumulates; higher values saturate faster.",
    )
