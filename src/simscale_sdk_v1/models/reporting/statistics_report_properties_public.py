from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.statistics_cutting_plane import StatisticsCuttingPlane
from simscale_sdk_v1.models.reporting.statistics_part_group import StatisticsPartGroup


class StatisticsReportPropertiesPublic(SimScaleModel):
    """Configuration for a statistics (bulk calculation) report. Computes scalar field statistics (minimum, maximum, average, integral, and area/volume-weighted equivalents) over model geometry at a chosen time step. At least one of partIdentifiers, partGroupIdentifiers, or cuttingPlanes must be provided. Parts are named surfaces or volumes that exist in the simulation result (e.g. wall patches in a CFD model or solid bodies in a structural model). Use partIdentifiers to get independent results per part, or partGroupIdentifiers to combine several parts into one aggregated result. Cutting planes are user-defined infinite planes that slice through the model geometry. They are specified by a point on the plane and a normal vector, and statistics are computed over the intersection."""

    report_type: str = Field(validation_alias="reportType", serialization_alias="reportType", default="STATISTICS")
    part_identifiers: list[str] | None = Field(
        validation_alias="partIdentifiers",
        serialization_alias="partIdentifiers",
        default=None,
        description="Names of individual model parts for which to compute statistics independently. Each name must exactly match a part name present in the simulation result. Each part produces a separate entry in the statisticsResult, keyed by part name.",
    )
    part_group_identifiers: list[StatisticsPartGroup] | None = Field(
        validation_alias="partGroupIdentifiers",
        serialization_alias="partGroupIdentifiers",
        default=None,
        description="Named groups of parts whose bulk values are aggregated into a single combined result entry. Useful when several parts form a logical unit (e.g. all wall patches) and a single aggregated metric is needed. Each group produces one entry in the statisticsResult, keyed by the group identifier.",
    )
    cutting_planes: list[StatisticsCuttingPlane] | None = Field(
        validation_alias="cuttingPlanes",
        serialization_alias="cuttingPlanes",
        default=None,
        description="Cutting planes for which to compute statistics. A cutting plane is an infinite plane defined by a point and a normal vector that slices through the model. Statistics are computed over the intersection geometry. Each plane produces one entry in the statisticsResult, keyed by the plane identifier.",
    )
    scalar_field: ScalarField = Field(validation_alias="scalarField", serialization_alias="scalarField")
    frame_index: int | None = Field(
        validation_alias="frameIndex",
        serialization_alias="frameIndex",
        default=None,
        description="Zero-based time step index at which to evaluate the field. When not provided, statistics are computed at the last available time step.",
    )
