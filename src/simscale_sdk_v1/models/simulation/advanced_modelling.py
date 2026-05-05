from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__advanced_modelling_porous_objects import (
    OneOf_AdvancedModellingPorousObjects,
)
from simscale_sdk_v1.models.simulation.rotating_wall import RotatingWall
from simscale_sdk_v1.models.simulation.surface_roughness_model import SurfaceRoughnessModel


class AdvancedModelling(SimScaleModel):
    surface_roughness_models: list[SurfaceRoughnessModel] | None = Field(
        validation_alias="surfaceRoughnessModels", serialization_alias="surfaceRoughnessModels", default=None
    )
    porous_objects: list[OneOf_AdvancedModellingPorousObjects] | None = Field(
        validation_alias="porousObjects", serialization_alias="porousObjects", default=None
    )
    rotating_walls: list[RotatingWall] | None = Field(
        validation_alias="rotatingWalls", serialization_alias="rotatingWalls", default=None
    )
