from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__kinematic_chaboche_hardening_marc_backstress_terms import (
    OneOf_KinematicChabocheHardeningMarcBackstressTerms,
)


class KinematicChabocheHardeningMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="KINEMATIC",
        description="Schema name: KinematicChabocheHardeningMarc",
    )
    backstress_terms: OneOf_KinematicChabocheHardeningMarcBackstressTerms | None = Field(
        validation_alias="backstressTerms", serialization_alias="backstressTerms", default=None
    )
