from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class InternVariablesField(SimScaleModel):
    """Select the field which should have a limited de-/increase within one increment."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INTERN_VARIABLES",
        description="Select the field which should have a limited de-/increase within one increment.  Schema name: InternVariablesField",
    )
    component_selection: Literal["V1", "V2", "V3"] | None = Field(
        validation_alias="componentSelection",
        serialization_alias="componentSelection",
        default="V1",
        description="Choose a field component for which the data schould be extracted.",
    )
