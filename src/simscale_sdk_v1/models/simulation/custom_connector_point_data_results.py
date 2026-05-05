from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CustomConnectorPointDataResults(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM",
        description="Schema name: CustomConnectorPointDataResults",
    )
    displacements: bool | None = Field(default=False)
    rotations: bool | None = Field(default=False)
    reaction_forces: bool | None = Field(
        validation_alias="reactionForces", serialization_alias="reactionForces", default=False
    )
    reaction_moments: bool | None = Field(
        validation_alias="reactionMoments", serialization_alias="reactionMoments", default=False
    )
    external_forces: bool | None = Field(
        validation_alias="externalForces", serialization_alias="externalForces", default=False
    )
    external_moments: bool | None = Field(
        validation_alias="externalMoments", serialization_alias="externalMoments", default=False
    )
