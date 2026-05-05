from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.acceleration_result_control_item import AccelerationResultControlItem
from simscale_sdk_v1.models.simulation.contact_result_control_item import ContactResultControlItem
from simscale_sdk_v1.models.simulation.displacement_result_control_item import DisplacementResultControlItem
from simscale_sdk_v1.models.simulation.erp_density_result_control_item import ERPDensityResultControlItem
from simscale_sdk_v1.models.simulation.force_result_control_item import ForceResultControlItem
from simscale_sdk_v1.models.simulation.harmonic_acceleration_result_control_item import (
    HarmonicAccelerationResultControlItem,
)
from simscale_sdk_v1.models.simulation.harmonic_displacement_result_control_item import (
    HarmonicDisplacementResultControlItem,
)
from simscale_sdk_v1.models.simulation.harmonic_velocity_result_control_item import HarmonicVelocityResultControlItem
from simscale_sdk_v1.models.simulation.heat_flux_result_control_item import HeatFluxResultControlItem
from simscale_sdk_v1.models.simulation.normalized_displacement_result_control_item import (
    NormalizedDisplacementResultControlItem,
)
from simscale_sdk_v1.models.simulation.strain_result_control_item import StrainResultControlItem
from simscale_sdk_v1.models.simulation.stress_result_control_item import StressResultControlItem
from simscale_sdk_v1.models.simulation.temperature_result_control_item import TemperatureResultControlItem
from simscale_sdk_v1.models.simulation.velocity_result_control_item import VelocityResultControlItem

_ONE_OF__SOLID_RESULT_CONTROL_SOLUTION_FIELDS_VARIANTS: dict[str, type] = {
    "CONTACT": ContactResultControlItem,
    "DISPLACEMENT": DisplacementResultControlItem,
    "HARMONIC_DISPLACEMENT": HarmonicDisplacementResultControlItem,
    "NORMALIZED_DISPLACEMENT": NormalizedDisplacementResultControlItem,
    "FORCE": ForceResultControlItem,
    "STRAIN": StrainResultControlItem,
    "STRESS": StressResultControlItem,
    "VELOCITY": VelocityResultControlItem,
    "HARMONIC_VELOCITY": HarmonicVelocityResultControlItem,
    "ACCELERATION": AccelerationResultControlItem,
    "HARMONIC_ACCELERATION": HarmonicAccelerationResultControlItem,
    "TEMPERATURE": TemperatureResultControlItem,
    "HEAT_FLUX": HeatFluxResultControlItem,
    "ERP_DENSITY": ERPDensityResultControlItem,
}

OneOf_SolidResultControlSolutionFields = Annotated[
    Union[
        ContactResultControlItem,
        DisplacementResultControlItem,
        HarmonicDisplacementResultControlItem,
        NormalizedDisplacementResultControlItem,
        ForceResultControlItem,
        StrainResultControlItem,
        StressResultControlItem,
        VelocityResultControlItem,
        HarmonicVelocityResultControlItem,
        AccelerationResultControlItem,
        HarmonicAccelerationResultControlItem,
        TemperatureResultControlItem,
        HeatFluxResultControlItem,
        ERPDensityResultControlItem,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_RESULT_CONTROL_SOLUTION_FIELDS_VARIANTS,
        )
    ),
]
