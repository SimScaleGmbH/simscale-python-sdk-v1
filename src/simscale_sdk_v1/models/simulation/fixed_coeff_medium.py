from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density
from simscale_sdk_v1.models.simulation.dimensional_vector__absorptivity import DimensionalVector_Absorptivity
from simscale_sdk_v1.models.simulation.dimensional_vector__specific_turbulence_dissipation_rate import (
    DimensionalVector_SpecificTurbulenceDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__fixed_coeff_medium_orientation import OneOf_FixedCoeffMediumOrientation
from simscale_sdk_v1.models.simulation.one_of__fixed_coeff_medium_porous_media_heat_transfer import (
    OneOf_FixedCoeffMediumPorousMediaHeatTransfer,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FixedCoeffMedium(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_COEFFICIENTS",
        description="Schema name: FixedCoeffMedium",
    )
    name: str | None = Field(default=None)
    alpha: DimensionalVector_SpecificTurbulenceDissipationRate | None = Field(default=None)
    beta: DimensionalVector_Absorptivity | None = Field(default=None)
    reference_density: Dimensional_Density | None = Field(
        validation_alias="referenceDensity", serialization_alias="referenceDensity", default=None
    )
    orientation: OneOf_FixedCoeffMediumOrientation | None = Field(default=None)
    porous_media_heat_transfer: OneOf_FixedCoeffMediumPorousMediaHeatTransfer | None = Field(
        validation_alias="porousMediaHeatTransfer", serialization_alias="porousMediaHeatTransfer", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
