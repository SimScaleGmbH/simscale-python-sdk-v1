from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__friction_augmentation import Dimensional_FrictionAugmentation


class FrictionAugmentedLagrangeCoef(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FRICTION_AUGMENTATION_COEF",
        description="Schema name: FrictionAugmentedLagrangeCoef",
    )
    friction_augmentation_coefficient: Dimensional_FrictionAugmentation | None = Field(
        validation_alias="frictionAugmentationCoefficient",
        serialization_alias="frictionAugmentationCoefficient",
        default=None,
    )
    coulomb_coefficient: float | None = Field(
        validation_alias="coulombCoefficient", serialization_alias="coulombCoefficient", default=0.1
    )
