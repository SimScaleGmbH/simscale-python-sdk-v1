from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bilinear_elasto_plastic_model import BilinearElastoPlasticModel
from simscale_sdk_v1.models.simulation.johnson_cook_elasto_plastic_model import JohnsonCookElastoPlasticModel
from simscale_sdk_v1.models.simulation.multilinear_elasto_plastic_model import MultilinearElastoPlasticModel

# Choose the Elasto-plastic model for your problem. Important remarks:Choose Bilinear if the material response is a combination of linear elastic and plastic behavior and is defined by the elastic modulus, yield strength, and, tangent modulus.Choose Multilinear if the material response is a combination of linear elastic-plastic behavior and is defined by the elastic modulus, yield strength, and, multiple tangent moduli.Choose Johnson-Cook if the material response includes strain hardening, strain rate hardening, and thermal softening effects, and is defined by parameters such as yield stress, hardening coefficient, hardening exponent, strain rate hardening coefficient, and thermal softening exponent. Learn more
_ONE_OF__PLASTIC_MATERIAL_BEHAVIOR_ELASTO_PLASTIC_MODEL_VARIANTS: dict[str, type] = {
    "BILINEAR": BilinearElastoPlasticModel,
    "MULTILINEAR": MultilinearElastoPlasticModel,
    "JOHNSON_COOK": JohnsonCookElastoPlasticModel,
}

OneOf_PlasticMaterialBehaviorElastoPlasticModel = Annotated[
    Union[BilinearElastoPlasticModel, MultilinearElastoPlasticModel, JohnsonCookElastoPlasticModel],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PLASTIC_MATERIAL_BEHAVIOR_ELASTO_PLASTIC_MODEL_VARIANTS,
        )
    ),
]
