from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.one_backstress_term import OneBackstressTerm
from simscale_sdk_v1.models.simulation.three_backstress_terms import ThreeBackstressTerms
from simscale_sdk_v1.models.simulation.two_backstress_terms import TwoBackstressTerms

# The number of superposed Armstrong-Frederick backstress terms used to represent the kinematic hardening. Additional terms allow a more accurate fit of the material's hardening behavior under cyclic and non-proportional loading, at the cost of more material parameters to calibrate.
_ONE_OF__COMBINED_VOCE_CHABOCHE_HARDENING_MARC_BACKSTRESS_TERMS_VARIANTS: dict[str, type] = {
    "ONE_TERM": OneBackstressTerm,
    "TWO_TERMS": TwoBackstressTerms,
    "THREE_TERMS": ThreeBackstressTerms,
}

OneOf_CombinedVoceChabocheHardeningMarcBackstressTerms = Annotated[
    Union[OneBackstressTerm, TwoBackstressTerms, ThreeBackstressTerms],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__COMBINED_VOCE_CHABOCHE_HARDENING_MARC_BACKSTRESS_TERMS_VARIANTS,
        )
    ),
]
