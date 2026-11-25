from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_marc_conductivity import IsotropicMarcConductivity
from simscale_sdk_v1.models.simulation.orthotropic_marc_conductivity import OrthotropicMarcConductivity

_ONE_OF__MARC_THERMAL_PROPERTIES_CONDUCTIVITY_VARIANTS: dict[str, type] = {
    "ISOTROPIC": IsotropicMarcConductivity,
    "ORTHOTROPIC": OrthotropicMarcConductivity,
}

OneOf_MarcThermalPropertiesConductivity = Annotated[
    Union[IsotropicMarcConductivity, OrthotropicMarcConductivity],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_THERMAL_PROPERTIES_CONDUCTIVITY_VARIANTS,
        )
    ),
]
