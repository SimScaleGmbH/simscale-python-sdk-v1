from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.opacity import Opacity
from simscale_sdk_v1.models.reporting.render_mode import RenderMode
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.vector3_d import Vector3D
from simscale_sdk_v1.models.reporting.vector_field import VectorField


class CuttingPlane(SimScaleModel):
    name: str
    center: Vector3D
    normal: Vector3D
    opacity: Opacity | None = Field(default=None)
    clipping: bool = Field(default=True)
    vector_grid_spacing: float | None = Field(
        validation_alias="vectorGridSpacing",
        serialization_alias="vectorGridSpacing",
        default=0.02,
        description="This field is required if projectVectorsOntoPlane is set to true.",
    )
    scalar_field: ScalarField | None = Field(
        validation_alias="scalarField", serialization_alias="scalarField", default=None
    )
    vector_field: VectorField | None = Field(
        validation_alias="vectorField", serialization_alias="vectorField", default=None
    )
    solid_color: Color | None = Field(validation_alias="solidColor", serialization_alias="solidColor", default=None)
    project_vectors_onto_plane: bool = Field(
        validation_alias="projectVectorsOntoPlane",
        serialization_alias="projectVectorsOntoPlane",
        default=False,
        description="If a vectorField is provided, this flag will project the vector field onto the cutting plane.",
    )
    render_mode: RenderMode | None = Field(
        validation_alias="renderMode", serialization_alias="renderMode", default=None
    )
