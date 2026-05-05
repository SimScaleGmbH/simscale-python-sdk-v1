from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SoftMagneticMaterial(SimScaleModel):
    """A soft magnetic material can be easily magnetized and demagnetized. It can be a ferromagnetic material such as iron and non-ferromagnetic material such as copper or air."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SOFT_MAGNETIC",
        description="A soft magnetic material can be easily magnetized and demagnetized. It can be a ferromagnetic material such as iron and non-ferromagnetic material such as copper or air.  Schema name: SoftMagneticMaterial",
    )
