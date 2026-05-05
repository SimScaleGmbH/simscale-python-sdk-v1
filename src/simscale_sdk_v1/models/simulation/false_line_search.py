from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FalseLineSearch(SimScaleModel):
    """Line search can be used to improve convergence for nonlinear calculations with the Newton method."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FALSE",
        description="Line search can be used to improve convergence for nonlinear calculations with the Newton method.  Schema name: FalseLineSearch",
    )
