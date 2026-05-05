from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cauchy_stress_type import CauchyStressType
from simscale_sdk_v1.models.simulation.principal_stress_type import PrincipalStressType
from simscale_sdk_v1.models.simulation.signed_von_mises_stress_type import SignedVonMisesStressType
from simscale_sdk_v1.models.simulation.tresca_stress_type import TrescaStressType
from simscale_sdk_v1.models.simulation.von_mises_stress_type import VonMisesStressType

_ONE_OF__STRESS_FIELD_SELECTION_STRESS_TYPE_VARIANTS: dict[str, type] = {
    "TRESCA": TrescaStressType,
    "CAUCHY": CauchyStressType,
    "PRINCIPAL": PrincipalStressType,
    "VON_MISES": VonMisesStressType,
    "SIGNED_VON_MISES": SignedVonMisesStressType,
}

OneOf_StressFieldSelectionStressType = Annotated[
    Union[TrescaStressType, CauchyStressType, PrincipalStressType, VonMisesStressType, SignedVonMisesStressType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__STRESS_FIELD_SELECTION_STRESS_TYPE_VARIANTS,
        )
    ),
]
