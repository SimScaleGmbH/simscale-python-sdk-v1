from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__linear_elastic_marc_material_behavior_poissons_ratio import (
    OneOf_LinearElasticMarcMaterialBehaviorPoissonsRatio,
)


class LinearElasticMarcMaterialBehavior(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LINEAR_ELASTIC_MARC",
        description="Schema name: LinearElasticMarcMaterialBehavior",
    )
    youngs_modulus: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulus", serialization_alias="youngsModulus", default=None
    )
    poissons_ratio: OneOf_LinearElasticMarcMaterialBehaviorPoissonsRatio | None = Field(
        validation_alias="poissonsRatio", serialization_alias="poissonsRatio", default=None
    )
