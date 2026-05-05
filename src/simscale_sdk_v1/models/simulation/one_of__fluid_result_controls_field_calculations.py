from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.field_calculations_adjoint_sensitivities_result_control import (
    FieldCalculationsAdjointSensitivitiesResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_friction_velocity_result_control import (
    FieldCalculationsFrictionVelocityResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_mean_age_of_fluid_result_control import (
    FieldCalculationsMeanAgeOfFluidResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_mean_radiant_temperature_result_control import (
    FieldCalculationsMeanRadiantTemperatureResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_modeled_ti_result_control import (
    FieldCalculationsModeledTIResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_operative_temperature_result_control import (
    FieldCalculationsOperativeTemperatureResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_pressure_result_control import (
    FieldCalculationsPressureResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_resolved_ti_result_control import (
    FieldCalculationsResolvedTIResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_resolved_tke_result_control import (
    FieldCalculationsResolvedTKEResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_surface_normals_result_control import (
    FieldCalculationsSurfaceNormalsResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_thermal_comfort_result_control import (
    FieldCalculationsThermalComfortResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_total_ti_result_control import (
    FieldCalculationsTotalTIResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_total_tke_result_control import (
    FieldCalculationsTotalTKEResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_turbulence_result_control import (
    FieldCalculationsTurbulenceResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_velocity_result_control import (
    FieldCalculationsVelocityResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_wall_fluxes_result_control import (
    FieldCalculationsWallFluxesResultControl,
)
from simscale_sdk_v1.models.simulation.field_calculations_wall_heat_flux_result_control import (
    FieldCalculationsWallHeatFluxResultControl,
)

_ONE_OF__FLUID_RESULT_CONTROLS_FIELD_CALCULATIONS_VARIANTS: dict[str, type] = {
    "PRESSURE": FieldCalculationsPressureResultControl,
    "TURBULENCE": FieldCalculationsTurbulenceResultControl,
    "VELOCITY": FieldCalculationsVelocityResultControl,
    "FRICTION_VELOCITY_U_TAU": FieldCalculationsFrictionVelocityResultControl,
    "SURFACE_NORMALS": FieldCalculationsSurfaceNormalsResultControl,
    "WALL_FLUXES": FieldCalculationsWallFluxesResultControl,
    "AGE_OF_FLUID": FieldCalculationsMeanAgeOfFluidResultControl,
    "THERMAL_COMFORT": FieldCalculationsThermalComfortResultControl,
    "ADJOINT_SENSITIVITIES": FieldCalculationsAdjointSensitivitiesResultControl,
    "WALL_HEAT_FLUX": FieldCalculationsWallHeatFluxResultControl,
    "MEAN_RADIANT_TEMPERATURE": FieldCalculationsMeanRadiantTemperatureResultControl,
    "OPERATIVE_TEMPERATURE": FieldCalculationsOperativeTemperatureResultControl,
    "RESOLVED_TURBULENT_KINETIC_ENERGY": FieldCalculationsResolvedTKEResultControl,
    "TOTAL_TURBULENT_KINETIC_ENERGY": FieldCalculationsTotalTKEResultControl,
    "MODELED_TURBULENCE_INTENSITY": FieldCalculationsModeledTIResultControl,
    "RESOLVED_TURBULENCE_INTENSITY": FieldCalculationsResolvedTIResultControl,
    "TOTAL_TURBULENCE_INTENSITY": FieldCalculationsTotalTIResultControl,
}

OneOf_FluidResultControlsFieldCalculations = Annotated[
    Union[
        FieldCalculationsPressureResultControl,
        FieldCalculationsTurbulenceResultControl,
        FieldCalculationsVelocityResultControl,
        FieldCalculationsFrictionVelocityResultControl,
        FieldCalculationsSurfaceNormalsResultControl,
        FieldCalculationsWallFluxesResultControl,
        FieldCalculationsMeanAgeOfFluidResultControl,
        FieldCalculationsThermalComfortResultControl,
        FieldCalculationsAdjointSensitivitiesResultControl,
        FieldCalculationsWallHeatFluxResultControl,
        FieldCalculationsMeanRadiantTemperatureResultControl,
        FieldCalculationsOperativeTemperatureResultControl,
        FieldCalculationsResolvedTKEResultControl,
        FieldCalculationsTotalTKEResultControl,
        FieldCalculationsModeledTIResultControl,
        FieldCalculationsResolvedTIResultControl,
        FieldCalculationsTotalTIResultControl,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_RESULT_CONTROLS_FIELD_CALCULATIONS_VARIANTS,
        )
    ),
]
