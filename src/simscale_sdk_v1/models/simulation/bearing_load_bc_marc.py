from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.automatic_load_ramping_marc import AutomaticLoadRampingMarc
from simscale_sdk_v1.models.simulation.bearing_load_distribution_marc import BearingLoadDistributionMarc
from simscale_sdk_v1.models.simulation.dimensional_vector_function_with_lcs__force import (
    DimensionalVectorFunctionWithLCS_Force,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class BearingLoadBCMarc(SimScaleModel):
    """Bearing load spreads a force over a sector of one or more cylindrical faces, the way a pin loads a bore or a housing loads a journal. The sector is centred on the direction of the force, and the nodal forces always sum to the resultant.All assigned faces must be cylindrical and share the same cylinder axis. Only the radial part of the force is applied: a component along the cylinder axis is ignored. Use a separate force for axial thrust."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BEARING_LOAD",
        description="Bearing load spreads a force over a sector of one or more cylindrical faces, the way a pin loads a bore or a housing loads a journal. The sector is centred on the direction of the force, and the nodal forces always sum to the resultant.All assigned faces must be cylindrical and share the same cylinder axis. Only the radial part of the force is applied: a component along the cylinder axis is ignored. Use a separate force for axial thrust.  Schema name: BearingLoadBCMarc",
    )
    name: str | None = Field(default=None)
    load_distribution: BearingLoadDistributionMarc | None = Field(
        validation_alias="loadDistribution", serialization_alias="loadDistribution", default=None
    )
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the vector components are expressed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Cylindrical — Vector components are defined as radial (ur), tangential (uΦ), and axial (uz).",
    )
    force: DimensionalVectorFunctionWithLCS_Force | None = Field(default=None)
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    automatic_load_ramping: AutomaticLoadRampingMarc | None = Field(
        validation_alias="automaticLoadRamping", serialization_alias="automaticLoadRamping", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
