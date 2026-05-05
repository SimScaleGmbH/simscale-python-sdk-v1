from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.darcy_forchheimer_medium import DarcyForchheimerMedium
from simscale_sdk_v1.models.simulation.darcy_medium import DarcyMedium
from simscale_sdk_v1.models.simulation.fixed_coeff_medium import FixedCoeffMedium
from simscale_sdk_v1.models.simulation.perforated_plate import PerforatedPlate
from simscale_sdk_v1.models.simulation.power_law_medium import PowerLawMedium
from simscale_sdk_v1.models.simulation.pressure_loss_curve import PressureLossCurve
from simscale_sdk_v1.models.simulation.pressure_loss_function_medium import PressureLossFunctionMedium

_ONE_OF__ADVANCED_CONCEPTS_POROUS_MEDIUMS_VARIANTS: dict[str, type] = {
    "DARCY": DarcyMedium,
    "PRESSURE_LOSS_FUNCTION": PressureLossFunctionMedium,
    "DARCY_FORCHHEIMER": DarcyForchheimerMedium,
    "FIXED_COEFFICIENTS": FixedCoeffMedium,
    "POWER_LAW": PowerLawMedium,
    "PRESSURE_LOSS_CURVE": PressureLossCurve,
    "PERFORATED_PLATE": PerforatedPlate,
}

OneOf_AdvancedConceptsPorousMediums = Annotated[
    Union[
        DarcyMedium,
        PressureLossFunctionMedium,
        DarcyForchheimerMedium,
        FixedCoeffMedium,
        PowerLawMedium,
        PressureLossCurve,
        PerforatedPlate,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_POROUS_MEDIUMS_VARIANTS,
        )
    ),
]
