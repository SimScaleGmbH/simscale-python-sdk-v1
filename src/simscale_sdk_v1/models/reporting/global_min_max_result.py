from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.data_type import DataType
from simscale_sdk_v1.models.reporting.global_min_max_extreme import GlobalMinMaxExtreme


class GlobalMinMaxResult(SimScaleModel):
    """The global minimum and maximum of a scalar field across the entire model over the selected steps."""

    field: str | None = Field(
        default=None, description="The label of the scalar field whose global minimum and maximum are reported here."
    )
    data_type: DataType | None = Field(validation_alias="dataType", serialization_alias="dataType", default=None)
    minimum: GlobalMinMaxExtreme | None = Field(default=None)
    maximum: GlobalMinMaxExtreme | None = Field(default=None)
