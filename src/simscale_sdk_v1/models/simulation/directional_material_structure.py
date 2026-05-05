from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless
from simscale_sdk_v1.models.simulation.one_of__directional_material_structure_mode import (
    OneOf_DirectionalMaterialStructureMode,
)
from simscale_sdk_v1.models.simulation.one_of__directional_material_structure_orientation import (
    OneOf_DirectionalMaterialStructureOrientation,
)


class DirectionalMaterialStructure(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DIRECTIONAL",
        description="Schema name: DirectionalMaterialStructure",
    )
    mode: OneOf_DirectionalMaterialStructureMode | None = Field(default=None)
    direction: DimensionalVector_Dimensionless | None = Field(default=None)
    orientation: OneOf_DirectionalMaterialStructureOrientation | None = Field(default=None)
