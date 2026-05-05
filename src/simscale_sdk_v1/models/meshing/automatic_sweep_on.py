from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AutomaticSweepOn(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC_SWEEP_MESHING_ON",
        description="Schema name: AutomaticSweepOn",
    )
    maximum_number_of_layers: int | None = Field(
        validation_alias="maximumNumberOfLayers", serialization_alias="maximumNumberOfLayers", default=500
    )
    minimum_number_of_layers: int | None = Field(
        validation_alias="minimumNumberOfLayers", serialization_alias="minimumNumberOfLayers", default=2
    )
    surface_element_type: Literal["TRIANGULAR", "QUADDOMINANT"] | None = Field(
        validation_alias="surfaceElementType", serialization_alias="surfaceElementType", default="QUADDOMINANT"
    )
    extrusion_direction: Literal["SHORTEST", "LONGEST"] | None = Field(
        validation_alias="extrusionDirection",
        serialization_alias="extrusionDirection",
        default="SHORTEST",
        description="If a part can be extruded along multiple directions, choose whether to extrude along the shortest or the longest direction (e.g. a simple plate can be extruded along its thickness or the other two dimensions. Choose Shortest to extrude across the thickness).",
    )
