from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__lanczos_subspace_settings import OneOf_LanczosSubspaceSettings


class Lanczos(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="TRI_DIAG", description="Schema name: Lanczos"
    )
    prec_ortho: float | None = Field(validation_alias="precOrtho", serialization_alias="precOrtho", default=1e-12)
    nmax_iter_ortho: int | None = Field(
        validation_alias="nmaxIterOrtho", serialization_alias="nmaxIterOrtho", default=5
    )
    prec_lanczos: float | None = Field(validation_alias="precLanczos", serialization_alias="precLanczos", default=1e-08)
    max_iter_qr: int | None = Field(validation_alias="maxIterQR", serialization_alias="maxIterQR", default=30)
    mode_rigid: bool | None = Field(validation_alias="modeRigid", serialization_alias="modeRigid", default=True)
    subspace_settings: OneOf_LanczosSubspaceSettings | None = Field(
        validation_alias="subspaceSettings", serialization_alias="subspaceSettings", default=None
    )
