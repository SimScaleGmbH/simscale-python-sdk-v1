"""Generated Cad models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.cad.axis import Axis
    from simscale_sdk_v1.models.cad.box import Box
    from simscale_sdk_v1.models.cad.box_with_unit import BoxWithUnit
    from simscale_sdk_v1.models.cad.cad_feature_request import CadFeatureRequest
    from simscale_sdk_v1.models.cad.cad_query_request import CadQueryRequest
    from simscale_sdk_v1.models.cad.cad_query_result import CadQueryResult
    from simscale_sdk_v1.models.cad.close_sheet_v2_parameters import CloseSheetV2Parameters
    from simscale_sdk_v1.models.cad.create_box_method import CreateBoxMethod
    from simscale_sdk_v1.models.cad.create_box_parameters import CreateBoxParameters
    from simscale_sdk_v1.models.cad.create_cylinder_group_parameter import CreateCylinderGroupParameter
    from simscale_sdk_v1.models.cad.create_cylinder_v3_parameters import CreateCylinderV3Parameters
    from simscale_sdk_v1.models.cad.cylinder import Cylinder
    from simscale_sdk_v1.models.cad.delete_face_v2_parameters import DeleteFaceV2Parameters
    from simscale_sdk_v1.models.cad.delete_occurrences_parameters import DeleteOccurrencesParameters
    from simscale_sdk_v1.models.cad.detect_contacts_v3_parameters import DetectContactsV3Parameters
    from simscale_sdk_v1.models.cad.detect_contacts_v3_response import DetectContactsV3Response
    from simscale_sdk_v1.models.cad.extrude_by_parameter import ExtrudeByParameter
    from simscale_sdk_v1.models.cad.extrude_faces_parameters import ExtrudeFacesParameters
    from simscale_sdk_v1.models.cad.face_contact import FaceContact
    from simscale_sdk_v1.models.cad.face_pairs import FacePairs
    from simscale_sdk_v1.models.cad.facet_split_bodies_parameters import FacetSplitBodiesParameters
    from simscale_sdk_v1.models.cad.feature_parameters import FeatureParameters
    from simscale_sdk_v1.models.cad.find_interfering_bodies_parameters import FindInterferingBodiesParameters
    from simscale_sdk_v1.models.cad.find_interfering_bodies_response import FindInterferingBodiesResponse
    from simscale_sdk_v1.models.cad.find_small_gaps_parameters import FindSmallGapsParameters
    from simscale_sdk_v1.models.cad.find_small_gaps_response import FindSmallGapsResponse
    from simscale_sdk_v1.models.cad.fix_interferences_parameters import FixInterferencesParameters
    from simscale_sdk_v1.models.cad.flow_volume_extraction_external_parameters import (
        FlowVolumeExtractionExternalParameters,
    )
    from simscale_sdk_v1.models.cad.flow_volume_extraction_internal_parameters import (
        FlowVolumeExtractionInternalParameters,
    )
    from simscale_sdk_v1.models.cad.imprint_bodies_parameters import ImprintBodiesParameters
    from simscale_sdk_v1.models.cad.interference import Interference
    from simscale_sdk_v1.models.cad.intersect_bodies_parameters import IntersectBodiesParameters
    from simscale_sdk_v1.models.cad.length import Length
    from simscale_sdk_v1.models.cad.measure_entities_parameters import MeasureEntitiesParameters
    from simscale_sdk_v1.models.cad.measure_entities_response import MeasureEntitiesResponse
    from simscale_sdk_v1.models.cad.measured_value import MeasuredValue
    from simscale_sdk_v1.models.cad.move_faces_group_parameter import MoveFacesGroupParameter
    from simscale_sdk_v1.models.cad.move_faces_parameters import MoveFacesParameters
    from simscale_sdk_v1.models.cad.plane import Plane
    from simscale_sdk_v1.models.cad.point_pair import PointPair
    from simscale_sdk_v1.models.cad.query_parameters import QueryParameters
    from simscale_sdk_v1.models.cad.region_contact import RegionContact
    from simscale_sdk_v1.models.cad.rotate_bodies_parameters import RotateBodiesParameters
    from simscale_sdk_v1.models.cad.scale_bodies_parameters import ScaleBodiesParameters
    from simscale_sdk_v1.models.cad.simplify_parameters import SimplifyParameters
    from simscale_sdk_v1.models.cad.split_bodies_parameters import SplitBodiesParameters
    from simscale_sdk_v1.models.cad.subtract_bodies_parameters import SubtractBodiesParameters
    from simscale_sdk_v1.models.cad.translate_bodies_parameters import TranslateBodiesParameters
    from simscale_sdk_v1.models.cad.translate_group_parameter import TranslateGroupParameter
    from simscale_sdk_v1.models.cad.union_bodies_parameters import UnionBodiesParameters
    from simscale_sdk_v1.models.cad.vector import Vector
    from simscale_sdk_v1.models.cad.vector_with_unit import VectorWithUnit
    from simscale_sdk_v1.models.cad.wrap_occurrences_parameters import WrapOccurrencesParameters
    from simscale_sdk_v1.models.cad.wrap_tunnel_detection_parameter import WrapTunnelDetectionParameter
    from simscale_sdk_v1.models.cad._root import Cad

_NAMES: dict[str, tuple[str, str]] = {
    "Axis": ("simscale_sdk_v1.models.cad.axis", "Axis"),
    "Box": ("simscale_sdk_v1.models.cad.box", "Box"),
    "BoxWithUnit": ("simscale_sdk_v1.models.cad.box_with_unit", "BoxWithUnit"),
    "CadFeatureRequest": ("simscale_sdk_v1.models.cad.cad_feature_request", "CadFeatureRequest"),
    "CadQueryRequest": ("simscale_sdk_v1.models.cad.cad_query_request", "CadQueryRequest"),
    "CadQueryResult": ("simscale_sdk_v1.models.cad.cad_query_result", "CadQueryResult"),
    "CloseSheetV2Parameters": ("simscale_sdk_v1.models.cad.close_sheet_v2_parameters", "CloseSheetV2Parameters"),
    "CreateBoxMethod": ("simscale_sdk_v1.models.cad.create_box_method", "CreateBoxMethod"),
    "CreateBoxParameters": ("simscale_sdk_v1.models.cad.create_box_parameters", "CreateBoxParameters"),
    "CreateCylinderGroupParameter": (
        "simscale_sdk_v1.models.cad.create_cylinder_group_parameter",
        "CreateCylinderGroupParameter",
    ),
    "CreateCylinderV3Parameters": (
        "simscale_sdk_v1.models.cad.create_cylinder_v3_parameters",
        "CreateCylinderV3Parameters",
    ),
    "Cylinder": ("simscale_sdk_v1.models.cad.cylinder", "Cylinder"),
    "DeleteFaceV2Parameters": ("simscale_sdk_v1.models.cad.delete_face_v2_parameters", "DeleteFaceV2Parameters"),
    "DeleteOccurrencesParameters": (
        "simscale_sdk_v1.models.cad.delete_occurrences_parameters",
        "DeleteOccurrencesParameters",
    ),
    "DetectContactsV3Parameters": (
        "simscale_sdk_v1.models.cad.detect_contacts_v3_parameters",
        "DetectContactsV3Parameters",
    ),
    "DetectContactsV3Response": ("simscale_sdk_v1.models.cad.detect_contacts_v3_response", "DetectContactsV3Response"),
    "ExtrudeByParameter": ("simscale_sdk_v1.models.cad.extrude_by_parameter", "ExtrudeByParameter"),
    "ExtrudeFacesParameters": ("simscale_sdk_v1.models.cad.extrude_faces_parameters", "ExtrudeFacesParameters"),
    "FaceContact": ("simscale_sdk_v1.models.cad.face_contact", "FaceContact"),
    "FacePairs": ("simscale_sdk_v1.models.cad.face_pairs", "FacePairs"),
    "FacetSplitBodiesParameters": (
        "simscale_sdk_v1.models.cad.facet_split_bodies_parameters",
        "FacetSplitBodiesParameters",
    ),
    "FeatureParameters": ("simscale_sdk_v1.models.cad.feature_parameters", "FeatureParameters"),
    "FindInterferingBodiesParameters": (
        "simscale_sdk_v1.models.cad.find_interfering_bodies_parameters",
        "FindInterferingBodiesParameters",
    ),
    "FindInterferingBodiesResponse": (
        "simscale_sdk_v1.models.cad.find_interfering_bodies_response",
        "FindInterferingBodiesResponse",
    ),
    "FindSmallGapsParameters": ("simscale_sdk_v1.models.cad.find_small_gaps_parameters", "FindSmallGapsParameters"),
    "FindSmallGapsResponse": ("simscale_sdk_v1.models.cad.find_small_gaps_response", "FindSmallGapsResponse"),
    "FixInterferencesParameters": (
        "simscale_sdk_v1.models.cad.fix_interferences_parameters",
        "FixInterferencesParameters",
    ),
    "FlowVolumeExtractionExternalParameters": (
        "simscale_sdk_v1.models.cad.flow_volume_extraction_external_parameters",
        "FlowVolumeExtractionExternalParameters",
    ),
    "FlowVolumeExtractionInternalParameters": (
        "simscale_sdk_v1.models.cad.flow_volume_extraction_internal_parameters",
        "FlowVolumeExtractionInternalParameters",
    ),
    "ImprintBodiesParameters": ("simscale_sdk_v1.models.cad.imprint_bodies_parameters", "ImprintBodiesParameters"),
    "Interference": ("simscale_sdk_v1.models.cad.interference", "Interference"),
    "IntersectBodiesParameters": (
        "simscale_sdk_v1.models.cad.intersect_bodies_parameters",
        "IntersectBodiesParameters",
    ),
    "Length": ("simscale_sdk_v1.models.cad.length", "Length"),
    "MeasureEntitiesParameters": (
        "simscale_sdk_v1.models.cad.measure_entities_parameters",
        "MeasureEntitiesParameters",
    ),
    "MeasureEntitiesResponse": ("simscale_sdk_v1.models.cad.measure_entities_response", "MeasureEntitiesResponse"),
    "MeasuredValue": ("simscale_sdk_v1.models.cad.measured_value", "MeasuredValue"),
    "MoveFacesGroupParameter": ("simscale_sdk_v1.models.cad.move_faces_group_parameter", "MoveFacesGroupParameter"),
    "MoveFacesParameters": ("simscale_sdk_v1.models.cad.move_faces_parameters", "MoveFacesParameters"),
    "Plane": ("simscale_sdk_v1.models.cad.plane", "Plane"),
    "PointPair": ("simscale_sdk_v1.models.cad.point_pair", "PointPair"),
    "QueryParameters": ("simscale_sdk_v1.models.cad.query_parameters", "QueryParameters"),
    "RegionContact": ("simscale_sdk_v1.models.cad.region_contact", "RegionContact"),
    "RotateBodiesParameters": ("simscale_sdk_v1.models.cad.rotate_bodies_parameters", "RotateBodiesParameters"),
    "ScaleBodiesParameters": ("simscale_sdk_v1.models.cad.scale_bodies_parameters", "ScaleBodiesParameters"),
    "SimplifyParameters": ("simscale_sdk_v1.models.cad.simplify_parameters", "SimplifyParameters"),
    "SplitBodiesParameters": ("simscale_sdk_v1.models.cad.split_bodies_parameters", "SplitBodiesParameters"),
    "SubtractBodiesParameters": ("simscale_sdk_v1.models.cad.subtract_bodies_parameters", "SubtractBodiesParameters"),
    "TranslateBodiesParameters": (
        "simscale_sdk_v1.models.cad.translate_bodies_parameters",
        "TranslateBodiesParameters",
    ),
    "TranslateGroupParameter": ("simscale_sdk_v1.models.cad.translate_group_parameter", "TranslateGroupParameter"),
    "UnionBodiesParameters": ("simscale_sdk_v1.models.cad.union_bodies_parameters", "UnionBodiesParameters"),
    "Vector": ("simscale_sdk_v1.models.cad.vector", "Vector"),
    "VectorWithUnit": ("simscale_sdk_v1.models.cad.vector_with_unit", "VectorWithUnit"),
    "WrapOccurrencesParameters": (
        "simscale_sdk_v1.models.cad.wrap_occurrences_parameters",
        "WrapOccurrencesParameters",
    ),
    "WrapTunnelDetectionParameter": (
        "simscale_sdk_v1.models.cad.wrap_tunnel_detection_parameter",
        "WrapTunnelDetectionParameter",
    ),
    "Cad": ("simscale_sdk_v1.models.cad._root", "Cad"),
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
