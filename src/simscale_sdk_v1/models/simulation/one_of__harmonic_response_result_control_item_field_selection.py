from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.acceleration_field_selection import AccelerationFieldSelection
from simscale_sdk_v1.models.simulation.displacement_field_selection import DisplacementFieldSelection
from simscale_sdk_v1.models.simulation.strain_field_selection import StrainFieldSelection
from simscale_sdk_v1.models.simulation.stress_field_selection import StressFieldSelection
from simscale_sdk_v1.models.simulation.velocity_field_selection import VelocityFieldSelection

_ONE_OF__HARMONIC_RESPONSE_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "DISPLACEMENT": DisplacementFieldSelection,
    "STRAIN": StrainFieldSelection,
    "STRESS": StressFieldSelection,
    "VELOCITY": VelocityFieldSelection,
    "ACCELERATION": AccelerationFieldSelection,
}

OneOf_HarmonicResponseResultControlItemFieldSelection = Annotated[
    Union[
        DisplacementFieldSelection,
        StrainFieldSelection,
        StressFieldSelection,
        VelocityFieldSelection,
        AccelerationFieldSelection,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HARMONIC_RESPONSE_RESULT_CONTROL_ITEM_FIELD_SELECTION_VARIANTS,
        )
    ),
]
