from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EntityAssignmentListCadPredicateFailures(SimScaleModel):
    assignments: Any | None = Field(
        default=None,
        description="Value model for an entity assignment list. Resolves to an object node following the [EntityAssignmentList] data model.",
    )
    query: Literal["FACE_IS_FLAT", "FACE_IS_NOT_FLAT", "FACE_IS_ROTATIONAL", "FACE_IS_NOT_ROTATIONAL"] | None = Field(
        default="", description="A per-entity geometric predicate about a CAD model, answered by the CAD services."
    )
    value_model_type: str
