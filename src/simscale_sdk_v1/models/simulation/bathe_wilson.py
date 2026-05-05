from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__bathe_wilson_subspace_settings import OneOf_BatheWilsonSubspaceSettings


class BatheWilson(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="JACOBI", description="Schema name: BatheWilson"
    )
    prec_bathe: float | None = Field(validation_alias="precBathe", serialization_alias="precBathe", default=1e-10)
    nmax_iter_bathe: int | None = Field(
        validation_alias="nmaxIterBathe", serialization_alias="nmaxIterBathe", default=40
    )
    prec_jacobi: float | None = Field(validation_alias="precJacobi", serialization_alias="precJacobi", default=0.01)
    max_iter_jacobi: int | None = Field(
        validation_alias="maxIterJacobi", serialization_alias="maxIterJacobi", default=12
    )
    subspace_settings: OneOf_BatheWilsonSubspaceSettings | None = Field(
        validation_alias="subspaceSettings", serialization_alias="subspaceSettings", default=None
    )
