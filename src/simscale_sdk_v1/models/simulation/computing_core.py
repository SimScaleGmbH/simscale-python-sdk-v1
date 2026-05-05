from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__computing_core_domain_decomposition import (
    OneOf_ComputingCoreDomainDecomposition,
)


class ComputingCore(SimScaleModel):
    num_of_processors: Literal[-1, 1, 2, 4, 8, 16, 32, 48, 64, 96, 128, 192] | None = Field(
        validation_alias="numOfProcessors",
        serialization_alias="numOfProcessors",
        default=-1,
        description="Selecting more processor cores will speed up the simulation process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    num_of_computing_processors: int | None = Field(
        validation_alias="numOfComputingProcessors",
        serialization_alias="numOfComputingProcessors",
        default=-1,
        description="Set the number of processors which shall be used for the parallel computation.",
    )
    domain_decomposition: OneOf_ComputingCoreDomainDecomposition | None = Field(
        validation_alias="domainDecomposition", serialization_alias="domainDecomposition", default=None
    )
    num_of_threads: int | None = Field(validation_alias="numOfThreads", serialization_alias="numOfThreads", default=1)
    partition_mesh: bool | None = Field(
        validation_alias="partitionMesh", serialization_alias="partitionMesh", default=False
    )
