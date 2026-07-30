from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__volumetric_power import DimensionalFunction_VolumetricPower
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class VolumeHeatFluxBCMarc(SimScaleModel):
    """This is a volume heat source boundary condition. It is applied to the volume elements in the selected volumes or volume groups.Important remarks: The total heat generated depends on the volume of the selection as the value is given as Watt per cubic meter.For positive values heat is generated, for negative values the bc represents a heat sink.You may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file)"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLUME_HEAT_FLUX",
        description="This is a volume heat source boundary condition. It is applied to the volume elements in the selected volumes or volume groups.Important remarks: The total heat generated depends on the volume of the selection as the value is given as Watt per cubic meter.For positive values heat is generated, for negative values the bc represents a heat sink.You may define a parameter dependent (x,y,z,t) value by defining a formula or uploading a table (csv-file)  Schema name: VolumeHeatFluxBCMarc",
    )
    name: str | None = Field(default=None)
    heatflux_value: DimensionalFunction_VolumetricPower | None = Field(
        validation_alias="heatfluxValue", serialization_alias="heatfluxValue", default=None
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
