from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__element_technology_definition_method import (
    OneOf_ElementTechnologyDefinitionMethod,
)


class ElementTechnology(SimScaleModel):
    definition_method: OneOf_ElementTechnologyDefinitionMethod | None = Field(
        validation_alias="definitionMethod", serialization_alias="definitionMethod", default=None
    )
