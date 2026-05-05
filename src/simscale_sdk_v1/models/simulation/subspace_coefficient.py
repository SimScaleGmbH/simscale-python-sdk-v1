from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SubspaceCoefficient(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SUBSPACE_COEFFICIENT",
        description="Schema name: SubspaceCoefficient",
    )
    subspace_coefficient: int | None = Field(
        validation_alias="subspaceCoefficient",
        serialization_alias="subspaceCoefficient",
        default=None,
        description="Choose a coefficient (css) with which the subspace dimension (dss) is calculated, depending on the number of computed frequencies (nf): IRAM Sorensen: dss = max(2 + nf , css * nf).Lanczos & Bathe - Wilson: dss = max(7 + nf , css * nf).",
    )
