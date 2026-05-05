from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.computing_core import ComputingCore
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.harmonic_response_control import HarmonicResponseControl
from simscale_sdk_v1.models.simulation.modal_base_control import ModalBaseControl
from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_eigenfrequency_scope import (
    OneOf_SolidSimulationControlEigenfrequencyScope,
)
from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_excitation_frequencies import (
    OneOf_SolidSimulationControlExcitationFrequencies,
)
from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_pseudo_time_stepping import (
    OneOf_SolidSimulationControlPseudoTimeStepping,
)
from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_timestep_definition import (
    OneOf_SolidSimulationControlTimestepDefinition,
)
from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_write_control_definition import (
    OneOf_SolidSimulationControlWriteControlDefinition,
)


class SolidSimulationControl(SimScaleModel):
    timestep_definition: OneOf_SolidSimulationControlTimestepDefinition | None = Field(
        validation_alias="timestepDefinition", serialization_alias="timestepDefinition", default=None
    )
    pseudo_time_stepping: OneOf_SolidSimulationControlPseudoTimeStepping | None = Field(
        validation_alias="pseudoTimeStepping", serialization_alias="pseudoTimeStepping", default=None
    )
    auto_load_ramping: bool | None = Field(
        validation_alias="autoLoadRamping",
        serialization_alias="autoLoadRamping",
        default=True,
        description="Loads and enforced motions will be ramped linearly over the simulation interval to aid solution convergence. Automatic ramping will only be applied if all boundary conditions (including gravity) are applied with constant values and if no creep formulation has been defined for the materials.",
    )
    write_control_definition: OneOf_SolidSimulationControlWriteControlDefinition | None = Field(
        validation_alias="writeControlDefinition", serialization_alias="writeControlDefinition", default=None
    )
    excitation_frequencies: OneOf_SolidSimulationControlExcitationFrequencies | None = Field(
        validation_alias="excitationFrequencies", serialization_alias="excitationFrequencies", default=None
    )
    eigenfrequency_scope: OneOf_SolidSimulationControlEigenfrequencyScope | None = Field(
        validation_alias="eigenfrequencyScope", serialization_alias="eigenfrequencyScope", default=None
    )
    modal_base: ModalBaseControl | None = Field(
        validation_alias="modalBase", serialization_alias="modalBase", default=None
    )
    harmonic_response: HarmonicResponseControl | None = Field(
        validation_alias="harmonicResponse", serialization_alias="harmonicResponse", default=None
    )
    processors: ComputingCore | None = Field(default=None)
    max_run_time: Dimensional_Time | None = Field(
        validation_alias="maxRunTime", serialization_alias="maxRunTime", default=None
    )
