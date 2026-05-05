from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.gauss_interface_compression_divergence_scheme import (
    GaussInterfaceCompressionDivergenceScheme,
)
from simscale_sdk_v1.models.simulation.gauss_vanleer_divergence_scheme import GaussVanleerDivergenceScheme

# With this option, you can choose your desired divergence scheme.
_ONE_OF__DIVERGENCE_SCHEMES_DIV_PHIRB_ALPHA_VARIANTS: dict[str, type] = {
    "GAUSS_VANLEER": GaussVanleerDivergenceScheme,
    "GAUSS_INTERFACECOMPRESSION": GaussInterfaceCompressionDivergenceScheme,
}

OneOf_DivergenceSchemesDiv_phirb_alpha = Annotated[
    Union[GaussVanleerDivergenceScheme, GaussInterfaceCompressionDivergenceScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIVERGENCE_SCHEMES_DIV_PHIRB_ALPHA_VARIANTS,
        )
    ),
]
