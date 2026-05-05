from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ILUCpPreconditioner(SimScaleModel):
    """Crout's version of the incomplete lower-upper (ILU) algorithm with arbitrary level of fill-in."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ILUCP",
        description="Crout's version of the incomplete lower-upper (ILU) algorithm with arbitrary level of fill-in.  Schema name: ILUCpPreconditioner",
    )
    fill_in_level: int | None = Field(
        validation_alias="fillInLevel",
        serialization_alias="fillInLevel",
        default=1,
        description="Number of face-neighbour layers to fill in. Increasing the level of fill-in improves the performance of preconditioner at the expense of computational overhead.",
    )
