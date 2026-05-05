from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__elasticity_marc_poissons_ratio import OneOf_ElasticityMarcPoissonsRatio


class ElasticityMarc(SimScaleModel):
    youngs_modulus: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulus", serialization_alias="youngsModulus", default=None
    )
    poissons_ratio: OneOf_ElasticityMarcPoissonsRatio | None = Field(
        validation_alias="poissonsRatio", serialization_alias="poissonsRatio", default=None
    )
