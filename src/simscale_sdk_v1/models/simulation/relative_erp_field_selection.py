from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__power import Dimensional_Power


class RelativeERPFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE_ERP",
        description="Schema name: RelativeERPFieldSelection",
    )
    reference_erp_value: Dimensional_Power | None = Field(
        validation_alias="referenceERPValue", serialization_alias="referenceERPValue", default=None
    )
