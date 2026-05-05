from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CauchyStressTensorField(SimScaleModel):
    """Select the field which should have a limited de-/increase within one increment."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CAUCHY_STRESS_TENSOR",
        description="Select the field which should have a limited de-/increase within one increment.  Schema name: CauchyStressTensorField",
    )
    component_selection: Literal["XX", "YY", "ZZ", "XY", "XZ", "YZ"] | None = Field(
        validation_alias="componentSelection",
        serialization_alias="componentSelection",
        default="XX",
        description="Choose a field component for which the data schould be extracted.",
    )
