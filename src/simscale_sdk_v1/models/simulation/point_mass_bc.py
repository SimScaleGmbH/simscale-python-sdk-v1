from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__mass import Dimensional_Mass
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.dimensional_vector__moment_of_inertia import DimensionalVector_MomentOfInertia
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PointMassBC(SimScaleModel):
    """Define a Point mass boundary condition in order to insert an additional mass on a specific location of the active model."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="POINT_MASS",
        description="Define a Point mass boundary condition in order to insert an additional mass on a specific location of the active model.  Schema name: PointMassBC",
    )
    name: str | None = Field(default=None)
    mass: Dimensional_Mass | None = Field(default=None)
    mass_moment_of_inertia: DimensionalVector_MomentOfInertia | None = Field(
        validation_alias="massMomentOfInertia", serialization_alias="massMomentOfInertia", default=None
    )
    external_point: DimensionalVector_Length | None = Field(
        validation_alias="externalPoint", serialization_alias="externalPoint", default=None
    )
    deformation_behavior: Literal["DEFORMABLE", "UNDEFORMABLE"] | None = Field(
        validation_alias="deformationBehavior",
        serialization_alias="deformationBehavior",
        default="DEFORMABLE",
        description="Choose the deformation behavior of the entity which the point mass is connected to. If deformable is selected, the entity is allowed to deform, selecting undeformable leads to a rigid entity.",
    )
    enable_search_radius: bool | None = Field(
        validation_alias="enableSearchRadius", serialization_alias="enableSearchRadius", default=False
    )
    search_radius: Dimensional_Length | None = Field(
        validation_alias="searchRadius", serialization_alias="searchRadius", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
