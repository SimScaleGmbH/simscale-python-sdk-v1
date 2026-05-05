from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AugmentedLagrangeMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUGMENTED_LAGRANGE",
        description="Schema name: AugmentedLagrangeMethod",
    )
    augmented_lagrange_coefficient: float | None = Field(
        validation_alias="augmentedLagrangeCoefficient", serialization_alias="augmentedLagrangeCoefficient", default=100
    )
