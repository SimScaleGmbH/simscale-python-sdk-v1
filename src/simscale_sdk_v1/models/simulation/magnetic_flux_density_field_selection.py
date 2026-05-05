from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MagneticFluxDensityFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MAGNETIC_FLUX_DENSITY",
        description="Schema name: MagneticFluxDensityFieldSelection",
    )
    component_selection: Literal["X", "Y", "Z", "MAG", "ALL"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="ALL"
    )
