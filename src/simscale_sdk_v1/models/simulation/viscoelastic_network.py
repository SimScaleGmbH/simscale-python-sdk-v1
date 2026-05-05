from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__viscoelastic_network_creep_model_viscoelastic_network import (
    OneOf_ViscoelasticNetworkCreepModelViscoelasticNetwork,
)


class ViscoelasticNetwork(SimScaleModel):
    creep_model_viscoelastic_network: OneOf_ViscoelasticNetworkCreepModelViscoelasticNetwork | None = Field(
        validation_alias="creepModelViscoelasticNetwork",
        serialization_alias="creepModelViscoelasticNetwork",
        default=None,
    )
