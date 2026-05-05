from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__coil_coil_type import OneOf_CoilCoilType
from simscale_sdk_v1.models.simulation.one_of__coil_excitation import OneOf_CoilExcitation
from simscale_sdk_v1.models.simulation.one_of__coil_topology import OneOf_CoilTopology


class Coil(SimScaleModel):
    name: str | None = Field(default=None)
    topology: OneOf_CoilTopology | None = Field(default=None)
    coil_type: OneOf_CoilCoilType | None = Field(
        validation_alias="coilType", serialization_alias="coilType", default=None
    )
    excitation: OneOf_CoilExcitation | None = Field(default=None)
