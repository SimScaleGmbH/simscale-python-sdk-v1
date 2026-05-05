from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NewtonNonLinearityResolution(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NEWTON",
        description="Schema name: NewtonNonLinearityResolution",
    )
    iteration_criterion: float | None = Field(
        validation_alias="iterationCriterion", serialization_alias="iterationCriterion", default=1e-05
    )
