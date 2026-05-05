from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TchamwaTimeIntegrationScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TCHAMWA",
        description="Schema name: TchamwaTimeIntegrationScheme",
    )
    phi: float | None = Field(
        default=1.05,
        description="The parameter &phi; allows inducing numerical damping. For &phi; = 1.0 there is no numerical damping whereas for &phi; > 1.0 the damping grows with the parameter value. It is thus not recommended to use a value for &phi; greater than 1.1.",
    )
