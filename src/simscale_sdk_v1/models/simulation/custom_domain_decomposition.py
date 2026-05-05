from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CustomDomainDecomposition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM",
        description="Schema name: CustomDomainDecomposition",
    )
    num_partitions: int | None = Field(validation_alias="numPartitions", serialization_alias="numPartitions", default=1)
    partitioner: Literal["METIS", "SCOTCH"] | None = Field(default="METIS")
