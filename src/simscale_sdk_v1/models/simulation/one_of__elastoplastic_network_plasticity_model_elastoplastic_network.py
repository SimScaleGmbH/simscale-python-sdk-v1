from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.arruda_boyce_plastic_elastoplastic_network import (
    ArrudaBoycePlasticElastoplasticNetwork,
)
from simscale_sdk_v1.models.simulation.no_elastoplasticity import NoElastoplasticity

# Selecting Arruda-Boyce Plasticity adds a network based on the "eight-chain" statistical model to account for the permanent, rate-independent alignment of molecular chains. This is the preferred choice for modeling the yielding and orientation-hardening behavior of polymers at large strains.
_ONE_OF__ELASTOPLASTIC_NETWORK_PLASTICITY_MODEL_ELASTOPLASTIC_NETWORK_VARIANTS: dict[str, type] = {
    "ARRUDA_BOYCE_PLASTIC": ArrudaBoycePlasticElastoplasticNetwork,
    "OFF": NoElastoplasticity,
}

OneOf_ElastoplasticNetworkPlasticityModelElastoplasticNetwork = Annotated[
    Union[ArrudaBoycePlasticElastoplasticNetwork, NoElastoplasticity],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELASTOPLASTIC_NETWORK_PLASTICITY_MODEL_ELASTOPLASTIC_NETWORK_VARIANTS,
        )
    ),
]
