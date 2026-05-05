from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TimeTransientMagnetics(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TIME_TRANSIENT_MAGNETICS",
        description="Schema name: TimeTransientMagnetics",
    )
    thermal: bool | None = Field(
        default=False,
        description="Coupling with thermal solves for the temperature by considering electromagnetic losses such as Ohmic, hysteric or displacement losses.",
    )
