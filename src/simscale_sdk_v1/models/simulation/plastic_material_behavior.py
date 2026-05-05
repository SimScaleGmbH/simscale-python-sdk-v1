from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__plastic_material_behavior_elasto_plastic_model import (
    OneOf_PlasticMaterialBehaviorElastoPlasticModel,
)


class PlasticMaterialBehavior(SimScaleModel):
    """Choose the material behavior for your problem.  Important remarks: Choose Linear elastic if the stress-strain relationship of your material is linear.Choose Elasto-plastic if the stress-strain relationship of your material is non-linear after some point e.g. yielding point.Choose Hyperelastic if your material responds elastically even at higher deformations."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PLASTIC",
        description="Choose the material behavior for your problem.  Important remarks: Choose Linear elastic if the stress-strain relationship of your material is linear.Choose Elasto-plastic if the stress-strain relationship of your material is non-linear after some point e.g. yielding point.Choose Hyperelastic if your material responds elastically even at higher deformations.   Schema name: PlasticMaterialBehavior",
    )
    elasto_plastic_model: OneOf_PlasticMaterialBehaviorElastoPlasticModel | None = Field(
        validation_alias="elastoPlasticModel", serialization_alias="elastoPlasticModel", default=None
    )
