from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GlobalDampingValue(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GLOBAL_DAMPING_VALUE",
        description="Schema name: GlobalDampingValue",
    )
