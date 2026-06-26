from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.statistics_centroid_metric import StatisticsCentroidMetric
from simscale_sdk_v1.models.reporting.statistics_metric import StatisticsMetric


class StatisticsCuttingPlaneRegionEntry(SimScaleModel):
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
    centroid: StatisticsCentroidMetric | None = Field(default=None)
    bounding_box_min: StatisticsCentroidMetric | None = Field(
        validation_alias="boundingBoxMin", serialization_alias="boundingBoxMin", default=None
    )
    bounding_box_max: StatisticsCentroidMetric | None = Field(
        validation_alias="boundingBoxMax", serialization_alias="boundingBoxMax", default=None
    )
    part_name: str | None = Field(
        validation_alias="partName",
        serialization_alias="partName",
        default=None,
        description="The mesh part name the plane intersected to produce this region; null when the part could not be resolved.",
    )
    part_label: str | None = Field(
        validation_alias="partLabel",
        serialization_alias="partLabel",
        default=None,
        description='The user-facing label of the intersected part, resolved from the mesh topology (e.g. "Air domain", "solid1"); null when no label could be resolved for the part.',
    )
