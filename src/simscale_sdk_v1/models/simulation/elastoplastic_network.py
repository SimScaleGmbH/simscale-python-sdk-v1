from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__elastoplastic_network_plasticity_model_elastoplastic_network import (
    OneOf_ElastoplasticNetworkPlasticityModelElastoplasticNetwork,
)


class ElastoplasticNetwork(SimScaleModel):
    plasticity_model_elastoplastic_network: OneOf_ElastoplasticNetworkPlasticityModelElastoplasticNetwork | None = (
        Field(
            validation_alias="plasticityModelElastoplasticNetwork",
            serialization_alias="plasticityModelElastoplasticNetwork",
            default=None,
        )
    )
