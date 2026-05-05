from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__hyper_elastic_material_behavior_hyper_elastic_model import (
    OneOf_HyperElasticMaterialBehaviorHyperElasticModel,
)


class HyperElasticMaterialBehavior(SimScaleModel):
    """Choose the material behavior for your problem.  Important remarks: Choose Linear elastic if the stress-strain relationship of your material is linear.Choose Elasto-plastic if the stress-strain relationship of your material is non-linear after some point e.g. yielding point.Choose Hyperelastic if your material responds elastically even at higher deformations."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HYPER_ELASTIC",
        description="Choose the material behavior for your problem.  Important remarks: Choose Linear elastic if the stress-strain relationship of your material is linear.Choose Elasto-plastic if the stress-strain relationship of your material is non-linear after some point e.g. yielding point.Choose Hyperelastic if your material responds elastically even at higher deformations.   Schema name: HyperElasticMaterialBehavior",
    )
    hyper_elastic_model: OneOf_HyperElasticMaterialBehaviorHyperElasticModel | None = Field(
        validation_alias="hyperElasticModel", serialization_alias="hyperElasticModel", default=None
    )
