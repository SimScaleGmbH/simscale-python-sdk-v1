from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_comfort_criterion_settings import AdvancedComfortCriterionSettings
from simscale_sdk_v1.models.simulation.comfort_criterion_definition_v2 import ComfortCriterionDefinitionV2


class CustomComfortCriterionResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_COMFORT_CRITERION",
        description="Schema name: CustomComfortCriterionResultControl",
    )
    name: str | None = Field(default=None)
    comfort_criterion_definition_v2: ComfortCriterionDefinitionV2 | None = Field(
        validation_alias="comfortCriterionDefinitionV2",
        serialization_alias="comfortCriterionDefinitionV2",
        default=None,
    )
    out_of_bounds_name: str | None = Field(
        validation_alias="outOfBoundsName",
        serialization_alias="outOfBoundsName",
        default="Uncomfortable",
        description="It defines the name of the category that is reached if all defined criteria are exceeded.",
    )
    advanced_settings: AdvancedComfortCriterionSettings | None = Field(
        validation_alias="advancedSettings", serialization_alias="advancedSettings", default=None
    )
