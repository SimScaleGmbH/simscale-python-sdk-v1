from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ListElementScope(SimScaleModel):
    """Per-element scope of a [ValidationRule]: the list whose elements are validated one by one, and the iterator reference through which the rule's cases address the element under evaluation (`iterator.relative("scale")` is the `scale` field of the current element)."""

    iterator_reference: Any | None = Field(
        validation_alias="iteratorReference",
        serialization_alias="iteratorReference",
        default=None,
        description="Iterator reference for processing collections.",
    )
    list_: Any | None = Field(
        validation_alias="list",
        serialization_alias="list",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
