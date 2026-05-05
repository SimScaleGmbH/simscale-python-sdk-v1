from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__area import Dimensional_Area
from simscale_sdk_v1.models.simulation.one_of__darcy_medium_porous_material_type import (
    OneOf_DarcyMediumPorousMaterialType,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class DarcyMedium(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="DARCY", description="Schema name: DarcyMedium"
    )
    name: str | None = Field(default=None)
    porosity: float | None = Field(
        default=1,
        description="Porosity is the fraction of a volume of material is that is void. It ranges from φ = 1 (completely empty) to φ = 0 (completely solid).",
    )
    permeability: Dimensional_Area | None = Field(default=None)
    drag_coefficient: float | None = Field(
        validation_alias="dragCoefficient",
        serialization_alias="dragCoefficient",
        default=0,
        description="The Darcy law may be extended to include the Forchheimer drag term for more inertial flows (Re > 10). This term is quadratic in flow velocity. Its coefficient includes the fluid drag coefficient Cd.",
    )
    porous_material_type: OneOf_DarcyMediumPorousMaterialType | None = Field(
        validation_alias="porousMaterialType", serialization_alias="porousMaterialType", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
