from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DefaultStateMetadata(SimScaleModel):
    state_type: str = Field(validation_alias="stateType", serialization_alias="stateType", default="DEFAULT")
    state_analysis_type: str = Field(
        validation_alias="stateAnalysisType",
        serialization_alias="stateAnalysisType",
        description="The analysis type (Mandatory for a DEFAULT state).",
    )
