from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__primary_network_damage_model_primary_network import (
    OneOf_PrimaryNetworkDamageModelPrimaryNetwork,
)
from simscale_sdk_v1.models.simulation.yeoh_primary_network import YeohPrimaryNetwork


class PrimaryNetwork(SimScaleModel):
    hyperelastic_model_primary_network: YeohPrimaryNetwork | None = Field(
        validation_alias="hyperelasticModelPrimaryNetwork",
        serialization_alias="hyperelasticModelPrimaryNetwork",
        default=None,
    )
    damage_model_primary_network: OneOf_PrimaryNetworkDamageModelPrimaryNetwork | None = Field(
        validation_alias="damageModelPrimaryNetwork", serialization_alias="damageModelPrimaryNetwork", default=None
    )
