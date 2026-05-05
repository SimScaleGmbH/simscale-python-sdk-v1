from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NewmarkTimeIntegrationScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NEWMARK",
        description="Schema name: NewmarkTimeIntegrationScheme",
    )
    beta: float | None = Field(
        default=0.25,
        description="The choice of the values for the parameters &alpha; and &beta; influences the stability, accuracy and numerical damping of the Newmark Sheme.",
    )
    gamma: float | None = Field(
        default=0.5,
        description="The choice of the values for the parameters &alpha; and &beta; influences the stability, accuracy and numerical damping of the Newmark Sheme.",
    )
