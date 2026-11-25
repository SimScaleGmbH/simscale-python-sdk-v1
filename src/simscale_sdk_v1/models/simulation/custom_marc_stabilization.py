from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CustomMarcStabilization(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM",
        description="Schema name: CustomMarcStabilization",
    )
    energy_dissipation_ratio: float | None = Field(
        validation_alias="energyDissipationRatio",
        serialization_alias="energyDissipationRatio",
        default=0.0002,
        description="Target ratio of the energy dissipated by the damping to the strain energy of a load step (damping ratio of the artificial damping in Marc). The solver estimates both in the first increment and scales the damping to match. Larger values stabilize more, but also change the result more.",
    )
