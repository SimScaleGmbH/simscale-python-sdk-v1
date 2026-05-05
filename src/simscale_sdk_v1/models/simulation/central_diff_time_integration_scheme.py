from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CentralDiffTimeIntegrationScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CENTRAL_DIFF",
        description="Schema name: CentralDiffTimeIntegrationScheme",
    )
