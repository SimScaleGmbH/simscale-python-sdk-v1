from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value import Value


class DerivedMaterialValue(SimScaleModel):
    """A value derived while materializing a material slot, written at a path within the effective material."""

    path: str | None = Field(default=None)
    value: Value | None = Field(default=None)
