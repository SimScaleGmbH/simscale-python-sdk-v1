from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__plasticity_marc_plasticity_model import (
    OneOf_PlasticityMarcPlasticityModel,
)


class PlasticityMarc(SimScaleModel):
    plasticity_model: OneOf_PlasticityMarcPlasticityModel | None = Field(
        validation_alias="plasticityModel", serialization_alias="plasticityModel", default=None
    )
