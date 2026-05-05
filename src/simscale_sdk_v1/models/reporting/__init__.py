"""Generated Reporting models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.reporting.animation_output_settings import AnimationOutputSettings
    from simscale_sdk_v1.models.reporting.animation_report_from_state_properties import (
        AnimationReportFromStateProperties,
    )
    from simscale_sdk_v1.models.reporting.animation_report_properties import AnimationReportProperties
    from simscale_sdk_v1.models.reporting.automatic_state_metadata import AutomaticStateMetadata
    from simscale_sdk_v1.models.reporting.color import Color
    from simscale_sdk_v1.models.reporting.comets_visualization_style import CometsVisualizationStyle
    from simscale_sdk_v1.models.reporting.cutting_plane import CuttingPlane
    from simscale_sdk_v1.models.reporting.cylinders_visualization_style import CylindersVisualizationStyle
    from simscale_sdk_v1.models.reporting.data_type import DataType
    from simscale_sdk_v1.models.reporting.default_state_metadata import DefaultStateMetadata
    from simscale_sdk_v1.models.reporting.displacement import Displacement
    from simscale_sdk_v1.models.reporting.download_info import DownloadInfo
    from simscale_sdk_v1.models.reporting.filters import Filters
    from simscale_sdk_v1.models.reporting.forty_five_view_predefined_camera_settings import (
        FortyFiveViewPredefinedCameraSettings,
    )
    from simscale_sdk_v1.models.reporting.iso_surface import IsoSurface
    from simscale_sdk_v1.models.reporting.iso_volume import IsoVolume
    from simscale_sdk_v1.models.reporting.manual_state_metadata import ManualStateMetadata
    from simscale_sdk_v1.models.reporting.model_settings import ModelSettings
    from simscale_sdk_v1.models.reporting.one_of_animation_output_settings import OneOfAnimationOutputSettings
    from simscale_sdk_v1.models.reporting.one_of_camera_settings import OneOfCameraSettings
    from simscale_sdk_v1.models.reporting.one_of_visualization_style import OneOfVisualizationStyle
    from simscale_sdk_v1.models.reporting.opacity import Opacity
    from simscale_sdk_v1.models.reporting.part import Part
    from simscale_sdk_v1.models.reporting.particle_trace import ParticleTrace
    from simscale_sdk_v1.models.reporting.particle_trace_animation_output_settings import (
        ParticleTraceAnimationOutputSettings,
    )
    from simscale_sdk_v1.models.reporting.projection_type import ProjectionType
    from simscale_sdk_v1.models.reporting.render_mode import RenderMode
    from simscale_sdk_v1.models.reporting.report_from_state_properties import ReportFromStateProperties
    from simscale_sdk_v1.models.reporting.report_from_state_request import ReportFromStateRequest
    from simscale_sdk_v1.models.reporting.report_properties import ReportProperties
    from simscale_sdk_v1.models.reporting.report_request import ReportRequest
    from simscale_sdk_v1.models.reporting.report_response import ReportResponse
    from simscale_sdk_v1.models.reporting.resolution_info import ResolutionInfo
    from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
    from simscale_sdk_v1.models.reporting.scalar_settings import ScalarSettings
    from simscale_sdk_v1.models.reporting.screenshot_output_settings import ScreenshotOutputSettings
    from simscale_sdk_v1.models.reporting.screenshot_report_from_state_properties import (
        ScreenshotReportFromStateProperties,
    )
    from simscale_sdk_v1.models.reporting.screenshot_report_properties import ScreenshotReportProperties
    from simscale_sdk_v1.models.reporting.seed_settings import SeedSettings
    from simscale_sdk_v1.models.reporting.shape_animation_output_settings import ShapeAnimationOutputSettings
    from simscale_sdk_v1.models.reporting.spheres_visualization_style import SpheresVisualizationStyle
    from simscale_sdk_v1.models.reporting.state_metadata import StateMetadata
    from simscale_sdk_v1.models.reporting.statistics_centroid_metric import StatisticsCentroidMetric
    from simscale_sdk_v1.models.reporting.statistics_cutting_plane import StatisticsCuttingPlane
    from simscale_sdk_v1.models.reporting.statistics_metric import StatisticsMetric
    from simscale_sdk_v1.models.reporting.statistics_part_group import StatisticsPartGroup
    from simscale_sdk_v1.models.reporting.statistics_report_properties import StatisticsReportProperties
    from simscale_sdk_v1.models.reporting.statistics_result_entry import StatisticsResultEntry
    from simscale_sdk_v1.models.reporting.time_step_animation_output_settings import TimeStepAnimationOutputSettings
    from simscale_sdk_v1.models.reporting.top_view_predefined_camera_settings import TopViewPredefinedCameraSettings
    from simscale_sdk_v1.models.reporting.user_input_camera_settings import UserInputCameraSettings
    from simscale_sdk_v1.models.reporting.vector3_d import Vector3D
    from simscale_sdk_v1.models.reporting.vector_field import VectorField
    from simscale_sdk_v1.models.reporting.vector_settings import VectorSettings

_NAMES: dict[str, tuple[str, str]] = {
    "AnimationOutputSettings": (
        "simscale_sdk_v1.models.reporting.animation_output_settings",
        "AnimationOutputSettings",
    ),
    "AnimationReportFromStateProperties": (
        "simscale_sdk_v1.models.reporting.animation_report_from_state_properties",
        "AnimationReportFromStateProperties",
    ),
    "AnimationReportProperties": (
        "simscale_sdk_v1.models.reporting.animation_report_properties",
        "AnimationReportProperties",
    ),
    "AutomaticStateMetadata": ("simscale_sdk_v1.models.reporting.automatic_state_metadata", "AutomaticStateMetadata"),
    "Color": ("simscale_sdk_v1.models.reporting.color", "Color"),
    "CometsVisualizationStyle": (
        "simscale_sdk_v1.models.reporting.comets_visualization_style",
        "CometsVisualizationStyle",
    ),
    "CuttingPlane": ("simscale_sdk_v1.models.reporting.cutting_plane", "CuttingPlane"),
    "CylindersVisualizationStyle": (
        "simscale_sdk_v1.models.reporting.cylinders_visualization_style",
        "CylindersVisualizationStyle",
    ),
    "DataType": ("simscale_sdk_v1.models.reporting.data_type", "DataType"),
    "DefaultStateMetadata": ("simscale_sdk_v1.models.reporting.default_state_metadata", "DefaultStateMetadata"),
    "Displacement": ("simscale_sdk_v1.models.reporting.displacement", "Displacement"),
    "DownloadInfo": ("simscale_sdk_v1.models.reporting.download_info", "DownloadInfo"),
    "Filters": ("simscale_sdk_v1.models.reporting.filters", "Filters"),
    "FortyFiveViewPredefinedCameraSettings": (
        "simscale_sdk_v1.models.reporting.forty_five_view_predefined_camera_settings",
        "FortyFiveViewPredefinedCameraSettings",
    ),
    "IsoSurface": ("simscale_sdk_v1.models.reporting.iso_surface", "IsoSurface"),
    "IsoVolume": ("simscale_sdk_v1.models.reporting.iso_volume", "IsoVolume"),
    "ManualStateMetadata": ("simscale_sdk_v1.models.reporting.manual_state_metadata", "ManualStateMetadata"),
    "ModelSettings": ("simscale_sdk_v1.models.reporting.model_settings", "ModelSettings"),
    "OneOfAnimationOutputSettings": (
        "simscale_sdk_v1.models.reporting.one_of_animation_output_settings",
        "OneOfAnimationOutputSettings",
    ),
    "OneOfCameraSettings": ("simscale_sdk_v1.models.reporting.one_of_camera_settings", "OneOfCameraSettings"),
    "OneOfVisualizationStyle": (
        "simscale_sdk_v1.models.reporting.one_of_visualization_style",
        "OneOfVisualizationStyle",
    ),
    "Opacity": ("simscale_sdk_v1.models.reporting.opacity", "Opacity"),
    "Part": ("simscale_sdk_v1.models.reporting.part", "Part"),
    "ParticleTrace": ("simscale_sdk_v1.models.reporting.particle_trace", "ParticleTrace"),
    "ParticleTraceAnimationOutputSettings": (
        "simscale_sdk_v1.models.reporting.particle_trace_animation_output_settings",
        "ParticleTraceAnimationOutputSettings",
    ),
    "ProjectionType": ("simscale_sdk_v1.models.reporting.projection_type", "ProjectionType"),
    "RenderMode": ("simscale_sdk_v1.models.reporting.render_mode", "RenderMode"),
    "ReportFromStateProperties": (
        "simscale_sdk_v1.models.reporting.report_from_state_properties",
        "ReportFromStateProperties",
    ),
    "ReportFromStateRequest": ("simscale_sdk_v1.models.reporting.report_from_state_request", "ReportFromStateRequest"),
    "ReportProperties": ("simscale_sdk_v1.models.reporting.report_properties", "ReportProperties"),
    "ReportRequest": ("simscale_sdk_v1.models.reporting.report_request", "ReportRequest"),
    "ReportResponse": ("simscale_sdk_v1.models.reporting.report_response", "ReportResponse"),
    "ResolutionInfo": ("simscale_sdk_v1.models.reporting.resolution_info", "ResolutionInfo"),
    "ScalarField": ("simscale_sdk_v1.models.reporting.scalar_field", "ScalarField"),
    "ScalarSettings": ("simscale_sdk_v1.models.reporting.scalar_settings", "ScalarSettings"),
    "ScreenshotOutputSettings": (
        "simscale_sdk_v1.models.reporting.screenshot_output_settings",
        "ScreenshotOutputSettings",
    ),
    "ScreenshotReportFromStateProperties": (
        "simscale_sdk_v1.models.reporting.screenshot_report_from_state_properties",
        "ScreenshotReportFromStateProperties",
    ),
    "ScreenshotReportProperties": (
        "simscale_sdk_v1.models.reporting.screenshot_report_properties",
        "ScreenshotReportProperties",
    ),
    "SeedSettings": ("simscale_sdk_v1.models.reporting.seed_settings", "SeedSettings"),
    "ShapeAnimationOutputSettings": (
        "simscale_sdk_v1.models.reporting.shape_animation_output_settings",
        "ShapeAnimationOutputSettings",
    ),
    "SpheresVisualizationStyle": (
        "simscale_sdk_v1.models.reporting.spheres_visualization_style",
        "SpheresVisualizationStyle",
    ),
    "StateMetadata": ("simscale_sdk_v1.models.reporting.state_metadata", "StateMetadata"),
    "StatisticsCentroidMetric": (
        "simscale_sdk_v1.models.reporting.statistics_centroid_metric",
        "StatisticsCentroidMetric",
    ),
    "StatisticsCuttingPlane": ("simscale_sdk_v1.models.reporting.statistics_cutting_plane", "StatisticsCuttingPlane"),
    "StatisticsMetric": ("simscale_sdk_v1.models.reporting.statistics_metric", "StatisticsMetric"),
    "StatisticsPartGroup": ("simscale_sdk_v1.models.reporting.statistics_part_group", "StatisticsPartGroup"),
    "StatisticsReportProperties": (
        "simscale_sdk_v1.models.reporting.statistics_report_properties",
        "StatisticsReportProperties",
    ),
    "StatisticsResultEntry": ("simscale_sdk_v1.models.reporting.statistics_result_entry", "StatisticsResultEntry"),
    "TimeStepAnimationOutputSettings": (
        "simscale_sdk_v1.models.reporting.time_step_animation_output_settings",
        "TimeStepAnimationOutputSettings",
    ),
    "TopViewPredefinedCameraSettings": (
        "simscale_sdk_v1.models.reporting.top_view_predefined_camera_settings",
        "TopViewPredefinedCameraSettings",
    ),
    "UserInputCameraSettings": (
        "simscale_sdk_v1.models.reporting.user_input_camera_settings",
        "UserInputCameraSettings",
    ),
    "Vector3D": ("simscale_sdk_v1.models.reporting.vector3_d", "Vector3D"),
    "VectorField": ("simscale_sdk_v1.models.reporting.vector_field", "VectorField"),
    "VectorSettings": ("simscale_sdk_v1.models.reporting.vector_settings", "VectorSettings"),
}


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys())
