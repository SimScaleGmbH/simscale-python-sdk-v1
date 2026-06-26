from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.statistics_centroid_metric import StatisticsCentroidMetric
from simscale_sdk_v1.models.reporting.statistics_metric import StatisticsMetric


class StatisticsBulkValues(SimScaleModel):
    """Bulk statistical values (metrics, centroid and bounding box) computed over a region of the model - a part, a part group, a whole cutting plane, or a single cutting-plane region. Each numeric metric is an object with a 'value' and a 'unit' field. Integral metrics carry composite units; all others carry the plain scalar field unit."""

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
