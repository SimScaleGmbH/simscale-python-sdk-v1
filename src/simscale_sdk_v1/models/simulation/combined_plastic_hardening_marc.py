from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CombinedPlasticHardeningMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COMBINED",
        description="Schema name: CombinedPlasticHardeningMarc",
    )
    kinematic_fraction: float | None = Field(
        validation_alias="kinematicFraction",
        serialization_alias="kinematicFraction",
        default=0.5,
        description="This value (from 0 to 1) defines the weight of the kinematic component relative to the isotropic component for the combined hardening rule. A value of 1 represents pure kinematic hardening, while 0 represents pure isotropic hardening.",
    )
