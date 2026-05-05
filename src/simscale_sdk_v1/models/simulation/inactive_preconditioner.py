from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class InactivePreconditioner(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INACTIVE",
        description="Schema name: InactivePreconditioner",
    )
    renumbering_method: Literal["RCMK", "INACTIVE"] | None = Field(
        validation_alias="renumberingMethod",
        serialization_alias="renumberingMethod",
        default="INACTIVE",
        description="Choose the renumbering method for the system matrix entries:RCMK uses the algorithm of Reverse Cuthill-MacKee for the renumbering. It often effectively reduces the matrig storage space and the matrix factorization time.When inactive is selected no renumbering is done. This option should only be chosen for testing purposes.",
    )
