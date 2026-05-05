from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.meshing.dimensional__area import Dimensional_Area
from simscale_sdk_v1.models.meshing.dimensional__volume import Dimensional_Volume


class MeshQualityControls(SimScaleModel):
    max_non_orthogonality: Dimensional_Angle | None = Field(
        validation_alias="maxNonOrthogonality", serialization_alias="maxNonOrthogonality", default=None
    )
    max_boundary_skewness: Dimensional_Angle | None = Field(
        validation_alias="maxBoundarySkewness", serialization_alias="maxBoundarySkewness", default=None
    )
    max_internal_skewness: Dimensional_Angle | None = Field(
        validation_alias="maxInternalSkewness", serialization_alias="maxInternalSkewness", default=None
    )
    max_concaveness: Dimensional_Angle | None = Field(
        validation_alias="maxConcaveness", serialization_alias="maxConcaveness", default=None
    )
    min_volume: Dimensional_Volume | None = Field(
        validation_alias="minVolume", serialization_alias="minVolume", default=None
    )
    min_tet_quality: float | None = Field(
        validation_alias="minTetQuality",
        serialization_alias="minTetQuality",
        default=-1000000000000000000000000000000,
        description="Define a minimum tetrahedron quality for cells (see documentation). Choose a low negative number to disable this check, e.g. -1e30.",
    )
    min_face_area: Dimensional_Area | None = Field(
        validation_alias="minFaceArea", serialization_alias="minFaceArea", default=None
    )
    min_face_twist: float | None = Field(
        validation_alias="minFaceTwist",
        serialization_alias="minFaceTwist",
        default=0.01,
        description="Define the minimum cosine of face twist allowed (see documentation). Set to a value smaller than -1 to disable. The value results from the dot product of the face normal and the face centre triangles normal.",
    )
    min_determinant: float | None = Field(
        validation_alias="minDeterminant",
        serialization_alias="minDeterminant",
        default=0.001,
        description="Define the minimum normalised cell determinant. Choose a value between 0 and 1. Hex corresponds to 1.",
    )
    min_face_weight: float | None = Field(
        validation_alias="minFaceWeight",
        serialization_alias="minFaceWeight",
        default=0.02,
        description="The face weight specifies the distribution of a face's contribution to its two neighbouring cells. A very small face weight would mean that the neighbouring cells are disproportionately different in size. Choose a value between 0 and 0.5. 0.5 refers to a face with neighbouring cells of the same size.",
    )
    min_volume_ratio: float | None = Field(
        validation_alias="minVolumeRatio",
        serialization_alias="minVolumeRatio",
        default=0.01,
        description="This parameter specifies the minimum allowed volume ratio between two adjacent cells. Choose a value between 0 and 1. 1 means that the neighbouring cells have the same volume.",
    )
    min_triangle_twist: float | None = Field(
        validation_alias="minTriangleTwist",
        serialization_alias="minTriangleTwist",
        default=-1,
        description="Same as Min Face Twist, but for adjacent triangular faces (see documentation). Choose a value below -1 to disable this feature.",
    )
    error_distribution_iterations: int | None = Field(
        validation_alias="errorDistributionIterations",
        serialization_alias="errorDistributionIterations",
        default=4,
        description="Define the number of error distribution iterations.",
    )
    error_reduction: float | None = Field(
        validation_alias="errorReduction",
        serialization_alias="errorReduction",
        default=0.75,
        description="This parameter specifies how much the displacement is scaled at error locations.",
    )
    relaxed_max_non_orthogonality: Dimensional_Angle | None = Field(
        validation_alias="relaxedMaxNonOrthogonality", serialization_alias="relaxedMaxNonOrthogonality", default=None
    )
    merge_tolerance: float | None = Field(
        validation_alias="mergeTolerance",
        serialization_alias="mergeTolerance",
        default=1e-06,
        description="This parameters specifies the accuracy of face merging as a fraction of the initial bounding box.",
    )
