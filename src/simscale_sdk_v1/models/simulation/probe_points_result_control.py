from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__probe_points_result_control_write_control import (
    OneOf_ProbePointsResultControlWriteControl,
)
from simscale_sdk_v1.models.simulation.table_defined_probe_locations import TableDefinedProbeLocations


class ProbePointsResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PROBE_POINTS",
        description="Schema name: ProbePointsResultControl",
    )
    name: str | None = Field(default=None)
    write_control: OneOf_ProbePointsResultControlWriteControl | None = Field(
        validation_alias="writeControl", serialization_alias="writeControl", default=None
    )
    fraction_from_end: float | None = Field(
        validation_alias="fractionFromEnd",
        serialization_alias="fractionFromEnd",
        default=0.2,
        description="It defines the point in simulation where the result output data extraction starts. For instance, Fraction from end of 1 (100%) extracts all data from the beginning of the simulation while default 0.2 extracts 20% data from the end of the simulation.",
    )
    export_statistics: bool | None = Field(
        validation_alias="exportStatistics",
        serialization_alias="exportStatistics",
        default=True,
        description="When this switch is activated, statistical data for the selected probe points will be exported:Minimum (MIN)Maximum (MAX)Average (AVG)Standard deviation (STDDEV)Root mean square (RMS)",
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
    probe_locations: TableDefinedProbeLocations | None = Field(
        validation_alias="probeLocations", serialization_alias="probeLocations", default=None
    )
