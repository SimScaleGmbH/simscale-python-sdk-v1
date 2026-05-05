from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class CyclicSymmetryBC(SimScaleModel):
    """The cyclic symmetry constraint enables to model only a sector of a 360° cyclic periodic structure and reduces the computation time and memory consumption considerably. The user defines the center and axis of the cyclic symmetry as well as the sector angle. The master and slave surfaces define the cyclic periodicity boundaries. Important remarks: All DOFs of the slave nodes will be constrained, adding an additional constraint on those nodes may lead to an overconstrained system.This is a linear constraint, so no large rotations or large deformations are allowed in the proximity of cyclic symmetry boundaries.  Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CYCLIC_SYMMETRY",
        description="The cyclic symmetry constraint enables to model only a sector of a 360° cyclic periodic structure and reduces the computation time and memory consumption considerably. The user defines the center and axis of the cyclic symmetry as well as the sector angle. The master and slave surfaces define the cyclic periodicity boundaries. Important remarks: All DOFs of the slave nodes will be constrained, adding an additional constraint on those nodes may lead to an overconstrained system.This is a linear constraint, so no large rotations or large deformations are allowed in the proximity of cyclic symmetry boundaries.  Learn more.  Schema name: CyclicSymmetryBC",
    )
    name: str | None = Field(default=None)
    enable_heat_transfer: Literal["YES", "NO", "HEAT_TRANSFER_ONLY"] | None = Field(
        validation_alias="enableHeatTransfer",
        serialization_alias="enableHeatTransfer",
        default="YES",
        description="Define if heat transfer should be allowed across the contact. If yes is chosen a perfectly bonded heat contact is assumed whereas if no is selected no heat transfer across the contact is allowed. Mechanical contact stays with both options active. With the selection of heat transfer only no mechanical contact is activated but only a bonded heat contact.",
    )
    axis_origin: DimensionalVector_Length | None = Field(
        validation_alias="axisOrigin", serialization_alias="axisOrigin", default=None
    )
    axis_direction: DimensionalVector_Length | None = Field(
        validation_alias="axisDirection", serialization_alias="axisDirection", default=None
    )
    sector_angle: Dimensional_Angle | None = Field(
        validation_alias="sectorAngle", serialization_alias="sectorAngle", default=None
    )
    master_topological_reference: TopologicalReference | None = Field(
        validation_alias="masterTopologicalReference", serialization_alias="masterTopologicalReference", default=None
    )
    slave_topological_reference: TopologicalReference | None = Field(
        validation_alias="slaveTopologicalReference", serialization_alias="slaveTopologicalReference", default=None
    )
