from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of_iram_sorensen_subspace_settings import OneOf_IRAMSorensenSubspaceSettings


class IRAMSorensen(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="SORENSEN", description="Schema name: IRAMSorensen"
    )
    prec_soren: float | None = Field(validation_alias="precSoren", serialization_alias="precSoren", default=0.0)
    nmax_iter_soren: int | None = Field(
        validation_alias="nmaxIterSoren", serialization_alias="nmaxIterSoren", default=20
    )
    subspace_settings: OneOf_IRAMSorensenSubspaceSettings | None = Field(
        validation_alias="subspaceSettings", serialization_alias="subspaceSettings", default=None
    )
