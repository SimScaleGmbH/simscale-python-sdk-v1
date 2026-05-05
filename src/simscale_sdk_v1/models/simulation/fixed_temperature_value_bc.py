from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FixedTemperatureValueBC(SimScaleModel):
    """This is a boundary condition for the temperature variable. It prescribes the given temperature value on all selected groups.Important remarks: Do not define a temperature and a heat flux boundary condition on the same groupDo not define the temperature on slave entities of Contact Constraints as they are constrained by the master temperatureYou may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file)"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_TEMPERATURE_VALUE",
        description="This is a boundary condition for the temperature variable. It prescribes the given temperature value on all selected groups.Important remarks: Do not define a temperature and a heat flux boundary condition on the same groupDo not define the temperature on slave entities of Contact Constraints as they are constrained by the master temperatureYou may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file)  Schema name: FixedTemperatureValueBC",
    )
    name: str | None = Field(default=None)
    temperature_value: DimensionalFunction_Temperature | None = Field(
        validation_alias="temperatureValue", serialization_alias="temperatureValue", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
