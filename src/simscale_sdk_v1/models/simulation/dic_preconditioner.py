from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DICPreconditioner(SimScaleModel):
    """Diagonal incomplete Cholesky algorithm for symmetric matrices without fill-in."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DIC",
        description="Diagonal incomplete Cholesky algorithm for symmetric matrices without fill-in.  Schema name: DICPreconditioner",
    )
