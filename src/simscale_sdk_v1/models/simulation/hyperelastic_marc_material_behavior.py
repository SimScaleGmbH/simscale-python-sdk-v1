from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.hyperelasticity import Hyperelasticity


class HyperelasticMarcMaterialBehavior(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HYPERELASTIC_MARC",
        description="Schema name: HyperelasticMarcMaterialBehavior",
    )
    hyperelasticity: Hyperelasticity | None = Field(default=None)
