from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.manual_timestep_calculation_type import ManualTimestepCalculationType


class CollisionRetimingEvent(SimScaleModel):
    """Select the event for the time step adaptation. Currently there are four different events possible that trigger a time step adaptation:Error: This is the case of a general error like for example non-convergence or singular matrix errors.Collision: This event is triggered if in a computation with physical contact a contact state change from open to closed is noticed. This time step adaptation is especially useful in dynamics to reduce the effect of artificial oscillations due to inexact collision detection.Field Change: The user can define the maximum delta that a field is allowed to change within one time step, if the defined threshold is exceeded the time step is adapted. This time stepping criteria is especially useful to capture material nonlinearitier more exact.Non-monotonous residual: This event is triggered if the residual has not been reduced within three iterations . This criteria is mostly used to reduce runtime by detecting diverging time steps before reaching the maximum number of allowed newton iterations."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COLLISION",
        description="Select the event for the time step adaptation. Currently there are four different events possible that trigger a time step adaptation:Error: This is the case of a general error like for example non-convergence or singular matrix errors.Collision: This event is triggered if in a computation with physical contact a contact state change from open to closed is noticed. This time step adaptation is especially useful in dynamics to reduce the effect of artificial oscillations due to inexact collision detection.Field Change: The user can define the maximum delta that a field is allowed to change within one time step, if the defined threshold is exceeded the time step is adapted. This time stepping criteria is especially useful to capture material nonlinearitier more exact.Non-monotonous residual: This event is triggered if the residual has not been reduced within three iterations . This criteria is mostly used to reduce runtime by detecting diverging time steps before reaching the maximum number of allowed newton iterations.  Schema name: CollisionRetimingEvent",
    )
    timestep_calculation_type: ManualTimestepCalculationType | None = Field(
        validation_alias="timestepCalculationType", serialization_alias="timestepCalculationType", default=None
    )
