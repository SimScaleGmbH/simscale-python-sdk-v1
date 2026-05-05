from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class IsotropicDarcyForchheimer(SimScaleModel):
    """Isotropic porous object where the same permeability and friction form coefficient are applied in all directions."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Isotropic porous object where the same permeability and friction form coefficient are applied in all directions.  Schema name: IsotropicDarcyForchheimer",
    )
