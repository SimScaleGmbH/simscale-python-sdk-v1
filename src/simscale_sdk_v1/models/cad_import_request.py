from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad_import_request_location import CadImportRequestLocation
from simscale_sdk_v1.models.cad_import_request_options import CadImportRequestOptions
from simscale_sdk_v1.models.cad_unit import CadUnit


class CadImportRequest(SimScaleModel):
    name: str = Field(description="The name of the imported CAD.")
    location: CadImportRequestLocation
    format: Literal[
        "ACIS",
        "CATIA",
        "CREO",
        "IGES",
        "INVENTOR",
        "NX",
        "PARASOLID",
        "REVIT",
        "RHINOCEROS",
        "SOLIDEDGE",
        "SOLIDWORKS",
        "STEP",
        "STL",
        "NTOP",
    ] = Field(description="The CAD format.")
    input_unit: CadUnit = Field(validation_alias="inputUnit", serialization_alias="inputUnit")
    options: CadImportRequestOptions
