from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.global_cauchy_stress_type import GlobalCauchyStressType
from simscale_sdk_v1.models.simulation.global_max_over_phase_von_mises_stress_type import (
    GlobalMaxOverPhaseVonMisesStressType,
)
from simscale_sdk_v1.models.simulation.global_principal_stress_type import GlobalPrincipalStressType
from simscale_sdk_v1.models.simulation.global_signed_von_mises_stress_type import GlobalSignedVonMisesStressType
from simscale_sdk_v1.models.simulation.global_tresca_stress_type import GlobalTrescaStressType
from simscale_sdk_v1.models.simulation.global_von_mises_stress_type import GlobalVonMisesStressType

_ONE_OF__STRESS_RESULT_CONTROL_ITEM_STRESS_TYPE_VARIANTS: dict[str, type] = {
    "TRESCA": GlobalTrescaStressType,
    "CAUCHY": GlobalCauchyStressType,
    "PRINCIPAL": GlobalPrincipalStressType,
    "VON_MISES": GlobalVonMisesStressType,
    "MAX_OVER_PHASE_VON_MISES": GlobalMaxOverPhaseVonMisesStressType,
    "SIGNED_VON_MISES": GlobalSignedVonMisesStressType,
}

OneOf_StressResultControlItemStressType = Annotated[
    Union[
        GlobalTrescaStressType,
        GlobalCauchyStressType,
        GlobalPrincipalStressType,
        GlobalVonMisesStressType,
        GlobalMaxOverPhaseVonMisesStressType,
        GlobalSignedVonMisesStressType,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__STRESS_RESULT_CONTROL_ITEM_STRESS_TYPE_VARIANTS,
        )
    ),
]
