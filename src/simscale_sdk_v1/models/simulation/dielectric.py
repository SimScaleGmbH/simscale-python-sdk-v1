from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dielectric(SimScaleModel):
    """Dielectric materials do not conduct electric field."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DIELECTRIC",
        description="Dielectric materials do not conduct electric field.  Schema name: Dielectric",
    )
