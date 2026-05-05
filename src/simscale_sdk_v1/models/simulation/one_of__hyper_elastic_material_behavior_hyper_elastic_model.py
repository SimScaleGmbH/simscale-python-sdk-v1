from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.mooney_rivlin_hyper_elastic_model import MooneyRivlinHyperElasticModel
from simscale_sdk_v1.models.simulation.neo_hooke_hyper_elastic_model import NeoHookeHyperElasticModel
from simscale_sdk_v1.models.simulation.ogden_hyper_elastic_model import OgdenHyperElasticModel
from simscale_sdk_v1.models.simulation.signorini_hyper_elastic_model import SignoriniHyperElasticModel
from simscale_sdk_v1.models.simulation.yeoh_hyper_elastic_model import YeohHyperElasticModel

# Choose the hyperelastic material model that should be used. All models derive the stress-strain relation from a strain energy function defined by the material model parameters.
_ONE_OF__HYPER_ELASTIC_MATERIAL_BEHAVIOR_HYPER_ELASTIC_MODEL_VARIANTS: dict[str, type] = {
    "MOONEY_RIVLIN": MooneyRivlinHyperElasticModel,
    "NEO_HOOKE": NeoHookeHyperElasticModel,
    "SIGNORINI": SignoriniHyperElasticModel,
    "YEOH": YeohHyperElasticModel,
    "OGDEN": OgdenHyperElasticModel,
}

OneOf_HyperElasticMaterialBehaviorHyperElasticModel = Annotated[
    Union[
        MooneyRivlinHyperElasticModel,
        NeoHookeHyperElasticModel,
        SignoriniHyperElasticModel,
        YeohHyperElasticModel,
        OgdenHyperElasticModel,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HYPER_ELASTIC_MATERIAL_BEHAVIOR_HYPER_ELASTIC_MODEL_VARIANTS,
        )
    ),
]
