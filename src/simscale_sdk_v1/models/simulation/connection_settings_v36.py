from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_contact_non_linearity_resolution import (
    OneOf_ConnectionSettingsV36ContactNonLinearityResolution,
)
from simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_friction import (
    OneOf_ConnectionSettingsV36Friction,
)
from simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_nonlinearity_resolution import (
    OneOf_ConnectionSettingsV36NonlinearityResolution,
)


class ConnectionSettingsV36(SimScaleModel):
    nonlinearity_resolution: OneOf_ConnectionSettingsV36NonlinearityResolution | None = Field(
        validation_alias="nonlinearityResolution", serialization_alias="nonlinearityResolution", default=None
    )
    friction: OneOf_ConnectionSettingsV36Friction | None = Field(default=None)
    contact_non_linearity_resolution: OneOf_ConnectionSettingsV36ContactNonLinearityResolution | None = Field(
        validation_alias="contactNonLinearityResolution",
        serialization_alias="contactNonLinearityResolution",
        default=None,
    )
    convergence_stabilization: bool | None = Field(
        validation_alias="convergenceStabilization", serialization_alias="convergenceStabilization", default=True
    )
    contact_smoothing: bool | None = Field(
        validation_alias="contactSmoothing", serialization_alias="contactSmoothing", default=False
    )
