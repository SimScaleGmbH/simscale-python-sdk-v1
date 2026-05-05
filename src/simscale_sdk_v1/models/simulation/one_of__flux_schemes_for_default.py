from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.kurganov_flux_scheme import KurganovFluxScheme
from simscale_sdk_v1.models.simulation.tadmor_flux_scheme import TadmorFluxScheme

_ONE_OF__FLUX_SCHEMES_FOR_DEFAULT_VARIANTS: dict[str, type] = {
    "TADMOR": TadmorFluxScheme,
    "KURGANOV": KurganovFluxScheme,
}

OneOf_FluxSchemesForDefault = Annotated[
    Union[TadmorFluxScheme, KurganovFluxScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUX_SCHEMES_FOR_DEFAULT_VARIANTS,
        )
    ),
]
