from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.parametric.parameters import Parameters
from simscale_sdk_v1.models.simulation.analysis import Analysis


class SimulationSpec(SimScaleModel):
    simulation_id: str | None = Field(validation_alias="simulationId", serialization_alias="simulationId", default=None)
    name: str
    version: str = Field(
        default="34.0",
        description="The schema version of the simulation spec. This can be either the external version like `30.0`, or the internal version like `internal:549`.",
    )
    created_at: datetime | None = Field(validation_alias="createdAt", serialization_alias="createdAt", default=None)
    modified_at: datetime | None = Field(validation_alias="modifiedAt", serialization_alias="modifiedAt", default=None)
    cad_id: str = Field(
        validation_alias="cadId", serialization_alias="cadId", description="The ID of CAD input to the simulation."
    )
    state_id: str = Field(
        validation_alias="stateId",
        serialization_alias="stateId",
        description="The ID of CAD state input to the simulation.",
    )
    mesh_id: str | None = Field(
        validation_alias="meshId",
        serialization_alias="meshId",
        default=None,
        description="The generated mesh ID which is to be used in the simulation. This field should be left empty for analysis types that do not require a generated mesh like 'INCOMPRESSIBLE_PACEFISH', 'WIND_COMFORT', and 'SIMERICS_ANALYSIS'.",
    )
    model: Analysis
    parameters: Parameters | None = Field(default=None)
