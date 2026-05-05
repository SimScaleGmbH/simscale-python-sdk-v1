from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__hyperelasticity_hyperelastic_model_marc import (
    OneOf_HyperelasticityHyperelasticModelMarc,
)


class Hyperelasticity(SimScaleModel):
    hyperelastic_model_marc: OneOf_HyperelasticityHyperelasticModelMarc | None = Field(
        validation_alias="hyperelasticModelMarc", serialization_alias="hyperelasticModelMarc", default=None
    )
