from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.perfect_plasticity_model import PerfectPlasticityModel
from simscale_sdk_v1.models.simulation.strain_hardening_model import StrainHardeningModel

# Choose the hardening model for your problem. Important remarks: Choose Strain Hardening if the material response is a combination of linear elastic and plastic hardening behavior, where the material becomes progressively stiffer with increasing strain.Choose Perfect Plasticity if the material response is a combination of linear elastic and perfect plastic hardening behavior (constant stress for applied strain). Learn more
_ONE_OF__BILINEAR_ELASTO_PLASTIC_MODEL_HARDENING_MODEL_VARIANTS: dict[str, type] = {
    "STRAIN_HARDENING": StrainHardeningModel,
    "PERFECT_PLASTICITY": PerfectPlasticityModel,
}

OneOf_BilinearElastoPlasticModelHardeningModel = Annotated[
    Union[StrainHardeningModel, PerfectPlasticityModel],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__BILINEAR_ELASTO_PLASTIC_MODEL_HARDENING_MODEL_VARIANTS,
        )
    ),
]
