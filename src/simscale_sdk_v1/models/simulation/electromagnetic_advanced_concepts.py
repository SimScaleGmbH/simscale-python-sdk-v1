from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.electromagnetic_circuit import ElectromagneticCircuit
from simscale_sdk_v1.models.simulation.predefined_rotational_motion import PredefinedRotationalMotion


class ElectromagneticAdvancedConcepts(SimScaleModel):
    motion_analysis: list[PredefinedRotationalMotion] | None = Field(
        validation_alias="motionAnalysis", serialization_alias="motionAnalysis", default=None
    )
    circuit: ElectromagneticCircuit | None = Field(default=None)
