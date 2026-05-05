from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.first_order_ogden import FirstOrderOgden
from simscale_sdk_v1.models.simulation.second_order_ogden import SecondOrderOgden
from simscale_sdk_v1.models.simulation.third_order_ogden import ThirdOrderOgden

# Number of terms in the Ogden model.
_ONE_OF__OGDEN_HYPER_ELASTIC_MODEL_ORDER_VARIANTS: dict[str, type] = {
    "FIRST_ORDER_OGDEN": FirstOrderOgden,
    "SECOND_ORDER_OGDEN": SecondOrderOgden,
    "THIRD_ORDER_OGDEN": ThirdOrderOgden,
}

OneOf_OgdenHyperElasticModelOrder = Annotated[
    Union[FirstOrderOgden, SecondOrderOgden, ThirdOrderOgden],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__OGDEN_HYPER_ELASTIC_MODEL_ORDER_VARIANTS,
        )
    ),
]
