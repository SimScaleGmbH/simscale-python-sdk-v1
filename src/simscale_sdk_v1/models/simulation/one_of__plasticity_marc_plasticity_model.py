from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bilinear_model_marc import BilinearModelMarc
from simscale_sdk_v1.models.simulation.multilinear_model_marc import MultilinearModelMarc

# This setting defines how the post-yield behavior is mathematically represented; Bilinear uses a single tangent modulus for simplified hardening, while Multilinear allows for a precise fit of experimental data points.
_ONE_OF__PLASTICITY_MARC_PLASTICITY_MODEL_VARIANTS: dict[str, type] = {
    "BILINEAR": BilinearModelMarc,
    "MULTILINEAR": MultilinearModelMarc,
}

OneOf_PlasticityMarcPlasticityModel = Annotated[
    Union[BilinearModelMarc, MultilinearModelMarc],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PLASTICITY_MARC_PLASTICITY_MODEL_VARIANTS,
        )
    ),
]
