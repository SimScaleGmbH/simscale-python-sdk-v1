from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.no_creep import NoCreep
from simscale_sdk_v1.models.simulation.prony_series import PronySeries

# By selecting the Prony series, you enable a viscoelastic network that models time-dependent behavior such as stress relaxation and creep. This model uses a series of decay constants (relaxation times) to define how the material's internal stresses dissipate over time under sustained loading.
_ONE_OF__VISCOELASTIC_NETWORK_CREEP_MODEL_VISCOELASTIC_NETWORK_VARIANTS: dict[str, type] = {
    "PRONY_SERIES": PronySeries,
    "OFF": NoCreep,
}

OneOf_ViscoelasticNetworkCreepModelViscoelasticNetwork = Annotated[
    Union[PronySeries, NoCreep],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VISCOELASTIC_NETWORK_CREEP_MODEL_VISCOELASTIC_NETWORK_VARIANTS,
        )
    ),
]
