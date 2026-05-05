from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_domain_decomposition import AutomaticDomainDecomposition
from simscale_sdk_v1.models.simulation.centralized_domain_decomposition import CentralizedDomainDecomposition
from simscale_sdk_v1.models.simulation.custom_domain_decomposition import CustomDomainDecomposition
from simscale_sdk_v1.models.simulation.element_groups_domain_decomposition import ElementGroupsDomainDecomposition

_ONE_OF__COMPUTING_CORE_DOMAIN_DECOMPOSITION_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticDomainDecomposition,
    "CENTRALIZED": CentralizedDomainDecomposition,
    "ELEMENT_GROUPS": ElementGroupsDomainDecomposition,
    "CUSTOM": CustomDomainDecomposition,
}

OneOf_ComputingCoreDomainDecomposition = Annotated[
    Union[
        AutomaticDomainDecomposition,
        CentralizedDomainDecomposition,
        ElementGroupsDomainDecomposition,
        CustomDomainDecomposition,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__COMPUTING_CORE_DOMAIN_DECOMPOSITION_VARIANTS,
        )
    ),
]
