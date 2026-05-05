from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.combined_plastic_hardening_marc import CombinedPlasticHardeningMarc
from simscale_sdk_v1.models.simulation.isotropic_plastic_hardening_marc import IsotropicPlasticHardeningMarc
from simscale_sdk_v1.models.simulation.kinematic_plastic_hardening_marc import KinematicPlasticHardeningMarc

# This determines how the yield surface evolves during cyclic loading; Isotropic expands the surface uniformly, Kinematic shifts it to account for the Bauschinger effect, and Combined utilizes both behaviors for maximum accuracy.
_ONE_OF__MULTILINEAR_MODEL_MARC_HARDENING_RULE_VARIANTS: dict[str, type] = {
    "ISOTROPIC": IsotropicPlasticHardeningMarc,
    "KINEMATIC": KinematicPlasticHardeningMarc,
    "COMBINED": CombinedPlasticHardeningMarc,
}

OneOf_MultilinearModelMarcHardeningRule = Annotated[
    Union[IsotropicPlasticHardeningMarc, KinematicPlasticHardeningMarc, CombinedPlasticHardeningMarc],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MULTILINEAR_MODEL_MARC_HARDENING_RULE_VARIANTS,
        )
    ),
]
