from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.acceleration_field_selection import AccelerationFieldSelection
from simscale_sdk_v1.models.simulation.contact_field_selection import ContactFieldSelection
from simscale_sdk_v1.models.simulation.displacement_field_selection import DisplacementFieldSelection
from simscale_sdk_v1.models.simulation.force_field_selection import ForceFieldSelection
from simscale_sdk_v1.models.simulation.heat_flux_field_selection import HeatFluxFieldSelection
from simscale_sdk_v1.models.simulation.strain_field_selection import StrainFieldSelection
from simscale_sdk_v1.models.simulation.stress_field_selection import StressFieldSelection
from simscale_sdk_v1.models.simulation.temperature_field_selection import TemperatureFieldSelection
from simscale_sdk_v1.models.simulation.velocity_field_selection import VelocityFieldSelection

_ONE_OF__AVERAGE_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "DISPLACEMENT": DisplacementFieldSelection,
    "FORCE": ForceFieldSelection,
    "CONTACT": ContactFieldSelection,
    "STRAIN": StrainFieldSelection,
    "STRESS": StressFieldSelection,
    "VELOCITY": VelocityFieldSelection,
    "ACCELERATION": AccelerationFieldSelection,
    "TEMPERATURE": TemperatureFieldSelection,
    "HEAT_FLUX": HeatFluxFieldSelection,
}

OneOf_AverageFieldsCalculationResultControlItemFieldSelection = Annotated[
    Union[
        DisplacementFieldSelection,
        ForceFieldSelection,
        ContactFieldSelection,
        StrainFieldSelection,
        StressFieldSelection,
        VelocityFieldSelection,
        AccelerationFieldSelection,
        TemperatureFieldSelection,
        HeatFluxFieldSelection,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__AVERAGE_FIELDS_CALCULATION_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS,
        )
    ),
]
