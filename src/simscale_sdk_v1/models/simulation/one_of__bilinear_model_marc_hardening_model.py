from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.perfect_plasticity_model_marc import PerfectPlasticityModelMarc
from simscale_sdk_v1.models.simulation.strain_hardening_model_marc import StrainHardeningModelMarc

# Choose Perfectly plastic if the material maintains a constant stress level after yielding, or Strain hardening if the material's strength increases as it undergoes further plastic deformation.
_ONE_OF__BILINEAR_MODEL_MARC_HARDENING_MODEL_VARIANTS: dict[str, type] = {
    "PERFECT_PLASTICITY": PerfectPlasticityModelMarc,
    "STRAIN_HARDENING": StrainHardeningModelMarc,
}

OneOf_BilinearModelMarcHardeningModel = Annotated[
    Union[PerfectPlasticityModelMarc, StrainHardeningModelMarc],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__BILINEAR_MODEL_MARC_HARDENING_MODEL_VARIANTS,
        )
    ),
]
