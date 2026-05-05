from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector_function__volume_force import (
    DimensionalVectorFunction_VolumeForce,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class VolumeLoadBC(SimScaleModel):
    """This is a volume load boundary condition representing a distributed load on the selected volumes applied in the global coordinate system and each element of the assignment is loaded with a volume force depending on the volume of the element.Important remarks: The applied total force depends on the volume of the selection.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLUME_LOAD",
        description="This is a volume load boundary condition representing a distributed load on the selected volumes applied in the global coordinate system and each element of the assignment is loaded with a volume force depending on the volume of the element.Important remarks: The applied total force depends on the volume of the selection.Learn more.  Schema name: VolumeLoadBC",
    )
    name: str | None = Field(default=None)
    load: DimensionalVectorFunction_VolumeForce | None = Field(default=None)
    scaling: DimensionalFunction_Dimensionless | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
