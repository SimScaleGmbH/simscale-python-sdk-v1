from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.query_parameters import QueryParameters


class CadQueryRequest(SimScaleModel):
    query: Literal["detect-contacts-v3", "find_interfering_bodies", "find_small_gaps", "measure-entities"] = Field(
        description="Available query types:   - `detect-contacts-v3`: Identify contacts between solid regions. Supported internal formats: `PARASOLID`.   - `find_interfering_bodies`: Find all interfering solid regions. Supported internal formats: `PARASOLID`.   - `find_small_gaps`: Identify all gaps between solid regions that do not exceed the specified maximum gap distance. Supported internal formats: `PARASOLID`.   - `measure-entities`: Calculate the measurements of the given entities. Supported internal formats: `PARASOLID`."
    )
    parameters: QueryParameters | None = Field(default=None)
