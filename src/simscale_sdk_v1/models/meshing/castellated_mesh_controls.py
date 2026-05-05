from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CastellatedMeshControls(SimScaleModel):
    max_local_cells: int | None = Field(
        validation_alias="maxLocalCells",
        serialization_alias="maxLocalCells",
        default=40000000,
        description="Define the maximal number of cells per processor during refinement",
    )
    max_global_cells: int | None = Field(
        validation_alias="maxGlobalCells",
        serialization_alias="maxGlobalCells",
        default=100000000,
        description="Define the maximum possible number of cells summed upon all processors. Note that this is before the castellation step (see documentation, so the actual number of cells after castellation might be considerably less.",
    )
    min_refinement_cells: int | None = Field(
        validation_alias="minRefinementCells",
        serialization_alias="minRefinementCells",
        default=1,
        description="If in a refinement iteration the number of cells selected for refinement is under this value, the refinement stops. Provide a small value to ensure that all surfaces are refined to the proper level.",
    )
    max_load_unbalance: float | None = Field(
        validation_alias="maxLoadUnbalance",
        serialization_alias="maxLoadUnbalance",
        default=0.2,
        description="Define a fraction indicating the maximum allowable load imbalance between processors working on this job. A value of 0 will force rebalancing for even a slight imbalance.",
    )
    cells_between_levels: int | None = Field(
        validation_alias="cellsBetweenLevels",
        serialization_alias="cellsBetweenLevels",
        default=3,
        description="This parameter specifies the number of layers of cells between different levels of refinement (see documentation).",
    )
    resolve_feature_angle: float | None = Field(
        validation_alias="resolveFeatureAngle",
        serialization_alias="resolveFeatureAngle",
        default=30,
        description="Cells that face multiple intersections with an intersection angle greater than this angle will be refined to the max level. Use this parameter to resolve sharp features to the maximum level of surface refinement specified (see documentation).",
    )
    allow_free_standing_zone_faces: bool | None = Field(
        validation_alias="allowFreeStandingZoneFaces",
        serialization_alias="allowFreeStandingZoneFaces",
        default=False,
        description="Decide whether you want to allow zone faces that share the same owner and neighbour cell zone. Allowing this can lead to problem when zone faces are snapped to features. This parameter is ignored when no faceZones are present.",
    )
