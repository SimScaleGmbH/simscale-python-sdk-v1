from __future__ import annotations
from typing import Union

from simscale_sdk_v1.models.cad.detect_contacts_v3_response import DetectContactsV3Response
from simscale_sdk_v1.models.cad.find_gaps_response import FindGapsResponse
from simscale_sdk_v1.models.cad.find_interfering_bodies_response import FindInterferingBodiesResponse
from simscale_sdk_v1.models.cad.measure_entities_response import MeasureEntitiesResponse

CadQueryResult = Union[
    DetectContactsV3Response, FindInterferingBodiesResponse, FindGapsResponse, MeasureEntitiesResponse
]
