from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DisplacementField(SimScaleModel):
    """Select the field which should have a limited de-/increase within one increment."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISPLACEMENT",
        description="Select the field which should have a limited de-/increase within one increment.  Schema name: DisplacementField",
    )
    component_selection: Literal["X", "Y", "Z"] | None = Field(
        validation_alias="componentSelection",
        serialization_alias="componentSelection",
        default="X",
        description="Choose a field component for which the data schould be extracted.",
    )
