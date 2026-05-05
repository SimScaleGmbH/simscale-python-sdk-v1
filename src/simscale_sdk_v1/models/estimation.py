from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cell_count import CellCount
from simscale_sdk_v1.models.compute_resource import ComputeResource
from simscale_sdk_v1.models.duration import Duration


class Estimation(SimScaleModel):
    duration: Duration | None = Field(default=None)
    compute_resource: ComputeResource | None = Field(
        validation_alias="computeResource", serialization_alias="computeResource", default=None
    )
    cell_count: CellCount | None = Field(validation_alias="cellCount", serialization_alias="cellCount", default=None)
    total_run_count: int | None = Field(
        validation_alias="totalRunCount",
        serialization_alias="totalRunCount",
        default=None,
        description="The total number of jobs that will be triggered for this simulation run or mesh operation.",
    )
