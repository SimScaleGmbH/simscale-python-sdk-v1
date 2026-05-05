from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SweepMeshingNumberOfElements(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SWEEP_MESHING_NUMBER_OF_ELEMENTS",
        description="Schema name: SweepMeshingNumberOfElements",
    )
    number_of_elements: int | None = Field(
        validation_alias="numberOfElements", serialization_alias="numberOfElements", default=10
    )
