from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_stress_result_control_item_stress_type import (
    OneOf_MarcStressResultControlItemStressType,
)


class MarcStressResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRESS",
        description="Schema name: MarcStressResultControlItem",
    )
    name: str | None = Field(default=None)
    stress_type: OneOf_MarcStressResultControlItemStressType | None = Field(
        validation_alias="stressType", serialization_alias="stressType", default=None
    )
    location: Literal["NODES", "ELEMENTS", "NODES_AND_ELEMENTS"] | None = Field(
        default="NODES_AND_ELEMENTS",
        description="Choose where stress and strain results are computed and stored.Nodes: Values are extrapolated from the integration points to the mesh nodes.Elements: Values are averaged from the integration points to give a single, representative value per element.Nodes and Elements: Both representations are computed and stored.",
    )
