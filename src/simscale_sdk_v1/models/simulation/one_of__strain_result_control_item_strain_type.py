from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.global_principal_green_lagrange_strain_type import (
    GlobalPrincipalGreenLagrangeStrainType,
)
from simscale_sdk_v1.models.simulation.global_principal_strain_type import GlobalPrincipalStrainType
from simscale_sdk_v1.models.simulation.global_total_equivalent_plastic_strain_type import (
    GlobalTotalEquivalentPlasticStrainType,
)
from simscale_sdk_v1.models.simulation.global_total_nonlinear_strain_type import GlobalTotalNonlinearStrainType
from simscale_sdk_v1.models.simulation.global_total_strain_type import GlobalTotalStrainType
from simscale_sdk_v1.models.simulation.global_unelastic_strain_type import GlobalUnelasticStrainType

_ONE_OF__STRAIN_RESULT_CONTROL_ITEM_STRAIN_TYPE_VARIANTS: dict[str, type] = {
    "TOTAL_NONLINEAR": GlobalTotalNonlinearStrainType,
    "TOTAL_EQUI_PLASTIC": GlobalTotalEquivalentPlasticStrainType,
    "UNELASTIC": GlobalUnelasticStrainType,
    "TOTAL": GlobalTotalStrainType,
    "PRINCIPAL": GlobalPrincipalStrainType,
    "PRINCIPAL_GREEN_LAGRANGE": GlobalPrincipalGreenLagrangeStrainType,
}

OneOf_StrainResultControlItemStrainType = Annotated[
    Union[
        GlobalTotalNonlinearStrainType,
        GlobalTotalEquivalentPlasticStrainType,
        GlobalUnelasticStrainType,
        GlobalTotalStrainType,
        GlobalPrincipalStrainType,
        GlobalPrincipalGreenLagrangeStrainType,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__STRAIN_RESULT_CONTROL_ITEM_STRAIN_TYPE_VARIANTS,
        )
    ),
]
