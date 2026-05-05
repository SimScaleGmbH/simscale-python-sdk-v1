from __future__ import annotations
from typing import Union

from simscale_sdk_v1.models.cad.close_sheet_v2_parameters import CloseSheetV2Parameters
from simscale_sdk_v1.models.cad.create_box_parameters import CreateBoxParameters
from simscale_sdk_v1.models.cad.create_cylinder_v3_parameters import CreateCylinderV3Parameters
from simscale_sdk_v1.models.cad.delete_face_v2_parameters import DeleteFaceV2Parameters
from simscale_sdk_v1.models.cad.delete_occurrences_parameters import DeleteOccurrencesParameters
from simscale_sdk_v1.models.cad.extrude_faces_parameters import ExtrudeFacesParameters
from simscale_sdk_v1.models.cad.facet_split_bodies_parameters import FacetSplitBodiesParameters
from simscale_sdk_v1.models.cad.fix_interferences_parameters import FixInterferencesParameters
from simscale_sdk_v1.models.cad.flow_volume_extraction_external_parameters import FlowVolumeExtractionExternalParameters
from simscale_sdk_v1.models.cad.flow_volume_extraction_internal_parameters import FlowVolumeExtractionInternalParameters
from simscale_sdk_v1.models.cad.imprint_bodies_parameters import ImprintBodiesParameters
from simscale_sdk_v1.models.cad.intersect_bodies_parameters import IntersectBodiesParameters
from simscale_sdk_v1.models.cad.move_faces_parameters import MoveFacesParameters
from simscale_sdk_v1.models.cad.rotate_bodies_parameters import RotateBodiesParameters
from simscale_sdk_v1.models.cad.scale_bodies_parameters import ScaleBodiesParameters
from simscale_sdk_v1.models.cad.simplify_parameters import SimplifyParameters
from simscale_sdk_v1.models.cad.split_bodies_parameters import SplitBodiesParameters
from simscale_sdk_v1.models.cad.subtract_bodies_parameters import SubtractBodiesParameters
from simscale_sdk_v1.models.cad.translate_bodies_parameters import TranslateBodiesParameters
from simscale_sdk_v1.models.cad.union_bodies_parameters import UnionBodiesParameters
from simscale_sdk_v1.models.cad.wrap_occurrences_parameters import WrapOccurrencesParameters

FeatureParameters = Union[
    CloseSheetV2Parameters,
    CreateBoxParameters,
    CreateCylinderV3Parameters,
    DeleteFaceV2Parameters,
    DeleteOccurrencesParameters,
    ExtrudeFacesParameters,
    FacetSplitBodiesParameters,
    FixInterferencesParameters,
    FlowVolumeExtractionExternalParameters,
    FlowVolumeExtractionInternalParameters,
    ImprintBodiesParameters,
    IntersectBodiesParameters,
    MoveFacesParameters,
    RotateBodiesParameters,
    ScaleBodiesParameters,
    SimplifyParameters,
    SplitBodiesParameters,
    SubtractBodiesParameters,
    TranslateBodiesParameters,
    UnionBodiesParameters,
    WrapOccurrencesParameters,
]
