from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DILUPreconditioner(SimScaleModel):
    """Diagonal incomplete lower-upper (ILU) algorithm for non-symmetric matrices without fill-in."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DILU",
        description="Diagonal incomplete lower-upper (ILU) algorithm for non-symmetric matrices without fill-in.  Schema name: DILUPreconditioner",
    )
