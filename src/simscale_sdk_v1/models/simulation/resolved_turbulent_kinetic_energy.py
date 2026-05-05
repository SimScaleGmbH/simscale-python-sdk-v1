from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ResolvedTurbulentKineticEnergy(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RESOLVED_TURBULENT_KINETIC_ENERGY",
        description="Schema name: ResolvedTurbulentKineticEnergy",
    )
