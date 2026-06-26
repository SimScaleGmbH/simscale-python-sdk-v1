from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflow_runner.resource_usage import ResourceUsage


class ResourceUsageSummary(SimScaleModel):
    """Resource usage split into total, chargeable, and non-chargeable parts."""

    chargeable: ResourceUsage | None = Field(default=None)
    non_chargeable: ResourceUsage | None = Field(
        validation_alias="nonChargeable", serialization_alias="nonChargeable", default=None
    )
    total: ResourceUsage | None = Field(default=None)
