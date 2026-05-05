from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.contact_conductance_layer import ContactConductanceLayer
from simscale_sdk_v1.models.simulation.contact_resistance_layer import ContactResistanceLayer
from simscale_sdk_v1.models.simulation.thin_resistance_layer import ThinResistanceLayer

_ONE_OF__ADVANCED_CONCEPTS_THERMAL_CONTACT_RESISTANCE_VARIANTS: dict[str, type] = {
    "THIN_RESISTANCE_LAYER": ThinResistanceLayer,
    "CONTACT_RESISTANCE_LAYER": ContactResistanceLayer,
    "CONTACT_CONDUCTANCE_LAYER": ContactConductanceLayer,
}

OneOf_AdvancedConceptsThermalContactResistance = Annotated[
    Union[ThinResistanceLayer, ContactResistanceLayer, ContactConductanceLayer],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_THERMAL_CONTACT_RESISTANCE_VARIANTS,
        )
    ),
]
