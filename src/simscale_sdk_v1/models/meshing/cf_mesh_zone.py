from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class CfMeshZone(SimScaleModel):
    """Cell zones tag all cells inside the assigned volumes so that they can be used in the simulation setup, for example for MRF rotating zones, momentum sources or porous media. The interface resolution controls whether a zone is meshed body-fitted or collected from the cells of the surrounding region.Cell zones are only available when physics-based meshing is disabled. With physics-based meshing enabled, the zones are created automatically from the simulation setup."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CF_MESH_ZONE",
        description="Cell zones tag all cells inside the assigned volumes so that they can be used in the simulation setup, for example for MRF rotating zones, momentum sources or porous media. The interface resolution controls whether a zone is meshed body-fitted or collected from the cells of the surrounding region.Cell zones are only available when physics-based meshing is disabled. With physics-based meshing enabled, the zones are created automatically from the simulation setup.  Schema name: CfMeshZone",
    )
    name: str | None = Field(default="Zone")
    interface_resolution: Literal["BODY_FITTED", "CRINKLE"] | None = Field(
        validation_alias="interfaceResolution",
        serialization_alias="interfaceResolution",
        default="CRINKLE",
        description="The interface resolution controls how the boundary of the cell zone is represented in the mesh.Body-fitted: the mesh conforms to the surfaces of the assigned volumes, at the cost of potentially lower mesh quality. Use this when the zone boundary must be captured accurately, for example for AMI rotating zones.Crinkle: the mesh is unaffected by the surfaces of the assigned volumes. Cells whose centers lie inside the assigned volumes are collected into the zone, so the zone boundary follows the existing cells. Use this when the exact shape of the zone boundary is not important, for example for momentum source terms.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
