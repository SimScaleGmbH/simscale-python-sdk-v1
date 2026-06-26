from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.statistics_cutting_plane import StatisticsCuttingPlane
from simscale_sdk_v1.models.reporting.statistics_part_group import StatisticsPartGroup


class StatisticsReportProperties(SimScaleModel):
    """Configuration for a statistics (bulk calculation) report. Computes scalar field statistics (minimum, maximum, average, integral, and area/volume-weighted equivalents) over model geometry at a chosen time step. Also carries the server-resolved resolution hints (cadAssociations, topologyLabelByName) that postproc-manager populates and postproc-result-query consumes; these hints are stripped from the public API response, which uses the reduced StatisticsReportPropertiesPublic projection. At least one of partIdentifiers, partGroupIdentifiers, or cuttingPlanes must be provided."""

    report_type: str = Field(validation_alias="reportType", serialization_alias="reportType", default="STATISTICS")
    part_identifiers: list[str] | None = Field(
        validation_alias="partIdentifiers",
        serialization_alias="partIdentifiers",
        default=None,
        description="Names of individual model parts for which to compute statistics independently. Each name must exactly match a part name present in the simulation result model. Each part produces a separate entry in the statisticsResult, keyed by part name.",
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
    cad_associations: dict[str, list[str]] | None = Field(
        validation_alias="cadAssociations",
        serialization_alias="cadAssociations",
        default=None,
        description='Filtered CAD-Mesh name mapping for the requested parts only. Each key is a CAD entity name provided by the user and each value is the list of mesh names it maps to. A value of "" means the CAD entity has no mesh equivalent. Absent when no CAD-Mesh mapping is available or when all requested names are already mesh names.',
    )
    topology_label_by_name: dict[str, str] | None = Field(
        validation_alias="topologyLabelByName",
        serialization_alias="topologyLabelByName",
        default=None,
        description='Mesh-part-name to user-facing label mapping for the mesh topology, used to label cutting-plane regions with a human-readable name (e.g. "region4" -> "Air domain"). Populated only for cutting-plane requests; absent otherwise.',
    )
