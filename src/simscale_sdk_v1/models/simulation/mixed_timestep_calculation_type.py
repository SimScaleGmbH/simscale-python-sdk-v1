from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.adaptive_augmentation import AdaptiveAugmentation
from simscale_sdk_v1.models.simulation.fixed_subdivision import FixedSubdivision


class MixedTimestepCalculationType(SimScaleModel):
    """Select how the time increments should be computed in case of an adaptation event. Currently four types are available (which may not all be available for every event):Manual: Here the user defines fixed time step subdivision and augmentation settings.Newton Iterations Target: With this setting the user defines a target value for the Newton Iterations and the time increments are calculated automatically to having this value as objective.Field Change Target: With this setting the user defines a target value for change of a specific field component within a time increment and the time increments are calculated automatically to having this value as objective.Mixed: The mixed type uses a fixed subdivision and an automatic adaptation of the time step with a target value for the change of the selected field component."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MIXED",
        description="Select how the time increments should be computed in case of an adaptation event. Currently four types are available (which may not all be available for every event):Manual: Here the user defines fixed time step subdivision and augmentation settings.Newton Iterations Target: With this setting the user defines a target value for the Newton Iterations and the time increments are calculated automatically to having this value as objective.Field Change Target: With this setting the user defines a target value for change of a specific field component within a time increment and the time increments are calculated automatically to having this value as objective.Mixed: The mixed type uses a fixed subdivision and an automatic adaptation of the time step with a target value for the change of the selected field component.  Schema name: MixedTimestepCalculationType",
    )
    fixed_subdivision: FixedSubdivision | None = Field(
        validation_alias="fixedSubdivision", serialization_alias="fixedSubdivision", default=None
    )
    adaptive_augmentation: AdaptiveAugmentation | None = Field(
        validation_alias="adaptiveAugmentation", serialization_alias="adaptiveAugmentation", default=None
    )
