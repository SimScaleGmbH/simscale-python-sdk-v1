from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FixedAugmentation(SimScaleModel):
    newton_iteration_threshold: int | None = Field(
        validation_alias="newtonIterationThreshold",
        serialization_alias="newtonIterationThreshold",
        default=5,
        description="Newton Iteration threshold defines the threshold below which the actual number of Newton Iterations has to fall in order to increase the time step by the percentage given by Timestep Augmentation.",
    )
    timestep_augmentation: float | None = Field(
        validation_alias="timestepAugmentation",
        serialization_alias="timestepAugmentation",
        default=100,
        description="Newton Iteration threshold defines the threshold below which the actual number of Newton Iterations has to fall in order to increase the time step by the percentage given by Timestep Augmentation.",
    )
