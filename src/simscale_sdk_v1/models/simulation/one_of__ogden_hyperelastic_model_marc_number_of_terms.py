from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.one_term import OneTerm
from simscale_sdk_v1.models.simulation.three_terms import ThreeTerms
from simscale_sdk_v1.models.simulation.two_terms import TwoTerms

# Number of terms defines the number of principal stretch power-law terms (up to 3) used to fit the material curve. Increasing the number of terms allows the model to more accurately capture highly non-linear experimental data across larger strain ranges.
_ONE_OF__OGDEN_HYPERELASTIC_MODEL_MARC_NUMBER_OF_TERMS_VARIANTS: dict[str, type] = {
    "ONE_TERM": OneTerm,
    "TWO_TERMS": TwoTerms,
    "THREE_TERMS": ThreeTerms,
}

OneOf_OgdenHyperelasticModelMarcNumberOfTerms = Annotated[
    Union[OneTerm, TwoTerms, ThreeTerms],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__OGDEN_HYPERELASTIC_MODEL_MARC_NUMBER_OF_TERMS_VARIANTS,
        )
    ),
]
