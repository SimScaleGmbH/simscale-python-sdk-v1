from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.decimal_vector import DecimalVector
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FieldCalculationsAdjointSensitivitiesResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ADJOINT_SENSITIVITIES",
        description="Schema name: FieldCalculationsAdjointSensitivitiesResultControl",
    )
    name: str | None = Field(default=None)
    compute_sensitivities_to: Literal["MAXIMIZE_FORCE", "MINIMIZE_FORCE"] | None = Field(
        validation_alias="computeSensitivitiesTo",
        serialization_alias="computeSensitivitiesTo",
        default="MINIMIZE_FORCE",
    )
    optimization_force_direction: DecimalVector | None = Field(
        validation_alias="optimizationForceDirection", serialization_alias="optimizationForceDirection", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
