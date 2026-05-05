from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.principal_green_lagrange_strain_type import PrincipalGreenLagrangeStrainType
from simscale_sdk_v1.models.simulation.principal_strain_type import PrincipalStrainType
from simscale_sdk_v1.models.simulation.total_equivalent_plastic_strain_type import TotalEquivalentPlasticStrainType
from simscale_sdk_v1.models.simulation.total_linear_strain_type import TotalLinearStrainType
from simscale_sdk_v1.models.simulation.total_non_linear_strain_type import TotalNonLinearStrainType
from simscale_sdk_v1.models.simulation.unelastic_strain_type import UnelasticStrainType

_ONE_OF__STRAIN_FIELD_SELECTION_STRAIN_TYPE_VARIANTS: dict[str, type] = {
    "TOTAL_LINEAR": TotalLinearStrainType,
    "TOTAL_NONLINEAR": TotalNonLinearStrainType,
    "TOTAL_EQUI_PLASTIC": TotalEquivalentPlasticStrainType,
    "UNELASTIC": UnelasticStrainType,
    "PRINCIPAL": PrincipalStrainType,
    "PRINCIPAL_GREEN_LAGRANGE": PrincipalGreenLagrangeStrainType,
}

OneOf_StrainFieldSelectionStrainType = Annotated[
    Union[
        TotalLinearStrainType,
        TotalNonLinearStrainType,
        TotalEquivalentPlasticStrainType,
        UnelasticStrainType,
        PrincipalStrainType,
        PrincipalGreenLagrangeStrainType,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__STRAIN_FIELD_SELECTION_STRAIN_TYPE_VARIANTS,
        )
    ),
]
