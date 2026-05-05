from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_contact_result_control_item import MarcContactResultControlItem
from simscale_sdk_v1.models.simulation.marc_displacement_result_control_item import MarcDisplacementResultControlItem
from simscale_sdk_v1.models.simulation.marc_force_result_control_item import MarcForceResultControlItem
from simscale_sdk_v1.models.simulation.marc_heat_flux_result_control_item import MarcHeatFluxResultControlItem
from simscale_sdk_v1.models.simulation.marc_pressure_result_control_item import MarcPressureResultControlItem
from simscale_sdk_v1.models.simulation.marc_strain_result_control_item import MarcStrainResultControlItem
from simscale_sdk_v1.models.simulation.marc_stress_result_control_item import MarcStressResultControlItem
from simscale_sdk_v1.models.simulation.marc_temperature_result_control_item import MarcTemperatureResultControlItem

_ONE_OF__MARC_RESULT_CONTROL_SOLUTION_FIELDS_VARIANTS: dict[str, type] = {
    "DISPLACEMENT": MarcDisplacementResultControlItem,
    "FORCE": MarcForceResultControlItem,
    "PRESSURE": MarcPressureResultControlItem,
    "STRESS": MarcStressResultControlItem,
    "STRAIN": MarcStrainResultControlItem,
    "CONTACT": MarcContactResultControlItem,
    "TEMPERATURE": MarcTemperatureResultControlItem,
    "HEAT_FLUX": MarcHeatFluxResultControlItem,
}

OneOf_MarcResultControlSolutionFields = Annotated[
    Union[
        MarcDisplacementResultControlItem,
        MarcForceResultControlItem,
        MarcPressureResultControlItem,
        MarcStressResultControlItem,
        MarcStrainResultControlItem,
        MarcContactResultControlItem,
        MarcTemperatureResultControlItem,
        MarcHeatFluxResultControlItem,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_RESULT_CONTROL_SOLUTION_FIELDS_VARIANTS,
        )
    ),
]
