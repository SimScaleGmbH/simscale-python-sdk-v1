from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EntityAssignmentListIntersect(SimScaleModel):
    first: Any | None = Field(
        default=None,
        description="Value model for an entity assignment list. Resolves to an object node following the [EntityAssignmentList] data model.",
    )
    second: Any | None = Field(
        default=None,
        description="Value model for an entity assignment list. Resolves to an object node following the [EntityAssignmentList] data model.",
    )
    value_model_type: str
