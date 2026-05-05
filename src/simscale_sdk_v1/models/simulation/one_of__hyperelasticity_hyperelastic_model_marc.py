from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marlow_hyperelastic_model_marc import MarlowHyperelasticModelMarc
from simscale_sdk_v1.models.simulation.mooney_type_hyperelastic_model_marc import MooneyTypeHyperelasticModelMarc
from simscale_sdk_v1.models.simulation.ogden_hyperelastic_model_marc import OgdenHyperelasticModelMarc

# Mooney: Mooney (or Mooney-Rivlin) is a very common phenomenological model used for modeling the behavior of rubber-like materials at moderate strains (up to ~100%). It is based on a linear combination of two strain invariants, making it computationally stable for simpler elastomeric applications.Ogden: A high-fidelity model that describes the strain energy density as a function of principal stretches rather than invariants. It is highly flexible and capable of capturing complex material behavior at very large strain levels.Marlow: A general-purpose model that allows the strain energy density function to be constructed directly from experimental test data. It is particularly useful when only one type of test data (e.g., uniaxial tension) is available to characterize the material.
_ONE_OF__HYPERELASTICITY_HYPERELASTIC_MODEL_MARC_VARIANTS: dict[str, type] = {
    "MOONEY_TYPE_MARC": MooneyTypeHyperelasticModelMarc,
    "OGDEN_MARC": OgdenHyperelasticModelMarc,
    "MARLOW_MARC": MarlowHyperelasticModelMarc,
}

OneOf_HyperelasticityHyperelasticModelMarc = Annotated[
    Union[MooneyTypeHyperelasticModelMarc, OgdenHyperelasticModelMarc, MarlowHyperelasticModelMarc],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HYPERELASTICITY_HYPERELASTIC_MODEL_MARC_VARIANTS,
        )
    ),
]
