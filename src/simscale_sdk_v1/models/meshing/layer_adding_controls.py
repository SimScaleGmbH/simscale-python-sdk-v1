from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__angle import Dimensional_Angle


class LayerAddingControls(SimScaleModel):
    relative_size: bool | None = Field(
        validation_alias="relativeSize",
        serialization_alias="relativeSize",
        default=True,
        description="If turned on, the length parameters for layer refinements (e.g. 'Thickness of the final layer', 'Minimum overall layer thickness') are multiplied by the local cell size outside that layer. Else, they are used as absolute lengths.",
    )
    max_cancelled_layers_near_sharp_features: int | None = Field(
        validation_alias="maxCancelledLayersNearSharpFeatures",
        serialization_alias="maxCancelledLayersNearSharpFeatures",
        default=0,
        description="If the algorithm faces difficulty generating layers, this is the maximum number of layers that are NOT generated in that region. Such cases might occur near sharp features. Set to 0 to force layer generation for all cases.",
    )
    feature_angle: Dimensional_Angle | None = Field(
        validation_alias="featureAngle", serialization_alias="featureAngle", default=None
    )
    slip_feature_angle: Dimensional_Angle | None = Field(
        validation_alias="slipFeatureAngle", serialization_alias="slipFeatureAngle", default=None
    )
    relax_iterations: int | None = Field(
        validation_alias="relaxIterations",
        serialization_alias="relaxIterations",
        default=8,
        description="Specify the maximum number of relaxation iterations for the snapping process for layers.",
    )
    surface_normals_max_smoothing_iterations: int | None = Field(
        validation_alias="surfaceNormalsMaxSmoothingIterations",
        serialization_alias="surfaceNormalsMaxSmoothingIterations",
        default=2,
        description="Specify the maximum number of smoothing iterations for the surface normals.",
    )
    internal_mesh_max_smoothing_iterations: int | None = Field(
        validation_alias="internalMeshMaxSmoothingIterations",
        serialization_alias="internalMeshMaxSmoothingIterations",
        default=5,
        description="Specify the number of smoothing iterations for the interior mesh movement. This movement occurs in order to make space for layers.",
    )
    layer_thickness_max_smoothing_iterations: int | None = Field(
        validation_alias="layerThicknessMaxSmoothingIterations",
        serialization_alias="layerThicknessMaxSmoothingIterations",
        default=10,
        description="This specifies the number of iterations for smoothing of the overall layer thickness over different surface patches.",
    )
    max_face_thickness_ratio: float | None = Field(
        validation_alias="maxFaceThicknessRatio",
        serialization_alias="maxFaceThicknessRatio",
        default=0.5,
        description="Specify the maximum allowable face aspect ratio beyond which layers will not be added.",
    )
    max_thickness_to_medial_ratio: float | None = Field(
        validation_alias="maxThicknessToMedialRatio",
        serialization_alias="maxThicknessToMedialRatio",
        default=0.3,
        description="The medial length is a measure of the aspect ratio for a non-quadrilateral face. This parameter prevents layer addition for non-quad faces that are highly anisotropic.",
    )
    min_median_axis_angle: Dimensional_Angle | None = Field(
        validation_alias="minMedianAxisAngle", serialization_alias="minMedianAxisAngle", default=None
    )
    buffer_cells_no_extrude: int | None = Field(
        validation_alias="bufferCellsNoExtrude",
        serialization_alias="bufferCellsNoExtrude",
        default=0,
        description="This parameter specifies the number of buffer cells to be extruded at cell-faces where layers terminate. Set to",
    )
    layer_addition_max_iterations: int | None = Field(
        validation_alias="layerAdditionMaxIterations",
        serialization_alias="layerAdditionMaxIterations",
        default=50,
        description="Specify the overall layer addition iteration number. The algorithm will abort definitely as soon as this number is reached. In this case, the mesh might be illegal.",
    )
    max_iterations_with_strict_quality_controls: int | None = Field(
        validation_alias="maxIterationsWithStrictQualityControls",
        serialization_alias="maxIterationsWithStrictQualityControls",
        default=20,
        description="This parameter specifies the maximum number of layer iterations that are done with the mesh quality controls. On exceeding these, the algorithm switches to less strict controls specified in the 'relaxed' category.",
    )
