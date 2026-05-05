from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class HierarchicalDecomposeAlgorithm(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HIERARCHICAL",
        description="Schema name: HierarchicalDecomposeAlgorithm",
    )
    decomposition_order: Literal["XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"] | None = Field(
        validation_alias="decompositionOrder",
        serialization_alias="decompositionOrder",
        default="XYZ",
        description="Choose the order of domain decomposition .",
    )
    delta: float | None = Field(
        default=0.01,
        description="Delta is cell skew factor. It represents the cell skewness allowed at the decomposed domain boundaries and is generally kept below 10^{-2}. Learn more.",
    )
    num_subdomain_x: int | None = Field(
        validation_alias="numSubdomainX",
        serialization_alias="numSubdomainX",
        default=1,
        description="Define the number of subdomains the mesh is split into in the specific direction.",
    )
    num_subdomain_y: int | None = Field(
        validation_alias="numSubdomainY",
        serialization_alias="numSubdomainY",
        default=1,
        description="Define the number of subdomains the mesh is split into in the specific direction.",
    )
    num_subdomain_z: int | None = Field(
        validation_alias="numSubdomainZ",
        serialization_alias="numSubdomainZ",
        default=1,
        description="Define the number of subdomains the mesh is split into in the specific direction.",
    )
