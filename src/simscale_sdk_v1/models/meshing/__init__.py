"""Generated Meshing models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.meshing.absolute_distance import AbsoluteDistance
    from simscale_sdk_v1.models.meshing.advanced_simmetrix_em_settings import AdvancedSimmetrixEmSettings
    from simscale_sdk_v1.models.meshing.advanced_simmetrix_fluid_settings import AdvancedSimmetrixFluidSettings
    from simscale_sdk_v1.models.meshing.advanced_simmetrix_solid_settings import AdvancedSimmetrixSolidSettings
    from simscale_sdk_v1.models.meshing.algorithm import Algorithm
    from simscale_sdk_v1.models.meshing.automatic_curvature import AutomaticCurvature
    from simscale_sdk_v1.models.meshing.automatic_layer_off import AutomaticLayerOff
    from simscale_sdk_v1.models.meshing.automatic_layer_on import AutomaticLayerOn
    from simscale_sdk_v1.models.meshing.automatic_mesh_grading import AutomaticMeshGrading
    from simscale_sdk_v1.models.meshing.automatic_mesh_sizing import AutomaticMeshSizing
    from simscale_sdk_v1.models.meshing.automatic_mesh_sizing_hex_dominant_snappy import (
        AutomaticMeshSizingHexDominantSnappy,
    )
    from simscale_sdk_v1.models.meshing.automatic_mesh_sizing_simmetrix import AutomaticMeshSizingSimmetrix
    from simscale_sdk_v1.models.meshing.automatic_polygrid_mesh_sizing import AutomaticPolygridMeshSizing
    from simscale_sdk_v1.models.meshing.automatic_sweep_off import AutomaticSweepOff
    from simscale_sdk_v1.models.meshing.automatic_sweep_on import AutomaticSweepOn
    from simscale_sdk_v1.models.meshing.bounding_box_layer_addition import BoundingBoxLayerAddition
    from simscale_sdk_v1.models.meshing.castellated_mesh_controls import CastellatedMeshControls
    from simscale_sdk_v1.models.meshing.custom_mesh_sizing_simmetrix import CustomMeshSizingSimmetrix
    from simscale_sdk_v1.models.meshing.custom_polygrid_mesh_sizing import CustomPolygridMeshSizing
    from simscale_sdk_v1.models.meshing.debug_mesh_sizing_simmetrix import DebugMeshSizingSimmetrix
    from simscale_sdk_v1.models.meshing.dimensional__angle import Dimensional_Angle
    from simscale_sdk_v1.models.meshing.dimensional__area import Dimensional_Area
    from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length
    from simscale_sdk_v1.models.meshing.dimensional__time import Dimensional_Time
    from simscale_sdk_v1.models.meshing.dimensional__volume import Dimensional_Volume
    from simscale_sdk_v1.models.meshing.distance_region_refinement_with_length import DistanceRegionRefinementWithLength
    from simscale_sdk_v1.models.meshing.distance_region_refinement_with_levels import DistanceRegionRefinementWithLevels
    from simscale_sdk_v1.models.meshing.distance_sizing import DistanceSizing
    from simscale_sdk_v1.models.meshing.distance_volume_custom_sizing import DistanceVolumeCustomSizing
    from simscale_sdk_v1.models.meshing.feature_refinement import FeatureRefinement
    from simscale_sdk_v1.models.meshing.feature_refinement_hex_dominant_snappy import FeatureRefinementHexDominantSnappy
    from simscale_sdk_v1.models.meshing.first_layer_growth import FirstLayerGrowth
    from simscale_sdk_v1.models.meshing.fractional_height1 import FractionalHeight1
    from simscale_sdk_v1.models.meshing.fractional_height2 import FractionalHeight2
    from simscale_sdk_v1.models.meshing.geometric_growth import GeometricGrowth
    from simscale_sdk_v1.models.meshing.hex_dominant_snappy import HexDominantSnappy
    from simscale_sdk_v1.models.meshing.inside_region_refinement_with_length import InsideRegionRefinementWithLength
    from simscale_sdk_v1.models.meshing.inside_region_refinement_with_levels import InsideRegionRefinementWithLevels
    from simscale_sdk_v1.models.meshing.inside_volume_custom_sizing import InsideVolumeCustomSizing
    from simscale_sdk_v1.models.meshing.layer_adding_controls import LayerAddingControls
    from simscale_sdk_v1.models.meshing.layer_addition import LayerAddition
    from simscale_sdk_v1.models.meshing.layer_addition_hex_dominant_snappy import LayerAdditionHexDominantSnappy
    from simscale_sdk_v1.models.meshing.layer_refinement import LayerRefinement
    from simscale_sdk_v1.models.meshing.local_element_size_cf_mesh import LocalElementSizeCfMesh
    from simscale_sdk_v1.models.meshing.local_element_size_ebm import LocalElementSizeEBM
    from simscale_sdk_v1.models.meshing.manual_cf_mesh_sizing import ManualCfMeshSizing
    from simscale_sdk_v1.models.meshing.manual_mesh_grading import ManualMeshGrading
    from simscale_sdk_v1.models.meshing.manual_mesh_sizing import ManualMeshSizing
    from simscale_sdk_v1.models.meshing.manual_mesh_sizing_hex_dominant_snappy import ManualMeshSizingHexDominantSnappy
    from simscale_sdk_v1.models.meshing.manual_mesh_sizing_simmetrix import ManualMeshSizingSimmetrix
    from simscale_sdk_v1.models.meshing.manual_polygrid_mesh_sizing import ManualPolygridMeshSizing
    from simscale_sdk_v1.models.meshing.mesh_quality_controls import MeshQualityControls
    from simscale_sdk_v1.models.meshing.number_of_cells_per_direction import NumberOfCellsPerDirection
    from simscale_sdk_v1.models.meshing.one_of__automatic_layer_on_layer_type import OneOf_AutomaticLayerOnLayerType
    from simscale_sdk_v1.models.meshing.one_of__automatic_mesh_sizing_simmetrix_curvature import (
        OneOf_AutomaticMeshSizingSimmetrixCurvature,
    )
    from simscale_sdk_v1.models.meshing.one_of__custom_mesh_sizing_simmetrix_curvature import (
        OneOf_CustomMeshSizingSimmetrixCurvature,
    )
    from simscale_sdk_v1.models.meshing.one_of__distance_volume_custom_sizing_curvature import (
        OneOf_DistanceVolumeCustomSizingCurvature,
    )
    from simscale_sdk_v1.models.meshing.one_of__hex_dominant_snappy_refinements import (
        OneOf_HexDominantSnappyRefinements,
    )
    from simscale_sdk_v1.models.meshing.one_of__hex_dominant_snappy_sizing import OneOf_HexDominantSnappySizing
    from simscale_sdk_v1.models.meshing.one_of__inside_volume_custom_sizing_sizing import (
        OneOf_InsideVolumeCustomSizingSizing,
    )
    from simscale_sdk_v1.models.meshing.one_of__manual_mesh_sizing_grading import OneOf_ManualMeshSizingGrading
    from simscale_sdk_v1.models.meshing.one_of__manual_mesh_sizing_simmetrix_curvature import (
        OneOf_ManualMeshSizingSimmetrixCurvature,
    )
    from simscale_sdk_v1.models.meshing.one_of__polygrid_meshing_refinements import OneOf_PolygridMeshingRefinements
    from simscale_sdk_v1.models.meshing.one_of__polygrid_meshing_sizing import OneOf_PolygridMeshingSizing
    from simscale_sdk_v1.models.meshing.one_of__region_refinement_ebm_refinement import (
        OneOf_RegionRefinementEBMRefinement,
    )
    from simscale_sdk_v1.models.meshing.one_of__region_refinement_with_length_curvature import (
        OneOf_RegionRefinementWithLengthCurvature,
    )
    from simscale_sdk_v1.models.meshing.one_of__region_refinement_with_length_refinement import (
        OneOf_RegionRefinementWithLengthRefinement,
    )
    from simscale_sdk_v1.models.meshing.one_of__region_refinement_with_levels_refinement import (
        OneOf_RegionRefinementWithLevelsRefinement,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_boundary_layer_refinement_layer_type import (
        OneOf_SimmetrixBoundaryLayerRefinementLayerType,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_extrusion_mesh_refinement_sizing_type import (
        OneOf_SimmetrixExtrusionMeshRefinementSizingType,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_local_sizing_refinement_curvature import (
        OneOf_SimmetrixLocalSizingRefinementCurvature,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_electromagnetics_refinements import (
        OneOf_SimmetrixMeshingElectromagneticsRefinements,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_electromagnetics_sizing import (
        OneOf_SimmetrixMeshingElectromagneticsSizing,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_automatic_layer_settings import (
        OneOf_SimmetrixMeshingFluidAutomaticLayerSettings,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_automatic_sweep_parameters import (
        OneOf_SimmetrixMeshingFluidAutomaticSweepParameters,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_refinements import (
        OneOf_SimmetrixMeshingFluidRefinements,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_sizing import OneOf_SimmetrixMeshingFluidSizing
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_automatic_sweep_parameters import (
        OneOf_SimmetrixMeshingSolidAutomaticSweepParameters,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_refinements import (
        OneOf_SimmetrixMeshingSolidRefinements,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_sizing import OneOf_SimmetrixMeshingSolidSizing
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_swept_mesh_refinement_sizing_type import (
        OneOf_SimmetrixSweptMeshRefinementSizingType,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_thin_section_mesh_refinement_distance_type import (
        OneOf_SimmetrixThinSectionMeshRefinementDistanceType,
    )
    from simscale_sdk_v1.models.meshing.one_of__simmetrix_thin_section_mesh_refinement_sizing_type import (
        OneOf_SimmetrixThinSectionMeshRefinementSizingType,
    )
    from simscale_sdk_v1.models.meshing.one_of__submesh_refinement_sizing import OneOf_SubmeshRefinementSizing
    from simscale_sdk_v1.models.meshing.one_of__surface_custom_sizing_sizing import OneOf_SurfaceCustomSizingSizing
    from simscale_sdk_v1.models.meshing.one_of__surface_refinement_cell_zone import OneOf_SurfaceRefinementCellZone
    from simscale_sdk_v1.models.meshing.one_of__surface_refinement_hex_dominant_snappy_cell_zone import (
        OneOf_SurfaceRefinementHexDominantSnappyCellZone,
    )
    from simscale_sdk_v1.models.meshing.one_of__volume_custom_sizing_custom_sizing_modes import (
        OneOf_VolumeCustomSizingCustomSizingModes,
    )
    from simscale_sdk_v1.models.meshing.outside_region_refinement_with_length import OutsideRegionRefinementWithLength
    from simscale_sdk_v1.models.meshing.outside_region_refinement_with_levels import OutsideRegionRefinementWithLevels
    from simscale_sdk_v1.models.meshing.polygrid_meshing import PolygridMeshing
    from simscale_sdk_v1.models.meshing.refinement_length import RefinementLength
    from simscale_sdk_v1.models.meshing.refinement_level import RefinementLevel
    from simscale_sdk_v1.models.meshing.region_refinement_cf_mesh import RegionRefinementCfMesh
    from simscale_sdk_v1.models.meshing.region_refinement_ebm import RegionRefinementEBM
    from simscale_sdk_v1.models.meshing.region_refinement_with_length import RegionRefinementWithLength
    from simscale_sdk_v1.models.meshing.region_refinement_with_levels import RegionRefinementWithLevels
    from simscale_sdk_v1.models.meshing.relative_curvature import RelativeCurvature
    from simscale_sdk_v1.models.meshing.relative_distance import RelativeDistance
    from simscale_sdk_v1.models.meshing.resolution import Resolution
    from simscale_sdk_v1.models.meshing.simmetrix_boundary_layer_refinement import SimmetrixBoundaryLayerRefinement
    from simscale_sdk_v1.models.meshing.simmetrix_cell_zones import SimmetrixCellZones
    from simscale_sdk_v1.models.meshing.simmetrix_extrusion_mesh_refinement import SimmetrixExtrusionMeshRefinement
    from simscale_sdk_v1.models.meshing.simmetrix_local_sizing_refinement import SimmetrixLocalSizingRefinement
    from simscale_sdk_v1.models.meshing.simmetrix_meshing_electromagnetics import SimmetrixMeshingElectromagnetics
    from simscale_sdk_v1.models.meshing.simmetrix_meshing_fluid import SimmetrixMeshingFluid
    from simscale_sdk_v1.models.meshing.simmetrix_meshing_solid import SimmetrixMeshingSolid
    from simscale_sdk_v1.models.meshing.simmetrix_swept_mesh_refinement import SimmetrixSweptMeshRefinement
    from simscale_sdk_v1.models.meshing.simmetrix_thin_section_mesh_refinement import SimmetrixThinSectionMeshRefinement
    from simscale_sdk_v1.models.meshing.snap_controls import SnapControls
    from simscale_sdk_v1.models.meshing.submesh_refinement import SubmeshRefinement
    from simscale_sdk_v1.models.meshing.surface_custom_sizing import SurfaceCustomSizing
    from simscale_sdk_v1.models.meshing.surface_refinement import SurfaceRefinement
    from simscale_sdk_v1.models.meshing.surface_refinement_hex_dominant_snappy import SurfaceRefinementHexDominantSnappy
    from simscale_sdk_v1.models.meshing.sweep_meshing_absolute_size import SweepMeshingAbsoluteSize
    from simscale_sdk_v1.models.meshing.sweep_meshing_number_of_elements import SweepMeshingNumberOfElements
    from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference
    from simscale_sdk_v1.models.meshing.volume_custom_sizing import VolumeCustomSizing
    from simscale_sdk_v1.models.meshing.with_cell_zone import WithCellZone
    from simscale_sdk_v1.models.meshing.without_cell_zone import WithoutCellZone

_NAMES: dict[str, tuple[str, str]] = {
    "AbsoluteDistance": ("simscale_sdk_v1.models.meshing.absolute_distance", "AbsoluteDistance"),
    "AdvancedSimmetrixEmSettings": (
        "simscale_sdk_v1.models.meshing.advanced_simmetrix_em_settings",
        "AdvancedSimmetrixEmSettings",
    ),
    "AdvancedSimmetrixFluidSettings": (
        "simscale_sdk_v1.models.meshing.advanced_simmetrix_fluid_settings",
        "AdvancedSimmetrixFluidSettings",
    ),
    "AdvancedSimmetrixSolidSettings": (
        "simscale_sdk_v1.models.meshing.advanced_simmetrix_solid_settings",
        "AdvancedSimmetrixSolidSettings",
    ),
    "Algorithm": ("simscale_sdk_v1.models.meshing.algorithm", "Algorithm"),
    "AutomaticCurvature": ("simscale_sdk_v1.models.meshing.automatic_curvature", "AutomaticCurvature"),
    "AutomaticLayerOff": ("simscale_sdk_v1.models.meshing.automatic_layer_off", "AutomaticLayerOff"),
    "AutomaticLayerOn": ("simscale_sdk_v1.models.meshing.automatic_layer_on", "AutomaticLayerOn"),
    "AutomaticMeshGrading": ("simscale_sdk_v1.models.meshing.automatic_mesh_grading", "AutomaticMeshGrading"),
    "AutomaticMeshSizing": ("simscale_sdk_v1.models.meshing.automatic_mesh_sizing", "AutomaticMeshSizing"),
    "AutomaticMeshSizingHexDominantSnappy": (
        "simscale_sdk_v1.models.meshing.automatic_mesh_sizing_hex_dominant_snappy",
        "AutomaticMeshSizingHexDominantSnappy",
    ),
    "AutomaticMeshSizingSimmetrix": (
        "simscale_sdk_v1.models.meshing.automatic_mesh_sizing_simmetrix",
        "AutomaticMeshSizingSimmetrix",
    ),
    "AutomaticPolygridMeshSizing": (
        "simscale_sdk_v1.models.meshing.automatic_polygrid_mesh_sizing",
        "AutomaticPolygridMeshSizing",
    ),
    "AutomaticSweepOff": ("simscale_sdk_v1.models.meshing.automatic_sweep_off", "AutomaticSweepOff"),
    "AutomaticSweepOn": ("simscale_sdk_v1.models.meshing.automatic_sweep_on", "AutomaticSweepOn"),
    "BoundingBoxLayerAddition": (
        "simscale_sdk_v1.models.meshing.bounding_box_layer_addition",
        "BoundingBoxLayerAddition",
    ),
    "CastellatedMeshControls": ("simscale_sdk_v1.models.meshing.castellated_mesh_controls", "CastellatedMeshControls"),
    "CustomMeshSizingSimmetrix": (
        "simscale_sdk_v1.models.meshing.custom_mesh_sizing_simmetrix",
        "CustomMeshSizingSimmetrix",
    ),
    "CustomPolygridMeshSizing": (
        "simscale_sdk_v1.models.meshing.custom_polygrid_mesh_sizing",
        "CustomPolygridMeshSizing",
    ),
    "DebugMeshSizingSimmetrix": (
        "simscale_sdk_v1.models.meshing.debug_mesh_sizing_simmetrix",
        "DebugMeshSizingSimmetrix",
    ),
    "Dimensional_Angle": ("simscale_sdk_v1.models.meshing.dimensional__angle", "Dimensional_Angle"),
    "Dimensional_Area": ("simscale_sdk_v1.models.meshing.dimensional__area", "Dimensional_Area"),
    "Dimensional_Length": ("simscale_sdk_v1.models.meshing.dimensional__length", "Dimensional_Length"),
    "Dimensional_Time": ("simscale_sdk_v1.models.meshing.dimensional__time", "Dimensional_Time"),
    "Dimensional_Volume": ("simscale_sdk_v1.models.meshing.dimensional__volume", "Dimensional_Volume"),
    "DistanceRegionRefinementWithLength": (
        "simscale_sdk_v1.models.meshing.distance_region_refinement_with_length",
        "DistanceRegionRefinementWithLength",
    ),
    "DistanceRegionRefinementWithLevels": (
        "simscale_sdk_v1.models.meshing.distance_region_refinement_with_levels",
        "DistanceRegionRefinementWithLevels",
    ),
    "DistanceSizing": ("simscale_sdk_v1.models.meshing.distance_sizing", "DistanceSizing"),
    "DistanceVolumeCustomSizing": (
        "simscale_sdk_v1.models.meshing.distance_volume_custom_sizing",
        "DistanceVolumeCustomSizing",
    ),
    "FeatureRefinement": ("simscale_sdk_v1.models.meshing.feature_refinement", "FeatureRefinement"),
    "FeatureRefinementHexDominantSnappy": (
        "simscale_sdk_v1.models.meshing.feature_refinement_hex_dominant_snappy",
        "FeatureRefinementHexDominantSnappy",
    ),
    "FirstLayerGrowth": ("simscale_sdk_v1.models.meshing.first_layer_growth", "FirstLayerGrowth"),
    "FractionalHeight1": ("simscale_sdk_v1.models.meshing.fractional_height1", "FractionalHeight1"),
    "FractionalHeight2": ("simscale_sdk_v1.models.meshing.fractional_height2", "FractionalHeight2"),
    "GeometricGrowth": ("simscale_sdk_v1.models.meshing.geometric_growth", "GeometricGrowth"),
    "HexDominantSnappy": ("simscale_sdk_v1.models.meshing.hex_dominant_snappy", "HexDominantSnappy"),
    "InsideRegionRefinementWithLength": (
        "simscale_sdk_v1.models.meshing.inside_region_refinement_with_length",
        "InsideRegionRefinementWithLength",
    ),
    "InsideRegionRefinementWithLevels": (
        "simscale_sdk_v1.models.meshing.inside_region_refinement_with_levels",
        "InsideRegionRefinementWithLevels",
    ),
    "InsideVolumeCustomSizing": (
        "simscale_sdk_v1.models.meshing.inside_volume_custom_sizing",
        "InsideVolumeCustomSizing",
    ),
    "LayerAddingControls": ("simscale_sdk_v1.models.meshing.layer_adding_controls", "LayerAddingControls"),
    "LayerAddition": ("simscale_sdk_v1.models.meshing.layer_addition", "LayerAddition"),
    "LayerAdditionHexDominantSnappy": (
        "simscale_sdk_v1.models.meshing.layer_addition_hex_dominant_snappy",
        "LayerAdditionHexDominantSnappy",
    ),
    "LayerRefinement": ("simscale_sdk_v1.models.meshing.layer_refinement", "LayerRefinement"),
    "LocalElementSizeCfMesh": ("simscale_sdk_v1.models.meshing.local_element_size_cf_mesh", "LocalElementSizeCfMesh"),
    "LocalElementSizeEBM": ("simscale_sdk_v1.models.meshing.local_element_size_ebm", "LocalElementSizeEBM"),
    "ManualCfMeshSizing": ("simscale_sdk_v1.models.meshing.manual_cf_mesh_sizing", "ManualCfMeshSizing"),
    "ManualMeshGrading": ("simscale_sdk_v1.models.meshing.manual_mesh_grading", "ManualMeshGrading"),
    "ManualMeshSizing": ("simscale_sdk_v1.models.meshing.manual_mesh_sizing", "ManualMeshSizing"),
    "ManualMeshSizingHexDominantSnappy": (
        "simscale_sdk_v1.models.meshing.manual_mesh_sizing_hex_dominant_snappy",
        "ManualMeshSizingHexDominantSnappy",
    ),
    "ManualMeshSizingSimmetrix": (
        "simscale_sdk_v1.models.meshing.manual_mesh_sizing_simmetrix",
        "ManualMeshSizingSimmetrix",
    ),
    "ManualPolygridMeshSizing": (
        "simscale_sdk_v1.models.meshing.manual_polygrid_mesh_sizing",
        "ManualPolygridMeshSizing",
    ),
    "MeshQualityControls": ("simscale_sdk_v1.models.meshing.mesh_quality_controls", "MeshQualityControls"),
    "NumberOfCellsPerDirection": (
        "simscale_sdk_v1.models.meshing.number_of_cells_per_direction",
        "NumberOfCellsPerDirection",
    ),
    "OneOf_AutomaticLayerOnLayerType": (
        "simscale_sdk_v1.models.meshing.one_of__automatic_layer_on_layer_type",
        "OneOf_AutomaticLayerOnLayerType",
    ),
    "OneOf_AutomaticMeshSizingSimmetrixCurvature": (
        "simscale_sdk_v1.models.meshing.one_of__automatic_mesh_sizing_simmetrix_curvature",
        "OneOf_AutomaticMeshSizingSimmetrixCurvature",
    ),
    "OneOf_CustomMeshSizingSimmetrixCurvature": (
        "simscale_sdk_v1.models.meshing.one_of__custom_mesh_sizing_simmetrix_curvature",
        "OneOf_CustomMeshSizingSimmetrixCurvature",
    ),
    "OneOf_DistanceVolumeCustomSizingCurvature": (
        "simscale_sdk_v1.models.meshing.one_of__distance_volume_custom_sizing_curvature",
        "OneOf_DistanceVolumeCustomSizingCurvature",
    ),
    "OneOf_HexDominantSnappyRefinements": (
        "simscale_sdk_v1.models.meshing.one_of__hex_dominant_snappy_refinements",
        "OneOf_HexDominantSnappyRefinements",
    ),
    "OneOf_HexDominantSnappySizing": (
        "simscale_sdk_v1.models.meshing.one_of__hex_dominant_snappy_sizing",
        "OneOf_HexDominantSnappySizing",
    ),
    "OneOf_InsideVolumeCustomSizingSizing": (
        "simscale_sdk_v1.models.meshing.one_of__inside_volume_custom_sizing_sizing",
        "OneOf_InsideVolumeCustomSizingSizing",
    ),
    "OneOf_ManualMeshSizingGrading": (
        "simscale_sdk_v1.models.meshing.one_of__manual_mesh_sizing_grading",
        "OneOf_ManualMeshSizingGrading",
    ),
    "OneOf_ManualMeshSizingSimmetrixCurvature": (
        "simscale_sdk_v1.models.meshing.one_of__manual_mesh_sizing_simmetrix_curvature",
        "OneOf_ManualMeshSizingSimmetrixCurvature",
    ),
    "OneOf_PolygridMeshingRefinements": (
        "simscale_sdk_v1.models.meshing.one_of__polygrid_meshing_refinements",
        "OneOf_PolygridMeshingRefinements",
    ),
    "OneOf_PolygridMeshingSizing": (
        "simscale_sdk_v1.models.meshing.one_of__polygrid_meshing_sizing",
        "OneOf_PolygridMeshingSizing",
    ),
    "OneOf_RegionRefinementEBMRefinement": (
        "simscale_sdk_v1.models.meshing.one_of__region_refinement_ebm_refinement",
        "OneOf_RegionRefinementEBMRefinement",
    ),
    "OneOf_RegionRefinementWithLengthCurvature": (
        "simscale_sdk_v1.models.meshing.one_of__region_refinement_with_length_curvature",
        "OneOf_RegionRefinementWithLengthCurvature",
    ),
    "OneOf_RegionRefinementWithLengthRefinement": (
        "simscale_sdk_v1.models.meshing.one_of__region_refinement_with_length_refinement",
        "OneOf_RegionRefinementWithLengthRefinement",
    ),
    "OneOf_RegionRefinementWithLevelsRefinement": (
        "simscale_sdk_v1.models.meshing.one_of__region_refinement_with_levels_refinement",
        "OneOf_RegionRefinementWithLevelsRefinement",
    ),
    "OneOf_SimmetrixBoundaryLayerRefinementLayerType": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_boundary_layer_refinement_layer_type",
        "OneOf_SimmetrixBoundaryLayerRefinementLayerType",
    ),
    "OneOf_SimmetrixExtrusionMeshRefinementSizingType": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_extrusion_mesh_refinement_sizing_type",
        "OneOf_SimmetrixExtrusionMeshRefinementSizingType",
    ),
    "OneOf_SimmetrixLocalSizingRefinementCurvature": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_local_sizing_refinement_curvature",
        "OneOf_SimmetrixLocalSizingRefinementCurvature",
    ),
    "OneOf_SimmetrixMeshingElectromagneticsRefinements": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_electromagnetics_refinements",
        "OneOf_SimmetrixMeshingElectromagneticsRefinements",
    ),
    "OneOf_SimmetrixMeshingElectromagneticsSizing": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_electromagnetics_sizing",
        "OneOf_SimmetrixMeshingElectromagneticsSizing",
    ),
    "OneOf_SimmetrixMeshingFluidAutomaticLayerSettings": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_automatic_layer_settings",
        "OneOf_SimmetrixMeshingFluidAutomaticLayerSettings",
    ),
    "OneOf_SimmetrixMeshingFluidAutomaticSweepParameters": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_automatic_sweep_parameters",
        "OneOf_SimmetrixMeshingFluidAutomaticSweepParameters",
    ),
    "OneOf_SimmetrixMeshingFluidRefinements": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_refinements",
        "OneOf_SimmetrixMeshingFluidRefinements",
    ),
    "OneOf_SimmetrixMeshingFluidSizing": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_fluid_sizing",
        "OneOf_SimmetrixMeshingFluidSizing",
    ),
    "OneOf_SimmetrixMeshingSolidAutomaticSweepParameters": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_automatic_sweep_parameters",
        "OneOf_SimmetrixMeshingSolidAutomaticSweepParameters",
    ),
    "OneOf_SimmetrixMeshingSolidRefinements": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_refinements",
        "OneOf_SimmetrixMeshingSolidRefinements",
    ),
    "OneOf_SimmetrixMeshingSolidSizing": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_meshing_solid_sizing",
        "OneOf_SimmetrixMeshingSolidSizing",
    ),
    "OneOf_SimmetrixSweptMeshRefinementSizingType": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_swept_mesh_refinement_sizing_type",
        "OneOf_SimmetrixSweptMeshRefinementSizingType",
    ),
    "OneOf_SimmetrixThinSectionMeshRefinementDistanceType": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_thin_section_mesh_refinement_distance_type",
        "OneOf_SimmetrixThinSectionMeshRefinementDistanceType",
    ),
    "OneOf_SimmetrixThinSectionMeshRefinementSizingType": (
        "simscale_sdk_v1.models.meshing.one_of__simmetrix_thin_section_mesh_refinement_sizing_type",
        "OneOf_SimmetrixThinSectionMeshRefinementSizingType",
    ),
    "OneOf_SubmeshRefinementSizing": (
        "simscale_sdk_v1.models.meshing.one_of__submesh_refinement_sizing",
        "OneOf_SubmeshRefinementSizing",
    ),
    "OneOf_SurfaceCustomSizingSizing": (
        "simscale_sdk_v1.models.meshing.one_of__surface_custom_sizing_sizing",
        "OneOf_SurfaceCustomSizingSizing",
    ),
    "OneOf_SurfaceRefinementCellZone": (
        "simscale_sdk_v1.models.meshing.one_of__surface_refinement_cell_zone",
        "OneOf_SurfaceRefinementCellZone",
    ),
    "OneOf_SurfaceRefinementHexDominantSnappyCellZone": (
        "simscale_sdk_v1.models.meshing.one_of__surface_refinement_hex_dominant_snappy_cell_zone",
        "OneOf_SurfaceRefinementHexDominantSnappyCellZone",
    ),
    "OneOf_VolumeCustomSizingCustomSizingModes": (
        "simscale_sdk_v1.models.meshing.one_of__volume_custom_sizing_custom_sizing_modes",
        "OneOf_VolumeCustomSizingCustomSizingModes",
    ),
    "OutsideRegionRefinementWithLength": (
        "simscale_sdk_v1.models.meshing.outside_region_refinement_with_length",
        "OutsideRegionRefinementWithLength",
    ),
    "OutsideRegionRefinementWithLevels": (
        "simscale_sdk_v1.models.meshing.outside_region_refinement_with_levels",
        "OutsideRegionRefinementWithLevels",
    ),
    "PolygridMeshing": ("simscale_sdk_v1.models.meshing.polygrid_meshing", "PolygridMeshing"),
    "RefinementLength": ("simscale_sdk_v1.models.meshing.refinement_length", "RefinementLength"),
    "RefinementLevel": ("simscale_sdk_v1.models.meshing.refinement_level", "RefinementLevel"),
    "RegionRefinementCfMesh": ("simscale_sdk_v1.models.meshing.region_refinement_cf_mesh", "RegionRefinementCfMesh"),
    "RegionRefinementEBM": ("simscale_sdk_v1.models.meshing.region_refinement_ebm", "RegionRefinementEBM"),
    "RegionRefinementWithLength": (
        "simscale_sdk_v1.models.meshing.region_refinement_with_length",
        "RegionRefinementWithLength",
    ),
    "RegionRefinementWithLevels": (
        "simscale_sdk_v1.models.meshing.region_refinement_with_levels",
        "RegionRefinementWithLevels",
    ),
    "RelativeCurvature": ("simscale_sdk_v1.models.meshing.relative_curvature", "RelativeCurvature"),
    "RelativeDistance": ("simscale_sdk_v1.models.meshing.relative_distance", "RelativeDistance"),
    "Resolution": ("simscale_sdk_v1.models.meshing.resolution", "Resolution"),
    "SimmetrixBoundaryLayerRefinement": (
        "simscale_sdk_v1.models.meshing.simmetrix_boundary_layer_refinement",
        "SimmetrixBoundaryLayerRefinement",
    ),
    "SimmetrixCellZones": ("simscale_sdk_v1.models.meshing.simmetrix_cell_zones", "SimmetrixCellZones"),
    "SimmetrixExtrusionMeshRefinement": (
        "simscale_sdk_v1.models.meshing.simmetrix_extrusion_mesh_refinement",
        "SimmetrixExtrusionMeshRefinement",
    ),
    "SimmetrixLocalSizingRefinement": (
        "simscale_sdk_v1.models.meshing.simmetrix_local_sizing_refinement",
        "SimmetrixLocalSizingRefinement",
    ),
    "SimmetrixMeshingElectromagnetics": (
        "simscale_sdk_v1.models.meshing.simmetrix_meshing_electromagnetics",
        "SimmetrixMeshingElectromagnetics",
    ),
    "SimmetrixMeshingFluid": ("simscale_sdk_v1.models.meshing.simmetrix_meshing_fluid", "SimmetrixMeshingFluid"),
    "SimmetrixMeshingSolid": ("simscale_sdk_v1.models.meshing.simmetrix_meshing_solid", "SimmetrixMeshingSolid"),
    "SimmetrixSweptMeshRefinement": (
        "simscale_sdk_v1.models.meshing.simmetrix_swept_mesh_refinement",
        "SimmetrixSweptMeshRefinement",
    ),
    "SimmetrixThinSectionMeshRefinement": (
        "simscale_sdk_v1.models.meshing.simmetrix_thin_section_mesh_refinement",
        "SimmetrixThinSectionMeshRefinement",
    ),
    "SnapControls": ("simscale_sdk_v1.models.meshing.snap_controls", "SnapControls"),
    "SubmeshRefinement": ("simscale_sdk_v1.models.meshing.submesh_refinement", "SubmeshRefinement"),
    "SurfaceCustomSizing": ("simscale_sdk_v1.models.meshing.surface_custom_sizing", "SurfaceCustomSizing"),
    "SurfaceRefinement": ("simscale_sdk_v1.models.meshing.surface_refinement", "SurfaceRefinement"),
    "SurfaceRefinementHexDominantSnappy": (
        "simscale_sdk_v1.models.meshing.surface_refinement_hex_dominant_snappy",
        "SurfaceRefinementHexDominantSnappy",
    ),
    "SweepMeshingAbsoluteSize": (
        "simscale_sdk_v1.models.meshing.sweep_meshing_absolute_size",
        "SweepMeshingAbsoluteSize",
    ),
    "SweepMeshingNumberOfElements": (
        "simscale_sdk_v1.models.meshing.sweep_meshing_number_of_elements",
        "SweepMeshingNumberOfElements",
    ),
    "TopologicalReference": ("simscale_sdk_v1.models.meshing.topological_reference", "TopologicalReference"),
    "VolumeCustomSizing": ("simscale_sdk_v1.models.meshing.volume_custom_sizing", "VolumeCustomSizing"),
    "WithCellZone": ("simscale_sdk_v1.models.meshing.with_cell_zone", "WithCellZone"),
    "WithoutCellZone": ("simscale_sdk_v1.models.meshing.without_cell_zone", "WithoutCellZone"),
}


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys())
