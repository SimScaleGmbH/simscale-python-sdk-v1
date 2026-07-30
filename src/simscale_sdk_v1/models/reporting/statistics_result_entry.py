from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.statistics_centroid_metric import StatisticsCentroidMetric
from simscale_sdk_v1.models.reporting.statistics_cutting_plane_region_entry import StatisticsCuttingPlaneRegionEntry
from simscale_sdk_v1.models.reporting.statistics_metric import StatisticsMetric


class StatisticsResultEntry(SimScaleModel):
    element_min: StatisticsMetric | None = Field(
        validation_alias="elementMin", serialization_alias="elementMin", default=None
    )
    element_max: StatisticsMetric | None = Field(
        validation_alias="elementMax", serialization_alias="elementMax", default=None
    )
    element_average: StatisticsMetric | None = Field(
        validation_alias="elementAverage", serialization_alias="elementAverage", default=None
    )
    element_integral: StatisticsMetric | None = Field(
        validation_alias="elementIntegral", serialization_alias="elementIntegral", default=None
    )
    element_area_weighted_average: StatisticsMetric | None = Field(
        validation_alias="elementAreaWeightedAverage", serialization_alias="elementAreaWeightedAverage", default=None
    )
    node_average: StatisticsMetric | None = Field(
        validation_alias="nodeAverage", serialization_alias="nodeAverage", default=None
    )
    node_min: StatisticsMetric | None = Field(validation_alias="nodeMin", serialization_alias="nodeMin", default=None)
    node_max: StatisticsMetric | None = Field(validation_alias="nodeMax", serialization_alias="nodeMax", default=None)
    volume_element_integral: StatisticsMetric | None = Field(
        validation_alias="volumeElementIntegral", serialization_alias="volumeElementIntegral", default=None
    )
    volume_element_average: StatisticsMetric | None = Field(
        validation_alias="volumeElementAverage", serialization_alias="volumeElementAverage", default=None
    )
    volume_element_volume_area_weighted_average: StatisticsMetric | None = Field(
        validation_alias="volumeElementVolumeAreaWeightedAverage",
        serialization_alias="volumeElementVolumeAreaWeightedAverage",
        default=None,
    )
    volume_element_min: StatisticsMetric | None = Field(
        validation_alias="volumeElementMin", serialization_alias="volumeElementMin", default=None
    )
    volume_element_max: StatisticsMetric | None = Field(
        validation_alias="volumeElementMax", serialization_alias="volumeElementMax", default=None
    )
    mass_flow_rate: StatisticsMetric | None = Field(
        validation_alias="massFlowRate", serialization_alias="massFlowRate", default=None
    )
    volumetric_flow_rate: StatisticsMetric | None = Field(
        validation_alias="volumetricFlowRate", serialization_alias="volumetricFlowRate", default=None
    )
    centroid: StatisticsCentroidMetric | None = Field(default=None)
    bounding_box_min: StatisticsCentroidMetric | None = Field(
        validation_alias="boundingBoxMin", serialization_alias="boundingBoxMin", default=None
    )
    bounding_box_max: StatisticsCentroidMetric | None = Field(
        validation_alias="boundingBoxMax", serialization_alias="boundingBoxMax", default=None
    )
    regions: list[StatisticsCuttingPlaneRegionEntry] | None = Field(
        default=None,
        description="For a cutting plane, the per-region breakdown: one entry per distinct area produced by the cut (one per intersected part, or several when a single part is cut in more than one place). The enclosing entry's own metrics remain the whole-plane aggregate over all regions; this array only adds the per-region split. Absent for part and part-group entries.",
    )
