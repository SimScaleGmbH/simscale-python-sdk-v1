from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__angle import DimensionalFunction_Angle
from simscale_sdk_v1.models.simulation.dimensional_vector_function__length import DimensionalVectorFunction_Length
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class RotatingMotionBC(SimScaleModel):
    """The rotating motion constraint applies a predefined rigid body rotation to the assigned entities. The rotation axis, the base point, and the rotation angle needs to be specified. Each component can be defined with a formula or table input.Important remarks: If a component of the rotation axis is input via formula or table, then ensure that the length of the axis vector is always positive.If a continuous, transient rotation is required, then the rotation angle has to be given either as a formula or table value.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ROTATING_MOTION",
        description="The rotating motion constraint applies a predefined rigid body rotation to the assigned entities. The rotation axis, the base point, and the rotation angle needs to be specified. Each component can be defined with a formula or table input.Important remarks: If a component of the rotation axis is input via formula or table, then ensure that the length of the axis vector is always positive.If a continuous, transient rotation is required, then the rotation angle has to be given either as a formula or table value.Learn more.  Schema name: RotatingMotionBC",
    )
    name: str | None = Field(default=None)
    rotation_origin: DimensionalVectorFunction_Length | None = Field(
        validation_alias="rotationOrigin", serialization_alias="rotationOrigin", default=None
    )
    rotation_axis: DimensionalVectorFunction_Length | None = Field(
        validation_alias="rotationAxis", serialization_alias="rotationAxis", default=None
    )
    omega: DimensionalFunction_Angle | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
