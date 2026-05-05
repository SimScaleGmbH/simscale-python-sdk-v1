from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__automatic_simerics_mesh_settings_refinements import (
    OneOf_AutomaticSimericsMeshSettingsRefinements,
)


class AutomaticSimericsMeshSettings(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC_SETTINGS",
        description="Schema name: AutomaticSimericsMeshSettings",
    )
    refinements: list[OneOf_AutomaticSimericsMeshSettingsRefinements] | None = Field(default=None)
    fineness: float | None = Field(
        default=1, description="Adjust the overall mesh sizing from coarse (value: 0) to fine (10)."
    )
    enable_cad_surface_merging: bool | None = Field(
        validation_alias="enableCADSurfaceMerging",
        serialization_alias="enableCADSurfaceMerging",
        default=True,
        description="Merge CAD surfaces combines all surfaces of the CAD model that are not assigned a boundary condition or result control. With this turned on, the probability of successful mesh generation for more complicated geometries significantly increases. If you need to inspect unassigned surfaces separately, turn it off. For more information, please contact Support.",
    )
