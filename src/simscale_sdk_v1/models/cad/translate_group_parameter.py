from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.vector_with_unit import VectorWithUnit


class TranslateGroupParameter(SimScaleModel):
    """Translation method."""

    selected: Literal["translate_to_entity", "translate_vector"] = Field(
        description="Defines the parameter set used to define the extrusion. It can be either: - `translate_vector`, in which case the translation distance and direction will be provided, or - `translate_to_entity`, in which case the translation distance and direction will be computed based on the provided face."
    )
    translation_vector: VectorWithUnit | None = Field(default=None)
    translation_face: str | None = Field(default=None, description="Face limiting the translation.")
