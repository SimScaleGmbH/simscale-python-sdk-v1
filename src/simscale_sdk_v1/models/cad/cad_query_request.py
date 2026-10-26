from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.query_parameters import QueryParameters


class CadQueryRequest(SimScaleModel):
    query: Literal["detect-contacts-v3", "find_gaps", "find_interfering_bodies", "measure-entities"] = Field(
        description="Available query types:   - `detect-contacts-v3`: Identify contacts between solid regions. Supported internal formats: `PARASOLID`.   - `find_gaps`: Find all gaps between solid regions. Supported internal formats: `PARASOLID`.   - `find_interfering_bodies`: Find all interfering solid regions. Supported internal formats: `PARASOLID`.   - `measure-entities`: Calculate the measurements of the given entities. Supported internal formats: `PARASOLID`.   - `measure-entities-v2`: Measure any mix of bodies, faces, edges and vertices in one call, unlike `measure-entities` which requires every entity to share a type. Can also report the combined size and centroid of the input entities when they share a type, and the relationship between them when exactly two are given. Supported internal formats: `PARASOLID`."
    )
    parameters: QueryParameters | None = Field(default=None)
