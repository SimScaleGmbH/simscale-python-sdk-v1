from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ManualStateMetadata(SimScaleModel):
    state_type: str = Field(validation_alias="stateType", serialization_alias="stateType", default="MANUAL")
    state_uuid: str = Field(
        validation_alias="stateUuid",
        serialization_alias="stateUuid",
        description="The UUID of the specific state (Mandatory for AUTOMATIC/MANUAL).",
    )
