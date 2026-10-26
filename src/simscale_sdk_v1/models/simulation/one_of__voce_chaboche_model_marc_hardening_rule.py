from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.combined_voce_chaboche_hardening_marc import CombinedVoceChabocheHardeningMarc
from simscale_sdk_v1.models.simulation.isotropic_voce_hardening_marc import IsotropicVoceHardeningMarc
from simscale_sdk_v1.models.simulation.kinematic_chaboche_hardening_marc import KinematicChabocheHardeningMarc

# This determines which hardening mechanisms are active for the Voce-Chaboche model; Isotropic expands the yield surface uniformly following a Voce saturation law, Kinematic translates it via one or more superposed Armstrong-Frederick backstresses to capture the Bauschinger effect, and Combined uses both.
_ONE_OF__VOCE_CHABOCHE_MODEL_MARC_HARDENING_RULE_VARIANTS: dict[str, type] = {
    "ISOTROPIC": IsotropicVoceHardeningMarc,
    "KINEMATIC": KinematicChabocheHardeningMarc,
    "COMBINED": CombinedVoceChabocheHardeningMarc,
}

OneOf_VoceChabocheModelMarcHardeningRule = Annotated[
    Union[IsotropicVoceHardeningMarc, KinematicChabocheHardeningMarc, CombinedVoceChabocheHardeningMarc],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VOCE_CHABOCHE_MODEL_MARC_HARDENING_RULE_VARIANTS,
        )
    ),
]
