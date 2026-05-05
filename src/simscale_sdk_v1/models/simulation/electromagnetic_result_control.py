from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.electromagnetic_resistance_set import ElectromagneticResistanceSet
from simscale_sdk_v1.models.simulation.electromagnetic_result_control_probe_point import (
    ElectromagneticResultControlProbePoint,
)
from simscale_sdk_v1.models.simulation.force_and_torque import ForceAndTorque


class ElectromagneticResultControl(SimScaleModel):
    calculate_inductances: bool | None = Field(
        validation_alias="calculateInductances",
        serialization_alias="calculateInductances",
        default=False,
        description="Calculate the inductance matrix of the coils.",
    )
    calculate_capacitances: bool | None = Field(
        validation_alias="calculateCapacitances",
        serialization_alias="calculateCapacitances",
        default=False,
        description="Calculate the capacitance matrix of the conductive bodies.Note that the field solution will be modified.",
    )
    forces_and_torques: list[ForceAndTorque] | None = Field(
        validation_alias="forcesAndTorques", serialization_alias="forcesAndTorques", default=None
    )
    probe_points: list[ElectromagneticResultControlProbePoint] | None = Field(
        validation_alias="probePoints", serialization_alias="probePoints", default=None
    )
    resistance_sets: list[ElectromagneticResistanceSet] | None = Field(
        validation_alias="resistanceSets", serialization_alias="resistanceSets", default=None
    )
