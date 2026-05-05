from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.no_damage import NoDamage
from simscale_sdk_v1.models.simulation.ogden_roxburgh import OgdenRoxburgh

# This setting activates the Ogden-Roxburgh (pseudo-elastic) model to simulate the Mullins effect, where the material undergoes significant softening during the first loading cycle. It is used to capture energy dissipation and the permanent loss of stiffness common in filled elastomers and many thermoplastics.
_ONE_OF__PRIMARY_NETWORK_DAMAGE_MODEL_PRIMARY_NETWORK_VARIANTS: dict[str, type] = {
    "OGDEN_ROXBURGH": OgdenRoxburgh,
    "OFF": NoDamage,
}

OneOf_PrimaryNetworkDamageModelPrimaryNetwork = Annotated[
    Union[OgdenRoxburgh, NoDamage],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PRIMARY_NETWORK_DAMAGE_MODEL_PRIMARY_NETWORK_VARIANTS,
        )
    ),
]
