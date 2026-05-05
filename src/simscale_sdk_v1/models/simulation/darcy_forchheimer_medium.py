from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__absorptivity import DimensionalVector_Absorptivity
from simscale_sdk_v1.models.simulation.dimensional_vector__reciprocal_permeability import (
    DimensionalVector_ReciprocalPermeability,
)
from simscale_sdk_v1.models.simulation.one_of__darcy_forchheimer_medium_orientation import (
    OneOf_DarcyForchheimerMediumOrientation,
)
from simscale_sdk_v1.models.simulation.one_of__darcy_forchheimer_medium_porous_media_heat_transfer import (
    OneOf_DarcyForchheimerMediumPorousMediaHeatTransfer,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class DarcyForchheimerMedium(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DARCY_FORCHHEIMER",
        description="Schema name: DarcyForchheimerMedium",
    )
    name: str | None = Field(default=None)
    coefficient_d: DimensionalVector_ReciprocalPermeability | None = Field(
        validation_alias="coefficientD", serialization_alias="coefficientD", default=None
    )
    coefficient_f: DimensionalVector_Absorptivity | None = Field(
        validation_alias="coefficientF", serialization_alias="coefficientF", default=None
    )
    orientation: OneOf_DarcyForchheimerMediumOrientation | None = Field(default=None)
    porous_media_heat_transfer: OneOf_DarcyForchheimerMediumPorousMediaHeatTransfer | None = Field(
        validation_alias="porousMediaHeatTransfer", serialization_alias="porousMediaHeatTransfer", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
