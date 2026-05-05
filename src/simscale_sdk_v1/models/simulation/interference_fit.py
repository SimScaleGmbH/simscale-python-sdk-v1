from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__length import DimensionalFunction_Length


class InterferenceFit(SimScaleModel):
    enable_interference_fit: bool | None = Field(
        validation_alias="enableInterferenceFit",
        serialization_alias="enableInterferenceFit",
        default=False,
        description="Enable Interference fit to resolve the initial penetration as a physical load (press-fit) rather than a geometric inaccuracy.Interference Closure Value: Specifies how much of the initial overlap should be &quot;removed&quot;. If left at default, the solver resolves the full overlap in the first time step to calculate the resulting stresses. Ramp the value from an initially negative (overlap) value gradually to zero to resolve nonlinearities robustly during the interference fit phase.",
    )
    closure: DimensionalFunction_Length | None = Field(default=None)
