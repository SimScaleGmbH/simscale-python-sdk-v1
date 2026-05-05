from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_modelling import AdvancedModelling
from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
from simscale_sdk_v1.models.simulation.pedestrian_comfort_surface import PedestrianComfortSurface
from simscale_sdk_v1.models.simulation.region_of_interest import RegionOfInterest
from simscale_sdk_v1.models.simulation.wind_comfort_mesh import WindComfortMesh
from simscale_sdk_v1.models.simulation.wind_comfort_simulation_control import WindComfortSimulationControl
from simscale_sdk_v1.models.simulation.wind_conditions import WindConditions


class WindComfort(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WIND_COMFORT",
        description="Schema name: WindComfort",
    )
    region_of_interest: RegionOfInterest | None = Field(
        validation_alias="regionOfInterest", serialization_alias="regionOfInterest", default=None
    )
    wind_conditions: WindConditions | None = Field(
        validation_alias="windConditions", serialization_alias="windConditions", default=None
    )
    pedestrian_comfort_map: list[PedestrianComfortSurface] | None = Field(
        validation_alias="pedestrianComfortMap", serialization_alias="pedestrianComfortMap", default=None
    )
    simulation_control: WindComfortSimulationControl | None = Field(
        validation_alias="simulationControl", serialization_alias="simulationControl", default=None
    )
    advanced_modelling: AdvancedModelling | None = Field(
        validation_alias="advancedModelling", serialization_alias="advancedModelling", default=None
    )
    additional_result_export: FluidResultControls | None = Field(
        validation_alias="additionalResultExport", serialization_alias="additionalResultExport", default=None
    )
    mesh_settings: WindComfortMesh | None = Field(
        validation_alias="meshSettings", serialization_alias="meshSettings", default=None
    )
