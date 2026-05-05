from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class TemperatureBCMarc(SimScaleModel):
    """This is a boundary condition for the temperature variable. It prescribes the given temperature value on all selected groups.Important remarks: Do not define a temperature and a heat flux boundary condition on the same groupDo not define the temperature on slave entities of Contact Constraints as they are constrained by the master temperatureYou may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file)"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TEMPERATURE",
        description="This is a boundary condition for the temperature variable. It prescribes the given temperature value on all selected groups.Important remarks: Do not define a temperature and a heat flux boundary condition on the same groupDo not define the temperature on slave entities of Contact Constraints as they are constrained by the master temperatureYou may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file)  Schema name: TemperatureBCMarc",
    )
    name: str | None = Field(default=None)
    temperature_value: DimensionalFunction_Temperature | None = Field(
        validation_alias="temperatureValue", serialization_alias="temperatureValue", default=None
    )
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
