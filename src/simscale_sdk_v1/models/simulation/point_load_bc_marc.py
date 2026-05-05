from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector_function__force import DimensionalVectorFunction_Force
from simscale_sdk_v1.models.simulation.dimensional_vector_function__torque import DimensionalVectorFunction_Torque


class PointLoadBCMarc(SimScaleModel):
    """This boundary condition adds a point force or moment load at a single remote point defined via a point geometry primitive.Important remarks:The assigned point geometry primitive point needs to be connected to the CAD model via an RBE3 or RBE2 connector.Gradually ramp the force and moment values via a table or formula depending on time [t], otherwise the full load will be applied on the first iteration already and the simulation might fail to converge."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="POINT_LOAD",
        description="This boundary condition adds a point force or moment load at a single remote point defined via a point geometry primitive.Important remarks:The assigned point geometry primitive point needs to be connected to the CAD model via an RBE3 or RBE2 connector.Gradually ramp the force and moment values via a table or formula depending on time [t], otherwise the full load will be applied on the first iteration already and the simulation might fail to converge.  Schema name: PointLoadBCMarc",
    )
    name: str | None = Field(default=None)
    force: DimensionalVectorFunction_Force | None = Field(default=None)
    moment: DimensionalVectorFunction_Torque | None = Field(default=None)
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
