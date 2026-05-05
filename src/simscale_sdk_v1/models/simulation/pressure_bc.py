from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PressureBC(SimScaleModel):
    """This is a pressure boundary condition representing a distributed load on the selection. It is applied normal to the surface of all face elements.Important remarks: The applied total force depends on the surface area of the selection.The normal direction of the faces is computed only in the undeformed state and not updated for large deformations.For transient analyses you may define a time dependent value by uploading a table (csv-file).Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE",
        description="This is a pressure boundary condition representing a distributed load on the selection. It is applied normal to the surface of all face elements.Important remarks: The applied total force depends on the surface area of the selection.The normal direction of the faces is computed only in the undeformed state and not updated for large deformations.For transient analyses you may define a time dependent value by uploading a table (csv-file).Learn more.  Schema name: PressureBC",
    )
    name: str | None = Field(default=None)
    pressure: DimensionalFunction_Pressure | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
