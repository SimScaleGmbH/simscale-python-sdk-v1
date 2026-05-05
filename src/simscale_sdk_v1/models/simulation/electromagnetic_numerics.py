from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ElectromagneticNumerics(SimScaleModel):
    nonlinear_residual: float | None = Field(
        validation_alias="nonlinearResidual",
        serialization_alias="nonlinearResidual",
        default=1e-06,
        description="The nonlinear residual error is computed as the difference between the calculated and expected flux density value when a BH curve is specified.",
    )
    element_accuracy: Literal["FIRST_ORDER", "SECOND_ORDER"] | None = Field(
        validation_alias="elementAccuracy",
        serialization_alias="elementAccuracy",
        default="FIRST_ORDER",
        description="Uses second order element shape functions for a higher accuracy. Especially recommended when calculating torques or forces. However this increases memory consumption and computational time.",
    )
