from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__manual_simerics_mesh_settings_cell_size_specification import (
    OneOf_ManualSimericsMeshSettingsCellSizeSpecification,
)
from simscale_sdk_v1.models.simulation.one_of__manual_simerics_mesh_settings_refinements import (
    OneOf_ManualSimericsMeshSettingsRefinements,
)


class ManualSimericsMeshSettings(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL_SETTINGS",
        description="Schema name: ManualSimericsMeshSettings",
    )
    refinements: list[OneOf_ManualSimericsMeshSettingsRefinements] | None = Field(default=None)
    cell_size_specification: OneOf_ManualSimericsMeshSettingsCellSizeSpecification | None = Field(
        validation_alias="cellSizeSpecification", serialization_alias="cellSizeSpecification", default=None
    )
    enable_cad_surface_merging: bool | None = Field(
        validation_alias="enableCADSurfaceMerging",
        serialization_alias="enableCADSurfaceMerging",
        default=True,
        description="Merge CAD surfaces combines all surfaces of the CAD model that are not assigned a boundary condition or result control. With this turned on, the probability of successful mesh generation for more complicated geometries significantly increases. If you need to inspect unassigned surfaces separately, turn it off. For more information, please contact Support.",
    )
