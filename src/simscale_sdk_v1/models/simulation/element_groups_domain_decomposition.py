from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ElementGroupsDomainDecomposition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ELEMENT_GROUPS",
        description="Schema name: ElementGroupsDomainDecomposition",
    )
    max_element_group_size: int | None = Field(
        validation_alias="maxElementGroupSize", serialization_alias="maxElementGroupSize", default=1000
    )
