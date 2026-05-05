from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_creep_formulation import (
    OneOf_LinearElasticMaterialBehaviorCreepFormulation,
)
from simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_damping import (
    OneOf_LinearElasticMaterialBehaviorDamping,
)
from simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_directional_dependency import (
    OneOf_LinearElasticMaterialBehaviorDirectionalDependency,
)


class LinearElasticMaterialBehavior(SimScaleModel):
    """Choose the material behavior for your problem.  Important remarks: Choose Linear elastic if the stress-strain relationship of your material is linear.Choose Elasto-plastic if the stress-strain relationship of your material is non-linear after some point e.g. yielding point.Choose Hyperelastic if your material responds elastically even at higher deformations."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LINEAR_ELASTIC",
        description="Choose the material behavior for your problem.  Important remarks: Choose Linear elastic if the stress-strain relationship of your material is linear.Choose Elasto-plastic if the stress-strain relationship of your material is non-linear after some point e.g. yielding point.Choose Hyperelastic if your material responds elastically even at higher deformations.   Schema name: LinearElasticMaterialBehavior",
    )
    directional_dependency: OneOf_LinearElasticMaterialBehaviorDirectionalDependency | None = Field(
        validation_alias="directionalDependency", serialization_alias="directionalDependency", default=None
    )
    damping: OneOf_LinearElasticMaterialBehaviorDamping | None = Field(default=None)
    creep_formulation: OneOf_LinearElasticMaterialBehaviorCreepFormulation | None = Field(
        validation_alias="creepFormulation", serialization_alias="creepFormulation", default=None
    )
