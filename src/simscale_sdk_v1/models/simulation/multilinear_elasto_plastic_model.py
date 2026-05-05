from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.isotropic_plastic_hardening import IsotropicPlasticHardening


class MultilinearElastoPlasticModel(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MULTILINEAR",
        description="Schema name: MultilinearElastoPlasticModel",
    )
    plastic_hardening: IsotropicPlasticHardening | None = Field(
        validation_alias="plasticHardening", serialization_alias="plasticHardening", default=None
    )
