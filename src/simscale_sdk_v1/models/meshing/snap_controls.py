from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SnapControls(SimScaleModel):
    mesh_to_geometry_conformation_iterations: int | None = Field(
        validation_alias="meshToGeometryConformationIterations",
        serialization_alias="meshToGeometryConformationIterations",
        default=5,
        description="Define the max number of iterations to ensure that the mesh conforms to the geometry. Higher values lead to a better conforming mesh.",
    )
    tolerance: float | None = Field(
        default=2,
        description="This parameter describes a distance (relative to the local maximum mesh edge length) within which the algorithm looks for a geometry point to snap the mesh to. Higher values lead to better snapping but are costlier.",
    )
    solver_iterations: int | None = Field(
        validation_alias="solverIterations",
        serialization_alias="solverIterations",
        default=150,
        description="This parameter defines the number of displacement relaxation iterations during the meshing process. Higher values lead to enhanced mesh quality but increase the computing time.",
    )
    relax_iterations: int | None = Field(
        validation_alias="relaxIterations",
        serialization_alias="relaxIterations",
        default=8,
        description="This parameter defines the max number of iterations to remove bad mesh points (see documentation).",
    )
    max_mex_conformation_iterations: int | None = Field(
        validation_alias="maxMexConformationIterations",
        serialization_alias="maxMexConformationIterations",
        default=10,
        description="This parameter defines the max number of iterations done to ensure that the mesh conforms to the geometry.",
    )
    implicit_feature_snap: bool | None = Field(
        validation_alias="implicitFeatureSnap",
        serialization_alias="implicitFeatureSnap",
        default=True,
        description="Activating this makes the snapping algorithm detecting geometrical features by sampling the surface. This might be time-consuming. The other option is to create a feature refinement which also enables feature snapping.",
    )
    explicit_feature_snap: bool | None = Field(
        validation_alias="explicitFeatureSnap",
        serialization_alias="explicitFeatureSnap",
        default=False,
        description="Use the explicitly given feature refinements for feature snapping. An explicit feature refinement can be added under 'Mesh refinement'. Specifying a feature refinement results in sharp mesh edges even with a refinement level of zero.",
    )
    detect_features_between_multiple_surfaces: bool | None = Field(
        validation_alias="detectFeaturesBetweenMultipleSurfaces",
        serialization_alias="detectFeaturesBetweenMultipleSurfaces",
        default=True,
        description="Also detect features between multiple surfaces. This is relevant when you want to create a mesh with multiple regions - used for example in the conjugate heat transfer solver. Needs 'Use feature refinement for snapping' turned on!",
    )
