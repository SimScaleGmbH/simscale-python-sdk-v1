from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.electric_current_density_field_selection import (
    ElectricCurrentDensityFieldSelection,
)
from simscale_sdk_v1.models.simulation.electric_displacement_field_field_selection import (
    ElectricDisplacementFieldFieldSelection,
)
from simscale_sdk_v1.models.simulation.electric_field_field_selection import ElectricFieldFieldSelection
from simscale_sdk_v1.models.simulation.electric_potential_field_selection import ElectricPotentialFieldSelection
from simscale_sdk_v1.models.simulation.magnetic_field_field_selection import MagneticFieldFieldSelection
from simscale_sdk_v1.models.simulation.magnetic_flux_density_field_selection import MagneticFluxDensityFieldSelection

_ONE_OF__ELECTROMAGNETIC_RESULT_CONTROL_PROBE_POINT_FIELD_SELECTION_VARIANTS: dict[str, type] = {
    "MAGNETIC_FLUX_DENSITY": MagneticFluxDensityFieldSelection,
    "MAGNETIC_FIELD": MagneticFieldFieldSelection,
    "ELECTRIC_CURRENT_DENSITY": ElectricCurrentDensityFieldSelection,
    "ELECTRIC_POTENTIAL": ElectricPotentialFieldSelection,
    "ELECTRIC_FIELD": ElectricFieldFieldSelection,
    "ELECTRIC_DISPLACEMENT_FIELD": ElectricDisplacementFieldFieldSelection,
}

OneOf_ElectromagneticResultControlProbePointFieldSelection = Annotated[
    Union[
        MagneticFluxDensityFieldSelection,
        MagneticFieldFieldSelection,
        ElectricCurrentDensityFieldSelection,
        ElectricPotentialFieldSelection,
        ElectricFieldFieldSelection,
        ElectricDisplacementFieldFieldSelection,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_RESULT_CONTROL_PROBE_POINT_FIELD_SELECTION_VARIANTS,
        )
    ),
]
