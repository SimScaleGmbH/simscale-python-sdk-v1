from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SnapshotResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SNAPSHOT",
        description="Schema name: SnapshotResultControl",
    )
    export_fluid: bool | None = Field(
        validation_alias="exportFluid",
        serialization_alias="exportFluid",
        default=False,
        description="When this switch is activated, simulation data of the flow-field enclosed in the assignments will be exported",
    )
    export_surface: bool | None = Field(
        validation_alias="exportSurface",
        serialization_alias="exportSurface",
        default=False,
        description="When this switch is activated, simulation data on all surfaces enclosed in the assignments will be exported",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
