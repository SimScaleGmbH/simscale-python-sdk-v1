from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_unit import GeometryUnit


class GeometryImportRequest(SimScaleModel):
    name: str = Field(description="The name of the imported geometry.")
    location: Any
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
    input_unit: GeometryUnit = Field(validation_alias="inputUnit", serialization_alias="inputUnit")
    options: Any = Field(
        description="CAD import options. Please refer to https://www.simscale.com/docs/cad-preparation/#cad-upload-options for a detailed description of the options."
    )
