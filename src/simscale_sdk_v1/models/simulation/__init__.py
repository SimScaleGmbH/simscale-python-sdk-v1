"""Generated Simulation models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.simulation.ami_rotating_zone import AMIRotatingZone
    from simscale_sdk_v1.models.simulation.absolute_convergence_criteria import AbsoluteConvergenceCriteria
    from simscale_sdk_v1.models.simulation.absolute_convergence_displacements import AbsoluteConvergenceDisplacements
    from simscale_sdk_v1.models.simulation.absolute_convergence_residuals import AbsoluteConvergenceResiduals
    from simscale_sdk_v1.models.simulation.absolute_convergence_residuals_or_displacements import (
        AbsoluteConvergenceResidualsOrDisplacements,
    )
    from simscale_sdk_v1.models.simulation.absolute_erp_field_selection import AbsoluteERPFieldSelection
    from simscale_sdk_v1.models.simulation.absolute_harmonic_acceleration_field_type import (
        AbsoluteHarmonicAccelerationFieldType,
    )
    from simscale_sdk_v1.models.simulation.absolute_harmonic_acceleration_type import AbsoluteHarmonicAccelerationType
    from simscale_sdk_v1.models.simulation.absolute_harmonic_displacement_field_type import (
        AbsoluteHarmonicDisplacementFieldType,
    )
    from simscale_sdk_v1.models.simulation.absolute_harmonic_displacement_type import AbsoluteHarmonicDisplacementType
    from simscale_sdk_v1.models.simulation.absolute_harmonic_velocity_field_type import (
        AbsoluteHarmonicVelocityFieldType,
    )
    from simscale_sdk_v1.models.simulation.absolute_harmonic_velocity_type import AbsoluteHarmonicVelocityType
    from simscale_sdk_v1.models.simulation.absolute_humidity_value import AbsoluteHumidityValue
    from simscale_sdk_v1.models.simulation.absolute_passive_scalar_source import AbsolutePassiveScalarSource
    from simscale_sdk_v1.models.simulation.absolute_power_source import AbsolutePowerSource
    from simscale_sdk_v1.models.simulation.absolute_to_all_cad_surfaces_settings import AbsoluteToAllCadSurfacesSettings
    from simscale_sdk_v1.models.simulation.acceleration_field_selection import AccelerationFieldSelection
    from simscale_sdk_v1.models.simulation.acceleration_result_control_item import AccelerationResultControlItem
    from simscale_sdk_v1.models.simulation.active_adjustable_timestep import ActiveAdjustableTimestep
    from simscale_sdk_v1.models.simulation.adaptive_augmentation import AdaptiveAugmentation
    from simscale_sdk_v1.models.simulation.adaptive_convergence_criteria import AdaptiveConvergenceCriteria
    from simscale_sdk_v1.models.simulation.adaptive_convergence_displacements import AdaptiveConvergenceDisplacements
    from simscale_sdk_v1.models.simulation.adaptive_convergence_residuals import AdaptiveConvergenceResiduals
    from simscale_sdk_v1.models.simulation.adaptive_convergence_residuals_or_displacements import (
        AdaptiveConvergenceResidualsOrDisplacements,
    )
    from simscale_sdk_v1.models.simulation.additional_directional_cells import AdditionalDirectionalCells
    from simscale_sdk_v1.models.simulation.adiabatic_interface_thermal import AdiabaticInterfaceThermal
    from simscale_sdk_v1.models.simulation.adiabatic_perfect_fluid_equation_of_state import (
        AdiabaticPerfectFluidEquationOfState,
    )
    from simscale_sdk_v1.models.simulation.adiabatic_tbc import AdiabaticTBC
    from simscale_sdk_v1.models.simulation.adjustable_runtime_write_control import AdjustableRuntimeWriteControl
    from simscale_sdk_v1.models.simulation.advanced_chronos_settings import AdvancedChronosSettings
    from simscale_sdk_v1.models.simulation.advanced_comfort_criterion_settings import AdvancedComfortCriterionSettings
    from simscale_sdk_v1.models.simulation.advanced_concepts import AdvancedConcepts
    from simscale_sdk_v1.models.simulation.advanced_connector_settings import AdvancedConnectorSettings
    from simscale_sdk_v1.models.simulation.advanced_mumps_settings import AdvancedMUMPSSettings
    from simscale_sdk_v1.models.simulation.advanced_modelling import AdvancedModelling
    from simscale_sdk_v1.models.simulation.advanced_petsc_settings import AdvancedPETSCSettings
    from simscale_sdk_v1.models.simulation.advanced_roi_settings import AdvancedROISettings
    from simscale_sdk_v1.models.simulation.advective_pbc import AdvectivePBC
    from simscale_sdk_v1.models.simulation.advective_vbc import AdvectiveVBC
    from simscale_sdk_v1.models.simulation.aerodynamic_roughness import AerodynamicRoughness
    from simscale_sdk_v1.models.simulation.all_computed import AllComputed
    from simscale_sdk_v1.models.simulation.all_computed_write_control import AllComputedWriteControl
    from simscale_sdk_v1.models.simulation.all_connector_point_data_results import AllConnectorPointDataResults
    from simscale_sdk_v1.models.simulation.allowed_direction import AllowedDirection
    from simscale_sdk_v1.models.simulation.ambient_pbc import AmbientPBC
    from simscale_sdk_v1.models.simulation.ambient_tbc import AmbientTBC
    from simscale_sdk_v1.models.simulation.analysis import Analysis
    from simscale_sdk_v1.models.simulation.angular_rotation import AngularRotation
    from simscale_sdk_v1.models.simulation.area_average_result_control import AreaAverageResultControl
    from simscale_sdk_v1.models.simulation.area_density_mass import AreaDensityMass
    from simscale_sdk_v1.models.simulation.area_integral_result_control import AreaIntegralResultControl
    from simscale_sdk_v1.models.simulation.arruda_boyce_plastic_elastoplastic_network import (
        ArrudaBoycePlasticElastoplasticNetwork,
    )
    from simscale_sdk_v1.models.simulation.atmospheric_boundary_layer_inlet_bc import AtmosphericBoundaryLayerInletBC
    from simscale_sdk_v1.models.simulation.augmented_lagrange_method import AugmentedLagrangeMethod
    from simscale_sdk_v1.models.simulation.auto_timestep_definition import AutoTimestepDefinition
    from simscale_sdk_v1.models.simulation.automatic_acceleration import AutomaticAcceleration
    from simscale_sdk_v1.models.simulation.automatic_axis_definition import AutomaticAxisDefinition
    from simscale_sdk_v1.models.simulation.automatic_domain_decomposition import AutomaticDomainDecomposition
    from simscale_sdk_v1.models.simulation.automatic_element_definition_method import AutomaticElementDefinitionMethod
    from simscale_sdk_v1.models.simulation.automatic_embedded_boundary_mesh_sizing import (
        AutomaticEmbeddedBoundaryMeshSizing,
    )
    from simscale_sdk_v1.models.simulation.automatic_mesh_sizing import AutomaticMeshSizing
    from simscale_sdk_v1.models.simulation.automatic_omega_dissipation import AutomaticOmegaDissipation
    from simscale_sdk_v1.models.simulation.automatic_reactualization import AutomaticReactualization
    from simscale_sdk_v1.models.simulation.automatic_reference_length import AutomaticReferenceLength
    from simscale_sdk_v1.models.simulation.automatic_reynolds_scaling import AutomaticReynoldsScaling
    from simscale_sdk_v1.models.simulation.automatic_simerics_mesh_settings import AutomaticSimericsMeshSettings
    from simscale_sdk_v1.models.simulation.automatic_subspace_settings import AutomaticSubspaceSettings
    from simscale_sdk_v1.models.simulation.automatic_time_step_defintion import AutomaticTimeStepDefintion
    from simscale_sdk_v1.models.simulation.automatic_turbulence import AutomaticTurbulence
    from simscale_sdk_v1.models.simulation.average_fields_calculation_result_control_item import (
        AverageFieldsCalculationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.average_velocity_momentum_source import AverageVelocityMomentumSource
    from simscale_sdk_v1.models.simulation.base_excitation_bc import BaseExcitationBC
    from simscale_sdk_v1.models.simulation.bathe_wilson import BatheWilson
    from simscale_sdk_v1.models.simulation.bilinear_elasto_plastic_model import BilinearElastoPlasticModel
    from simscale_sdk_v1.models.simulation.bilinear_model_marc import BilinearModelMarc
    from simscale_sdk_v1.models.simulation.bird_carreau_viscosity_model import BirdCarreauViscosityModel
    from simscale_sdk_v1.models.simulation.blocked_direction import BlockedDirection
    from simscale_sdk_v1.models.simulation.bolt_connector import BoltConnector
    from simscale_sdk_v1.models.simulation.bolt_mechanical_properties import BoltMechanicalProperties
    from simscale_sdk_v1.models.simulation.bolt_preload_bc import BoltPreloadBC
    from simscale_sdk_v1.models.simulation.bonded_contact import BondedContact
    from simscale_sdk_v1.models.simulation.bounded_gauss_upwind_divergence_scheme import (
        BoundedGaussUpwindDivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.buildings_of_interest import BuildingsOfInterest
    from simscale_sdk_v1.models.simulation.calculate_frequency import CalculateFrequency
    from simscale_sdk_v1.models.simulation.calculated_dvbc import CalculatedDVBC
    from simscale_sdk_v1.models.simulation.calculated_evbc import CalculatedEVBC
    from simscale_sdk_v1.models.simulation.calculated_evcbc import CalculatedEVCBC
    from simscale_sdk_v1.models.simulation.calculated_tdbc import CalculatedTDBC
    from simscale_sdk_v1.models.simulation.calculated_tdcbc import CalculatedTDCBC
    from simscale_sdk_v1.models.simulation.cartesian_orientation import CartesianOrientation
    from simscale_sdk_v1.models.simulation.cauchy_stress import CauchyStress
    from simscale_sdk_v1.models.simulation.cauchy_stress_tensor_field import CauchyStressTensorField
    from simscale_sdk_v1.models.simulation.cauchy_stress_type import CauchyStressType
    from simscale_sdk_v1.models.simulation.cavitation import Cavitation
    from simscale_sdk_v1.models.simulation.celllimited_gauss_linear_gradient_scheme import (
        CelllimitedGaussLinearGradientScheme,
    )
    from simscale_sdk_v1.models.simulation.celllimited_least_squares_gradient_scheme import (
        CelllimitedLeastSquaresGradientScheme,
    )
    from simscale_sdk_v1.models.simulation.center_frequency import CenterFrequency
    from simscale_sdk_v1.models.simulation.central_diff_time_integration_scheme import CentralDiffTimeIntegrationScheme
    from simscale_sdk_v1.models.simulation.central_difference_spatial_scheme import CentralDifferenceSpatialScheme
    from simscale_sdk_v1.models.simulation.centralized_domain_decomposition import CentralizedDomainDecomposition
    from simscale_sdk_v1.models.simulation.centrifugal_force_bc import CentrifugalForceBC
    from simscale_sdk_v1.models.simulation.charge_density import ChargeDensity
    from simscale_sdk_v1.models.simulation.chestnut import Chestnut
    from simscale_sdk_v1.models.simulation.chronos_solver import ChronosSolver
    from simscale_sdk_v1.models.simulation.circular_hole_shape import CircularHoleShape
    from simscale_sdk_v1.models.simulation.clock_time_write_control import ClockTimeWriteControl
    from simscale_sdk_v1.models.simulation.closed_coil import ClosedCoil
    from simscale_sdk_v1.models.simulation.cluster_around_modes import ClusterAroundModes
    from simscale_sdk_v1.models.simulation.coarse_resolution import CoarseResolution
    from simscale_sdk_v1.models.simulation.coil import Coil
    from simscale_sdk_v1.models.simulation.collision_retiming_event import CollisionRetimingEvent
    from simscale_sdk_v1.models.simulation.combined_plastic_hardening_marc import CombinedPlasticHardeningMarc
    from simscale_sdk_v1.models.simulation.comfort_criterion_definition_v2 import ComfortCriterionDefinitionV2
    from simscale_sdk_v1.models.simulation.component_vector_function import ComponentVectorFunction
    from simscale_sdk_v1.models.simulation.compressible import Compressible
    from simscale_sdk_v1.models.simulation.compressible_fluid_materials import CompressibleFluidMaterials
    from simscale_sdk_v1.models.simulation.computing_core import ComputingCore
    from simscale_sdk_v1.models.simulation.conductivity_thickness_pair import ConductivityThicknessPair
    from simscale_sdk_v1.models.simulation.conjugate_heat_transfer import ConjugateHeatTransfer
    from simscale_sdk_v1.models.simulation.conjugate_heat_transfer_materials import ConjugateHeatTransferMaterials
    from simscale_sdk_v1.models.simulation.connection_settings_v36 import ConnectionSettingsV36
    from simscale_sdk_v1.models.simulation.const_an_iso_transport import ConstAnIsoTransport
    from simscale_sdk_v1.models.simulation.const_cross_plane_orthotropic_transport import (
        ConstCrossPlaneOrthotropicTransport,
    )
    from simscale_sdk_v1.models.simulation.const_iso_transport import ConstIsoTransport
    from simscale_sdk_v1.models.simulation.const_transport import ConstTransport
    from simscale_sdk_v1.models.simulation.constant_contact_angle_pfbc import ConstantContactAnglePFBC
    from simscale_sdk_v1.models.simulation.constant_function import ConstantFunction
    from simscale_sdk_v1.models.simulation.contact import Contact
    from simscale_sdk_v1.models.simulation.contact_conductance_layer import ContactConductanceLayer
    from simscale_sdk_v1.models.simulation.contact_field_selection import ContactFieldSelection
    from simscale_sdk_v1.models.simulation.contact_gap_type import ContactGapType
    from simscale_sdk_v1.models.simulation.contact_interface_material_interface_thermal import (
        ContactInterfaceMaterialInterfaceThermal,
    )
    from simscale_sdk_v1.models.simulation.contact_normal_force_type import ContactNormalForceType
    from simscale_sdk_v1.models.simulation.contact_pressure_type import ContactPressureType
    from simscale_sdk_v1.models.simulation.contact_resistance_layer import ContactResistanceLayer
    from simscale_sdk_v1.models.simulation.contact_result_control_item import ContactResultControlItem
    from simscale_sdk_v1.models.simulation.contact_state_type import ContactStateType
    from simscale_sdk_v1.models.simulation.convection_radiation_tbc import ConvectionRadiationTBC
    from simscale_sdk_v1.models.simulation.convection_tbc import ConvectionTBC
    from simscale_sdk_v1.models.simulation.convective_heat_flux import ConvectiveHeatFlux
    from simscale_sdk_v1.models.simulation.convective_heat_flux_bc import ConvectiveHeatFluxBC
    from simscale_sdk_v1.models.simulation.convective_heat_transfer import ConvectiveHeatTransfer
    from simscale_sdk_v1.models.simulation.convective_heat_transfer_materials import ConvectiveHeatTransferMaterials
    from simscale_sdk_v1.models.simulation.corrected_surface_normal_gradient_scheme import (
        CorrectedSurfaceNormalGradientScheme,
    )
    from simscale_sdk_v1.models.simulation.coulomb_friction import CoulombFriction
    from simscale_sdk_v1.models.simulation.coupled_conjugate_heat_transfer import CoupledConjugateHeatTransfer
    from simscale_sdk_v1.models.simulation.coupled_conjugate_heat_transfer_materials import (
        CoupledConjugateHeatTransferMaterials,
    )
    from simscale_sdk_v1.models.simulation.coupled_interface_thermal import CoupledInterfaceThermal
    from simscale_sdk_v1.models.simulation.cover_spectrum import CoverSpectrum
    from simscale_sdk_v1.models.simulation.cpu_time_write_control import CpuTimeWriteControl
    from simscale_sdk_v1.models.simulation.cross_plane_custom_orientation import CrossPlaneCustomOrientation
    from simscale_sdk_v1.models.simulation.cross_plane_orthotropic_conductivity import CrossPlaneOrthotropicConductivity
    from simscale_sdk_v1.models.simulation.cross_power_law_viscosity_model import CrossPowerLawViscosityModel
    from simscale_sdk_v1.models.simulation.cube_root_vol_les_delta import CubeRootVolLesDelta
    from simscale_sdk_v1.models.simulation.cubic_interpolation_scheme import CubicInterpolationScheme
    from simscale_sdk_v1.models.simulation.current_excitation import CurrentExcitation
    from simscale_sdk_v1.models.simulation.current_inflow_ebc import CurrentInflowEBC
    from simscale_sdk_v1.models.simulation.current_outflow_ebc import CurrentOutflowEBC
    from simscale_sdk_v1.models.simulation.custom_axis_definition import CustomAxisDefinition
    from simscale_sdk_v1.models.simulation.custom_comfort_criterion_result_control import (
        CustomComfortCriterionResultControl,
    )
    from simscale_sdk_v1.models.simulation.custom_connector_point_data_results import CustomConnectorPointDataResults
    from simscale_sdk_v1.models.simulation.custom_contact_stiffness import CustomContactStiffness
    from simscale_sdk_v1.models.simulation.custom_domain_decomposition import CustomDomainDecomposition
    from simscale_sdk_v1.models.simulation.custom_element_definition_method import CustomElementDefinitionMethod
    from simscale_sdk_v1.models.simulation.custom_embedded_boundary_mesh_sizing import CustomEmbeddedBoundaryMeshSizing
    from simscale_sdk_v1.models.simulation.custom_fluid_bc import CustomFluidBC
    from simscale_sdk_v1.models.simulation.custom_fraction_body_surface import CustomFractionBodySurface
    from simscale_sdk_v1.models.simulation.custom_omega_dissipation import CustomOmegaDissipation
    from simscale_sdk_v1.models.simulation.custom_orientation import CustomOrientation
    from simscale_sdk_v1.models.simulation.custom_resolution import CustomResolution
    from simscale_sdk_v1.models.simulation.custom_solar_load import CustomSolarLoad
    from simscale_sdk_v1.models.simulation.custom_sun_direction import CustomSunDirection
    from simscale_sdk_v1.models.simulation.custom_tree import CustomTree
    from simscale_sdk_v1.models.simulation.cyclic_symmetry_bc import CyclicSymmetryBC
    from simscale_sdk_v1.models.simulation.dic_preconditioner import DICPreconditioner
    from simscale_sdk_v1.models.simulation.dilu_preconditioner import DILUPreconditioner
    from simscale_sdk_v1.models.simulation.darcy_forchheimer_medium import DarcyForchheimerMedium
    from simscale_sdk_v1.models.simulation.darcy_medium import DarcyMedium
    from simscale_sdk_v1.models.simulation.decimal_vector import DecimalVector
    from simscale_sdk_v1.models.simulation.decimal_vector2d import DecimalVector2d
    from simscale_sdk_v1.models.simulation.derived_heat_flux import DerivedHeatFlux
    from simscale_sdk_v1.models.simulation.dielectric import Dielectric
    from simscale_sdk_v1.models.simulation.dimensional_function_initial_condition_domains__temperature import (
        DimensionalFunctionInitialConditionDomains_Temperature,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__acceleration import DimensionalFunction_Acceleration
    from simscale_sdk_v1.models.simulation.dimensional_function__angle import DimensionalFunction_Angle
    from simscale_sdk_v1.models.simulation.dimensional_function__density import DimensionalFunction_Density
    from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
    from simscale_sdk_v1.models.simulation.dimensional_function__dynamic_viscosity import (
        DimensionalFunction_DynamicViscosity,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__electric_conductivity import (
        DimensionalFunction_ElectricConductivity,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__electric_current import (
        DimensionalFunction_ElectricCurrent,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__electric_field_strength import (
        DimensionalFunction_ElectricFieldStrength,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__electric_potential import (
        DimensionalFunction_ElectricPotential,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__electric_resistivity import (
        DimensionalFunction_ElectricResistivity,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__heat_flux import DimensionalFunction_HeatFlux
    from simscale_sdk_v1.models.simulation.dimensional_function__kinematic_viscosity import (
        DimensionalFunction_KinematicViscosity,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__length import DimensionalFunction_Length
    from simscale_sdk_v1.models.simulation.dimensional_function__magnetic_flux_density import (
        DimensionalFunction_MagneticFluxDensity,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__mass_flow_rate import DimensionalFunction_MassFlowRate
    from simscale_sdk_v1.models.simulation.dimensional_function__power import DimensionalFunction_Power
    from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
    from simscale_sdk_v1.models.simulation.dimensional_function__rotation_speed import DimensionalFunction_RotationSpeed
    from simscale_sdk_v1.models.simulation.dimensional_function__specific_energy import (
        DimensionalFunction_SpecificEnergy,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__specific_heat import DimensionalFunction_SpecificHeat
    from simscale_sdk_v1.models.simulation.dimensional_function__specific_turbulence_dissipation_rate import (
        DimensionalFunction_SpecificTurbulenceDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__speed import DimensionalFunction_Speed
    from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
    from simscale_sdk_v1.models.simulation.dimensional_function__temperature_gradient import (
        DimensionalFunction_TemperatureGradient,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__thermal_conductivity import (
        DimensionalFunction_ThermalConductivity,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__thermal_expansion_rate import (
        DimensionalFunction_ThermalExpansionRate,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__thermal_transmittance import (
        DimensionalFunction_ThermalTransmittance,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__time import DimensionalFunction_Time
    from simscale_sdk_v1.models.simulation.dimensional_function__total_thermal_transmittance import (
        DimensionalFunction_TotalThermalTransmittance,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__turbulence_kinetic_energy import (
        DimensionalFunction_TurbulenceKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__turbulent_dissipation import (
        DimensionalFunction_TurbulentDissipation,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__volumetric_flow_rate import (
        DimensionalFunction_VolumetricFlowRate,
    )
    from simscale_sdk_v1.models.simulation.dimensional_function__volumetric_power import (
        DimensionalFunction_VolumetricPower,
    )
    from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__dimensionless import (
        DimensionalInitialConditionDomains_Dimensionless,
    )
    from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__kinematic_viscosity import (
        DimensionalInitialConditionDomains_KinematicViscosity,
    )
    from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__pressure import (
        DimensionalInitialConditionDomains_Pressure,
    )
    from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__specific_turbulence_dissipation_rate import (
        DimensionalInitialConditionDomains_SpecificTurbulenceDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__temperature import (
        DimensionalInitialConditionDomains_Temperature,
    )
    from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__turbulence_kinetic_energy import (
        DimensionalInitialConditionDomains_TurbulenceKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__turbulent_dissipation import (
        DimensionalInitialConditionDomains_TurbulentDissipation,
    )
    from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__angle import (
        DimensionalPartialVectorFunction_Angle,
    )
    from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__length import (
        DimensionalPartialVectorFunction_Length,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector2d__length import DimensionalVector2d_Length
    from simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__acceleration import (
        DimensionalVectorFunctionInitialConditionWithDomains_Acceleration,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__length import (
        DimensionalVectorFunctionInitialConditionWithDomains_Length,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__speed import (
        DimensionalVectorFunctionInitialConditionWithDomains_Speed,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector_function__acceleration import (
        DimensionalVectorFunction_Acceleration,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector_function__force import DimensionalVectorFunction_Force
    from simscale_sdk_v1.models.simulation.dimensional_vector_function__length import DimensionalVectorFunction_Length
    from simscale_sdk_v1.models.simulation.dimensional_vector_function__pressure import (
        DimensionalVectorFunction_Pressure,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector_function__speed import DimensionalVectorFunction_Speed
    from simscale_sdk_v1.models.simulation.dimensional_vector_function__torque import DimensionalVectorFunction_Torque
    from simscale_sdk_v1.models.simulation.dimensional_vector_function__volume_force import (
        DimensionalVectorFunction_VolumeForce,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector_initial_condition_domains__speed import (
        DimensionalVectorInitialConditionDomains_Speed,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector__absorptivity import DimensionalVector_Absorptivity
    from simscale_sdk_v1.models.simulation.dimensional_vector__acceleration import DimensionalVector_Acceleration
    from simscale_sdk_v1.models.simulation.dimensional_vector__angle import DimensionalVector_Angle
    from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless
    from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
    from simscale_sdk_v1.models.simulation.dimensional_vector__moment_of_inertia import (
        DimensionalVector_MomentOfInertia,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector__reciprocal_permeability import (
        DimensionalVector_ReciprocalPermeability,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector__rotation_speed import DimensionalVector_RotationSpeed
    from simscale_sdk_v1.models.simulation.dimensional_vector__specific_turbulence_dissipation_rate import (
        DimensionalVector_SpecificTurbulenceDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed
    from simscale_sdk_v1.models.simulation.dimensional_vector__surface_tension import DimensionalVector_SurfaceTension
    from simscale_sdk_v1.models.simulation.dimensional_vector__volume_force import DimensionalVector_VolumeForce
    from simscale_sdk_v1.models.simulation.dimensional__absolute_humidity_rate import Dimensional_AbsoluteHumidityRate
    from simscale_sdk_v1.models.simulation.dimensional__absorptivity import Dimensional_Absorptivity
    from simscale_sdk_v1.models.simulation.dimensional__acceleration import Dimensional_Acceleration
    from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
    from simscale_sdk_v1.models.simulation.dimensional__area import Dimensional_Area
    from simscale_sdk_v1.models.simulation.dimensional__charge import Dimensional_Charge
    from simscale_sdk_v1.models.simulation.dimensional__charge_density import Dimensional_ChargeDensity
    from simscale_sdk_v1.models.simulation.dimensional__contact_resistance import Dimensional_ContactResistance
    from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density
    from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
    from simscale_sdk_v1.models.simulation.dimensional__dynamic_viscosity import Dimensional_DynamicViscosity
    from simscale_sdk_v1.models.simulation.dimensional__eddy_viscosity_gradient import Dimensional_EddyViscosityGradient
    from simscale_sdk_v1.models.simulation.dimensional__electric_conductance import Dimensional_ElectricConductance
    from simscale_sdk_v1.models.simulation.dimensional__electric_current import Dimensional_ElectricCurrent
    from simscale_sdk_v1.models.simulation.dimensional__electric_potential import Dimensional_ElectricPotential
    from simscale_sdk_v1.models.simulation.dimensional__electric_resistance import Dimensional_ElectricResistance
    from simscale_sdk_v1.models.simulation.dimensional__electric_resistivity import Dimensional_ElectricResistivity
    from simscale_sdk_v1.models.simulation.dimensional__energy_density import Dimensional_EnergyDensity
    from simscale_sdk_v1.models.simulation.dimensional__epsilon_gradient import Dimensional_EpsilonGradient
    from simscale_sdk_v1.models.simulation.dimensional__force import Dimensional_Force
    from simscale_sdk_v1.models.simulation.dimensional__force_density import Dimensional_ForceDensity
    from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency
    from simscale_sdk_v1.models.simulation.dimensional__friction_augmentation import Dimensional_FrictionAugmentation
    from simscale_sdk_v1.models.simulation.dimensional__heat_flux import Dimensional_HeatFlux
    from simscale_sdk_v1.models.simulation.dimensional__inv_pressure import Dimensional_InvPressure
    from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
    from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
    from simscale_sdk_v1.models.simulation.dimensional__magnetic_flux_density import Dimensional_MagneticFluxDensity
    from simscale_sdk_v1.models.simulation.dimensional__mass import Dimensional_Mass
    from simscale_sdk_v1.models.simulation.dimensional__mass_area_density import Dimensional_MassAreaDensity
    from simscale_sdk_v1.models.simulation.dimensional__mass_flow_rate import Dimensional_MassFlowRate
    from simscale_sdk_v1.models.simulation.dimensional__mass_fraction import Dimensional_MassFraction
    from simscale_sdk_v1.models.simulation.dimensional__molar_mass import Dimensional_MolarMass
    from simscale_sdk_v1.models.simulation.dimensional__passive_scalar_source_rate import (
        Dimensional_PassiveScalarSourceRate,
    )
    from simscale_sdk_v1.models.simulation.dimensional__phase_fraction_gradient import Dimensional_PhaseFractionGradient
    from simscale_sdk_v1.models.simulation.dimensional__power import Dimensional_Power
    from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
    from simscale_sdk_v1.models.simulation.dimensional__rotation_speed import Dimensional_RotationSpeed
    from simscale_sdk_v1.models.simulation.dimensional__rotational_stiffness import Dimensional_RotationalStiffness
    from simscale_sdk_v1.models.simulation.dimensional__specific_contact_resistance import (
        Dimensional_SpecificContactResistance,
    )
    from simscale_sdk_v1.models.simulation.dimensional__specific_electric_conductance import (
        Dimensional_SpecificElectricConductance,
    )
    from simscale_sdk_v1.models.simulation.dimensional__specific_electric_resistance import (
        Dimensional_SpecificElectricResistance,
    )
    from simscale_sdk_v1.models.simulation.dimensional__specific_heat import Dimensional_SpecificHeat
    from simscale_sdk_v1.models.simulation.dimensional__specific_turbulence_dissipation_rate import (
        Dimensional_SpecificTurbulenceDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.dimensional__specific_turbulence_dissipation_rate_gradient import (
        Dimensional_SpecificTurbulenceDissipationRateGradient,
    )
    from simscale_sdk_v1.models.simulation.dimensional__speed import Dimensional_Speed
    from simscale_sdk_v1.models.simulation.dimensional__stiffness import Dimensional_Stiffness
    from simscale_sdk_v1.models.simulation.dimensional__strain_rate import Dimensional_StrainRate
    from simscale_sdk_v1.models.simulation.dimensional__surface_tension import Dimensional_SurfaceTension
    from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
    from simscale_sdk_v1.models.simulation.dimensional__thermal_conductivity import Dimensional_ThermalConductivity
    from simscale_sdk_v1.models.simulation.dimensional__thermal_expansion_rate import Dimensional_ThermalExpansionRate
    from simscale_sdk_v1.models.simulation.dimensional__thermal_transmittance import Dimensional_ThermalTransmittance
    from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
    from simscale_sdk_v1.models.simulation.dimensional__torque import Dimensional_Torque
    from simscale_sdk_v1.models.simulation.dimensional__total_thermal_transmittance import (
        Dimensional_TotalThermalTransmittance,
    )
    from simscale_sdk_v1.models.simulation.dimensional__turbulence_kinetic_energy import (
        Dimensional_TurbulenceKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.dimensional__turbulent_dissipation import Dimensional_TurbulentDissipation
    from simscale_sdk_v1.models.simulation.dimensional__volume_force import Dimensional_VolumeForce
    from simscale_sdk_v1.models.simulation.dimensional__volumetric_passive_scalar_source_rate import (
        Dimensional_VolumetricPassiveScalarSourceRate,
    )
    from simscale_sdk_v1.models.simulation.dimensionless_initial_condition_domains import (
        DimensionlessInitialConditionDomains,
    )
    from simscale_sdk_v1.models.simulation.directional_dependency import DirectionalDependency
    from simscale_sdk_v1.models.simulation.directional_material_structure import DirectionalMaterialStructure
    from simscale_sdk_v1.models.simulation.displacement_field import DisplacementField
    from simscale_sdk_v1.models.simulation.displacement_field_selection import DisplacementFieldSelection
    from simscale_sdk_v1.models.simulation.displacement_result_control_item import DisplacementResultControlItem
    from simscale_sdk_v1.models.simulation.displacements_convergence_method import DisplacementsConvergenceMethod
    from simscale_sdk_v1.models.simulation.distance_region_refinement_with_length import (
        DistanceRegionRefinementWithLength,
    )
    from simscale_sdk_v1.models.simulation.distributed_isotropic_stiffness_definition import (
        DistributedIsotropicStiffnessDefinition,
    )
    from simscale_sdk_v1.models.simulation.distributed_mass_bc import DistributedMassBC
    from simscale_sdk_v1.models.simulation.distributed_orthotropic_stiffness_definition import (
        DistributedOrthotropicStiffnessDefinition,
    )
    from simscale_sdk_v1.models.simulation.divergence_schemes import DivergenceSchemes
    from simscale_sdk_v1.models.simulation.dynamic_analysis import DynamicAnalysis
    from simscale_sdk_v1.models.simulation.dynamic_contact_angle_pfbc import DynamicContactAnglePFBC
    from simscale_sdk_v1.models.simulation.e_const_thermo import EConstThermo
    from simscale_sdk_v1.models.simulation.erp_calculation_result_control_item import ERPCalculationResultControlItem
    from simscale_sdk_v1.models.simulation.erp_density_result_control_item import ERPDensityResultControlItem
    from simscale_sdk_v1.models.simulation.effective_conductivity_heat_transfer import EffectiveConductivityHeatTransfer
    from simscale_sdk_v1.models.simulation.eigen_mode_verification import EigenModeVerification
    from simscale_sdk_v1.models.simulation.elastic_jacobian_matrix import ElasticJacobianMatrix
    from simscale_sdk_v1.models.simulation.elastic_strain import ElasticStrain
    from simscale_sdk_v1.models.simulation.elastic_support_bc import ElasticSupportBC
    from simscale_sdk_v1.models.simulation.elasticity_marc import ElasticityMarc
    from simscale_sdk_v1.models.simulation.elastoplastic_marc_material_behavior import ElastoplasticMarcMaterialBehavior
    from simscale_sdk_v1.models.simulation.elastoplastic_network import ElastoplasticNetwork
    from simscale_sdk_v1.models.simulation.electric_current_density_field_selection import (
        ElectricCurrentDensityFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.electric_displacement_field_field_selection import (
        ElectricDisplacementFieldFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.electric_field_field_selection import ElectricFieldFieldSelection
    from simscale_sdk_v1.models.simulation.electric_potential_field_selection import ElectricPotentialFieldSelection
    from simscale_sdk_v1.models.simulation.electrical_steel_core_loss import ElectricalSteelCoreLoss
    from simscale_sdk_v1.models.simulation.electromagnetic_advanced_concepts import ElectromagneticAdvancedConcepts
    from simscale_sdk_v1.models.simulation.electromagnetic_analysis import ElectromagneticAnalysis
    from simscale_sdk_v1.models.simulation.electromagnetic_circuit import ElectromagneticCircuit
    from simscale_sdk_v1.models.simulation.electromagnetic_current_type_constant import (
        ElectromagneticCurrentTypeConstant,
    )
    from simscale_sdk_v1.models.simulation.electromagnetic_current_type_sinusoidal import (
        ElectromagneticCurrentTypeSinusoidal,
    )
    from simscale_sdk_v1.models.simulation.electromagnetic_current_type_table import ElectromagneticCurrentTypeTable
    from simscale_sdk_v1.models.simulation.electromagnetic_initial_conditions import ElectromagneticInitialConditions
    from simscale_sdk_v1.models.simulation.electromagnetic_material import ElectromagneticMaterial
    from simscale_sdk_v1.models.simulation.electromagnetic_numerics import ElectromagneticNumerics
    from simscale_sdk_v1.models.simulation.electromagnetic_resistance_set import ElectromagneticResistanceSet
    from simscale_sdk_v1.models.simulation.electromagnetic_result_control import ElectromagneticResultControl
    from simscale_sdk_v1.models.simulation.electromagnetic_result_control_probe_point import (
        ElectromagneticResultControlProbePoint,
    )
    from simscale_sdk_v1.models.simulation.electromagnetic_simulation_control import ElectromagneticSimulationControl
    from simscale_sdk_v1.models.simulation.electromagnetic_transient_control import ElectromagneticTransientControl
    from simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_constant import (
        ElectromagneticVoltageTypeConstant,
    )
    from simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_sinusoidal import (
        ElectromagneticVoltageTypeSinusoidal,
    )
    from simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_table import ElectromagneticVoltageTypeTable
    from simscale_sdk_v1.models.simulation.electrostatics import Electrostatics
    from simscale_sdk_v1.models.simulation.element_groups_domain_decomposition import ElementGroupsDomainDecomposition
    from simscale_sdk_v1.models.simulation.element_technology import ElementTechnology
    from simscale_sdk_v1.models.simulation.element_technology_definition import ElementTechnologyDefinition
    from simscale_sdk_v1.models.simulation.embedded_boundary import EmbeddedBoundary
    from simscale_sdk_v1.models.simulation.embedded_boundary_meshing import EmbeddedBoundaryMeshing
    from simscale_sdk_v1.models.simulation.empty2_dbc import Empty2DBC
    from simscale_sdk_v1.models.simulation.equivalent_elastic_strain import EquivalentElasticStrain
    from simscale_sdk_v1.models.simulation.equivalent_plastic_strain import EquivalentPlasticStrain
    from simscale_sdk_v1.models.simulation.equivalent_radiated_power_density_type import (
        EquivalentRadiatedPowerDensityType,
    )
    from simscale_sdk_v1.models.simulation.equivalent_sand_grain_roughness import EquivalentSandGrainRoughness
    from simscale_sdk_v1.models.simulation.error_retiming_event import ErrorRetimingEvent
    from simscale_sdk_v1.models.simulation.euler_time_differentiation_scheme import EulerTimeDifferentiationScheme
    from simscale_sdk_v1.models.simulation.explicit_time_integration_type import ExplicitTimeIntegrationType
    from simscale_sdk_v1.models.simulation.expression_function import ExpressionFunction
    from simscale_sdk_v1.models.simulation.external_force import ExternalForce
    from simscale_sdk_v1.models.simulation.external_pressure import ExternalPressure
    from simscale_sdk_v1.models.simulation.external_wall_heat_flux_tbc import ExternalWallHeatFluxTBC
    from simscale_sdk_v1.models.simulation.face_normal_magnetization_direction_method import (
        FaceNormalMagnetizationDirectionMethod,
    )
    from simscale_sdk_v1.models.simulation.fair_weather_conditions import FairWeatherConditions
    from simscale_sdk_v1.models.simulation.false_change_jacobian_matrix import FalseChangeJacobianMatrix
    from simscale_sdk_v1.models.simulation.false_line_search import FalseLineSearch
    from simscale_sdk_v1.models.simulation.false_semi_implicit import FalseSemiImplicit
    from simscale_sdk_v1.models.simulation.fan_bc import FanBC
    from simscale_sdk_v1.models.simulation.fan_pbc import FanPBC
    from simscale_sdk_v1.models.simulation.fan_pressure_drop_momentum_source import FanPressureDropMomentumSource
    from simscale_sdk_v1.models.simulation.field_calculations_adjoint_sensitivities_result_control import (
        FieldCalculationsAdjointSensitivitiesResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_friction_velocity_result_control import (
        FieldCalculationsFrictionVelocityResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_mean_age_of_fluid_result_control import (
        FieldCalculationsMeanAgeOfFluidResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_mean_radiant_temperature_result_control import (
        FieldCalculationsMeanRadiantTemperatureResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_modeled_ti_result_control import (
        FieldCalculationsModeledTIResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_operative_temperature_result_control import (
        FieldCalculationsOperativeTemperatureResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_pressure_result_control import (
        FieldCalculationsPressureResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_resolved_ti_result_control import (
        FieldCalculationsResolvedTIResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_resolved_tke_result_control import (
        FieldCalculationsResolvedTKEResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_surface_normals_result_control import (
        FieldCalculationsSurfaceNormalsResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_thermal_comfort_result_control import (
        FieldCalculationsThermalComfortResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_total_ti_result_control import (
        FieldCalculationsTotalTIResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_total_tke_result_control import (
        FieldCalculationsTotalTKEResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_turbulence_result_control import (
        FieldCalculationsTurbulenceResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_velocity_result_control import (
        FieldCalculationsVelocityResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_wall_fluxes_result_control import (
        FieldCalculationsWallFluxesResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_calculations_wall_heat_flux_result_control import (
        FieldCalculationsWallHeatFluxResultControl,
    )
    from simscale_sdk_v1.models.simulation.field_change_retiming_event import FieldChangeRetimingEvent
    from simscale_sdk_v1.models.simulation.field_change_target_calculation_type import FieldChangeTargetCalculationType
    from simscale_sdk_v1.models.simulation.field_limits import FieldLimits
    from simscale_sdk_v1.models.simulation.first_mode import FirstMode
    from simscale_sdk_v1.models.simulation.first_order_ogden import FirstOrderOgden
    from simscale_sdk_v1.models.simulation.first_order_upwind_spatial_scheme import FirstOrderUpwindSpatialScheme
    from simscale_sdk_v1.models.simulation.fixed_augmentation import FixedAugmentation
    from simscale_sdk_v1.models.simulation.fixed_coeff_medium import FixedCoeffMedium
    from simscale_sdk_v1.models.simulation.fixed_electric_potential_ebc import FixedElectricPotentialEBC
    from simscale_sdk_v1.models.simulation.fixed_flux_pbc import FixedFluxPBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_dvbc import FixedGradientDVBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_ebc import FixedGradientEBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_evbc import FixedGradientEVBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_evcbc import FixedGradientEVCBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_nbc import FixedGradientNBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_obc import FixedGradientOBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_pbc import FixedGradientPBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_pfbc import FixedGradientPFBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_psbc import FixedGradientPSBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_tbc import FixedGradientTBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_tdbc import FixedGradientTDBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_tdcbc import FixedGradientTDCBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_tkebc import FixedGradientTKEBC
    from simscale_sdk_v1.models.simulation.fixed_gradient_vbc import FixedGradientVBC
    from simscale_sdk_v1.models.simulation.fixed_heat_flux import FixedHeatFlux
    from simscale_sdk_v1.models.simulation.fixed_magnitude_vbc import FixedMagnitudeVBC
    from simscale_sdk_v1.models.simulation.fixed_point_contact_non_linearity_resolution import (
        FixedPointContactNonLinearityResolution,
    )
    from simscale_sdk_v1.models.simulation.fixed_point_friction_non_linearity_resolution import (
        FixedPointFrictionNonLinearityResolution,
    )
    from simscale_sdk_v1.models.simulation.fixed_point_non_linearity_resolution import FixedPointNonLinearityResolution
    from simscale_sdk_v1.models.simulation.fixed_potential import FixedPotential
    from simscale_sdk_v1.models.simulation.fixed_power_heat_flux import FixedPowerHeatFlux
    from simscale_sdk_v1.models.simulation.fixed_subdivision import FixedSubdivision
    from simscale_sdk_v1.models.simulation.fixed_support_bc import FixedSupportBC
    from simscale_sdk_v1.models.simulation.fixed_temperature import FixedTemperature
    from simscale_sdk_v1.models.simulation.fixed_temperature_heat_transfer_coefficient_result_type import (
        FixedTemperatureHeatTransferCoefficientResultType,
    )
    from simscale_sdk_v1.models.simulation.fixed_temperature_value_bc import FixedTemperatureValueBC
    from simscale_sdk_v1.models.simulation.fixed_value_bc import FixedValueBC
    from simscale_sdk_v1.models.simulation.fixed_value_bc_marc import FixedValueBCMarc
    from simscale_sdk_v1.models.simulation.fixed_value_dvbc import FixedValueDVBC
    from simscale_sdk_v1.models.simulation.fixed_value_ebc import FixedValueEBC
    from simscale_sdk_v1.models.simulation.fixed_value_evbc import FixedValueEVBC
    from simscale_sdk_v1.models.simulation.fixed_value_evcbc import FixedValueEVCBC
    from simscale_sdk_v1.models.simulation.fixed_value_mass_fraction_bc import FixedValueMassFractionBC
    from simscale_sdk_v1.models.simulation.fixed_value_nbc import FixedValueNBC
    from simscale_sdk_v1.models.simulation.fixed_value_obc import FixedValueOBC
    from simscale_sdk_v1.models.simulation.fixed_value_pbc import FixedValuePBC
    from simscale_sdk_v1.models.simulation.fixed_value_pfbc import FixedValuePFBC
    from simscale_sdk_v1.models.simulation.fixed_value_psbc import FixedValuePSBC
    from simscale_sdk_v1.models.simulation.fixed_value_phase_fraction_bc import FixedValuePhaseFractionBC
    from simscale_sdk_v1.models.simulation.fixed_value_rhbc import FixedValueRHBC
    from simscale_sdk_v1.models.simulation.fixed_value_tbc import FixedValueTBC
    from simscale_sdk_v1.models.simulation.fixed_value_tdbc import FixedValueTDBC
    from simscale_sdk_v1.models.simulation.fixed_value_tdcbc import FixedValueTDCBC
    from simscale_sdk_v1.models.simulation.fixed_value_tkebc import FixedValueTKEBC
    from simscale_sdk_v1.models.simulation.fixed_value_turbulence import FixedValueTurbulence
    from simscale_sdk_v1.models.simulation.fixed_value_vbc import FixedValueVBC
    from simscale_sdk_v1.models.simulation.flexible_axial_translation import FlexibleAxialTranslation
    from simscale_sdk_v1.models.simulation.floating_potential import FloatingPotential
    from simscale_sdk_v1.models.simulation.flow_dependent_value_pfbc import FlowDependentValuePFBC
    from simscale_sdk_v1.models.simulation.flow_domain_boundaries import FlowDomainBoundaries
    from simscale_sdk_v1.models.simulation.flow_rate_inlet_vbc import FlowRateInletVBC
    from simscale_sdk_v1.models.simulation.flow_rate_mean_inlet_vbc import FlowRateMeanInletVBC
    from simscale_sdk_v1.models.simulation.flow_rate_mean_outlet_vbc import FlowRateMeanOutletVBC
    from simscale_sdk_v1.models.simulation.flow_rate_outlet_vbc import FlowRateOutletVBC
    from simscale_sdk_v1.models.simulation.flow_rate_stable_outlet_vbc import FlowRateStableOutletVBC
    from simscale_sdk_v1.models.simulation.fluid_compressible_material import FluidCompressibleMaterial
    from simscale_sdk_v1.models.simulation.fluid_initial_conditions import FluidInitialConditions
    from simscale_sdk_v1.models.simulation.fluid_interface import FluidInterface
    from simscale_sdk_v1.models.simulation.fluid_model import FluidModel
    from simscale_sdk_v1.models.simulation.fluid_numerics import FluidNumerics
    from simscale_sdk_v1.models.simulation.fluid_only_heat_transfer import FluidOnlyHeatTransfer
    from simscale_sdk_v1.models.simulation.fluid_result_controls import FluidResultControls
    from simscale_sdk_v1.models.simulation.fluid_simulation_control import FluidSimulationControl
    from simscale_sdk_v1.models.simulation.fluid_solvers import FluidSolvers
    from simscale_sdk_v1.models.simulation.fluid_type_gas import FluidTypeGas
    from simscale_sdk_v1.models.simulation.fluid_type_liquid import FluidTypeLiquid
    from simscale_sdk_v1.models.simulation.flux_heat_source import FluxHeatSource
    from simscale_sdk_v1.models.simulation.flux_schemes import FluxSchemes
    from simscale_sdk_v1.models.simulation.follower_pressure_bc import FollowerPressureBC
    from simscale_sdk_v1.models.simulation.force_and_torque import ForceAndTorque
    from simscale_sdk_v1.models.simulation.force_field_selection import ForceFieldSelection
    from simscale_sdk_v1.models.simulation.force_load_bc import ForceLoadBC
    from simscale_sdk_v1.models.simulation.force_moment_coefficients_result_control import (
        ForceMomentCoefficientsResultControl,
    )
    from simscale_sdk_v1.models.simulation.force_preload import ForcePreload
    from simscale_sdk_v1.models.simulation.force_result_control_item import ForceResultControlItem
    from simscale_sdk_v1.models.simulation.forces_moments_result_control import ForcesMomentsResultControl
    from simscale_sdk_v1.models.simulation.fourth_gradient_scheme import FourthGradientScheme
    from simscale_sdk_v1.models.simulation.fraction_value_initial_condition import FractionValueInitialCondition
    from simscale_sdk_v1.models.simulation.fraction_values_initial_conditions import FractionValuesInitialConditions
    from simscale_sdk_v1.models.simulation.free_axial_rotation import FreeAxialRotation
    from simscale_sdk_v1.models.simulation.free_axial_translation import FreeAxialTranslation
    from simscale_sdk_v1.models.simulation.freestream_pbc import FreestreamPBC
    from simscale_sdk_v1.models.simulation.freestream_vbc import FreestreamVBC
    from simscale_sdk_v1.models.simulation.frequency_analysis import FrequencyAnalysis
    from simscale_sdk_v1.models.simulation.frequency_list import FrequencyList
    from simscale_sdk_v1.models.simulation.frequency_range import FrequencyRange
    from simscale_sdk_v1.models.simulation.friction_augmented_lagrange_coef import FrictionAugmentedLagrangeCoef
    from simscale_sdk_v1.models.simulation.friction_contact import FrictionContact
    from simscale_sdk_v1.models.simulation.friction_penalty_coef import FrictionPenaltyCoef
    from simscale_sdk_v1.models.simulation.friction_velocity_momentum_source import FrictionVelocityMomentumSource
    from simscale_sdk_v1.models.simulation.friction_velocity_result_type import FrictionVelocityResultType
    from simscale_sdk_v1.models.simulation.frictionless_contact import FrictionlessContact
    from simscale_sdk_v1.models.simulation.full_rank_acceleration import FullRankAcceleration
    from simscale_sdk_v1.models.simulation.full_resolution_dvbc import FullResolutionDVBC
    from simscale_sdk_v1.models.simulation.full_resolution_ebc import FullResolutionEBC
    from simscale_sdk_v1.models.simulation.full_resolution_evbc import FullResolutionEVBC
    from simscale_sdk_v1.models.simulation.full_resolution_evcbc import FullResolutionEVCBC
    from simscale_sdk_v1.models.simulation.full_resolution_nbc import FullResolutionNBC
    from simscale_sdk_v1.models.simulation.full_resolution_obc import FullResolutionOBC
    from simscale_sdk_v1.models.simulation.full_resolution_tdbc import FullResolutionTDBC
    from simscale_sdk_v1.models.simulation.full_resolution_tdcbc import FullResolutionTDCBC
    from simscale_sdk_v1.models.simulation.full_resolution_tkebc import FullResolutionTKEBC
    from simscale_sdk_v1.models.simulation.function_parameter import FunctionParameter
    from simscale_sdk_v1.models.simulation.gamg_solver import GAMGSolver
    from simscale_sdk_v1.models.simulation.gauss_interface_compression_divergence_scheme import (
        GaussInterfaceCompressionDivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_limited_linear1_divergence_scheme import (
        GaussLimitedLinear1DivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_limited_linear_v1_divergence_scheme import (
        GaussLimitedLinearV1DivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_linear_corrected_laplacian_scheme import (
        GaussLinearCorrectedLaplacianScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_linear_divergence_scheme import GaussLinearDivergenceScheme
    from simscale_sdk_v1.models.simulation.gauss_linear_gradient_scheme import GaussLinearGradientScheme
    from simscale_sdk_v1.models.simulation.gauss_linear_limited_corrected_laplacian_scheme import (
        GaussLinearLimitedCorrectedLaplacianScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_linear_uncorrected_laplacian_scheme import (
        GaussLinearUncorrectedLaplacianScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_linear_upwind_limited_grad_divergence_scheme import (
        GaussLinearUpwindLimitedGradDivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_linear_upwind_unlimited_divergence_scheme import (
        GaussLinearUpwindUnlimitedDivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_linear_upwind_v_grad_u_divergence_scheme import (
        GaussLinearUpwindVGradUDivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_linear_upwind_v_unlimited_divergence_scheme import (
        GaussLinearUpwindVUnlimitedDivergenceScheme,
    )
    from simscale_sdk_v1.models.simulation.gauss_upwind_divergence_scheme import GaussUpwindDivergenceScheme
    from simscale_sdk_v1.models.simulation.gauss_vanleer_divergence_scheme import GaussVanleerDivergenceScheme
    from simscale_sdk_v1.models.simulation.general_darcy_forchheimer_pacefish import GeneralDarcyForchheimerPacefish
    from simscale_sdk_v1.models.simulation.general_hole_shape import GeneralHoleShape
    from simscale_sdk_v1.models.simulation.geographical_location import GeographicalLocation
    from simscale_sdk_v1.models.simulation.global_acceleration_type import GlobalAccelerationType
    from simscale_sdk_v1.models.simulation.global_cartesian_magnetization_direction_method import (
        GlobalCartesianMagnetizationDirectionMethod,
    )
    from simscale_sdk_v1.models.simulation.global_cauchy_stress_type import GlobalCauchyStressType
    from simscale_sdk_v1.models.simulation.global_damping_value import GlobalDampingValue
    from simscale_sdk_v1.models.simulation.global_displacement import GlobalDisplacement
    from simscale_sdk_v1.models.simulation.global_displacement_type import GlobalDisplacementType
    from simscale_sdk_v1.models.simulation.global_max_over_phase_von_mises_stress_type import (
        GlobalMaxOverPhaseVonMisesStressType,
    )
    from simscale_sdk_v1.models.simulation.global_nodal_force_type import GlobalNodalForceType
    from simscale_sdk_v1.models.simulation.global_principal_green_lagrange_strain_type import (
        GlobalPrincipalGreenLagrangeStrainType,
    )
    from simscale_sdk_v1.models.simulation.global_principal_strain_type import GlobalPrincipalStrainType
    from simscale_sdk_v1.models.simulation.global_principal_stress_type import GlobalPrincipalStressType
    from simscale_sdk_v1.models.simulation.global_reaction_force_type import GlobalReactionForceType
    from simscale_sdk_v1.models.simulation.global_signed_von_mises_stress_type import GlobalSignedVonMisesStressType
    from simscale_sdk_v1.models.simulation.global_total_equivalent_plastic_strain_type import (
        GlobalTotalEquivalentPlasticStrainType,
    )
    from simscale_sdk_v1.models.simulation.global_total_nonlinear_strain_type import GlobalTotalNonlinearStrainType
    from simscale_sdk_v1.models.simulation.global_total_strain_type import GlobalTotalStrainType
    from simscale_sdk_v1.models.simulation.global_tresca_stress_type import GlobalTrescaStressType
    from simscale_sdk_v1.models.simulation.global_unelastic_strain_type import GlobalUnelasticStrainType
    from simscale_sdk_v1.models.simulation.global_velocity_type import GlobalVelocityType
    from simscale_sdk_v1.models.simulation.global_von_mises_stress_type import GlobalVonMisesStressType
    from simscale_sdk_v1.models.simulation.gradient_schemes import GradientSchemes
    from simscale_sdk_v1.models.simulation.greybody_diffusive_rsbc import GreybodyDiffusiveRSBC
    from simscale_sdk_v1.models.simulation.greybody_diffusive_ray_bc import GreybodyDiffusiveRayBC
    from simscale_sdk_v1.models.simulation.ground_absolute import GroundAbsolute
    from simscale_sdk_v1.models.simulation.ground_relative import GroundRelative
    from simscale_sdk_v1.models.simulation.h_const_thermo import HConstThermo
    from simscale_sdk_v1.models.simulation.harmonic_acceleration_result_control_item import (
        HarmonicAccelerationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.harmonic_analysis import HarmonicAnalysis
    from simscale_sdk_v1.models.simulation.harmonic_displacement_result_control_item import (
        HarmonicDisplacementResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.harmonic_response import HarmonicResponse
    from simscale_sdk_v1.models.simulation.harmonic_response_control import HarmonicResponseControl
    from simscale_sdk_v1.models.simulation.harmonic_response_result_control_item import (
        HarmonicResponseResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.harmonic_velocity_result_control_item import (
        HarmonicVelocityResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.heat_exchanger_performance import HeatExchangerPerformance
    from simscale_sdk_v1.models.simulation.heat_exchanger_source import HeatExchangerSource
    from simscale_sdk_v1.models.simulation.heat_flow_calculation_result_control_item import (
        HeatFlowCalculationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.heat_flux_field_selection import HeatFluxFieldSelection
    from simscale_sdk_v1.models.simulation.heat_flux_result_control_item import HeatFluxResultControlItem
    from simscale_sdk_v1.models.simulation.heat_transfer import HeatTransfer
    from simscale_sdk_v1.models.simulation.heat_transfer_coefficients import HeatTransferCoefficients
    from simscale_sdk_v1.models.simulation.herschel_bulkley_transport import HerschelBulkleyTransport
    from simscale_sdk_v1.models.simulation.herschel_bulkley_viscosity_model import HerschelBulkleyViscosityModel
    from simscale_sdk_v1.models.simulation.hht_time_integration_scheme import HhtTimeIntegrationScheme
    from simscale_sdk_v1.models.simulation.hierarchical_decompose_algorithm import HierarchicalDecomposeAlgorithm
    from simscale_sdk_v1.models.simulation.high_contact_stiffness import HighContactStiffness
    from simscale_sdk_v1.models.simulation.high_resolution import HighResolution
    from simscale_sdk_v1.models.simulation.high_resolution_spatial_scheme import HighResolutionSpatialScheme
    from simscale_sdk_v1.models.simulation.hinge_constraint_bc import HingeConstraintBC
    from simscale_sdk_v1.models.simulation.homogeneous_material_structure import HomogeneousMaterialStructure
    from simscale_sdk_v1.models.simulation.hydrostatic_fan_pbc import HydrostaticFanPBC
    from simscale_sdk_v1.models.simulation.hydrostatic_isothermal_freestream_pbc import (
        HydrostaticIsothermalFreestreamPBC,
    )
    from simscale_sdk_v1.models.simulation.hydrostatic_isothermal_pbc import HydrostaticIsothermalPBC
    from simscale_sdk_v1.models.simulation.hydrostatic_isothermal_total_pbc import HydrostaticIsothermalTotalPBC
    from simscale_sdk_v1.models.simulation.hydrostatic_pressure import HydrostaticPressure
    from simscale_sdk_v1.models.simulation.hyper_elastic_material_behavior import HyperElasticMaterialBehavior
    from simscale_sdk_v1.models.simulation.hyperelastic_marc_material_behavior import HyperelasticMarcMaterialBehavior
    from simscale_sdk_v1.models.simulation.hyperelasticity import Hyperelasticity
    from simscale_sdk_v1.models.simulation.hysteretic_damping import HystereticDamping
    from simscale_sdk_v1.models.simulation.ilu_cp_preconditioner import ILUCpPreconditioner
    from simscale_sdk_v1.models.simulation.iram_sorensen import IRAMSorensen
    from simscale_sdk_v1.models.simulation.implicit_time_integration_type import ImplicitTimeIntegrationType
    from simscale_sdk_v1.models.simulation.inactive_adjustable_timestep import InactiveAdjustableTimestep
    from simscale_sdk_v1.models.simulation.inactive_preconditioner import InactivePreconditioner
    from simscale_sdk_v1.models.simulation.incomplete_preconditioner_v33 import IncompletePreconditionerV33
    from simscale_sdk_v1.models.simulation.incompressible import Incompressible
    from simscale_sdk_v1.models.simulation.incompressible_fluid_materials import IncompressibleFluidMaterials
    from simscale_sdk_v1.models.simulation.incompressible_material import IncompressibleMaterial
    from simscale_sdk_v1.models.simulation.incompressible_pacefish import IncompressiblePacefish
    from simscale_sdk_v1.models.simulation.incompressible_perfect_gas_equation_of_state import (
        IncompressiblePerfectGasEquationOfState,
    )
    from simscale_sdk_v1.models.simulation.initial_timesteps_write_control import InitialTimestepsWriteControl
    from simscale_sdk_v1.models.simulation.inlet_fixed_mf_values import InletFixedMFValues
    from simscale_sdk_v1.models.simulation.inlet_fixed_pf_values import InletFixedPFValues
    from simscale_sdk_v1.models.simulation.inlet_outlet_dvbc import InletOutletDVBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_ebc import InletOutletEBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_evbc import InletOutletEVBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_evcbc import InletOutletEVCBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_nbc import InletOutletNBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_obc import InletOutletOBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_pfbc import InletOutletPFBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_psbc import InletOutletPSBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_rhbc import InletOutletRHBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_tbc import InletOutletTBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_tkebc import InletOutletTKEBC
    from simscale_sdk_v1.models.simulation.inlet_outlet_vbc import InletOutletVBC
    from simscale_sdk_v1.models.simulation.inside_region_refinement_with_length import InsideRegionRefinementWithLength
    from simscale_sdk_v1.models.simulation.intensity_kinetic_energy_inlet_tkebc import IntensityKineticEnergyInletTKEBC
    from simscale_sdk_v1.models.simulation.interference_fit import InterferenceFit
    from simscale_sdk_v1.models.simulation.intern_variables_field import InternVariablesField
    from simscale_sdk_v1.models.simulation.interpolation_parameter import InterpolationParameter
    from simscale_sdk_v1.models.simulation.interpolation_schemes import InterpolationSchemes
    from simscale_sdk_v1.models.simulation.isotropic_conductivity import IsotropicConductivity
    from simscale_sdk_v1.models.simulation.isotropic_darcy_forchheimer import IsotropicDarcyForchheimer
    from simscale_sdk_v1.models.simulation.isotropic_density_method import IsotropicDensityMethod
    from simscale_sdk_v1.models.simulation.isotropic_dielectric_strength import IsotropicDielectricStrength
    from simscale_sdk_v1.models.simulation.isotropic_directional_dependency import IsotropicDirectionalDependency
    from simscale_sdk_v1.models.simulation.isotropic_electric_conductivity import IsotropicElectricConductivity
    from simscale_sdk_v1.models.simulation.isotropic_electric_conductivity_method import (
        IsotropicElectricConductivityMethod,
    )
    from simscale_sdk_v1.models.simulation.isotropic_expansion import IsotropicExpansion
    from simscale_sdk_v1.models.simulation.isotropic_loss_tangent import IsotropicLossTangent
    from simscale_sdk_v1.models.simulation.isotropic_plastic_hardening import IsotropicPlasticHardening
    from simscale_sdk_v1.models.simulation.isotropic_plastic_hardening_marc import IsotropicPlasticHardeningMarc
    from simscale_sdk_v1.models.simulation.isotropic_relative_permeability_method import (
        IsotropicRelativePermeabilityMethod,
    )
    from simscale_sdk_v1.models.simulation.isotropic_specific_heat_method import IsotropicSpecificHeatMethod
    from simscale_sdk_v1.models.simulation.isotropic_spring_stiffness import IsotropicSpringStiffness
    from simscale_sdk_v1.models.simulation.isotropic_thermal_conductivity_method import (
        IsotropicThermalConductivityMethod,
    )
    from simscale_sdk_v1.models.simulation.jacobi_preconditioner import JacobiPreconditioner
    from simscale_sdk_v1.models.simulation.johnson_cook_elasto_plastic_model import JohnsonCookElastoPlasticModel
    from simscale_sdk_v1.models.simulation.kinematic_plastic_hardening_marc import KinematicPlasticHardeningMarc
    from simscale_sdk_v1.models.simulation.kurganov_flux_scheme import KurganovFluxScheme
    from simscale_sdk_v1.models.simulation.lanczos import Lanczos
    from simscale_sdk_v1.models.simulation.laplacian_schemes import LaplacianSchemes
    from simscale_sdk_v1.models.simulation.layer_wall_thermal import LayerWallThermal
    from simscale_sdk_v1.models.simulation.leastsquares_gradient_scheme import LeastsquaresGradientScheme
    from simscale_sdk_v1.models.simulation.limited_surface_normal_gradient_scheme import (
        LimitedSurfaceNormalGradientScheme,
    )
    from simscale_sdk_v1.models.simulation.linear_elastic_marc_material_behavior import (
        LinearElasticMarcMaterialBehavior,
    )
    from simscale_sdk_v1.models.simulation.linear_elastic_material_behavior import LinearElasticMaterialBehavior
    from simscale_sdk_v1.models.simulation.linear_interpolation_scheme import LinearInterpolationScheme
    from simscale_sdk_v1.models.simulation.linear_isotropic_permittivity_method import LinearIsotropicPermittivityMethod
    from simscale_sdk_v1.models.simulation.linear_sbm import LinearSBM
    from simscale_sdk_v1.models.simulation.litz_wire_coil import LitzWireCoil
    from simscale_sdk_v1.models.simulation.load_step import LoadStep
    from simscale_sdk_v1.models.simulation.local_element_size_ebm import LocalElementSizeEBM
    from simscale_sdk_v1.models.simulation.local_euler_time_differentiation_scheme import (
        LocalEulerTimeDifferentiationScheme,
    )
    from simscale_sdk_v1.models.simulation.low_contact_stiffness import LowContactStiffness
    from simscale_sdk_v1.models.simulation.low_rank_acceleration import LowRankAcceleration
    from simscale_sdk_v1.models.simulation.mrf_rotating_zone import MRFRotatingZone
    from simscale_sdk_v1.models.simulation.mules_solver import MULESSolver
    from simscale_sdk_v1.models.simulation.mumps_preconditoner import MUMPSPreconditoner
    from simscale_sdk_v1.models.simulation.mumps_solver import MUMPSSolver
    from simscale_sdk_v1.models.simulation.magnetic_field_field_selection import MagneticFieldFieldSelection
    from simscale_sdk_v1.models.simulation.magnetic_field_normal import MagneticFieldNormal
    from simscale_sdk_v1.models.simulation.magnetic_flux_density_field_selection import (
        MagneticFluxDensityFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.magnetic_flux_tangential import MagneticFluxTangential
    from simscale_sdk_v1.models.simulation.magnetostatics import Magnetostatics
    from simscale_sdk_v1.models.simulation.manual_embedded_boundary_mesh_sizing import ManualEmbeddedBoundaryMeshSizing
    from simscale_sdk_v1.models.simulation.manual_reactualization import ManualReactualization
    from simscale_sdk_v1.models.simulation.manual_reference_length import ManualReferenceLength
    from simscale_sdk_v1.models.simulation.manual_region_sizing_pacefish import ManualRegionSizingPacefish
    from simscale_sdk_v1.models.simulation.manual_reynolds_scaling import ManualReynoldsScaling
    from simscale_sdk_v1.models.simulation.manual_simerics_mesh_settings import ManualSimericsMeshSettings
    from simscale_sdk_v1.models.simulation.manual_surface_sizing_pacefish import ManualSurfaceSizingPacefish
    from simscale_sdk_v1.models.simulation.manual_time_step_defintion import ManualTimeStepDefintion
    from simscale_sdk_v1.models.simulation.manual_timestep_calculation_type import ManualTimestepCalculationType
    from simscale_sdk_v1.models.simulation.manual_timestep_definition import ManualTimestepDefinition
    from simscale_sdk_v1.models.simulation.marc_analysis import MarcAnalysis
    from simscale_sdk_v1.models.simulation.marc_average_fields_calculation_result_control_item import (
        MarcAverageFieldsCalculationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.marc_bonded_and_touching_contact_connection import (
        MarcBondedAndTouchingContactConnection,
    )
    from simscale_sdk_v1.models.simulation.marc_bonded_contact_connection import MarcBondedContactConnection
    from simscale_sdk_v1.models.simulation.marc_cauchy_stress_type import MarcCauchyStressType
    from simscale_sdk_v1.models.simulation.marc_connection_group import MarcConnectionGroup
    from simscale_sdk_v1.models.simulation.marc_connector_point_data_item import MarcConnectorPointDataItem
    from simscale_sdk_v1.models.simulation.marc_contact_body_force_type import MarcContactBodyForceType
    from simscale_sdk_v1.models.simulation.marc_contact_field_selection import MarcContactFieldSelection
    from simscale_sdk_v1.models.simulation.marc_contact_force_field_selection import MarcContactForceFieldSelection
    from simscale_sdk_v1.models.simulation.marc_contact_friction_force import MarcContactFrictionForce
    from simscale_sdk_v1.models.simulation.marc_contact_friction_force_type import MarcContactFrictionForceType
    from simscale_sdk_v1.models.simulation.marc_contact_friction_stress import MarcContactFrictionStress
    from simscale_sdk_v1.models.simulation.marc_contact_friction_stress_type import MarcContactFrictionStressType
    from simscale_sdk_v1.models.simulation.marc_contact_gap import MarcContactGap
    from simscale_sdk_v1.models.simulation.marc_contact_gap_type import MarcContactGapType
    from simscale_sdk_v1.models.simulation.marc_contact_normal_force import MarcContactNormalForce
    from simscale_sdk_v1.models.simulation.marc_contact_normal_force_type import MarcContactNormalForceType
    from simscale_sdk_v1.models.simulation.marc_contact_normal_stress import MarcContactNormalStress
    from simscale_sdk_v1.models.simulation.marc_contact_normal_stress_type import MarcContactNormalStressType
    from simscale_sdk_v1.models.simulation.marc_contact_pressure import MarcContactPressure
    from simscale_sdk_v1.models.simulation.marc_contact_pressure_type import MarcContactPressureType
    from simscale_sdk_v1.models.simulation.marc_contact_result_control_item import MarcContactResultControlItem
    from simscale_sdk_v1.models.simulation.marc_contact_status import MarcContactStatus
    from simscale_sdk_v1.models.simulation.marc_contact_status_type import MarcContactStatusType
    from simscale_sdk_v1.models.simulation.marc_displacement_field_selection import MarcDisplacementFieldSelection
    from simscale_sdk_v1.models.simulation.marc_displacement_result_control_item import (
        MarcDisplacementResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.marc_elastic_strain_type import MarcElasticStrainType
    from simscale_sdk_v1.models.simulation.marc_element_technology import MarcElementTechnology
    from simscale_sdk_v1.models.simulation.marc_equivalent_elastic_strain_type import MarcEquivalentElasticStrainType
    from simscale_sdk_v1.models.simulation.marc_equivalent_plastic_strain_type import MarcEquivalentPlasticStrainType
    from simscale_sdk_v1.models.simulation.marc_external_force_type import MarcExternalForceType
    from simscale_sdk_v1.models.simulation.marc_external_pressure_type import MarcExternalPressureType
    from simscale_sdk_v1.models.simulation.marc_force_field_selection import MarcForceFieldSelection
    from simscale_sdk_v1.models.simulation.marc_force_result_control_item import MarcForceResultControlItem
    from simscale_sdk_v1.models.simulation.marc_global_displacement_field_type import MarcGlobalDisplacementFieldType
    from simscale_sdk_v1.models.simulation.marc_heat_flux_result_control_item import MarcHeatFluxResultControlItem
    from simscale_sdk_v1.models.simulation.marc_linear_solver_settings import MarcLinearSolverSettings
    from simscale_sdk_v1.models.simulation.marc_material import MarcMaterial
    from simscale_sdk_v1.models.simulation.marc_min_max_fields_calculation_result_control_item import (
        MarcMinMaxFieldsCalculationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.marc_nonlinear_solver_settings import MarcNonlinearSolverSettings
    from simscale_sdk_v1.models.simulation.marc_numerics import MarcNumerics
    from simscale_sdk_v1.models.simulation.marc_output_writing_container import MarcOutputWritingContainer
    from simscale_sdk_v1.models.simulation.marc_plastic_strain_type import MarcPlasticStrainType
    from simscale_sdk_v1.models.simulation.marc_pressure_field_selection import MarcPressureFieldSelection
    from simscale_sdk_v1.models.simulation.marc_pressure_result_control_item import MarcPressureResultControlItem
    from simscale_sdk_v1.models.simulation.marc_principal_elastic_strain_type import MarcPrincipalElasticStrainType
    from simscale_sdk_v1.models.simulation.marc_principal_plastic_strain_type import MarcPrincipalPlasticStrainType
    from simscale_sdk_v1.models.simulation.marc_principal_stress_type import MarcPrincipalStressType
    from simscale_sdk_v1.models.simulation.marc_principal_total_strain_type import MarcPrincipalTotalStrainType
    from simscale_sdk_v1.models.simulation.marc_reaction_force_type import MarcReactionForceType
    from simscale_sdk_v1.models.simulation.marc_result_control import MarcResultControl
    from simscale_sdk_v1.models.simulation.marc_simulation_control import MarcSimulationControl
    from simscale_sdk_v1.models.simulation.marc_strain_field_selection import MarcStrainFieldSelection
    from simscale_sdk_v1.models.simulation.marc_strain_result_control_item import MarcStrainResultControlItem
    from simscale_sdk_v1.models.simulation.marc_stress_field_selection import MarcStressFieldSelection
    from simscale_sdk_v1.models.simulation.marc_stress_result_control_item import MarcStressResultControlItem
    from simscale_sdk_v1.models.simulation.marc_sum_fields_calculation_result_control_item import (
        MarcSumFieldsCalculationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.marc_temperature_result_control_item import MarcTemperatureResultControlItem
    from simscale_sdk_v1.models.simulation.marc_total_strain_type import MarcTotalStrainType
    from simscale_sdk_v1.models.simulation.marc_touching_contact_connection import MarcTouchingContactConnection
    from simscale_sdk_v1.models.simulation.marc_von_mises_stress_type import MarcVonMisesStressType
    from simscale_sdk_v1.models.simulation.marlow_hyperelastic_model_marc import MarlowHyperelasticModelMarc
    from simscale_sdk_v1.models.simulation.mass_flow import MassFlow
    from simscale_sdk_v1.models.simulation.material_library_reference import MaterialLibraryReference
    from simscale_sdk_v1.models.simulation.maximum_number_iteration_control import MaximumNumberIterationControl
    from simscale_sdk_v1.models.simulation.mean_age_of_fluid_result_type import MeanAgeOfFluidResultType
    from simscale_sdk_v1.models.simulation.mean_radiant_temperature_result_type import MeanRadiantTemperatureResultType
    from simscale_sdk_v1.models.simulation.mean_value_outlet_vbc import MeanValueOutletVBC
    from simscale_sdk_v1.models.simulation.mean_value_pbc import MeanValuePBC
    from simscale_sdk_v1.models.simulation.mean_value_vbc import MeanValueVBC
    from simscale_sdk_v1.models.simulation.min_max_fields_calculation_result_control_item import (
        MinMaxFieldsCalculationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.minimum_gap_size import MinimumGapSize
    from simscale_sdk_v1.models.simulation.mixed_timestep_calculation_type import MixedTimestepCalculationType
    from simscale_sdk_v1.models.simulation.mixing_length_inlet_ebc import MixingLengthInletEBC
    from simscale_sdk_v1.models.simulation.modal_base_control import ModalBaseControl
    from simscale_sdk_v1.models.simulation.modal_solver import ModalSolver
    from simscale_sdk_v1.models.simulation.modeled_turbulence_intensity import ModeledTurbulenceIntensity
    from simscale_sdk_v1.models.simulation.moderate_contact_stiffness import ModerateContactStiffness
    from simscale_sdk_v1.models.simulation.moderate_resolution import ModerateResolution
    from simscale_sdk_v1.models.simulation.moment_field_selection import MomentFieldSelection
    from simscale_sdk_v1.models.simulation.mooney_rivlin_hyper_elastic_model import MooneyRivlinHyperElasticModel
    from simscale_sdk_v1.models.simulation.mooney_type_hyperelastic_model_marc import MooneyTypeHyperelasticModelMarc
    from simscale_sdk_v1.models.simulation.moving_wall_vbc import MovingWallVBC
    from simscale_sdk_v1.models.simulation.mrt_solar_parameters import MrtSolarParameters
    from simscale_sdk_v1.models.simulation.multifrontal_solver import MultifrontalSolver
    from simscale_sdk_v1.models.simulation.multilinear_elasto_plastic_model import MultilinearElastoPlasticModel
    from simscale_sdk_v1.models.simulation.multilinear_model_marc import MultilinearModelMarc
    from simscale_sdk_v1.models.simulation.multiphase import Multiphase
    from simscale_sdk_v1.models.simulation.multiplied_slave_nodes_iteration_control import (
        MultipliedSlaveNodesIterationControl,
    )
    from simscale_sdk_v1.models.simulation.mumps_direct_solver import MumpsDirectSolver
    from simscale_sdk_v1.models.simulation.natural_convection_inlet_outlet_bc import NaturalConvectionInletOutletBC
    from simscale_sdk_v1.models.simulation.neo_hooke_hyper_elastic_model import NeoHookeHyperElasticModel
    from simscale_sdk_v1.models.simulation.new_region_refinement_pacefish_v38 import NewRegionRefinementPacefishV38
    from simscale_sdk_v1.models.simulation.new_surface_refinement_pacefish_v38 import NewSurfaceRefinementPacefishV38
    from simscale_sdk_v1.models.simulation.newmark_time_integration_scheme import NewmarkTimeIntegrationScheme
    from simscale_sdk_v1.models.simulation.newton_contact_non_linearity_resolution import (
        NewtonContactNonLinearityResolution,
    )
    from simscale_sdk_v1.models.simulation.newton_friction_non_linearity_resolution import (
        NewtonFrictionNonLinearityResolution,
    )
    from simscale_sdk_v1.models.simulation.newton_iteration_timestep_calculation_type import (
        NewtonIterationTimestepCalculationType,
    )
    from simscale_sdk_v1.models.simulation.newton_krylov_resolution_type import NewtonKrylovResolutionType
    from simscale_sdk_v1.models.simulation.newton_non_linearity_resolution import NewtonNonLinearityResolution
    from simscale_sdk_v1.models.simulation.newton_resolution_type import NewtonResolutionType
    from simscale_sdk_v1.models.simulation.newtonian_viscosity_model import NewtonianViscosityModel
    from simscale_sdk_v1.models.simulation.no_core_loss import NoCoreLoss
    from simscale_sdk_v1.models.simulation.no_creep import NoCreep
    from simscale_sdk_v1.models.simulation.no_creep_formulation import NoCreepFormulation
    from simscale_sdk_v1.models.simulation.no_current_ebc import NoCurrentEBC
    from simscale_sdk_v1.models.simulation.no_damage import NoDamage
    from simscale_sdk_v1.models.simulation.no_dielectric_losses import NoDielectricLosses
    from simscale_sdk_v1.models.simulation.no_dielectric_strength import NoDielectricStrength
    from simscale_sdk_v1.models.simulation.no_elastoplasticity import NoElastoplasticity
    from simscale_sdk_v1.models.simulation.no_fictitious_clearance import NoFictitiousClearance
    from simscale_sdk_v1.models.simulation.no_friction import NoFriction
    from simscale_sdk_v1.models.simulation.no_slip_vbc import NoSlipVBC
    from simscale_sdk_v1.models.simulation.no_slip_wall_aerodynamic_roughness import NoSlipWallAerodynamicRoughness
    from simscale_sdk_v1.models.simulation.no_slip_wall_equivalent_sand_roughness import (
        NoSlipWallEquivalentSandRoughness,
    )
    from simscale_sdk_v1.models.simulation.no_wall_thermal import NoWallThermal
    from simscale_sdk_v1.models.simulation.nodal_force_type import NodalForceType
    from simscale_sdk_v1.models.simulation.nodal_load_bc import NodalLoadBC
    from simscale_sdk_v1.models.simulation.nodal_moment_type import NodalMomentType
    from simscale_sdk_v1.models.simulation.non_monotomous_residual_retiming_event import (
        NonMonotomousResidualRetimingEvent,
    )
    from simscale_sdk_v1.models.simulation.none_damping import NoneDamping
    from simscale_sdk_v1.models.simulation.none_reactualization import NoneReactualization
    from simscale_sdk_v1.models.simulation.nonlinear_isotropic_permeability import NonlinearIsotropicPermeability
    from simscale_sdk_v1.models.simulation.normalized_displacement_result_control_item import (
        NormalizedDisplacementResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.normalized_displacement_type import NormalizedDisplacementType
    from simscale_sdk_v1.models.simulation.norton_creep_formulation import NortonCreepFormulation
    from simscale_sdk_v1.models.simulation.number_iterations_write_control import NumberIterationsWriteControl
    from simscale_sdk_v1.models.simulation.number_of_cells_per_direction import NumberOfCellsPerDirection
    from simscale_sdk_v1.models.simulation.oak import Oak
    from simscale_sdk_v1.models.simulation.off_position_tolerance import OffPositionTolerance
    from simscale_sdk_v1.models.simulation.ogden_hyper_elastic_model import OgdenHyperElasticModel
    from simscale_sdk_v1.models.simulation.ogden_hyperelastic_model_marc import OgdenHyperelasticModelMarc
    from simscale_sdk_v1.models.simulation.ogden_roxburgh import OgdenRoxburgh
    from simscale_sdk_v1.models.simulation.one_of_ami_rotating_zone_motion_type import OneOf_AMIRotatingZoneMotionType
    from simscale_sdk_v1.models.simulation.one_of__acceleration_field_selection_acceleration_type import (
        OneOf_AccelerationFieldSelectionAccelerationType,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_humidity_sources import (
        OneOf_AdvancedConceptsHumiditySources,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_momentum_sources import (
        OneOf_AdvancedConceptsMomentumSources,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_passive_scalar_sources import (
        OneOf_AdvancedConceptsPassiveScalarSources,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_porous_mediums import (
        OneOf_AdvancedConceptsPorousMediums,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_power_sources import (
        OneOf_AdvancedConceptsPowerSources,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_rotating_zones import (
        OneOf_AdvancedConceptsRotatingZones,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_solid_body_motions import (
        OneOf_AdvancedConceptsSolidBodyMotions,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_thermal_contact_resistance import (
        OneOf_AdvancedConceptsThermalContactResistance,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_concepts_thermal_resistance_networks import (
        OneOf_AdvancedConceptsThermalResistanceNetworks,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_mumps_settings_mumps_acceleration import (
        OneOf_AdvancedMUMPSSettingsMumpsAcceleration,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_modelling_porous_objects import (
        OneOf_AdvancedModellingPorousObjects,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_petsc_settings_preconditioner import (
        OneOf_AdvancedPETSCSettingsPreconditioner,
    )
    from simscale_sdk_v1.models.simulation.one_of__advanced_roi_settings_wind_tunnel_size import (
        OneOf_AdvancedROISettingsWindTunnelSize,
    )
    from simscale_sdk_v1.models.simulation.one_of__area_average_result_control_write_control import (
        OneOf_AreaAverageResultControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__area_integral_result_control_write_control import (
        OneOf_AreaIntegralResultControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__auto_timestep_definition_retiming_event import (
        OneOf_AutoTimestepDefinitionRetimingEvent,
    )
    from simscale_sdk_v1.models.simulation.one_of__automatic_simerics_mesh_settings_refinements import (
        OneOf_AutomaticSimericsMeshSettingsRefinements,
    )
    from simscale_sdk_v1.models.simulation.one_of__average_fields_calculation_result_control_item_field_selection import (
        OneOf_AverageFieldsCalculationResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__bathe_wilson_subspace_settings import (
        OneOf_BatheWilsonSubspaceSettings,
    )
    from simscale_sdk_v1.models.simulation.one_of__bilinear_elasto_plastic_model_hardening_model import (
        OneOf_BilinearElastoPlasticModelHardeningModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__bilinear_elasto_plastic_model_poissons_ratio import (
        OneOf_BilinearElastoPlasticModelPoissonsRatio,
    )
    from simscale_sdk_v1.models.simulation.one_of__bilinear_model_marc_hardening_model import (
        OneOf_BilinearModelMarcHardeningModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__bilinear_model_marc_hardening_rule import (
        OneOf_BilinearModelMarcHardeningRule,
    )
    from simscale_sdk_v1.models.simulation.one_of__bonded_contact_position_tolerance import (
        OneOf_BondedContactPositionTolerance,
    )
    from simscale_sdk_v1.models.simulation.one_of__coil_coil_type import OneOf_CoilCoilType
    from simscale_sdk_v1.models.simulation.one_of__coil_excitation import OneOf_CoilExcitation
    from simscale_sdk_v1.models.simulation.one_of__coil_topology import OneOf_CoilTopology
    from simscale_sdk_v1.models.simulation.one_of__component_vector_function_x import OneOf_ComponentVectorFunctionX
    from simscale_sdk_v1.models.simulation.one_of__component_vector_function_y import OneOf_ComponentVectorFunctionY
    from simscale_sdk_v1.models.simulation.one_of__component_vector_function_z import OneOf_ComponentVectorFunctionZ
    from simscale_sdk_v1.models.simulation.one_of__compressible_boundary_conditions import (
        OneOf_CompressibleBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__compressible_time_dependency import OneOf_CompressibleTimeDependency
    from simscale_sdk_v1.models.simulation.one_of__computing_core_domain_decomposition import (
        OneOf_ComputingCoreDomainDecomposition,
    )
    from simscale_sdk_v1.models.simulation.one_of__conjugate_heat_transfer_boundary_conditions import (
        OneOf_ConjugateHeatTransferBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__conjugate_heat_transfer_time_dependency import (
        OneOf_ConjugateHeatTransferTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_contact_non_linearity_resolution import (
        OneOf_ConnectionSettingsV36ContactNonLinearityResolution,
    )
    from simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_friction import (
        OneOf_ConnectionSettingsV36Friction,
    )
    from simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_nonlinearity_resolution import (
        OneOf_ConnectionSettingsV36NonlinearityResolution,
    )
    from simscale_sdk_v1.models.simulation.one_of__const_an_iso_transport_orientation import (
        OneOf_ConstAnIsoTransportOrientation,
    )
    from simscale_sdk_v1.models.simulation.one_of__const_cross_plane_orthotropic_transport_orientation import (
        OneOf_ConstCrossPlaneOrthotropicTransportOrientation,
    )
    from simscale_sdk_v1.models.simulation.one_of__const_transport_thermo import OneOf_ConstTransportThermo
    from simscale_sdk_v1.models.simulation.one_of__contact_conductance_layer_interface_thermal import (
        OneOf_ContactConductanceLayerInterfaceThermal,
    )
    from simscale_sdk_v1.models.simulation.one_of__contact_connections import OneOf_ContactConnections
    from simscale_sdk_v1.models.simulation.one_of__contact_field_selection_contact_type import (
        OneOf_ContactFieldSelectionContactType,
    )
    from simscale_sdk_v1.models.simulation.one_of__contact_resistance_layer_interface_thermal import (
        OneOf_ContactResistanceLayerInterfaceThermal,
    )
    from simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_boundary_conditions import (
        OneOf_ConvectiveHeatTransferBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_materials_fluids import (
        OneOf_ConvectiveHeatTransferMaterialsFluids,
    )
    from simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_time_dependency import (
        OneOf_ConvectiveHeatTransferTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__coulomb_friction_nonlinearity_resolution import (
        OneOf_CoulombFrictionNonlinearityResolution,
    )
    from simscale_sdk_v1.models.simulation.one_of__coupled_conjugate_heat_transfer_boundary_conditions import (
        OneOf_CoupledConjugateHeatTransferBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__coupled_conjugate_heat_transfer_materials_fluids import (
        OneOf_CoupledConjugateHeatTransferMaterialsFluids,
    )
    from simscale_sdk_v1.models.simulation.one_of__coupled_conjugate_heat_transfer_time_dependency import (
        OneOf_CoupledConjugateHeatTransferTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__current_excitation_current_type import (
        OneOf_CurrentExcitationCurrentType,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_eddy_viscosity import (
        OneOf_CustomFluidBCEddyViscosity,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_eddy_viscosity_compressible import (
        OneOf_CustomFluidBCEddyViscosityCompressible,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_epsilon_dissipation_rate import (
        OneOf_CustomFluidBCEpsilonDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_gauge_pressure import (
        OneOf_CustomFluidBCGaugePressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_gauge_pressure_rgh import (
        OneOf_CustomFluidBCGaugePressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_net_radiative_heat_flux import (
        OneOf_CustomFluidBCNetRadiativeHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_nu_tilda import OneOf_CustomFluidBCNuTilda
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_omega_dissipation_rate import (
        OneOf_CustomFluidBCOmegaDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_passive_scalars import (
        OneOf_CustomFluidBCPassiveScalars,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_phase_fraction import (
        OneOf_CustomFluidBCPhaseFraction,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_pressure import OneOf_CustomFluidBCPressure
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_pressure_rgh import OneOf_CustomFluidBCPressureRgh
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_temperature import OneOf_CustomFluidBCTemperature
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_dynamic_viscosity import (
        OneOf_CustomFluidBCTurbulentDynamicViscosity,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_kinetic_energy import (
        OneOf_CustomFluidBCTurbulentKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_thermal_diffusivity import (
        OneOf_CustomFluidBCTurbulentThermalDiffusivity,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_thermal_diffusivity_compressible import (
        OneOf_CustomFluidBCTurbulentThermalDiffusivityCompressible,
    )
    from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_velocity import OneOf_CustomFluidBCVelocity
    from simscale_sdk_v1.models.simulation.one_of__darcy_forchheimer_medium_orientation import (
        OneOf_DarcyForchheimerMediumOrientation,
    )
    from simscale_sdk_v1.models.simulation.one_of__darcy_forchheimer_medium_porous_media_heat_transfer import (
        OneOf_DarcyForchheimerMediumPorousMediaHeatTransfer,
    )
    from simscale_sdk_v1.models.simulation.one_of__darcy_medium_porous_material_type import (
        OneOf_DarcyMediumPorousMaterialType,
    )
    from simscale_sdk_v1.models.simulation.one_of__derived_heat_flux_wall_thermal import (
        OneOf_DerivedHeatFluxWallThermal,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__acceleration_value import (
        OneOf_DimensionalFunction_AccelerationValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__angle_value import (
        OneOf_DimensionalFunction_AngleValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__density_value import (
        OneOf_DimensionalFunction_DensityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__dimensionless_value import (
        OneOf_DimensionalFunction_DimensionlessValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__dynamic_viscosity_value import (
        OneOf_DimensionalFunction_DynamicViscosityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_conductivity_value import (
        OneOf_DimensionalFunction_ElectricConductivityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_current_value import (
        OneOf_DimensionalFunction_ElectricCurrentValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_field_strength_value import (
        OneOf_DimensionalFunction_ElectricFieldStrengthValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_potential_value import (
        OneOf_DimensionalFunction_ElectricPotentialValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_resistivity_value import (
        OneOf_DimensionalFunction_ElectricResistivityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__heat_flux_value import (
        OneOf_DimensionalFunction_HeatFluxValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__kinematic_viscosity_value import (
        OneOf_DimensionalFunction_KinematicViscosityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__length_value import (
        OneOf_DimensionalFunction_LengthValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__magnetic_flux_density_value import (
        OneOf_DimensionalFunction_MagneticFluxDensityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__mass_flow_rate_value import (
        OneOf_DimensionalFunction_MassFlowRateValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__power_value import (
        OneOf_DimensionalFunction_PowerValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__pressure_value import (
        OneOf_DimensionalFunction_PressureValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__rotation_speed_value import (
        OneOf_DimensionalFunction_RotationSpeedValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_energy_value import (
        OneOf_DimensionalFunction_SpecificEnergyValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_heat_value import (
        OneOf_DimensionalFunction_SpecificHeatValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_turbulence_dissipation_rate_value import (
        OneOf_DimensionalFunction_SpecificTurbulenceDissipationRateValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__speed_value import (
        OneOf_DimensionalFunction_SpeedValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__temperature_gradient_value import (
        OneOf_DimensionalFunction_TemperatureGradientValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__temperature_value import (
        OneOf_DimensionalFunction_TemperatureValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_conductivity_value import (
        OneOf_DimensionalFunction_ThermalConductivityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_expansion_rate_value import (
        OneOf_DimensionalFunction_ThermalExpansionRateValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_transmittance_value import (
        OneOf_DimensionalFunction_ThermalTransmittanceValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__time_value import (
        OneOf_DimensionalFunction_TimeValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__total_thermal_transmittance_value import (
        OneOf_DimensionalFunction_TotalThermalTransmittanceValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__turbulence_kinetic_energy_value import (
        OneOf_DimensionalFunction_TurbulenceKineticEnergyValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__turbulent_dissipation_value import (
        OneOf_DimensionalFunction_TurbulentDissipationValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__volumetric_flow_rate_value import (
        OneOf_DimensionalFunction_VolumetricFlowRateValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_function__volumetric_power_value import (
        OneOf_DimensionalFunction_VolumetricPowerValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__acceleration_value import (
        OneOf_DimensionalVectorFunction_AccelerationValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__force_value import (
        OneOf_DimensionalVectorFunction_ForceValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__length_value import (
        OneOf_DimensionalVectorFunction_LengthValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__pressure_value import (
        OneOf_DimensionalVectorFunction_PressureValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__speed_value import (
        OneOf_DimensionalVectorFunction_SpeedValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__torque_value import (
        OneOf_DimensionalVectorFunction_TorqueValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__volume_force_value import (
        OneOf_DimensionalVectorFunction_VolumeForceValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__directional_dependency_darcy_forchheimer_type import (
        OneOf_DirectionalDependencyDarcyForchheimerType,
    )
    from simscale_sdk_v1.models.simulation.one_of__directional_material_structure_mode import (
        OneOf_DirectionalMaterialStructureMode,
    )
    from simscale_sdk_v1.models.simulation.one_of__directional_material_structure_orientation import (
        OneOf_DirectionalMaterialStructureOrientation,
    )
    from simscale_sdk_v1.models.simulation.one_of__displacement_field_selection_displacement_type import (
        OneOf_DisplacementFieldSelectionDisplacementType,
    )
    from simscale_sdk_v1.models.simulation.one_of__displacements_convergence_method_convergence_criteria import (
        OneOf_DisplacementsConvergenceMethodConvergenceCriteria,
    )
    from simscale_sdk_v1.models.simulation.one_of__distributed_mass_bc_mass_definition import (
        OneOf_DistributedMassBCMassDefinition,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_r import OneOf_DivergenceSchemesDiv_Phi_R
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_enthalpy import (
        OneOf_DivergenceSchemesDiv_Phi_enthalpy,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_epsilon_dissipation_rate import (
        OneOf_DivergenceSchemesDiv_Phi_epsilonDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_internal_energy import (
        OneOf_DivergenceSchemesDiv_Phi_internalEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_kinetic_energy import (
        OneOf_DivergenceSchemesDiv_Phi_kineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_nu_tilda import (
        OneOf_DivergenceSchemesDiv_Phi_nuTilda,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_omega_dissipation_rate import (
        OneOf_DivergenceSchemesDiv_Phi_omegaDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_passive_scalar import (
        OneOf_DivergenceSchemesDiv_Phi_passiveScalar,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_temperature import (
        OneOf_DivergenceSchemesDiv_Phi_temperature,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_turbulent_kinetic_energy import (
        OneOf_DivergenceSchemesDiv_Phi_turbulentKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_velocity import (
        OneOf_DivergenceSchemesDiv_Phi_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phiv_pressure import (
        OneOf_DivergenceSchemesDiv_Phiv_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_r import OneOf_DivergenceSchemesDiv_R
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phi__ekp import (
        OneOf_DivergenceSchemesDiv_phi_Ekp,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phi_alpha import (
        OneOf_DivergenceSchemesDiv_phi_alpha,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phid_pressure import (
        OneOf_DivergenceSchemesDiv_phid_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phirb_alpha import (
        OneOf_DivergenceSchemesDiv_phirb_alpha,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_rho_phi_velocity import (
        OneOf_DivergenceSchemesDiv_rhoPhi_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_tau_mc import OneOf_DivergenceSchemesDiv_tauMC
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_velocity import (
        OneOf_DivergenceSchemesDiv_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_for_default import (
        OneOf_DivergenceSchemesForDefault,
    )
    from simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_boundary_conditions import (
        OneOf_DynamicAnalysisBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_connection_groups import (
        OneOf_DynamicAnalysisConnectionGroups,
    )
    from simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_connectors import OneOf_DynamicAnalysisConnectors
    from simscale_sdk_v1.models.simulation.one_of_erp_calculation_result_control_item_field_selection import (
        OneOf_ERPCalculationResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__elastic_support_bc_spring_stiffness import (
        OneOf_ElasticSupportBCSpringStiffness,
    )
    from simscale_sdk_v1.models.simulation.one_of__elasticity_marc_poissons_ratio import (
        OneOf_ElasticityMarcPoissonsRatio,
    )
    from simscale_sdk_v1.models.simulation.one_of__elastoplastic_network_plasticity_model_elastoplastic_network import (
        OneOf_ElastoplasticNetworkPlasticityModelElastoplasticNetwork,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_analysis_boundary_conditions import (
        OneOf_ElectromagneticAnalysisBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_analysis_model import (
        OneOf_ElectromagneticAnalysisModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_core_losses_type import (
        OneOf_ElectromagneticMaterialCoreLossesType,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_dielectric_loss_type import (
        OneOf_ElectromagneticMaterialDielectricLossType,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_dielectric_strength_type import (
        OneOf_ElectromagneticMaterialDielectricStrengthType,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_electric_conductivity_type import (
        OneOf_ElectromagneticMaterialElectricConductivityType,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_magnetic_permeability_type import (
        OneOf_ElectromagneticMaterialMagneticPermeabilityType,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_material_behavior import (
        OneOf_ElectromagneticMaterialMaterialBehavior,
    )
    from simscale_sdk_v1.models.simulation.one_of__electromagnetic_result_control_probe_point_field_selection import (
        OneOf_ElectromagneticResultControlProbePointFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__element_technology_definition_method import (
        OneOf_ElementTechnologyDefinitionMethod,
    )
    from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_boundary_conditions import (
        OneOf_EmbeddedBoundaryBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_external_flow_boundary_condition import (
        OneOf_EmbeddedBoundaryExternalFlowBoundaryCondition,
    )
    from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_meshing_refinements import (
        OneOf_EmbeddedBoundaryMeshingRefinements,
    )
    from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_meshing_sizing import (
        OneOf_EmbeddedBoundaryMeshingSizing,
    )
    from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_time_dependency import (
        OneOf_EmbeddedBoundaryTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__error_retiming_event_timestep_calculation_type import (
        OneOf_ErrorRetimingEventTimestepCalculationType,
    )
    from simscale_sdk_v1.models.simulation.one_of__explicit_time_integration_type_scheme import (
        OneOf_ExplicitTimeIntegrationTypeScheme,
    )
    from simscale_sdk_v1.models.simulation.one_of__external_wall_heat_flux_tbc_heat_flux import (
        OneOf_ExternalWallHeatFluxTBCHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__fan_bc_net_radiative_heat_flux import OneOf_FanBCNetRadiativeHeatFlux
    from simscale_sdk_v1.models.simulation.one_of__fan_bc_pressure_rgh import OneOf_FanBCPressureRgh
    from simscale_sdk_v1.models.simulation.one_of__fan_bc_radiative_intensity_ray import (
        OneOf_FanBCRadiativeIntensityRay,
    )
    from simscale_sdk_v1.models.simulation.one_of__fan_bc_temperature import OneOf_FanBCTemperature
    from simscale_sdk_v1.models.simulation.one_of__fan_bc_turbulence import OneOf_FanBCTurbulence
    from simscale_sdk_v1.models.simulation.one_of__field_calculations_pressure_result_control_pressure_type import (
        OneOf_FieldCalculationsPressureResultControlPressureType,
    )
    from simscale_sdk_v1.models.simulation.one_of__field_calculations_pressure_result_control_result_type import (
        OneOf_FieldCalculationsPressureResultControlResultType,
    )
    from simscale_sdk_v1.models.simulation.one_of__field_calculations_turbulence_result_control_result_type import (
        OneOf_FieldCalculationsTurbulenceResultControlResultType,
    )
    from simscale_sdk_v1.models.simulation.one_of__field_calculations_wall_heat_flux_result_control_reference_temperature_result_type import (
        OneOf_FieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType,
    )
    from simscale_sdk_v1.models.simulation.one_of__field_change_retiming_event_field_selection import (
        OneOf_FieldChangeRetimingEventFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__field_change_retiming_event_timestep_calculation_type import (
        OneOf_FieldChangeRetimingEventTimestepCalculationType,
    )
    from simscale_sdk_v1.models.simulation.one_of__fixed_coeff_medium_orientation import (
        OneOf_FixedCoeffMediumOrientation,
    )
    from simscale_sdk_v1.models.simulation.one_of__fixed_coeff_medium_porous_media_heat_transfer import (
        OneOf_FixedCoeffMediumPorousMediaHeatTransfer,
    )
    from simscale_sdk_v1.models.simulation.one_of__fixed_point_contact_non_linearity_resolution_iteration_control import (
        OneOf_FixedPointContactNonLinearityResolutionIterationControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__fixed_point_non_linearity_resolution_geometry_reactualization import (
        OneOf_FixedPointNonLinearityResolutionGeometryReactualization,
    )
    from simscale_sdk_v1.models.simulation.one_of__fixed_value_rhbc_humidity_value import (
        OneOf_FixedValueRHBCHumidityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_xmax import OneOf_FlowDomainBoundariesXMAX
    from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_xmin import OneOf_FlowDomainBoundariesXMIN
    from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_ymax import OneOf_FlowDomainBoundariesYMAX
    from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_ymin import OneOf_FlowDomainBoundariesYMIN
    from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_zmax import OneOf_FlowDomainBoundariesZMAX
    from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_zmin import OneOf_FlowDomainBoundariesZMIN
    from simscale_sdk_v1.models.simulation.one_of__flow_rate_inlet_vbc_flow_rate import OneOf_FlowRateInletVBCFlowRate
    from simscale_sdk_v1.models.simulation.one_of__flow_rate_mean_inlet_vbc_flow_rate import (
        OneOf_FlowRateMeanInletVBCFlowRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__flow_rate_mean_outlet_vbc_flow_rate import (
        OneOf_FlowRateMeanOutletVBCFlowRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__flow_rate_outlet_vbc_flow_rate import OneOf_FlowRateOutletVBCFlowRate
    from simscale_sdk_v1.models.simulation.one_of__flow_rate_stable_outlet_vbc_flow_rate import (
        OneOf_FlowRateStableOutletVBCFlowRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_equation_of_state import (
        OneOf_FluidCompressibleMaterialEquationOfState,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_fluid_type import (
        OneOf_FluidCompressibleMaterialFluidType,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_transport import (
        OneOf_FluidCompressibleMaterialTransport,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_viscosity_model import (
        OneOf_FluidCompressibleMaterialViscosityModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_model_delta_coefficient import OneOf_FluidModelDeltaCoefficient
    from simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_field_calculations import (
        OneOf_FluidResultControlsFieldCalculations,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_forces_moments import (
        OneOf_FluidResultControlsForcesMoments,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_surface_data import (
        OneOf_FluidResultControlsSurfaceData,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_adjustable_timestep import (
        OneOf_FluidSimulationControlAdjustableTimestep,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_decompose_algorithm import (
        OneOf_FluidSimulationControlDecomposeAlgorithm,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_write_control import (
        OneOf_FluidSimulationControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_density_final_solver import (
        OneOf_FluidSolversDensityFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_density_solver import OneOf_FluidSolversDensitySolver
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_enthalpy_final_solver import (
        OneOf_FluidSolversEnthalpyFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_enthalpy_solver import OneOf_FluidSolversEnthalpySolver
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_epsilon_dissipation_rate_final_solver import (
        OneOf_FluidSolversEpsilonDissipationRateFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_epsilon_dissipation_rate_solver import (
        OneOf_FluidSolversEpsilonDissipationRateSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_internal_energy_final_solver import (
        OneOf_FluidSolversInternalEnergyFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_internal_energy_solver import (
        OneOf_FluidSolversInternalEnergySolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_nu_tilda_final_solver import (
        OneOf_FluidSolversNuTildaFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_nu_tilda_solver import OneOf_FluidSolversNuTildaSolver
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_omega_dissipation_rate_final_solver import (
        OneOf_FluidSolversOmegaDissipationRateFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_omega_dissipation_rate_solver import (
        OneOf_FluidSolversOmegaDissipationRateSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_passive_scalar_solver import (
        OneOf_FluidSolversPassiveScalarSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_final_solver import (
        OneOf_FluidSolversPressureFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_rgh_final_solver import (
        OneOf_FluidSolversPressureRghFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_rgh_solver import (
        OneOf_FluidSolversPressureRghSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_solver import OneOf_FluidSolversPressureSolver
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_radiative_intensity_ray_solver import (
        OneOf_FluidSolversRadiativeIntensityRaySolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_solid_enthalpy_final_solver import (
        OneOf_FluidSolversSolidEnthalpyFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_solid_enthalpy_solver import (
        OneOf_FluidSolversSolidEnthalpySolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_specific_humidity_solver import (
        OneOf_FluidSolversSpecificHumiditySolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_temperature_final_solver import (
        OneOf_FluidSolversTemperatureFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_temperature_solver import (
        OneOf_FluidSolversTemperatureSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_turbulent_kinetic_energy_final_solver import (
        OneOf_FluidSolversTurbulentKineticEnergyFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_turbulent_kinetic_energy_solver import (
        OneOf_FluidSolversTurbulentKineticEnergySolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_velocity_final_solver import (
        OneOf_FluidSolversVelocityFinalSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_velocity_solver import OneOf_FluidSolversVelocitySolver
    from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_voltage_solver import OneOf_FluidSolversVoltageSolver
    from simscale_sdk_v1.models.simulation.one_of__flux_schemes_for_default import OneOf_FluxSchemesForDefault
    from simscale_sdk_v1.models.simulation.one_of__force_field_selection_force_type import (
        OneOf_ForceFieldSelectionForceType,
    )
    from simscale_sdk_v1.models.simulation.one_of__force_moment_coefficients_result_control_write_control import (
        OneOf_ForceMomentCoefficientsResultControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__force_result_control_item_force_type import (
        OneOf_ForceResultControlItemForceType,
    )
    from simscale_sdk_v1.models.simulation.one_of__forces_moments_result_control_write_control import (
        OneOf_ForcesMomentsResultControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__freestream_vbc_ambient_pressure import (
        OneOf_FreestreamVBCAmbientPressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__frequency_analysis_boundary_conditions import (
        OneOf_FrequencyAnalysisBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__frequency_analysis_connectors import (
        OneOf_FrequencyAnalysisConnectors,
    )
    from simscale_sdk_v1.models.simulation.one_of__friction_contact_contact_solution_method import (
        OneOf_FrictionContactContactSolutionMethod,
    )
    from simscale_sdk_v1.models.simulation.one_of__friction_contact_fictitious_clearance import (
        OneOf_FrictionContactFictitiousClearance,
    )
    from simscale_sdk_v1.models.simulation.one_of__friction_contact_friction_coefficient import (
        OneOf_FrictionContactFrictionCoefficient,
    )
    from simscale_sdk_v1.models.simulation.one_of__frictionless_contact_contact_solution_method import (
        OneOf_FrictionlessContactContactSolutionMethod,
    )
    from simscale_sdk_v1.models.simulation.one_of__frictionless_contact_fictitious_clearance import (
        OneOf_FrictionlessContactFictitiousClearance,
    )
    from simscale_sdk_v1.models.simulation.one_of__general_darcy_forchheimer_pacefish_darcy_forchheimer_type import (
        OneOf_GeneralDarcyForchheimerPacefishDarcyForchheimerType,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_for_default import OneOf_GradientSchemesForDefault
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_density import (
        OneOf_GradientSchemesGrad_density,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_enthalpy import (
        OneOf_GradientSchemesGrad_enthalpy,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_epsilon_dissipation_rate import (
        OneOf_GradientSchemesGrad_epsilonDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_internal_energy import (
        OneOf_GradientSchemesGrad_internalEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_nu_tilda import (
        OneOf_GradientSchemesGrad_nuTilda,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_omega_dissipation_rate import (
        OneOf_GradientSchemesGrad_omegaDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_pressure import (
        OneOf_GradientSchemesGrad_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_pressure_rgh import (
        OneOf_GradientSchemesGrad_pressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_rhok import OneOf_GradientSchemesGrad_rhok
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_temperature import (
        OneOf_GradientSchemesGrad_temperature,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_turbulent_kinetic_energy import (
        OneOf_GradientSchemesGrad_turbulentKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_velocity import (
        OneOf_GradientSchemesGrad_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of_h_const_thermo_equation_of_state import (
        OneOf_HConstThermoEquationOfState,
    )
    from simscale_sdk_v1.models.simulation.one_of__harmonic_acceleration_result_control_item_harmonic_acceleration_type import (
        OneOf_HarmonicAccelerationResultControlItemHarmonicAccelerationType,
    )
    from simscale_sdk_v1.models.simulation.one_of__harmonic_analysis_boundary_conditions import (
        OneOf_HarmonicAnalysisBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__harmonic_analysis_connectors import OneOf_HarmonicAnalysisConnectors
    from simscale_sdk_v1.models.simulation.one_of__harmonic_displacement_result_control_item_harmonic_displacement_type import (
        OneOf_HarmonicDisplacementResultControlItemHarmonicDisplacementType,
    )
    from simscale_sdk_v1.models.simulation.one_of__harmonic_response_control_excitation_frequencies import (
        OneOf_HarmonicResponseControlExcitationFrequencies,
    )
    from simscale_sdk_v1.models.simulation.one_of__harmonic_response_result_control_item_field_selection import (
        OneOf_HarmonicResponseResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__harmonic_velocity_result_control_item_harmonic_velocity_type import (
        OneOf_HarmonicVelocityResultControlItemHarmonicVelocityType,
    )
    from simscale_sdk_v1.models.simulation.one_of__heat_exchanger_source_heat_exchanger_mode import (
        OneOf_HeatExchangerSourceHeatExchangerMode,
    )
    from simscale_sdk_v1.models.simulation.one_of__heat_transfer_boundary_conditions import (
        OneOf_HeatTransferBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__heat_transfer_time_dependency import OneOf_HeatTransferTimeDependency
    from simscale_sdk_v1.models.simulation.one_of__hinge_constraint_bc_axis_definition import (
        OneOf_HingeConstraintBCAxisDefinition,
    )
    from simscale_sdk_v1.models.simulation.one_of__hyper_elastic_material_behavior_hyper_elastic_model import (
        OneOf_HyperElasticMaterialBehaviorHyperElasticModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__hyperelasticity_hyperelastic_model_marc import (
        OneOf_HyperelasticityHyperelasticModelMarc,
    )
    from simscale_sdk_v1.models.simulation.one_of_iram_sorensen_subspace_settings import (
        OneOf_IRAMSorensenSubspaceSettings,
    )
    from simscale_sdk_v1.models.simulation.one_of__implicit_time_integration_type_scheme import (
        OneOf_ImplicitTimeIntegrationTypeScheme,
    )
    from simscale_sdk_v1.models.simulation.one_of__incompressible_boundary_conditions import (
        OneOf_IncompressibleBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__incompressible_material_fluid_type import (
        OneOf_IncompressibleMaterialFluidType,
    )
    from simscale_sdk_v1.models.simulation.one_of__incompressible_material_viscosity_model import (
        OneOf_IncompressibleMaterialViscosityModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__incompressible_pacefish_mesh_settings_new import (
        OneOf_IncompressiblePacefishMeshSettingsNew,
    )
    from simscale_sdk_v1.models.simulation.one_of__incompressible_time_dependency import (
        OneOf_IncompressibleTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__inlet_outlet_rhbc_humidity_value import (
        OneOf_InletOutletRHBCHumidityValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_for_default import (
        OneOf_InterpolationSchemesForDefault,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate__hby_a import (
        OneOf_InterpolationSchemesInterpolate_HbyA,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_grad_enthalpy import (
        OneOf_InterpolationSchemesInterpolate_grad_enthalpy,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_kappa import (
        OneOf_InterpolationSchemesInterpolate_kappa,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_map__kappa import (
        OneOf_InterpolationSchemesInterpolate_map_Kappa,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_r_au import (
        OneOf_InterpolationSchemesInterpolate_rAU,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho import (
        OneOf_InterpolationSchemesInterpolate_rho,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho_0_velocity0 import (
        OneOf_InterpolationSchemesInterpolate_rho_0_velocity0,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho__hbya import (
        OneOf_InterpolationSchemesInterpolate_rho_Hbya,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho_r_au import (
        OneOf_InterpolationSchemesInterpolate_rho_rAU,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_thermo_rho__cp import (
        OneOf_InterpolationSchemesInterpolate_thermo_rho_Cp,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_velocity import (
        OneOf_InterpolationSchemesInterpolate_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_velocity0 import (
        OneOf_InterpolationSchemesInterpolate_velocity0,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_rho import (
        OneOf_InterpolationSchemesReconstruct_rho,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_temperature import (
        OneOf_InterpolationSchemesReconstruct_temperature,
    )
    from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_velocity import (
        OneOf_InterpolationSchemesReconstruct_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__isotropic_directional_dependency_poissons_ratio import (
        OneOf_IsotropicDirectionalDependencyPoissonsRatio,
    )
    from simscale_sdk_v1.models.simulation.one_of__isotropic_plastic_hardening_poissons_ratio import (
        OneOf_IsotropicPlasticHardeningPoissonsRatio,
    )
    from simscale_sdk_v1.models.simulation.one_of__isotropic_spring_stiffness_stiffness_definition import (
        OneOf_IsotropicSpringStiffnessStiffnessDefinition,
    )
    from simscale_sdk_v1.models.simulation.one_of__johnson_cook_elasto_plastic_model_poissons_ratio import (
        OneOf_JohnsonCookElastoPlasticModelPoissonsRatio,
    )
    from simscale_sdk_v1.models.simulation.one_of__lanczos_subspace_settings import OneOf_LanczosSubspaceSettings
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_for_default import OneOf_LaplacianSchemesForDefault
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_1_a_u_pressure import (
        OneOf_LaplacianSchemesLaplacian_1A_U_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_dr_eff_r import (
        OneOf_LaplacianSchemesLaplacian_DREff_R,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_dt_passive_scalar import (
        OneOf_LaplacianSchemesLaplacian_DT_passiveScalar,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__depsilon_eff_epsilon_dissipation_rate import (
        OneOf_LaplacianSchemesLaplacian_DepsilonEff_epsilonDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dk_eff_turbulent_kinetic_energy import (
        OneOf_LaplacianSchemesLaplacian_DkEff_turbulentKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dnu_tilda_eff_nu_tilda import (
        OneOf_LaplacianSchemesLaplacian_DnuTildaEff_nuTilda,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__domega_eff_omega_dissipation_rate import (
        OneOf_LaplacianSchemesLaplacian_DomegaEff_omegaDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dp_pressure import (
        OneOf_LaplacianSchemesLaplacian_Dp_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__nu_eff_velocity import (
        OneOf_LaplacianSchemesLaplacian_NuEff_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__nu_velocity import (
        OneOf_LaplacianSchemesLaplacian_Nu_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_enthalpy import (
        OneOf_LaplacianSchemesLaplacian_alphaEff_enthalpy,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_internal_energy import (
        OneOf_LaplacianSchemesLaplacian_alphaEff_internalEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_temperature import (
        OneOf_LaplacianSchemesLaplacian_alphaEff_temperature,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_enthalpy import (
        OneOf_LaplacianSchemesLaplacian_alpha_enthalpy,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_mu_eff_velocity import (
        OneOf_LaplacianSchemesLaplacian_muEff_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_mut_velocity import (
        OneOf_LaplacianSchemesLaplacian_mut_velocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_r_a_uf_pressure import (
        OneOf_LaplacianSchemesLaplacian_rAUf_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_r_a_uf_pressure_rgh import (
        OneOf_LaplacianSchemesLaplacian_rAUf_pressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rho_1_a_u_pressure import (
        OneOf_LaplacianSchemesLaplacian_rho_1_A_U_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rhor_a_uf_pressure import (
        OneOf_LaplacianSchemesLaplacian_rhorAUf_pressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rhor_a_uf_pressure_rgh import (
        OneOf_LaplacianSchemesLaplacian_rhorAUf_pressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__linear_elastic_marc_material_behavior_poissons_ratio import (
        OneOf_LinearElasticMarcMaterialBehaviorPoissonsRatio,
    )
    from simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_creep_formulation import (
        OneOf_LinearElasticMaterialBehaviorCreepFormulation,
    )
    from simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_damping import (
        OneOf_LinearElasticMaterialBehaviorDamping,
    )
    from simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_directional_dependency import (
        OneOf_LinearElasticMaterialBehaviorDirectionalDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__litz_wire_coil_strand_cross_section_type import (
        OneOf_LitzWireCoilStrandCrossSectionType,
    )
    from simscale_sdk_v1.models.simulation.one_of_mules_solver_semi_implicit import OneOf_MULESSolverSemiImplicit
    from simscale_sdk_v1.models.simulation.one_of__manual_simerics_mesh_settings_cell_size_specification import (
        OneOf_ManualSimericsMeshSettingsCellSizeSpecification,
    )
    from simscale_sdk_v1.models.simulation.one_of__manual_simerics_mesh_settings_refinements import (
        OneOf_ManualSimericsMeshSettingsRefinements,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_analysis_boundary_conditions import (
        OneOf_MarcAnalysisBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_average_fields_calculation_result_control_item_field_selection import (
        OneOf_MarcAverageFieldsCalculationResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_bonded_and_touching_contact_connection_position_tolerance import (
        OneOf_MarcBondedAndTouchingContactConnectionPositionTolerance,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_bonded_contact_connection_position_tolerance import (
        OneOf_MarcBondedContactConnectionPositionTolerance,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_connection_group_connections import (
        OneOf_MarcConnectionGroupConnections,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_connector_point_data_item_results import (
        OneOf_MarcConnectorPointDataItemResults,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_contact_field_selection_contact_type import (
        OneOf_MarcContactFieldSelectionContactType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_contact_force_field_selection_contact_type import (
        OneOf_MarcContactForceFieldSelectionContactType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_contact_result_control_item_contact_type import (
        OneOf_MarcContactResultControlItemContactType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_force_field_selection_force_type import (
        OneOf_MarcForceFieldSelectionForceType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_force_result_control_item_force_type import (
        OneOf_MarcForceResultControlItemForceType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_linear_solver_settings_linear_solver import (
        OneOf_MarcLinearSolverSettingsLinearSolver,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_material_marc_material_behavior import (
        OneOf_MarcMaterialMarcMaterialBehavior,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_min_max_fields_calculation_result_control_item_field_selection import (
        OneOf_MarcMinMaxFieldsCalculationResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_nonlinear_solver_settings_convergence_method import (
        OneOf_MarcNonlinearSolverSettingsConvergenceMethod,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_output_writing_container_output_writing import (
        OneOf_MarcOutputWritingContainerOutputWriting,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_result_control_area_calculation import (
        OneOf_MarcResultControlAreaCalculation,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_result_control_solution_fields import (
        OneOf_MarcResultControlSolutionFields,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_result_control_volume_calculation import (
        OneOf_MarcResultControlVolumeCalculation,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_simulation_control_timestep_definition import (
        OneOf_MarcSimulationControlTimestepDefinition,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_strain_field_selection_strain_type import (
        OneOf_MarcStrainFieldSelectionStrainType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_strain_result_control_item_strain_type import (
        OneOf_MarcStrainResultControlItemStrainType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_stress_field_selection_stress_type import (
        OneOf_MarcStressFieldSelectionStressType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_stress_result_control_item_stress_type import (
        OneOf_MarcStressResultControlItemStressType,
    )
    from simscale_sdk_v1.models.simulation.one_of__marc_sum_fields_calculation_result_control_item_field_selection import (
        OneOf_MarcSumFieldsCalculationResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__min_max_fields_calculation_result_control_item_field_selection import (
        OneOf_MinMaxFieldsCalculationResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__modal_base_control_eigenfrequency_scope import (
        OneOf_ModalBaseControlEigenfrequencyScope,
    )
    from simscale_sdk_v1.models.simulation.one_of__modal_solver_eigen_solver import OneOf_ModalSolverEigenSolver
    from simscale_sdk_v1.models.simulation.one_of__modal_solver_solver import OneOf_ModalSolverSolver
    from simscale_sdk_v1.models.simulation.one_of__moment_field_selection_moment_type import (
        OneOf_MomentFieldSelectionMomentType,
    )
    from simscale_sdk_v1.models.simulation.one_of__mrt_solar_parameters_fraction_body_surface import (
        OneOf_MrtSolarParametersFractionBodySurface,
    )
    from simscale_sdk_v1.models.simulation.one_of__multilinear_model_marc_hardening_rule import (
        OneOf_MultilinearModelMarcHardeningRule,
    )
    from simscale_sdk_v1.models.simulation.one_of__multiphase_boundary_conditions import (
        OneOf_MultiphaseBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_net_radiative_heat_flux import (
        OneOf_NaturalConvectionInletOutletBCNetRadiativeHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_pressure_rgh import (
        OneOf_NaturalConvectionInletOutletBCPressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_turbulence import (
        OneOf_NaturalConvectionInletOutletBCTurbulence,
    )
    from simscale_sdk_v1.models.simulation.one_of__new_region_refinement_pacefish_v38_mesh_sizing import (
        OneOf_NewRegionRefinementPacefishV38MeshSizing,
    )
    from simscale_sdk_v1.models.simulation.one_of__new_surface_refinement_pacefish_v38_mesh_sizing import (
        OneOf_NewSurfaceRefinementPacefishV38MeshSizing,
    )
    from simscale_sdk_v1.models.simulation.one_of__newton_krylov_resolution_type_convergence_criteria import (
        OneOf_NewtonKrylovResolutionTypeConvergenceCriteria,
    )
    from simscale_sdk_v1.models.simulation.one_of__newton_krylov_resolution_type_jacobian_matrix import (
        OneOf_NewtonKrylovResolutionTypeJacobianMatrix,
    )
    from simscale_sdk_v1.models.simulation.one_of__newton_resolution_type_convergence_criteria import (
        OneOf_NewtonResolutionTypeConvergenceCriteria,
    )
    from simscale_sdk_v1.models.simulation.one_of__newton_resolution_type_jacobian_matrix import (
        OneOf_NewtonResolutionTypeJacobianMatrix,
    )
    from simscale_sdk_v1.models.simulation.one_of__no_slip_vbc_no_slip_wall_roughness_type import (
        OneOf_NoSlipVBCNoSlipWallRoughnessType,
    )
    from simscale_sdk_v1.models.simulation.one_of__non_monotomous_residual_retiming_event_timestep_calculation_type import (
        OneOf_NonMonotomousResidualRetimingEventTimestepCalculationType,
    )
    from simscale_sdk_v1.models.simulation.one_of__ogden_hyper_elastic_model_order import (
        OneOf_OgdenHyperElasticModelOrder,
    )
    from simscale_sdk_v1.models.simulation.one_of__ogden_hyperelastic_model_marc_number_of_terms import (
        OneOf_OgdenHyperelasticModelMarcNumberOfTerms,
    )
    from simscale_sdk_v1.models.simulation.one_of__orthotropic_directional_dependency_poissons_ratio_xy import (
        OneOf_OrthotropicDirectionalDependencyPoissonsRatioXY,
    )
    from simscale_sdk_v1.models.simulation.one_of__orthotropic_directional_dependency_poissons_ratio_xz import (
        OneOf_OrthotropicDirectionalDependencyPoissonsRatioXZ,
    )
    from simscale_sdk_v1.models.simulation.one_of__orthotropic_directional_dependency_poissons_ratio_yz import (
        OneOf_OrthotropicDirectionalDependencyPoissonsRatioYZ,
    )
    from simscale_sdk_v1.models.simulation.one_of__orthotropic_spring_stiffness_stiffness_definition import (
        OneOf_OrthotropicSpringStiffnessStiffnessDefinition,
    )
    from simscale_sdk_v1.models.simulation.one_of_pbicg_solver_preconditioner import OneOf_PBICGSolverPreconditioner
    from simscale_sdk_v1.models.simulation.one_of_pbicg_stab_solver_preconditioner import (
        OneOf_PBICGStabSolverPreconditioner,
    )
    from simscale_sdk_v1.models.simulation.one_of_pcg_solver_preconditioner import OneOf_PCGSolverPreconditioner
    from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_automatic_gap_closing import (
        OneOf_PacefishAutomeshAutomaticGapClosing,
    )
    from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_new_fineness import (
        OneOf_PacefishAutomeshNewFineness,
    )
    from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_primary_topology import (
        OneOf_PacefishAutomeshPrimaryTopology,
    )
    from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_reference_length_computation import (
        OneOf_PacefishAutomeshReferenceLengthComputation,
    )
    from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_refinements import (
        OneOf_PacefishAutomeshRefinements,
    )
    from simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_reynolds_scaling_type import (
        OneOf_PacefishAutomeshReynoldsScalingType,
    )
    from simscale_sdk_v1.models.simulation.one_of__pacefish_mesh_legacy_refinements import (
        OneOf_PacefishMeshLegacyRefinements,
    )
    from simscale_sdk_v1.models.simulation.one_of__partial_vector_function_x import OneOf_PartialVectorFunctionX
    from simscale_sdk_v1.models.simulation.one_of__partial_vector_function_y import OneOf_PartialVectorFunctionY
    from simscale_sdk_v1.models.simulation.one_of__partial_vector_function_z import OneOf_PartialVectorFunctionZ
    from simscale_sdk_v1.models.simulation.one_of__pedestrian_comfort_surface_ground import (
        OneOf_PedestrianComfortSurfaceGround,
    )
    from simscale_sdk_v1.models.simulation.one_of__penalty_method_contact_stiffness import (
        OneOf_PenaltyMethodContactStiffness,
    )
    from simscale_sdk_v1.models.simulation.one_of__perforated_plate_porous_media_heat_transfer import (
        OneOf_PerforatedPlatePorousMediaHeatTransfer,
    )
    from simscale_sdk_v1.models.simulation.one_of__permanent_magnet_material_magnetization_direction_type import (
        OneOf_PermanentMagnetMaterialMagnetizationDirectionType,
    )
    from simscale_sdk_v1.models.simulation.one_of__physical_contact_connections import OneOf_PhysicalContactConnections
    from simscale_sdk_v1.models.simulation.one_of__pin_kinematic_behavior_axial_translation import (
        OneOf_PinKinematicBehaviorAxialTranslation,
    )
    from simscale_sdk_v1.models.simulation.one_of__pin_kinematic_behavior_rotation import (
        OneOf_PinKinematicBehaviorRotation,
    )
    from simscale_sdk_v1.models.simulation.one_of__plastic_material_behavior_elasto_plastic_model import (
        OneOf_PlasticMaterialBehaviorElastoPlasticModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__plasticity_marc_plasticity_model import (
        OneOf_PlasticityMarcPlasticityModel,
    )
    from simscale_sdk_v1.models.simulation.one_of__plate_data_hole_shape import OneOf_PlateDataHoleShape
    from simscale_sdk_v1.models.simulation.one_of__porous_tree_tree_type import OneOf_PorousTreeTreeType
    from simscale_sdk_v1.models.simulation.one_of__power_law_medium_porous_media_heat_transfer import (
        OneOf_PowerLawMediumPorousMediaHeatTransfer,
    )
    from simscale_sdk_v1.models.simulation.one_of__prandtl_les_delta_delta_coefficient import (
        OneOf_PrandtlLesDeltaDeltaCoefficient,
    )
    from simscale_sdk_v1.models.simulation.one_of__prescribed_optional_function_value import (
        OneOf_PrescribedOptionalFunctionValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_gauge_pressure import (
        OneOf_PressureInletBCGaugePressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_net_radiative_heat_flux import (
        OneOf_PressureInletBCNetRadiativeHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_pressure import OneOf_PressureInletBCPressure
    from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_pressure_rgh import (
        OneOf_PressureInletBCPressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_radiative_intensity_ray import (
        OneOf_PressureInletBCRadiativeIntensityRay,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_temperature import OneOf_PressureInletBCTemperature
    from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_turbulence import OneOf_PressureInletBCTurbulence
    from simscale_sdk_v1.models.simulation.one_of__pressure_loss_curve_porous_media_heat_transfer import (
        OneOf_PressureLossCurvePorousMediaHeatTransfer,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_loss_function_medium_porous_material_type import (
        OneOf_PressureLossFunctionMediumPorousMaterialType,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_gauge_pressure import (
        OneOf_PressureOutletBCGaugePressure,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_gauge_pressure_rgh import (
        OneOf_PressureOutletBCGaugePressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_net_radiative_heat_flux import (
        OneOf_PressureOutletBCNetRadiativeHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_phase_fractions_v2 import (
        OneOf_PressureOutletBCPhaseFractionsV2,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_pressure import OneOf_PressureOutletBCPressure
    from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_pressure_rgh import (
        OneOf_PressureOutletBCPressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_radiative_intensity_ray import (
        OneOf_PressureOutletBCRadiativeIntensityRay,
    )
    from simscale_sdk_v1.models.simulation.one_of__primary_network_damage_model_primary_network import (
        OneOf_PrimaryNetworkDamageModelPrimaryNetwork,
    )
    from simscale_sdk_v1.models.simulation.one_of__probe_points_result_control_write_control import (
        OneOf_ProbePointsResultControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__region_interface_interface_thermal import (
        OneOf_RegionInterfaceInterfaceThermal,
    )
    from simscale_sdk_v1.models.simulation.one_of__region_refinement_ebm_refinement import (
        OneOf_RegionRefinementEBMRefinement,
    )
    from simscale_sdk_v1.models.simulation.one_of__region_refinement_wind_comfort_new_fineness import (
        OneOf_RegionRefinementWindComfortNewFineness,
    )
    from simscale_sdk_v1.models.simulation.one_of__residuals_convergence_method_convergence_criteria import (
        OneOf_ResidualsConvergenceMethodConvergenceCriteria,
    )
    from simscale_sdk_v1.models.simulation.one_of__residuals_or_displacements_convergence_method_convergence_criteria import (
        OneOf_ResidualsOrDisplacementsConvergenceMethodConvergenceCriteria,
    )
    from simscale_sdk_v1.models.simulation.one_of__restricted_dimensional_function__frequency_value import (
        OneOf_RestrictedDimensionalFunction_FrequencyValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__restricted_dimensional_function__time_value import (
        OneOf_RestrictedDimensionalFunction_TimeValue,
    )
    from simscale_sdk_v1.models.simulation.one_of__rotating_motion_type_rotation import OneOf_RotatingMotionTypeRotation
    from simscale_sdk_v1.models.simulation.one_of__rotating_sbm_rotation import OneOf_RotatingSBMRotation
    from simscale_sdk_v1.models.simulation.one_of__scalar_transport_result_control_write_control import (
        OneOf_ScalarTransportResultControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__simerics_analysis_boundary_conditions import (
        OneOf_SimericsAnalysisBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__simerics_analysis_mesh_settings import (
        OneOf_SimericsAnalysisMeshSettings,
    )
    from simscale_sdk_v1.models.simulation.one_of__simerics_analysis_time_dependency import (
        OneOf_SimericsAnalysisTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__simerics_materials_fluids import OneOf_SimericsMaterialsFluids
    from simscale_sdk_v1.models.simulation.one_of__sliding_contact_position_tolerance import (
        OneOf_SlidingContactPositionTolerance,
    )
    from simscale_sdk_v1.models.simulation.one_of__solar_calculator_solar_load import OneOf_SolarCalculatorSolarLoad
    from simscale_sdk_v1.models.simulation.one_of__solar_calculator_sun_direction import (
        OneOf_SolarCalculatorSunDirection,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_electric_conductivity_type import (
        OneOf_SolidCompressibleMaterialElectricConductivityType,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_radiative_behavior import (
        OneOf_SolidCompressibleMaterialRadiativeBehavior,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_transport import (
        OneOf_SolidCompressibleMaterialTransport,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_material_conductivity import OneOf_SolidMaterialConductivity
    from simscale_sdk_v1.models.simulation.one_of__solid_material_material_behavior import (
        OneOf_SolidMaterialMaterialBehavior,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_numerics_eigen_solver import OneOf_SolidNumericsEigenSolver
    from simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_line_search import (
        OneOf_SolidNumericsMechanicalLineSearch,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_resolution_type import (
        OneOf_SolidNumericsMechanicalResolutionType,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_time_integration_type import (
        OneOf_SolidNumericsMechanicalTimeIntegrationType,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_numerics_solver import OneOf_SolidNumericsSolver
    from simscale_sdk_v1.models.simulation.one_of__solid_numerics_thermal_line_search import (
        OneOf_SolidNumericsThermalLineSearch,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_numerics_thermal_resolution_type import (
        OneOf_SolidNumericsThermalResolutionType,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_result_control_area_calculation import (
        OneOf_SolidResultControlAreaCalculation,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_result_control_edge_calculation import (
        OneOf_SolidResultControlEdgeCalculation,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_result_control_point_data import (
        OneOf_SolidResultControlPointData,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_result_control_solution_fields import (
        OneOf_SolidResultControlSolutionFields,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_result_control_volume_calculation import (
        OneOf_SolidResultControlVolumeCalculation,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_eigenfrequency_scope import (
        OneOf_SolidSimulationControlEigenfrequencyScope,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_excitation_frequencies import (
        OneOf_SolidSimulationControlExcitationFrequencies,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_pseudo_time_stepping import (
        OneOf_SolidSimulationControlPseudoTimeStepping,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_timestep_definition import (
        OneOf_SolidSimulationControlTimestepDefinition,
    )
    from simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_write_control_definition import (
        OneOf_SolidSimulationControlWriteControlDefinition,
    )
    from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_density import (
        OneOf_SpatialDiscretizationSchemesDensity,
    )
    from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_gas_mixture_transport import (
        OneOf_SpatialDiscretizationSchemesGasMixtureTransport,
    )
    from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_internal_energy import (
        OneOf_SpatialDiscretizationSchemesInternalEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_turbulent_energy_dissipation_rate import (
        OneOf_SpatialDiscretizationSchemesTurbulentEnergyDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_turbulent_kinetic_energy import (
        OneOf_SpatialDiscretizationSchemesTurbulentKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_velocity import (
        OneOf_SpatialDiscretizationSchemesVelocity,
    )
    from simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_volume_of_fluid import (
        OneOf_SpatialDiscretizationSchemesVolumeOfFluid,
    )
    from simscale_sdk_v1.models.simulation.one_of__static_analysis_boundary_conditions import (
        OneOf_StaticAnalysisBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__static_analysis_connection_groups import (
        OneOf_StaticAnalysisConnectionGroups,
    )
    from simscale_sdk_v1.models.simulation.one_of__static_analysis_connectors import OneOf_StaticAnalysisConnectors
    from simscale_sdk_v1.models.simulation.one_of__statistical_averaging_result_control_v2_sampling_interval import (
        OneOf_StatisticalAveragingResultControlV2SamplingInterval,
    )
    from simscale_sdk_v1.models.simulation.one_of__strain_field_selection_strain_type import (
        OneOf_StrainFieldSelectionStrainType,
    )
    from simscale_sdk_v1.models.simulation.one_of__strain_result_control_item_strain_type import (
        OneOf_StrainResultControlItemStrainType,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_field_selection_stress_type import (
        OneOf_StressFieldSelectionStressType,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_result_control_item_stress_type import (
        OneOf_StressResultControlItemStressType,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xx import (
        OneOf_StressTensor_PressureSigmaXX,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xy import (
        OneOf_StressTensor_PressureSigmaXY,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xz import (
        OneOf_StressTensor_PressureSigmaXZ,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_yy import (
        OneOf_StressTensor_PressureSigmaYY,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_yz import (
        OneOf_StressTensor_PressureSigmaYZ,
    )
    from simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_zz import (
        OneOf_StressTensor_PressureSigmaZZ,
    )
    from simscale_sdk_v1.models.simulation.one_of__sum_fields_calculation_result_control_item_field_selection import (
        OneOf_SumFieldsCalculationResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_for_default import (
        OneOf_SurfaceNormalGradientSchemesForDefault,
    )
    from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_pressure_rgh import (
        OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_pressureRgh,
    )
    from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_rho import (
        OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rho,
    )
    from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_rhok import (
        OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rhok,
    )
    from simscale_sdk_v1.models.simulation.one_of__surface_refinement_wind_comfort_new_fineness import (
        OneOf_SurfaceRefinementWindComfortNewFineness,
    )
    from simscale_sdk_v1.models.simulation.one_of__surface_roughness_model_surface_roughness_type import (
        OneOf_SurfaceRoughnessModelSurfaceRoughnessType,
    )
    from simscale_sdk_v1.models.simulation.one_of__sutherland_transport_thermo import OneOf_SutherlandTransportThermo
    from simscale_sdk_v1.models.simulation.one_of__tangent_jacobian_matrix_change_jacobian_matrix import (
        OneOf_TangentJacobianMatrixChangeJacobianMatrix,
    )
    from simscale_sdk_v1.models.simulation.one_of__temporal_response_result_control_item_field_selection import (
        OneOf_TemporalResponseResultControlItemFieldSelection,
    )
    from simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_boundary_conditions import (
        OneOf_ThermalMechanicalBoundaryConditions,
    )
    from simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_connection_groups import (
        OneOf_ThermalMechanicalConnectionGroups,
    )
    from simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_time_dependency import (
        OneOf_ThermalMechanicalTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__time_differentiation_schemes_for_default import (
        OneOf_TimeDifferentiationSchemesForDefault,
    )
    from simscale_sdk_v1.models.simulation.one_of__time_harmonic_magnetics_time_dependency import (
        OneOf_TimeHarmonicMagneticsTimeDependency,
    )
    from simscale_sdk_v1.models.simulation.one_of__transient_result_control_write_control import (
        OneOf_TransientResultControlWriteControl,
    )
    from simscale_sdk_v1.models.simulation.one_of__true_semi_implicit_solver import OneOf_TrueSemiImplicitSolver
    from simscale_sdk_v1.models.simulation.one_of__turbulent_heat_flux_tbc_heat_source import (
        OneOf_TurbulentHeatFluxTBCHeatSource,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_field_selection_velocity_type import (
        OneOf_VelocityFieldSelectionVelocityType,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_dissipation_type import (
        OneOf_VelocityInletBCDissipationType,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_net_radiative_heat_flux import (
        OneOf_VelocityInletBCNetRadiativeHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_radiative_intensity_ray import (
        OneOf_VelocityInletBCRadiativeIntensityRay,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_temperature import OneOf_VelocityInletBCTemperature
    from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_turbulence import OneOf_VelocityInletBCTurbulence
    from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_turbulence_intensity import (
        OneOf_VelocityInletBCTurbulenceIntensity,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_velocity import OneOf_VelocityInletBCVelocity
    from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_net_radiative_heat_flux import (
        OneOf_VelocityOutletBCNetRadiativeHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_phase_fraction import (
        OneOf_VelocityOutletBCPhaseFraction,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_phase_fractions_v2 import (
        OneOf_VelocityOutletBCPhaseFractionsV2,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_radiative_intensity_ray import (
        OneOf_VelocityOutletBCRadiativeIntensityRay,
    )
    from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_velocity import OneOf_VelocityOutletBCVelocity
    from simscale_sdk_v1.models.simulation.one_of__viscoelastic_network_creep_model_viscoelastic_network import (
        OneOf_ViscoelasticNetworkCreepModelViscoelasticNetwork,
    )
    from simscale_sdk_v1.models.simulation.one_of__voltage_excitation_voltage_type import (
        OneOf_VoltageExcitationVoltageType,
    )
    from simscale_sdk_v1.models.simulation.one_of__wall_bc_electric_boundary_condition import (
        OneOf_WallBCElectricBoundaryCondition,
    )
    from simscale_sdk_v1.models.simulation.one_of__wall_bc_net_radiative_heat_flux import (
        OneOf_WallBCNetRadiativeHeatFlux,
    )
    from simscale_sdk_v1.models.simulation.one_of__wall_bc_phase_fraction import OneOf_WallBCPhaseFraction
    from simscale_sdk_v1.models.simulation.one_of__wall_bc_radiative_intensity_ray import (
        OneOf_WallBCRadiativeIntensityRay,
    )
    from simscale_sdk_v1.models.simulation.one_of__wall_bc_relative_humidity import OneOf_WallBCRelativeHumidity
    from simscale_sdk_v1.models.simulation.one_of__wall_bc_temperature import OneOf_WallBCTemperature
    from simscale_sdk_v1.models.simulation.one_of__wall_bc_velocity import OneOf_WallBCVelocity
    from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_automatic_gap_closing import (
        OneOf_WindComfortMeshAutomaticGapClosing,
    )
    from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_refinements import OneOf_WindComfortMeshRefinements
    from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_reynolds_scaling_type import (
        OneOf_WindComfortMeshReynoldsScalingType,
    )
    from simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_wind_comfort_fineness import (
        OneOf_WindComfortMeshWindComfortFineness,
    )
    from simscale_sdk_v1.models.simulation.one_term import OneTerm
    from simscale_sdk_v1.models.simulation.opaque_material import OpaqueMaterial
    from simscale_sdk_v1.models.simulation.open_boundary_ray_bc import OpenBoundaryRayBC
    from simscale_sdk_v1.models.simulation.open_coil import OpenCoil
    from simscale_sdk_v1.models.simulation.open_window_rsbc import OpenWindowRSBC
    from simscale_sdk_v1.models.simulation.operative_temperature_result_type import OperativeTemperatureResultType
    from simscale_sdk_v1.models.simulation.orthotropic_conductivity import OrthotropicConductivity
    from simscale_sdk_v1.models.simulation.orthotropic_directional_dependency import OrthotropicDirectionalDependency
    from simscale_sdk_v1.models.simulation.orthotropic_electric_conductivity import OrthotropicElectricConductivity
    from simscale_sdk_v1.models.simulation.orthotropic_spring_stiffness import OrthotropicSpringStiffness
    from simscale_sdk_v1.models.simulation.oscillating_linear_sbm import OscillatingLinearSBM
    from simscale_sdk_v1.models.simulation.oscillating_rotating_motion_type import OscillatingRotatingMotionType
    from simscale_sdk_v1.models.simulation.oscillating_rotating_sbm import OscillatingRotatingSBM
    from simscale_sdk_v1.models.simulation.outlet_back_flow_mf_values import OutletBackFlowMFValues
    from simscale_sdk_v1.models.simulation.outlet_back_flow_pf_values import OutletBackFlowPFValues
    from simscale_sdk_v1.models.simulation.outlet_flow_driven_pf import OutletFlowDrivenPF
    from simscale_sdk_v1.models.simulation.outlet_mean_phase_vbc import OutletMeanPhaseVBC
    from simscale_sdk_v1.models.simulation.output_steps import OutputSteps
    from simscale_sdk_v1.models.simulation.pbicg_solver import PBICGSolver
    from simscale_sdk_v1.models.simulation.pbicg_stab_solver import PBICGStabSolver
    from simscale_sdk_v1.models.simulation.pcg_solver import PCGSolver
    from simscale_sdk_v1.models.simulation.petsc_solver import PETSCSolver
    from simscale_sdk_v1.models.simulation.pacefish_automesh import PacefishAutomesh
    from simscale_sdk_v1.models.simulation.pacefish_fineness_coarse import PacefishFinenessCoarse
    from simscale_sdk_v1.models.simulation.pacefish_fineness_fine import PacefishFinenessFine
    from simscale_sdk_v1.models.simulation.pacefish_fineness_moderate import PacefishFinenessModerate
    from simscale_sdk_v1.models.simulation.pacefish_fineness_target_size import PacefishFinenessTargetSize
    from simscale_sdk_v1.models.simulation.pacefish_fineness_very_coarse import PacefishFinenessVeryCoarse
    from simscale_sdk_v1.models.simulation.pacefish_fineness_very_fine import PacefishFinenessVeryFine
    from simscale_sdk_v1.models.simulation.pacefish_mesh_legacy import PacefishMeshLegacy
    from simscale_sdk_v1.models.simulation.pardiso_direct_solver import PardisoDirectSolver
    from simscale_sdk_v1.models.simulation.partial_vector_function import PartialVectorFunction
    from simscale_sdk_v1.models.simulation.pedestrian_comfort_surface import PedestrianComfortSurface
    from simscale_sdk_v1.models.simulation.penalty_method import PenaltyMethod
    from simscale_sdk_v1.models.simulation.peng_robinson_gas_equation_of_state import PengRobinsonGasEquationOfState
    from simscale_sdk_v1.models.simulation.perfect_fluid_equation_of_state import PerfectFluidEquationOfState
    from simscale_sdk_v1.models.simulation.perfect_gas_equation_of_state import PerfectGasEquationOfState
    from simscale_sdk_v1.models.simulation.perfect_plasticity_model import PerfectPlasticityModel
    from simscale_sdk_v1.models.simulation.perfect_plasticity_model_marc import PerfectPlasticityModelMarc
    from simscale_sdk_v1.models.simulation.perforated_plate import PerforatedPlate
    from simscale_sdk_v1.models.simulation.periodic_bc import PeriodicBC
    from simscale_sdk_v1.models.simulation.permanent_magnet_material import PermanentMagnetMaterial
    from simscale_sdk_v1.models.simulation.phase_fraction_ic import PhaseFractionIC
    from simscale_sdk_v1.models.simulation.phase_fractions_ic import PhaseFractionsIC
    from simscale_sdk_v1.models.simulation.physical_contact import PhysicalContact
    from simscale_sdk_v1.models.simulation.pin_connector import PinConnector
    from simscale_sdk_v1.models.simulation.pin_kinematic_behavior import PinKinematicBehavior
    from simscale_sdk_v1.models.simulation.plane_tree import PlaneTree
    from simscale_sdk_v1.models.simulation.plastic_material_behavior import PlasticMaterialBehavior
    from simscale_sdk_v1.models.simulation.plastic_strain import PlasticStrain
    from simscale_sdk_v1.models.simulation.plasticity_marc import PlasticityMarc
    from simscale_sdk_v1.models.simulation.plate_data import PlateData
    from simscale_sdk_v1.models.simulation.point_displacement_bc_marc import PointDisplacementBCMarc
    from simscale_sdk_v1.models.simulation.point_load_bc_marc import PointLoadBCMarc
    from simscale_sdk_v1.models.simulation.point_mass_bc import PointMassBC
    from simscale_sdk_v1.models.simulation.polynomial_function import PolynomialFunction
    from simscale_sdk_v1.models.simulation.porous_tree import PorousTree
    from simscale_sdk_v1.models.simulation.power_ferrite_core_loss import PowerFerriteCoreLoss
    from simscale_sdk_v1.models.simulation.power_heat_source import PowerHeatSource
    from simscale_sdk_v1.models.simulation.power_law_medium import PowerLawMedium
    from simscale_sdk_v1.models.simulation.power_law_viscosity_model import PowerLawViscosityModel
    from simscale_sdk_v1.models.simulation.prandtl_les_delta import PrandtlLesDelta
    from simscale_sdk_v1.models.simulation.predefined_rotational_motion import PredefinedRotationalMotion
    from simscale_sdk_v1.models.simulation.prescribed_optional_function import PrescribedOptionalFunction
    from simscale_sdk_v1.models.simulation.pressure_bc import PressureBC
    from simscale_sdk_v1.models.simulation.pressure_bc_marc import PressureBCMarc
    from simscale_sdk_v1.models.simulation.pressure_coefficient_result_type import PressureCoefficientResultType
    from simscale_sdk_v1.models.simulation.pressure_difference_result_control import PressureDifferenceResultControl
    from simscale_sdk_v1.models.simulation.pressure_inlet_bc import PressureInletBC
    from simscale_sdk_v1.models.simulation.pressure_inlet_outlet_vbc import PressureInletOutletVBC
    from simscale_sdk_v1.models.simulation.pressure_inlet_vbc import PressureInletVBC
    from simscale_sdk_v1.models.simulation.pressure_loss_curve import PressureLossCurve
    from simscale_sdk_v1.models.simulation.pressure_loss_data import PressureLossData
    from simscale_sdk_v1.models.simulation.pressure_loss_function_medium import PressureLossFunctionMedium
    from simscale_sdk_v1.models.simulation.pressure_outlet_bc import PressureOutletBC
    from simscale_sdk_v1.models.simulation.pressure_value_result_type import PressureValueResultType
    from simscale_sdk_v1.models.simulation.primary_network import PrimaryNetwork
    from simscale_sdk_v1.models.simulation.principal_elastic_strain import PrincipalElasticStrain
    from simscale_sdk_v1.models.simulation.principal_green_lagrange_strain_type import PrincipalGreenLagrangeStrainType
    from simscale_sdk_v1.models.simulation.principal_plastic_strain import PrincipalPlasticStrain
    from simscale_sdk_v1.models.simulation.principal_strain_type import PrincipalStrainType
    from simscale_sdk_v1.models.simulation.principal_stress import PrincipalStress
    from simscale_sdk_v1.models.simulation.principal_stress_type import PrincipalStressType
    from simscale_sdk_v1.models.simulation.principal_total_strain import PrincipalTotalStrain
    from simscale_sdk_v1.models.simulation.probe_points_result_control import ProbePointsResultControl
    from simscale_sdk_v1.models.simulation.progressive_refinement import ProgressiveRefinement
    from simscale_sdk_v1.models.simulation.prony_series import PronySeries
    from simscale_sdk_v1.models.simulation.qz import QZ
    from simscale_sdk_v1.models.simulation.radiation_heat_flux import RadiationHeatFlux
    from simscale_sdk_v1.models.simulation.radiation_tbc import RadiationTBC
    from simscale_sdk_v1.models.simulation.rayleigh_damping import RayleighDamping
    from simscale_sdk_v1.models.simulation.reaction_force import ReactionForce
    from simscale_sdk_v1.models.simulation.reaction_force_type import ReactionForceType
    from simscale_sdk_v1.models.simulation.reaction_moment_type import ReactionMomentType
    from simscale_sdk_v1.models.simulation.real_gas_equation_of_state import RealGasEquationOfState
    from simscale_sdk_v1.models.simulation.rectifying_darcy_forchheimer import RectifyingDarcyForchheimer
    from simscale_sdk_v1.models.simulation.refinement_length import RefinementLength
    from simscale_sdk_v1.models.simulation.region import Region
    from simscale_sdk_v1.models.simulation.region_interface import RegionInterface
    from simscale_sdk_v1.models.simulation.region_of_interest import RegionOfInterest
    from simscale_sdk_v1.models.simulation.region_refinement_ebm import RegionRefinementEBM
    from simscale_sdk_v1.models.simulation.region_refinement_pacefish import RegionRefinementPacefish
    from simscale_sdk_v1.models.simulation.region_refinement_simerics import RegionRefinementSimerics
    from simscale_sdk_v1.models.simulation.region_refinement_wind_comfort import RegionRefinementWindComfort
    from simscale_sdk_v1.models.simulation.relative_convergence_criteria import RelativeConvergenceCriteria
    from simscale_sdk_v1.models.simulation.relative_convergence_displacements import RelativeConvergenceDisplacements
    from simscale_sdk_v1.models.simulation.relative_convergence_residuals import RelativeConvergenceResiduals
    from simscale_sdk_v1.models.simulation.relative_convergence_residuals_or_displacements import (
        RelativeConvergenceResidualsOrDisplacements,
    )
    from simscale_sdk_v1.models.simulation.relative_erp_field_selection import RelativeERPFieldSelection
    from simscale_sdk_v1.models.simulation.relative_harmonic_acceleration_field_type import (
        RelativeHarmonicAccelerationFieldType,
    )
    from simscale_sdk_v1.models.simulation.relative_harmonic_acceleration_type import RelativeHarmonicAccelerationType
    from simscale_sdk_v1.models.simulation.relative_harmonic_displacement_field_type import (
        RelativeHarmonicDisplacementFieldType,
    )
    from simscale_sdk_v1.models.simulation.relative_harmonic_displacement_type import RelativeHarmonicDisplacementType
    from simscale_sdk_v1.models.simulation.relative_harmonic_velocity_field_type import (
        RelativeHarmonicVelocityFieldType,
    )
    from simscale_sdk_v1.models.simulation.relative_harmonic_velocity_type import RelativeHarmonicVelocityType
    from simscale_sdk_v1.models.simulation.relative_humidity_value import RelativeHumidityValue
    from simscale_sdk_v1.models.simulation.relative_to_all_cad_surfaces_settings import RelativeToAllCadSurfacesSettings
    from simscale_sdk_v1.models.simulation.relaxation_factor import RelaxationFactor
    from simscale_sdk_v1.models.simulation.remote_displacement_load_bc import RemoteDisplacementLoadBC
    from simscale_sdk_v1.models.simulation.remote_force_load_bc import RemoteForceLoadBC
    from simscale_sdk_v1.models.simulation.remote_point_connection_marc import RemotePointConnectionMarc
    from simscale_sdk_v1.models.simulation.residual_controls import ResidualControls
    from simscale_sdk_v1.models.simulation.residuals_convergence_method import ResidualsConvergenceMethod
    from simscale_sdk_v1.models.simulation.residuals_or_displacements_convergence_method import (
        ResidualsOrDisplacementsConvergenceMethod,
    )
    from simscale_sdk_v1.models.simulation.resolved_turbulence_intensity import ResolvedTurbulenceIntensity
    from simscale_sdk_v1.models.simulation.resolved_turbulent_kinetic_energy import ResolvedTurbulentKineticEnergy
    from simscale_sdk_v1.models.simulation.restricted_dimensional_function__frequency import (
        RestrictedDimensionalFunction_Frequency,
    )
    from simscale_sdk_v1.models.simulation.restricted_dimensional_function__time import (
        RestrictedDimensionalFunction_Time,
    )
    from simscale_sdk_v1.models.simulation.restricted_table_defined_function import RestrictedTableDefinedFunction
    from simscale_sdk_v1.models.simulation.reynolds_stress_result_type import ReynoldsStressResultType
    from simscale_sdk_v1.models.simulation.rho_const_equation_of_state import RhoConstEquationOfState
    from simscale_sdk_v1.models.simulation.rigid_axial_rotation import RigidAxialRotation
    from simscale_sdk_v1.models.simulation.rigid_axial_translation import RigidAxialTranslation
    from simscale_sdk_v1.models.simulation.rotating_motion_bc import RotatingMotionBC
    from simscale_sdk_v1.models.simulation.rotating_motion_type import RotatingMotionType
    from simscale_sdk_v1.models.simulation.rotating_sbm import RotatingSBM
    from simscale_sdk_v1.models.simulation.rotating_wall import RotatingWall
    from simscale_sdk_v1.models.simulation.rotating_wall_vbc import RotatingWallVBC
    from simscale_sdk_v1.models.simulation.round import Round
    from simscale_sdk_v1.models.simulation.run_time_write_control import RunTimeWriteControl
    from simscale_sdk_v1.models.simulation.scalar_transport_result_control import ScalarTransportResultControl
    from simscale_sdk_v1.models.simulation.schemes import Schemes
    from simscale_sdk_v1.models.simulation.scotch_decompose_algorithm import ScotchDecomposeAlgorithm
    from simscale_sdk_v1.models.simulation.second_order_ogden import SecondOrderOgden
    from simscale_sdk_v1.models.simulation.second_order_upwind_spatial_scheme import SecondOrderUpwindSpatialScheme
    from simscale_sdk_v1.models.simulation.semi_open_boundary_ray_bc import SemiOpenBoundaryRayBC
    from simscale_sdk_v1.models.simulation.semi_transparent_material import SemiTransparentMaterial
    from simscale_sdk_v1.models.simulation.set_value_position_tolerance import SetValuePositionTolerance
    from simscale_sdk_v1.models.simulation.ship_design_analysis_sbm import ShipDesignAnalysisSBM
    from simscale_sdk_v1.models.simulation.signed_von_mises_stress_type import SignedVonMisesStressType
    from simscale_sdk_v1.models.simulation.signorini_hyper_elastic_model import SignoriniHyperElasticModel
    from simscale_sdk_v1.models.simulation.silver_birch import SilverBirch
    from simscale_sdk_v1.models.simulation.simerics_analysis import SimericsAnalysis
    from simscale_sdk_v1.models.simulation.simerics_materials import SimericsMaterials
    from simscale_sdk_v1.models.simulation.simple_decompose_algorithm import SimpleDecomposeAlgorithm
    from simscale_sdk_v1.models.simulation.single_frequency import SingleFrequency
    from simscale_sdk_v1.models.simulation.single_step_pseudo_time_stepping import SingleStepPseudoTimeStepping
    from simscale_sdk_v1.models.simulation.sitting_fraction_body_surface import SittingFractionBodySurface
    from simscale_sdk_v1.models.simulation.sliding_contact import SlidingContact
    from simscale_sdk_v1.models.simulation.slip_vbc import SlipVBC
    from simscale_sdk_v1.models.simulation.smallest_cell import SmallestCell
    from simscale_sdk_v1.models.simulation.smooth_les_delta import SmoothLesDelta
    from simscale_sdk_v1.models.simulation.smooth_solver import SmoothSolver
    from simscale_sdk_v1.models.simulation.snapshot_result_control import SnapshotResultControl
    from simscale_sdk_v1.models.simulation.soft_magnetic_material import SoftMagneticMaterial
    from simscale_sdk_v1.models.simulation.solar_calculator import SolarCalculator
    from simscale_sdk_v1.models.simulation.solid_coil import SolidCoil
    from simscale_sdk_v1.models.simulation.solid_compressible_material import SolidCompressibleMaterial
    from simscale_sdk_v1.models.simulation.solid_element_technology import SolidElementTechnology
    from simscale_sdk_v1.models.simulation.solid_global_physics import SolidGlobalPhysics
    from simscale_sdk_v1.models.simulation.solid_initial_conditions import SolidInitialConditions
    from simscale_sdk_v1.models.simulation.solid_material import SolidMaterial
    from simscale_sdk_v1.models.simulation.solid_model import SolidModel
    from simscale_sdk_v1.models.simulation.solid_numerics import SolidNumerics
    from simscale_sdk_v1.models.simulation.solid_result_control import SolidResultControl
    from simscale_sdk_v1.models.simulation.solid_simulation_control import SolidSimulationControl
    from simscale_sdk_v1.models.simulation.solver_model import SolverModel
    from simscale_sdk_v1.models.simulation.sor_preconditioner import SorPreconditioner
    from simscale_sdk_v1.models.simulation.sparse_iterative import SparseIterative
    from simscale_sdk_v1.models.simulation.spatial_discretization_schemes import SpatialDiscretizationSchemes
    from simscale_sdk_v1.models.simulation.specie_default import SpecieDefault
    from simscale_sdk_v1.models.simulation.species_humidity_source import SpeciesHumiditySource
    from simscale_sdk_v1.models.simulation.specific_conductance_interface_thermal import (
        SpecificConductanceInterfaceThermal,
    )
    from simscale_sdk_v1.models.simulation.specific_conductance_wall_thermal import SpecificConductanceWallThermal
    from simscale_sdk_v1.models.simulation.specific_humidity_value import SpecificHumidityValue
    from simscale_sdk_v1.models.simulation.specific_passive_scalar_source import SpecificPassiveScalarSource
    from simscale_sdk_v1.models.simulation.specific_power_source import SpecificPowerSource
    from simscale_sdk_v1.models.simulation.specific_resistance_interface_thermal import (
        SpecificResistanceInterfaceThermal,
    )
    from simscale_sdk_v1.models.simulation.square import Square
    from simscale_sdk_v1.models.simulation.stabilization import Stabilization
    from simscale_sdk_v1.models.simulation.standard_herschel_bulkley_viscosity_model import (
        StandardHerschelBulkleyViscosityModel,
    )
    from simscale_sdk_v1.models.simulation.standing_fraction_body_surface import StandingFractionBodySurface
    from simscale_sdk_v1.models.simulation.star_thermal_resistance_network import StarThermalResistanceNetwork
    from simscale_sdk_v1.models.simulation.static_analysis import StaticAnalysis
    from simscale_sdk_v1.models.simulation.static_pressure_pressure_type import StaticPressurePressureType
    from simscale_sdk_v1.models.simulation.stationary_time_dependency import StationaryTimeDependency
    from simscale_sdk_v1.models.simulation.statistical_averaging_result_control_v2 import (
        StatisticalAveragingResultControlV2,
    )
    from simscale_sdk_v1.models.simulation.steadystate_time_differentiation_scheme import (
        SteadystateTimeDifferentiationScheme,
    )
    from simscale_sdk_v1.models.simulation.stepping_list_pseudo_time_stepping import SteppingListPseudoTimeStepping
    from simscale_sdk_v1.models.simulation.strain_energy_convergence_method import StrainEnergyConvergenceMethod
    from simscale_sdk_v1.models.simulation.strain_field_selection import StrainFieldSelection
    from simscale_sdk_v1.models.simulation.strain_hardening_creep_formulation import StrainHardeningCreepFormulation
    from simscale_sdk_v1.models.simulation.strain_hardening_model import StrainHardeningModel
    from simscale_sdk_v1.models.simulation.strain_hardening_model_marc import StrainHardeningModelMarc
    from simscale_sdk_v1.models.simulation.strain_result_control_item import StrainResultControlItem
    from simscale_sdk_v1.models.simulation.stranded_coil import StrandedCoil
    from simscale_sdk_v1.models.simulation.stress_field_selection import StressFieldSelection
    from simscale_sdk_v1.models.simulation.stress_initial_condition_domains import StressInitialConditionDomains
    from simscale_sdk_v1.models.simulation.stress_result_control_item import StressResultControlItem
    from simscale_sdk_v1.models.simulation.stress_tensor__pressure import StressTensor_Pressure
    from simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__acceleration import (
        SubdomainBasedDimensionalVectorFunctionInitialCondition_Acceleration,
    )
    from simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__length import (
        SubdomainBasedDimensionalVectorFunctionInitialCondition_Length,
    )
    from simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__speed import (
        SubdomainBasedDimensionalVectorFunctionInitialCondition_Speed,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_function_initial_condition__temperature import (
        SubdomainDimensionalFunctionInitialCondition_Temperature,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__dimensionless import (
        SubdomainDimensionalInitialCondition_Dimensionless,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__kinematic_viscosity import (
        SubdomainDimensionalInitialCondition_KinematicViscosity,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__pressure import (
        SubdomainDimensionalInitialCondition_Pressure,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__specific_turbulence_dissipation_rate import (
        SubdomainDimensionalInitialCondition_SpecificTurbulenceDissipationRate,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__temperature import (
        SubdomainDimensionalInitialCondition_Temperature,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__turbulence_kinetic_energy import (
        SubdomainDimensionalInitialCondition_TurbulenceKineticEnergy,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__turbulent_dissipation import (
        SubdomainDimensionalInitialCondition_TurbulentDissipation,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensional_vector_initial_condition__speed import (
        SubdomainDimensionalVectorInitialCondition_Speed,
    )
    from simscale_sdk_v1.models.simulation.subdomain_dimensionless_initial_condition import (
        SubdomainDimensionlessInitialCondition,
    )
    from simscale_sdk_v1.models.simulation.subdomain_fraction_value_initial_condition import (
        SubdomainFractionValueInitialCondition,
    )
    from simscale_sdk_v1.models.simulation.subdomain_stress_initial_condition import SubdomainStressInitialCondition
    from simscale_sdk_v1.models.simulation.subspace_coefficient import SubspaceCoefficient
    from simscale_sdk_v1.models.simulation.subspace_dimension import SubspaceDimension
    from simscale_sdk_v1.models.simulation.sum_fields_calculation_result_control_item import (
        SumFieldsCalculationResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.surface_heat_flux import SurfaceHeatFlux
    from simscale_sdk_v1.models.simulation.surface_heat_flux_bc import SurfaceHeatFluxBC
    from simscale_sdk_v1.models.simulation.surface_load_bc import SurfaceLoadBC
    from simscale_sdk_v1.models.simulation.surface_normal_gradient_schemes import SurfaceNormalGradientSchemes
    from simscale_sdk_v1.models.simulation.surface_normals_result_type import SurfaceNormalsResultType
    from simscale_sdk_v1.models.simulation.surface_refinement_pacefish import SurfaceRefinementPacefish
    from simscale_sdk_v1.models.simulation.surface_refinement_simerics import SurfaceRefinementSimerics
    from simscale_sdk_v1.models.simulation.surface_refinement_wind_comfort import SurfaceRefinementWindComfort
    from simscale_sdk_v1.models.simulation.surface_roughness_model import SurfaceRoughnessModel
    from simscale_sdk_v1.models.simulation.surface_water_vapor_flux_humidity_bc import SurfaceWaterVaporFluxHumidityBC
    from simscale_sdk_v1.models.simulation.sutherland_transport import SutherlandTransport
    from simscale_sdk_v1.models.simulation.sutherland_viscosity import SutherlandViscosity
    from simscale_sdk_v1.models.simulation.sycamore import Sycamore
    from simscale_sdk_v1.models.simulation.symmetry_bc import SymmetryBC
    from simscale_sdk_v1.models.simulation.symmetry_bc_marc import SymmetryBCMarc
    from simscale_sdk_v1.models.simulation.symmetry_dvbc import SymmetryDVBC
    from simscale_sdk_v1.models.simulation.symmetry_ebc import SymmetryEBC
    from simscale_sdk_v1.models.simulation.symmetry_evbc import SymmetryEVBC
    from simscale_sdk_v1.models.simulation.symmetry_evcbc import SymmetryEVCBC
    from simscale_sdk_v1.models.simulation.symmetry_nbc import SymmetryNBC
    from simscale_sdk_v1.models.simulation.symmetry_obc import SymmetryOBC
    from simscale_sdk_v1.models.simulation.symmetry_pbc import SymmetryPBC
    from simscale_sdk_v1.models.simulation.symmetry_pfbc import SymmetryPFBC
    from simscale_sdk_v1.models.simulation.symmetry_psbc import SymmetryPSBC
    from simscale_sdk_v1.models.simulation.symmetry_plane_bc import SymmetryPlaneBC
    from simscale_sdk_v1.models.simulation.symmetry_tbc import SymmetryTBC
    from simscale_sdk_v1.models.simulation.symmetry_tdbc import SymmetryTDBC
    from simscale_sdk_v1.models.simulation.symmetry_tdcbc import SymmetryTDCBC
    from simscale_sdk_v1.models.simulation.symmetry_tkebc import SymmetryTKEBC
    from simscale_sdk_v1.models.simulation.symmetry_vbc import SymmetryVBC
    from simscale_sdk_v1.models.simulation.synchronize_with_field_output_write_control import (
        SynchronizeWithFieldOutputWriteControl,
    )
    from simscale_sdk_v1.models.simulation.table_defined_function import TableDefinedFunction
    from simscale_sdk_v1.models.simulation.table_defined_probe_locations import TableDefinedProbeLocations
    from simscale_sdk_v1.models.simulation.table_defined_vector_function import TableDefinedVectorFunction
    from simscale_sdk_v1.models.simulation.table_function_parameter import TableFunctionParameter
    from simscale_sdk_v1.models.simulation.tadmor_flux_scheme import TadmorFluxScheme
    from simscale_sdk_v1.models.simulation.tangent_jacobian_matrix import TangentJacobianMatrix
    from simscale_sdk_v1.models.simulation.tchamwa_time_integration_scheme import TchamwaTimeIntegrationScheme
    from simscale_sdk_v1.models.simulation.temperature_bc_marc import TemperatureBCMarc
    from simscale_sdk_v1.models.simulation.temperature_field_selection import TemperatureFieldSelection
    from simscale_sdk_v1.models.simulation.temperature_result_control_item import TemperatureResultControlItem
    from simscale_sdk_v1.models.simulation.temporal_response_result_control_item import (
        TemporalResponseResultControlItem,
    )
    from simscale_sdk_v1.models.simulation.testsolver_simulation_control import TestsolverSimulationControl
    from simscale_sdk_v1.models.simulation.thermal_mechanical import ThermalMechanical
    from simscale_sdk_v1.models.simulation.theta_method_time_integration_type import ThetaMethodTimeIntegrationType
    from simscale_sdk_v1.models.simulation.thin_resistance_layer import ThinResistanceLayer
    from simscale_sdk_v1.models.simulation.third_order_ogden import ThirdOrderOgden
    from simscale_sdk_v1.models.simulation.three_terms import ThreeTerms
    from simscale_sdk_v1.models.simulation.time_and_place_sun_direction import TimeAndPlaceSunDirection
    from simscale_sdk_v1.models.simulation.time_differentiation_schemes import TimeDifferentiationSchemes
    from simscale_sdk_v1.models.simulation.time_hardening_creep_formulation import TimeHardeningCreepFormulation
    from simscale_sdk_v1.models.simulation.time_harmonic_electrics import TimeHarmonicElectrics
    from simscale_sdk_v1.models.simulation.time_harmonic_magnetics import TimeHarmonicMagnetics
    from simscale_sdk_v1.models.simulation.time_step_write_control import TimeStepWriteControl
    from simscale_sdk_v1.models.simulation.time_transient_magnetics import TimeTransientMagnetics
    from simscale_sdk_v1.models.simulation.tolerance import Tolerance
    from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference
    from simscale_sdk_v1.models.simulation.torsional_axial_rotation import TorsionalAxialRotation
    from simscale_sdk_v1.models.simulation.total_charge import TotalCharge
    from simscale_sdk_v1.models.simulation.total_conductance_interface_thermal import TotalConductanceInterfaceThermal
    from simscale_sdk_v1.models.simulation.total_equivalent_plastic_strain_type import TotalEquivalentPlasticStrainType
    from simscale_sdk_v1.models.simulation.total_isotropic_stiffness_definition import TotalIsotropicStiffnessDefinition
    from simscale_sdk_v1.models.simulation.total_linear_strain_type import TotalLinearStrainType
    from simscale_sdk_v1.models.simulation.total_mass import TotalMass
    from simscale_sdk_v1.models.simulation.total_non_linear_strain_type import TotalNonLinearStrainType
    from simscale_sdk_v1.models.simulation.total_orthotropic_stiffness_definition import (
        TotalOrthotropicStiffnessDefinition,
    )
    from simscale_sdk_v1.models.simulation.total_pbc import TotalPBC
    from simscale_sdk_v1.models.simulation.total_pressure_pressure_type import TotalPressurePressureType
    from simscale_sdk_v1.models.simulation.total_resistance_interface_thermal import TotalResistanceInterfaceThermal
    from simscale_sdk_v1.models.simulation.total_resistance_wall_thermal import TotalResistanceWallThermal
    from simscale_sdk_v1.models.simulation.total_strain import TotalStrain
    from simscale_sdk_v1.models.simulation.total_tbc import TotalTBC
    from simscale_sdk_v1.models.simulation.total_turbulence_intensity import TotalTurbulenceIntensity
    from simscale_sdk_v1.models.simulation.total_turbulent_kinetic_energy import TotalTurbulentKineticEnergy
    from simscale_sdk_v1.models.simulation.tr_absolute_power_source import TrAbsolutePowerSource
    from simscale_sdk_v1.models.simulation.tr_specific_power_source import TrSpecificPowerSource
    from simscale_sdk_v1.models.simulation.transient_result_control import TransientResultControl
    from simscale_sdk_v1.models.simulation.transient_time_dependency import TransientTimeDependency
    from simscale_sdk_v1.models.simulation.transparent_material import TransparentMaterial
    from simscale_sdk_v1.models.simulation.tresca_stress_type import TrescaStressType
    from simscale_sdk_v1.models.simulation.true_change_jacobian_matrix import TrueChangeJacobianMatrix
    from simscale_sdk_v1.models.simulation.true_line_search import TrueLineSearch
    from simscale_sdk_v1.models.simulation.true_semi_implicit import TrueSemiImplicit
    from simscale_sdk_v1.models.simulation.turbulence_intensity_tibc import TurbulenceIntensityTIBC
    from simscale_sdk_v1.models.simulation.turbulence_kinetic_energy_tibc import TurbulenceKineticEnergyTIBC
    from simscale_sdk_v1.models.simulation.turbulent_heat_flux_tbc import TurbulentHeatFluxTBC
    from simscale_sdk_v1.models.simulation.turbulent_intensity_and_reference_length_turbulence import (
        TurbulentIntensityAndReferenceLengthTurbulence,
    )
    from simscale_sdk_v1.models.simulation.twice_max_loading_frequency import TwiceMaxLoadingFrequency
    from simscale_sdk_v1.models.simulation.two_resistor_network import TwoResistorNetwork
    from simscale_sdk_v1.models.simulation.two_terms import TwoTerms
    from simscale_sdk_v1.models.simulation.unconstrained_optional_function import UnconstrainedOptionalFunction
    from simscale_sdk_v1.models.simulation.uncorrected_surface_normal_gradient_scheme import (
        UncorrectedSurfaceNormalGradientScheme,
    )
    from simscale_sdk_v1.models.simulation.unelastic_strain_type import UnelasticStrainType
    from simscale_sdk_v1.models.simulation.unit__dimensionless import Unit_Dimensionless
    from simscale_sdk_v1.models.simulation.unit__frequency import Unit_Frequency
    from simscale_sdk_v1.models.simulation.unit__length import Unit_Length
    from simscale_sdk_v1.models.simulation.unit__magnetic_field_strength import Unit_MagneticFieldStrength
    from simscale_sdk_v1.models.simulation.unit__pressure import Unit_Pressure
    from simscale_sdk_v1.models.simulation.unit__speed import Unit_Speed
    from simscale_sdk_v1.models.simulation.unit__temperature import Unit_Temperature
    from simscale_sdk_v1.models.simulation.unit__text import Unit_Text
    from simscale_sdk_v1.models.simulation.unit__time import Unit_Time
    from simscale_sdk_v1.models.simulation.unit__volumetric_flow_rate import Unit_VolumetricFlowRate
    from simscale_sdk_v1.models.simulation.user_defined_write_control import UserDefinedWriteControl
    from simscale_sdk_v1.models.simulation.variable_group_empty import VariableGroup_EMPTY
    from simscale_sdk_v1.models.simulation.variable_group_engineering_strain import VariableGroup_ENGINEERING_STRAIN
    from simscale_sdk_v1.models.simulation.variable_group_f import VariableGroup_F
    from simscale_sdk_v1.models.simulation.variable_group_height import VariableGroup_HEIGHT
    from simscale_sdk_v1.models.simulation.variable_group_legend_probability import VariableGroup_LEGEND_PROBABILITY
    from simscale_sdk_v1.models.simulation.variable_group_magnetic_field_strength import (
        VariableGroup_MAGNETIC_FIELD_STRENGTH,
    )
    from simscale_sdk_v1.models.simulation.variable_group_plastic_strain import VariableGroup_PLASTIC_STRAIN
    from simscale_sdk_v1.models.simulation.variable_group_relaxation_time import VariableGroup_RELAXATION_TIME
    from simscale_sdk_v1.models.simulation.variable_group_strain import VariableGroup_STRAIN
    from simscale_sdk_v1.models.simulation.variable_group_temp import VariableGroup_TEMP
    from simscale_sdk_v1.models.simulation.variable_group_temp_engineering_strain import (
        VariableGroup_TEMP_ENGINEERING_STRAIN,
    )
    from simscale_sdk_v1.models.simulation.variable_group_temp_plastic_strain import VariableGroup_TEMP_PLASTIC_STRAIN
    from simscale_sdk_v1.models.simulation.variable_group_temp_pressure import VariableGroup_TEMP_PRESSURE
    from simscale_sdk_v1.models.simulation.variable_group_temp_strain import VariableGroup_TEMP_STRAIN
    from simscale_sdk_v1.models.simulation.variable_group_time import VariableGroup_TIME
    from simscale_sdk_v1.models.simulation.variable_group_velocity import VariableGroup_VELOCITY
    from simscale_sdk_v1.models.simulation.variable_group_v_dot import VariableGroup_V_DOT
    from simscale_sdk_v1.models.simulation.variable_group_x_y_z import VariableGroup_X_Y_Z
    from simscale_sdk_v1.models.simulation.variable_group_x_y_z_time import VariableGroup_X_Y_Z_TIME
    from simscale_sdk_v1.models.simulation.variable_group_x_y_z_time_temp import VariableGroup_X_Y_Z_TIME_TEMP
    from simscale_sdk_v1.models.simulation.vector_rotation import VectorRotation
    from simscale_sdk_v1.models.simulation.velocity_field_selection import VelocityFieldSelection
    from simscale_sdk_v1.models.simulation.velocity_inlet_bc import VelocityInletBC
    from simscale_sdk_v1.models.simulation.velocity_outlet_bc import VelocityOutletBC
    from simscale_sdk_v1.models.simulation.velocity_result_control_item import VelocityResultControlItem
    from simscale_sdk_v1.models.simulation.viscoelastic_network import ViscoelasticNetwork
    from simscale_sdk_v1.models.simulation.viscoplastic_marc_material_behavior import ViscoplasticMarcMaterialBehavior
    from simscale_sdk_v1.models.simulation.voltage_excitation import VoltageExcitation
    from simscale_sdk_v1.models.simulation.volume_heat_flux import VolumeHeatFlux
    from simscale_sdk_v1.models.simulation.volume_heat_flux_bc import VolumeHeatFluxBC
    from simscale_sdk_v1.models.simulation.volume_load_bc import VolumeLoadBC
    from simscale_sdk_v1.models.simulation.volumetric_flow import VolumetricFlow
    from simscale_sdk_v1.models.simulation.volumetric_species_humidity_source import VolumetricSpeciesHumiditySource
    from simscale_sdk_v1.models.simulation.von_mises_stress import VonMisesStress
    from simscale_sdk_v1.models.simulation.von_mises_stress_type import VonMisesStressType
    from simscale_sdk_v1.models.simulation.vorticity_result_type import VorticityResultType
    from simscale_sdk_v1.models.simulation.wall_bc import WallBC
    from simscale_sdk_v1.models.simulation.wall_contact_angle import WallContactAngle
    from simscale_sdk_v1.models.simulation.wall_convection_model import WallConvectionModel
    from simscale_sdk_v1.models.simulation.wall_function_dvbc import WallFunctionDVBC
    from simscale_sdk_v1.models.simulation.wall_function_ebc import WallFunctionEBC
    from simscale_sdk_v1.models.simulation.wall_function_evbc import WallFunctionEVBC
    from simscale_sdk_v1.models.simulation.wall_function_evcbc import WallFunctionEVCBC
    from simscale_sdk_v1.models.simulation.wall_function_nbc import WallFunctionNBC
    from simscale_sdk_v1.models.simulation.wall_function_obc import WallFunctionOBC
    from simscale_sdk_v1.models.simulation.wall_function_tdbc import WallFunctionTDBC
    from simscale_sdk_v1.models.simulation.wall_function_tdcbc import WallFunctionTDCBC
    from simscale_sdk_v1.models.simulation.wall_function_tkebc import WallFunctionTKEBC
    from simscale_sdk_v1.models.simulation.wall_heat_flux_result_type import WallHeatFluxResultType
    from simscale_sdk_v1.models.simulation.wall_heat_transfer_tbc import WallHeatTransferTBC
    from simscale_sdk_v1.models.simulation.wall_next_cell_heat_transfer_coefficient_result_type import (
        WallNextCellHeatTransferCoefficientResultType,
    )
    from simscale_sdk_v1.models.simulation.wall_radiation_model import WallRadiationModel
    from simscale_sdk_v1.models.simulation.wall_shear_stress_result_type import WallShearStressResultType
    from simscale_sdk_v1.models.simulation.water_vapor_flux_humidity_bc import WaterVaporFluxHumidityBC
    from simscale_sdk_v1.models.simulation.wave_transmissive_pbc import WaveTransmissivePBC
    from simscale_sdk_v1.models.simulation.wedge_bc import WedgeBC
    from simscale_sdk_v1.models.simulation.wind_comfort import WindComfort
    from simscale_sdk_v1.models.simulation.wind_comfort_mesh import WindComfortMesh
    from simscale_sdk_v1.models.simulation.wind_comfort_simulation_control import WindComfortSimulationControl
    from simscale_sdk_v1.models.simulation.wind_conditions import WindConditions
    from simscale_sdk_v1.models.simulation.wind_exposure_roughness import WindExposureRoughness
    from simscale_sdk_v1.models.simulation.wind_rose import WindRose
    from simscale_sdk_v1.models.simulation.wind_rose_velocity_bucket import WindRoseVelocityBucket
    from simscale_sdk_v1.models.simulation.wind_tunnel_size_custom import WindTunnelSizeCustom
    from simscale_sdk_v1.models.simulation.wind_tunnel_size_large import WindTunnelSizeLarge
    from simscale_sdk_v1.models.simulation.wind_tunnel_size_moderate import WindTunnelSizeModerate
    from simscale_sdk_v1.models.simulation.with_fictitious_clearance import WithFictitiousClearance
    from simscale_sdk_v1.models.simulation.write_interval import WriteInterval
    from simscale_sdk_v1.models.simulation.write_interval_write_control import WriteIntervalWriteControl
    from simscale_sdk_v1.models.simulation.x_axis import XAxis
    from simscale_sdk_v1.models.simulation.y_axis import YAxis
    from simscale_sdk_v1.models.simulation.y_plus_ras_result_type import YPlusRASResultType
    from simscale_sdk_v1.models.simulation.yeoh_hyper_elastic_model import YeohHyperElasticModel
    from simscale_sdk_v1.models.simulation.yeoh_primary_network import YeohPrimaryNetwork
    from simscale_sdk_v1.models.simulation.z_axis import ZAxis
    from simscale_sdk_v1.models.simulation.zero_gradient_dvbc import ZeroGradientDVBC
    from simscale_sdk_v1.models.simulation.zero_gradient_ebc import ZeroGradientEBC
    from simscale_sdk_v1.models.simulation.zero_gradient_evbc import ZeroGradientEVBC
    from simscale_sdk_v1.models.simulation.zero_gradient_evcbc import ZeroGradientEVCBC
    from simscale_sdk_v1.models.simulation.zero_gradient_humidity_bc import ZeroGradientHumidityBC
    from simscale_sdk_v1.models.simulation.zero_gradient_nbc import ZeroGradientNBC
    from simscale_sdk_v1.models.simulation.zero_gradient_obc import ZeroGradientOBC
    from simscale_sdk_v1.models.simulation.zero_gradient_pbc import ZeroGradientPBC
    from simscale_sdk_v1.models.simulation.zero_gradient_pfbc import ZeroGradientPFBC
    from simscale_sdk_v1.models.simulation.zero_gradient_psbc import ZeroGradientPSBC
    from simscale_sdk_v1.models.simulation.zero_gradient_tdbc import ZeroGradientTDBC
    from simscale_sdk_v1.models.simulation.zero_gradient_tdcbc import ZeroGradientTDCBC
    from simscale_sdk_v1.models.simulation.zero_gradient_tkebc import ZeroGradientTKEBC
    from simscale_sdk_v1.models.simulation.zero_gradient_vbc import ZeroGradientVBC
    from simscale_sdk_v1.models.simulation._root import Simulation

_NAMES: dict[str, tuple[str, str]] = {
    "AMIRotatingZone": ("simscale_sdk_v1.models.simulation.ami_rotating_zone", "AMIRotatingZone"),
    "AbsoluteConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.absolute_convergence_criteria",
        "AbsoluteConvergenceCriteria",
    ),
    "AbsoluteConvergenceDisplacements": (
        "simscale_sdk_v1.models.simulation.absolute_convergence_displacements",
        "AbsoluteConvergenceDisplacements",
    ),
    "AbsoluteConvergenceResiduals": (
        "simscale_sdk_v1.models.simulation.absolute_convergence_residuals",
        "AbsoluteConvergenceResiduals",
    ),
    "AbsoluteConvergenceResidualsOrDisplacements": (
        "simscale_sdk_v1.models.simulation.absolute_convergence_residuals_or_displacements",
        "AbsoluteConvergenceResidualsOrDisplacements",
    ),
    "AbsoluteERPFieldSelection": (
        "simscale_sdk_v1.models.simulation.absolute_erp_field_selection",
        "AbsoluteERPFieldSelection",
    ),
    "AbsoluteHarmonicAccelerationFieldType": (
        "simscale_sdk_v1.models.simulation.absolute_harmonic_acceleration_field_type",
        "AbsoluteHarmonicAccelerationFieldType",
    ),
    "AbsoluteHarmonicAccelerationType": (
        "simscale_sdk_v1.models.simulation.absolute_harmonic_acceleration_type",
        "AbsoluteHarmonicAccelerationType",
    ),
    "AbsoluteHarmonicDisplacementFieldType": (
        "simscale_sdk_v1.models.simulation.absolute_harmonic_displacement_field_type",
        "AbsoluteHarmonicDisplacementFieldType",
    ),
    "AbsoluteHarmonicDisplacementType": (
        "simscale_sdk_v1.models.simulation.absolute_harmonic_displacement_type",
        "AbsoluteHarmonicDisplacementType",
    ),
    "AbsoluteHarmonicVelocityFieldType": (
        "simscale_sdk_v1.models.simulation.absolute_harmonic_velocity_field_type",
        "AbsoluteHarmonicVelocityFieldType",
    ),
    "AbsoluteHarmonicVelocityType": (
        "simscale_sdk_v1.models.simulation.absolute_harmonic_velocity_type",
        "AbsoluteHarmonicVelocityType",
    ),
    "AbsoluteHumidityValue": ("simscale_sdk_v1.models.simulation.absolute_humidity_value", "AbsoluteHumidityValue"),
    "AbsolutePassiveScalarSource": (
        "simscale_sdk_v1.models.simulation.absolute_passive_scalar_source",
        "AbsolutePassiveScalarSource",
    ),
    "AbsolutePowerSource": ("simscale_sdk_v1.models.simulation.absolute_power_source", "AbsolutePowerSource"),
    "AbsoluteToAllCadSurfacesSettings": (
        "simscale_sdk_v1.models.simulation.absolute_to_all_cad_surfaces_settings",
        "AbsoluteToAllCadSurfacesSettings",
    ),
    "AccelerationFieldSelection": (
        "simscale_sdk_v1.models.simulation.acceleration_field_selection",
        "AccelerationFieldSelection",
    ),
    "AccelerationResultControlItem": (
        "simscale_sdk_v1.models.simulation.acceleration_result_control_item",
        "AccelerationResultControlItem",
    ),
    "ActiveAdjustableTimestep": (
        "simscale_sdk_v1.models.simulation.active_adjustable_timestep",
        "ActiveAdjustableTimestep",
    ),
    "AdaptiveAugmentation": ("simscale_sdk_v1.models.simulation.adaptive_augmentation", "AdaptiveAugmentation"),
    "AdaptiveConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.adaptive_convergence_criteria",
        "AdaptiveConvergenceCriteria",
    ),
    "AdaptiveConvergenceDisplacements": (
        "simscale_sdk_v1.models.simulation.adaptive_convergence_displacements",
        "AdaptiveConvergenceDisplacements",
    ),
    "AdaptiveConvergenceResiduals": (
        "simscale_sdk_v1.models.simulation.adaptive_convergence_residuals",
        "AdaptiveConvergenceResiduals",
    ),
    "AdaptiveConvergenceResidualsOrDisplacements": (
        "simscale_sdk_v1.models.simulation.adaptive_convergence_residuals_or_displacements",
        "AdaptiveConvergenceResidualsOrDisplacements",
    ),
    "AdditionalDirectionalCells": (
        "simscale_sdk_v1.models.simulation.additional_directional_cells",
        "AdditionalDirectionalCells",
    ),
    "AdiabaticInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.adiabatic_interface_thermal",
        "AdiabaticInterfaceThermal",
    ),
    "AdiabaticPerfectFluidEquationOfState": (
        "simscale_sdk_v1.models.simulation.adiabatic_perfect_fluid_equation_of_state",
        "AdiabaticPerfectFluidEquationOfState",
    ),
    "AdiabaticTBC": ("simscale_sdk_v1.models.simulation.adiabatic_tbc", "AdiabaticTBC"),
    "AdjustableRuntimeWriteControl": (
        "simscale_sdk_v1.models.simulation.adjustable_runtime_write_control",
        "AdjustableRuntimeWriteControl",
    ),
    "AdvancedChronosSettings": (
        "simscale_sdk_v1.models.simulation.advanced_chronos_settings",
        "AdvancedChronosSettings",
    ),
    "AdvancedComfortCriterionSettings": (
        "simscale_sdk_v1.models.simulation.advanced_comfort_criterion_settings",
        "AdvancedComfortCriterionSettings",
    ),
    "AdvancedConcepts": ("simscale_sdk_v1.models.simulation.advanced_concepts", "AdvancedConcepts"),
    "AdvancedConnectorSettings": (
        "simscale_sdk_v1.models.simulation.advanced_connector_settings",
        "AdvancedConnectorSettings",
    ),
    "AdvancedMUMPSSettings": ("simscale_sdk_v1.models.simulation.advanced_mumps_settings", "AdvancedMUMPSSettings"),
    "AdvancedModelling": ("simscale_sdk_v1.models.simulation.advanced_modelling", "AdvancedModelling"),
    "AdvancedPETSCSettings": ("simscale_sdk_v1.models.simulation.advanced_petsc_settings", "AdvancedPETSCSettings"),
    "AdvancedROISettings": ("simscale_sdk_v1.models.simulation.advanced_roi_settings", "AdvancedROISettings"),
    "AdvectivePBC": ("simscale_sdk_v1.models.simulation.advective_pbc", "AdvectivePBC"),
    "AdvectiveVBC": ("simscale_sdk_v1.models.simulation.advective_vbc", "AdvectiveVBC"),
    "AerodynamicRoughness": ("simscale_sdk_v1.models.simulation.aerodynamic_roughness", "AerodynamicRoughness"),
    "AllComputed": ("simscale_sdk_v1.models.simulation.all_computed", "AllComputed"),
    "AllComputedWriteControl": (
        "simscale_sdk_v1.models.simulation.all_computed_write_control",
        "AllComputedWriteControl",
    ),
    "AllConnectorPointDataResults": (
        "simscale_sdk_v1.models.simulation.all_connector_point_data_results",
        "AllConnectorPointDataResults",
    ),
    "AllowedDirection": ("simscale_sdk_v1.models.simulation.allowed_direction", "AllowedDirection"),
    "AmbientPBC": ("simscale_sdk_v1.models.simulation.ambient_pbc", "AmbientPBC"),
    "AmbientTBC": ("simscale_sdk_v1.models.simulation.ambient_tbc", "AmbientTBC"),
    "Analysis": ("simscale_sdk_v1.models.simulation.analysis", "Analysis"),
    "AngularRotation": ("simscale_sdk_v1.models.simulation.angular_rotation", "AngularRotation"),
    "AreaAverageResultControl": (
        "simscale_sdk_v1.models.simulation.area_average_result_control",
        "AreaAverageResultControl",
    ),
    "AreaDensityMass": ("simscale_sdk_v1.models.simulation.area_density_mass", "AreaDensityMass"),
    "AreaIntegralResultControl": (
        "simscale_sdk_v1.models.simulation.area_integral_result_control",
        "AreaIntegralResultControl",
    ),
    "ArrudaBoycePlasticElastoplasticNetwork": (
        "simscale_sdk_v1.models.simulation.arruda_boyce_plastic_elastoplastic_network",
        "ArrudaBoycePlasticElastoplasticNetwork",
    ),
    "AtmosphericBoundaryLayerInletBC": (
        "simscale_sdk_v1.models.simulation.atmospheric_boundary_layer_inlet_bc",
        "AtmosphericBoundaryLayerInletBC",
    ),
    "AugmentedLagrangeMethod": (
        "simscale_sdk_v1.models.simulation.augmented_lagrange_method",
        "AugmentedLagrangeMethod",
    ),
    "AutoTimestepDefinition": ("simscale_sdk_v1.models.simulation.auto_timestep_definition", "AutoTimestepDefinition"),
    "AutomaticAcceleration": ("simscale_sdk_v1.models.simulation.automatic_acceleration", "AutomaticAcceleration"),
    "AutomaticAxisDefinition": (
        "simscale_sdk_v1.models.simulation.automatic_axis_definition",
        "AutomaticAxisDefinition",
    ),
    "AutomaticDomainDecomposition": (
        "simscale_sdk_v1.models.simulation.automatic_domain_decomposition",
        "AutomaticDomainDecomposition",
    ),
    "AutomaticElementDefinitionMethod": (
        "simscale_sdk_v1.models.simulation.automatic_element_definition_method",
        "AutomaticElementDefinitionMethod",
    ),
    "AutomaticEmbeddedBoundaryMeshSizing": (
        "simscale_sdk_v1.models.simulation.automatic_embedded_boundary_mesh_sizing",
        "AutomaticEmbeddedBoundaryMeshSizing",
    ),
    "AutomaticMeshSizing": ("simscale_sdk_v1.models.simulation.automatic_mesh_sizing", "AutomaticMeshSizing"),
    "AutomaticOmegaDissipation": (
        "simscale_sdk_v1.models.simulation.automatic_omega_dissipation",
        "AutomaticOmegaDissipation",
    ),
    "AutomaticReactualization": (
        "simscale_sdk_v1.models.simulation.automatic_reactualization",
        "AutomaticReactualization",
    ),
    "AutomaticReferenceLength": (
        "simscale_sdk_v1.models.simulation.automatic_reference_length",
        "AutomaticReferenceLength",
    ),
    "AutomaticReynoldsScaling": (
        "simscale_sdk_v1.models.simulation.automatic_reynolds_scaling",
        "AutomaticReynoldsScaling",
    ),
    "AutomaticSimericsMeshSettings": (
        "simscale_sdk_v1.models.simulation.automatic_simerics_mesh_settings",
        "AutomaticSimericsMeshSettings",
    ),
    "AutomaticSubspaceSettings": (
        "simscale_sdk_v1.models.simulation.automatic_subspace_settings",
        "AutomaticSubspaceSettings",
    ),
    "AutomaticTimeStepDefintion": (
        "simscale_sdk_v1.models.simulation.automatic_time_step_defintion",
        "AutomaticTimeStepDefintion",
    ),
    "AutomaticTurbulence": ("simscale_sdk_v1.models.simulation.automatic_turbulence", "AutomaticTurbulence"),
    "AverageFieldsCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.average_fields_calculation_result_control_item",
        "AverageFieldsCalculationResultControlItem",
    ),
    "AverageVelocityMomentumSource": (
        "simscale_sdk_v1.models.simulation.average_velocity_momentum_source",
        "AverageVelocityMomentumSource",
    ),
    "BaseExcitationBC": ("simscale_sdk_v1.models.simulation.base_excitation_bc", "BaseExcitationBC"),
    "BatheWilson": ("simscale_sdk_v1.models.simulation.bathe_wilson", "BatheWilson"),
    "BilinearElastoPlasticModel": (
        "simscale_sdk_v1.models.simulation.bilinear_elasto_plastic_model",
        "BilinearElastoPlasticModel",
    ),
    "BilinearModelMarc": ("simscale_sdk_v1.models.simulation.bilinear_model_marc", "BilinearModelMarc"),
    "BirdCarreauViscosityModel": (
        "simscale_sdk_v1.models.simulation.bird_carreau_viscosity_model",
        "BirdCarreauViscosityModel",
    ),
    "BlockedDirection": ("simscale_sdk_v1.models.simulation.blocked_direction", "BlockedDirection"),
    "BoltConnector": ("simscale_sdk_v1.models.simulation.bolt_connector", "BoltConnector"),
    "BoltMechanicalProperties": (
        "simscale_sdk_v1.models.simulation.bolt_mechanical_properties",
        "BoltMechanicalProperties",
    ),
    "BoltPreloadBC": ("simscale_sdk_v1.models.simulation.bolt_preload_bc", "BoltPreloadBC"),
    "BondedContact": ("simscale_sdk_v1.models.simulation.bonded_contact", "BondedContact"),
    "BoundedGaussUpwindDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.bounded_gauss_upwind_divergence_scheme",
        "BoundedGaussUpwindDivergenceScheme",
    ),
    "BuildingsOfInterest": ("simscale_sdk_v1.models.simulation.buildings_of_interest", "BuildingsOfInterest"),
    "CalculateFrequency": ("simscale_sdk_v1.models.simulation.calculate_frequency", "CalculateFrequency"),
    "CalculatedDVBC": ("simscale_sdk_v1.models.simulation.calculated_dvbc", "CalculatedDVBC"),
    "CalculatedEVBC": ("simscale_sdk_v1.models.simulation.calculated_evbc", "CalculatedEVBC"),
    "CalculatedEVCBC": ("simscale_sdk_v1.models.simulation.calculated_evcbc", "CalculatedEVCBC"),
    "CalculatedTDBC": ("simscale_sdk_v1.models.simulation.calculated_tdbc", "CalculatedTDBC"),
    "CalculatedTDCBC": ("simscale_sdk_v1.models.simulation.calculated_tdcbc", "CalculatedTDCBC"),
    "CartesianOrientation": ("simscale_sdk_v1.models.simulation.cartesian_orientation", "CartesianOrientation"),
    "CauchyStress": ("simscale_sdk_v1.models.simulation.cauchy_stress", "CauchyStress"),
    "CauchyStressTensorField": (
        "simscale_sdk_v1.models.simulation.cauchy_stress_tensor_field",
        "CauchyStressTensorField",
    ),
    "CauchyStressType": ("simscale_sdk_v1.models.simulation.cauchy_stress_type", "CauchyStressType"),
    "Cavitation": ("simscale_sdk_v1.models.simulation.cavitation", "Cavitation"),
    "CelllimitedGaussLinearGradientScheme": (
        "simscale_sdk_v1.models.simulation.celllimited_gauss_linear_gradient_scheme",
        "CelllimitedGaussLinearGradientScheme",
    ),
    "CelllimitedLeastSquaresGradientScheme": (
        "simscale_sdk_v1.models.simulation.celllimited_least_squares_gradient_scheme",
        "CelllimitedLeastSquaresGradientScheme",
    ),
    "CenterFrequency": ("simscale_sdk_v1.models.simulation.center_frequency", "CenterFrequency"),
    "CentralDiffTimeIntegrationScheme": (
        "simscale_sdk_v1.models.simulation.central_diff_time_integration_scheme",
        "CentralDiffTimeIntegrationScheme",
    ),
    "CentralDifferenceSpatialScheme": (
        "simscale_sdk_v1.models.simulation.central_difference_spatial_scheme",
        "CentralDifferenceSpatialScheme",
    ),
    "CentralizedDomainDecomposition": (
        "simscale_sdk_v1.models.simulation.centralized_domain_decomposition",
        "CentralizedDomainDecomposition",
    ),
    "CentrifugalForceBC": ("simscale_sdk_v1.models.simulation.centrifugal_force_bc", "CentrifugalForceBC"),
    "ChargeDensity": ("simscale_sdk_v1.models.simulation.charge_density", "ChargeDensity"),
    "Chestnut": ("simscale_sdk_v1.models.simulation.chestnut", "Chestnut"),
    "ChronosSolver": ("simscale_sdk_v1.models.simulation.chronos_solver", "ChronosSolver"),
    "CircularHoleShape": ("simscale_sdk_v1.models.simulation.circular_hole_shape", "CircularHoleShape"),
    "ClockTimeWriteControl": ("simscale_sdk_v1.models.simulation.clock_time_write_control", "ClockTimeWriteControl"),
    "ClosedCoil": ("simscale_sdk_v1.models.simulation.closed_coil", "ClosedCoil"),
    "ClusterAroundModes": ("simscale_sdk_v1.models.simulation.cluster_around_modes", "ClusterAroundModes"),
    "CoarseResolution": ("simscale_sdk_v1.models.simulation.coarse_resolution", "CoarseResolution"),
    "Coil": ("simscale_sdk_v1.models.simulation.coil", "Coil"),
    "CollisionRetimingEvent": ("simscale_sdk_v1.models.simulation.collision_retiming_event", "CollisionRetimingEvent"),
    "CombinedPlasticHardeningMarc": (
        "simscale_sdk_v1.models.simulation.combined_plastic_hardening_marc",
        "CombinedPlasticHardeningMarc",
    ),
    "ComfortCriterionDefinitionV2": (
        "simscale_sdk_v1.models.simulation.comfort_criterion_definition_v2",
        "ComfortCriterionDefinitionV2",
    ),
    "ComponentVectorFunction": (
        "simscale_sdk_v1.models.simulation.component_vector_function",
        "ComponentVectorFunction",
    ),
    "Compressible": ("simscale_sdk_v1.models.simulation.compressible", "Compressible"),
    "CompressibleFluidMaterials": (
        "simscale_sdk_v1.models.simulation.compressible_fluid_materials",
        "CompressibleFluidMaterials",
    ),
    "ComputingCore": ("simscale_sdk_v1.models.simulation.computing_core", "ComputingCore"),
    "ConductivityThicknessPair": (
        "simscale_sdk_v1.models.simulation.conductivity_thickness_pair",
        "ConductivityThicknessPair",
    ),
    "ConjugateHeatTransfer": ("simscale_sdk_v1.models.simulation.conjugate_heat_transfer", "ConjugateHeatTransfer"),
    "ConjugateHeatTransferMaterials": (
        "simscale_sdk_v1.models.simulation.conjugate_heat_transfer_materials",
        "ConjugateHeatTransferMaterials",
    ),
    "ConnectionSettingsV36": ("simscale_sdk_v1.models.simulation.connection_settings_v36", "ConnectionSettingsV36"),
    "ConstAnIsoTransport": ("simscale_sdk_v1.models.simulation.const_an_iso_transport", "ConstAnIsoTransport"),
    "ConstCrossPlaneOrthotropicTransport": (
        "simscale_sdk_v1.models.simulation.const_cross_plane_orthotropic_transport",
        "ConstCrossPlaneOrthotropicTransport",
    ),
    "ConstIsoTransport": ("simscale_sdk_v1.models.simulation.const_iso_transport", "ConstIsoTransport"),
    "ConstTransport": ("simscale_sdk_v1.models.simulation.const_transport", "ConstTransport"),
    "ConstantContactAnglePFBC": (
        "simscale_sdk_v1.models.simulation.constant_contact_angle_pfbc",
        "ConstantContactAnglePFBC",
    ),
    "ConstantFunction": ("simscale_sdk_v1.models.simulation.constant_function", "ConstantFunction"),
    "Contact": ("simscale_sdk_v1.models.simulation.contact", "Contact"),
    "ContactConductanceLayer": (
        "simscale_sdk_v1.models.simulation.contact_conductance_layer",
        "ContactConductanceLayer",
    ),
    "ContactFieldSelection": ("simscale_sdk_v1.models.simulation.contact_field_selection", "ContactFieldSelection"),
    "ContactGapType": ("simscale_sdk_v1.models.simulation.contact_gap_type", "ContactGapType"),
    "ContactInterfaceMaterialInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.contact_interface_material_interface_thermal",
        "ContactInterfaceMaterialInterfaceThermal",
    ),
    "ContactNormalForceType": ("simscale_sdk_v1.models.simulation.contact_normal_force_type", "ContactNormalForceType"),
    "ContactPressureType": ("simscale_sdk_v1.models.simulation.contact_pressure_type", "ContactPressureType"),
    "ContactResistanceLayer": ("simscale_sdk_v1.models.simulation.contact_resistance_layer", "ContactResistanceLayer"),
    "ContactResultControlItem": (
        "simscale_sdk_v1.models.simulation.contact_result_control_item",
        "ContactResultControlItem",
    ),
    "ContactStateType": ("simscale_sdk_v1.models.simulation.contact_state_type", "ContactStateType"),
    "ConvectionRadiationTBC": ("simscale_sdk_v1.models.simulation.convection_radiation_tbc", "ConvectionRadiationTBC"),
    "ConvectionTBC": ("simscale_sdk_v1.models.simulation.convection_tbc", "ConvectionTBC"),
    "ConvectiveHeatFlux": ("simscale_sdk_v1.models.simulation.convective_heat_flux", "ConvectiveHeatFlux"),
    "ConvectiveHeatFluxBC": ("simscale_sdk_v1.models.simulation.convective_heat_flux_bc", "ConvectiveHeatFluxBC"),
    "ConvectiveHeatTransfer": ("simscale_sdk_v1.models.simulation.convective_heat_transfer", "ConvectiveHeatTransfer"),
    "ConvectiveHeatTransferMaterials": (
        "simscale_sdk_v1.models.simulation.convective_heat_transfer_materials",
        "ConvectiveHeatTransferMaterials",
    ),
    "CorrectedSurfaceNormalGradientScheme": (
        "simscale_sdk_v1.models.simulation.corrected_surface_normal_gradient_scheme",
        "CorrectedSurfaceNormalGradientScheme",
    ),
    "CoulombFriction": ("simscale_sdk_v1.models.simulation.coulomb_friction", "CoulombFriction"),
    "CoupledConjugateHeatTransfer": (
        "simscale_sdk_v1.models.simulation.coupled_conjugate_heat_transfer",
        "CoupledConjugateHeatTransfer",
    ),
    "CoupledConjugateHeatTransferMaterials": (
        "simscale_sdk_v1.models.simulation.coupled_conjugate_heat_transfer_materials",
        "CoupledConjugateHeatTransferMaterials",
    ),
    "CoupledInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.coupled_interface_thermal",
        "CoupledInterfaceThermal",
    ),
    "CoverSpectrum": ("simscale_sdk_v1.models.simulation.cover_spectrum", "CoverSpectrum"),
    "CpuTimeWriteControl": ("simscale_sdk_v1.models.simulation.cpu_time_write_control", "CpuTimeWriteControl"),
    "CrossPlaneCustomOrientation": (
        "simscale_sdk_v1.models.simulation.cross_plane_custom_orientation",
        "CrossPlaneCustomOrientation",
    ),
    "CrossPlaneOrthotropicConductivity": (
        "simscale_sdk_v1.models.simulation.cross_plane_orthotropic_conductivity",
        "CrossPlaneOrthotropicConductivity",
    ),
    "CrossPowerLawViscosityModel": (
        "simscale_sdk_v1.models.simulation.cross_power_law_viscosity_model",
        "CrossPowerLawViscosityModel",
    ),
    "CubeRootVolLesDelta": ("simscale_sdk_v1.models.simulation.cube_root_vol_les_delta", "CubeRootVolLesDelta"),
    "CubicInterpolationScheme": (
        "simscale_sdk_v1.models.simulation.cubic_interpolation_scheme",
        "CubicInterpolationScheme",
    ),
    "CurrentExcitation": ("simscale_sdk_v1.models.simulation.current_excitation", "CurrentExcitation"),
    "CurrentInflowEBC": ("simscale_sdk_v1.models.simulation.current_inflow_ebc", "CurrentInflowEBC"),
    "CurrentOutflowEBC": ("simscale_sdk_v1.models.simulation.current_outflow_ebc", "CurrentOutflowEBC"),
    "CustomAxisDefinition": ("simscale_sdk_v1.models.simulation.custom_axis_definition", "CustomAxisDefinition"),
    "CustomComfortCriterionResultControl": (
        "simscale_sdk_v1.models.simulation.custom_comfort_criterion_result_control",
        "CustomComfortCriterionResultControl",
    ),
    "CustomConnectorPointDataResults": (
        "simscale_sdk_v1.models.simulation.custom_connector_point_data_results",
        "CustomConnectorPointDataResults",
    ),
    "CustomContactStiffness": ("simscale_sdk_v1.models.simulation.custom_contact_stiffness", "CustomContactStiffness"),
    "CustomDomainDecomposition": (
        "simscale_sdk_v1.models.simulation.custom_domain_decomposition",
        "CustomDomainDecomposition",
    ),
    "CustomElementDefinitionMethod": (
        "simscale_sdk_v1.models.simulation.custom_element_definition_method",
        "CustomElementDefinitionMethod",
    ),
    "CustomEmbeddedBoundaryMeshSizing": (
        "simscale_sdk_v1.models.simulation.custom_embedded_boundary_mesh_sizing",
        "CustomEmbeddedBoundaryMeshSizing",
    ),
    "CustomFluidBC": ("simscale_sdk_v1.models.simulation.custom_fluid_bc", "CustomFluidBC"),
    "CustomFractionBodySurface": (
        "simscale_sdk_v1.models.simulation.custom_fraction_body_surface",
        "CustomFractionBodySurface",
    ),
    "CustomOmegaDissipation": ("simscale_sdk_v1.models.simulation.custom_omega_dissipation", "CustomOmegaDissipation"),
    "CustomOrientation": ("simscale_sdk_v1.models.simulation.custom_orientation", "CustomOrientation"),
    "CustomResolution": ("simscale_sdk_v1.models.simulation.custom_resolution", "CustomResolution"),
    "CustomSolarLoad": ("simscale_sdk_v1.models.simulation.custom_solar_load", "CustomSolarLoad"),
    "CustomSunDirection": ("simscale_sdk_v1.models.simulation.custom_sun_direction", "CustomSunDirection"),
    "CustomTree": ("simscale_sdk_v1.models.simulation.custom_tree", "CustomTree"),
    "CyclicSymmetryBC": ("simscale_sdk_v1.models.simulation.cyclic_symmetry_bc", "CyclicSymmetryBC"),
    "DICPreconditioner": ("simscale_sdk_v1.models.simulation.dic_preconditioner", "DICPreconditioner"),
    "DILUPreconditioner": ("simscale_sdk_v1.models.simulation.dilu_preconditioner", "DILUPreconditioner"),
    "DarcyForchheimerMedium": ("simscale_sdk_v1.models.simulation.darcy_forchheimer_medium", "DarcyForchheimerMedium"),
    "DarcyMedium": ("simscale_sdk_v1.models.simulation.darcy_medium", "DarcyMedium"),
    "DecimalVector": ("simscale_sdk_v1.models.simulation.decimal_vector", "DecimalVector"),
    "DecimalVector2d": ("simscale_sdk_v1.models.simulation.decimal_vector2d", "DecimalVector2d"),
    "DerivedHeatFlux": ("simscale_sdk_v1.models.simulation.derived_heat_flux", "DerivedHeatFlux"),
    "Dielectric": ("simscale_sdk_v1.models.simulation.dielectric", "Dielectric"),
    "DimensionalFunctionInitialConditionDomains_Temperature": (
        "simscale_sdk_v1.models.simulation.dimensional_function_initial_condition_domains__temperature",
        "DimensionalFunctionInitialConditionDomains_Temperature",
    ),
    "DimensionalFunction_Acceleration": (
        "simscale_sdk_v1.models.simulation.dimensional_function__acceleration",
        "DimensionalFunction_Acceleration",
    ),
    "DimensionalFunction_Angle": (
        "simscale_sdk_v1.models.simulation.dimensional_function__angle",
        "DimensionalFunction_Angle",
    ),
    "DimensionalFunction_Density": (
        "simscale_sdk_v1.models.simulation.dimensional_function__density",
        "DimensionalFunction_Density",
    ),
    "DimensionalFunction_Dimensionless": (
        "simscale_sdk_v1.models.simulation.dimensional_function__dimensionless",
        "DimensionalFunction_Dimensionless",
    ),
    "DimensionalFunction_DynamicViscosity": (
        "simscale_sdk_v1.models.simulation.dimensional_function__dynamic_viscosity",
        "DimensionalFunction_DynamicViscosity",
    ),
    "DimensionalFunction_ElectricConductivity": (
        "simscale_sdk_v1.models.simulation.dimensional_function__electric_conductivity",
        "DimensionalFunction_ElectricConductivity",
    ),
    "DimensionalFunction_ElectricCurrent": (
        "simscale_sdk_v1.models.simulation.dimensional_function__electric_current",
        "DimensionalFunction_ElectricCurrent",
    ),
    "DimensionalFunction_ElectricFieldStrength": (
        "simscale_sdk_v1.models.simulation.dimensional_function__electric_field_strength",
        "DimensionalFunction_ElectricFieldStrength",
    ),
    "DimensionalFunction_ElectricPotential": (
        "simscale_sdk_v1.models.simulation.dimensional_function__electric_potential",
        "DimensionalFunction_ElectricPotential",
    ),
    "DimensionalFunction_ElectricResistivity": (
        "simscale_sdk_v1.models.simulation.dimensional_function__electric_resistivity",
        "DimensionalFunction_ElectricResistivity",
    ),
    "DimensionalFunction_HeatFlux": (
        "simscale_sdk_v1.models.simulation.dimensional_function__heat_flux",
        "DimensionalFunction_HeatFlux",
    ),
    "DimensionalFunction_KinematicViscosity": (
        "simscale_sdk_v1.models.simulation.dimensional_function__kinematic_viscosity",
        "DimensionalFunction_KinematicViscosity",
    ),
    "DimensionalFunction_Length": (
        "simscale_sdk_v1.models.simulation.dimensional_function__length",
        "DimensionalFunction_Length",
    ),
    "DimensionalFunction_MagneticFluxDensity": (
        "simscale_sdk_v1.models.simulation.dimensional_function__magnetic_flux_density",
        "DimensionalFunction_MagneticFluxDensity",
    ),
    "DimensionalFunction_MassFlowRate": (
        "simscale_sdk_v1.models.simulation.dimensional_function__mass_flow_rate",
        "DimensionalFunction_MassFlowRate",
    ),
    "DimensionalFunction_Power": (
        "simscale_sdk_v1.models.simulation.dimensional_function__power",
        "DimensionalFunction_Power",
    ),
    "DimensionalFunction_Pressure": (
        "simscale_sdk_v1.models.simulation.dimensional_function__pressure",
        "DimensionalFunction_Pressure",
    ),
    "DimensionalFunction_RotationSpeed": (
        "simscale_sdk_v1.models.simulation.dimensional_function__rotation_speed",
        "DimensionalFunction_RotationSpeed",
    ),
    "DimensionalFunction_SpecificEnergy": (
        "simscale_sdk_v1.models.simulation.dimensional_function__specific_energy",
        "DimensionalFunction_SpecificEnergy",
    ),
    "DimensionalFunction_SpecificHeat": (
        "simscale_sdk_v1.models.simulation.dimensional_function__specific_heat",
        "DimensionalFunction_SpecificHeat",
    ),
    "DimensionalFunction_SpecificTurbulenceDissipationRate": (
        "simscale_sdk_v1.models.simulation.dimensional_function__specific_turbulence_dissipation_rate",
        "DimensionalFunction_SpecificTurbulenceDissipationRate",
    ),
    "DimensionalFunction_Speed": (
        "simscale_sdk_v1.models.simulation.dimensional_function__speed",
        "DimensionalFunction_Speed",
    ),
    "DimensionalFunction_Temperature": (
        "simscale_sdk_v1.models.simulation.dimensional_function__temperature",
        "DimensionalFunction_Temperature",
    ),
    "DimensionalFunction_TemperatureGradient": (
        "simscale_sdk_v1.models.simulation.dimensional_function__temperature_gradient",
        "DimensionalFunction_TemperatureGradient",
    ),
    "DimensionalFunction_ThermalConductivity": (
        "simscale_sdk_v1.models.simulation.dimensional_function__thermal_conductivity",
        "DimensionalFunction_ThermalConductivity",
    ),
    "DimensionalFunction_ThermalExpansionRate": (
        "simscale_sdk_v1.models.simulation.dimensional_function__thermal_expansion_rate",
        "DimensionalFunction_ThermalExpansionRate",
    ),
    "DimensionalFunction_ThermalTransmittance": (
        "simscale_sdk_v1.models.simulation.dimensional_function__thermal_transmittance",
        "DimensionalFunction_ThermalTransmittance",
    ),
    "DimensionalFunction_Time": (
        "simscale_sdk_v1.models.simulation.dimensional_function__time",
        "DimensionalFunction_Time",
    ),
    "DimensionalFunction_TotalThermalTransmittance": (
        "simscale_sdk_v1.models.simulation.dimensional_function__total_thermal_transmittance",
        "DimensionalFunction_TotalThermalTransmittance",
    ),
    "DimensionalFunction_TurbulenceKineticEnergy": (
        "simscale_sdk_v1.models.simulation.dimensional_function__turbulence_kinetic_energy",
        "DimensionalFunction_TurbulenceKineticEnergy",
    ),
    "DimensionalFunction_TurbulentDissipation": (
        "simscale_sdk_v1.models.simulation.dimensional_function__turbulent_dissipation",
        "DimensionalFunction_TurbulentDissipation",
    ),
    "DimensionalFunction_VolumetricFlowRate": (
        "simscale_sdk_v1.models.simulation.dimensional_function__volumetric_flow_rate",
        "DimensionalFunction_VolumetricFlowRate",
    ),
    "DimensionalFunction_VolumetricPower": (
        "simscale_sdk_v1.models.simulation.dimensional_function__volumetric_power",
        "DimensionalFunction_VolumetricPower",
    ),
    "DimensionalInitialConditionDomains_Dimensionless": (
        "simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__dimensionless",
        "DimensionalInitialConditionDomains_Dimensionless",
    ),
    "DimensionalInitialConditionDomains_KinematicViscosity": (
        "simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__kinematic_viscosity",
        "DimensionalInitialConditionDomains_KinematicViscosity",
    ),
    "DimensionalInitialConditionDomains_Pressure": (
        "simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__pressure",
        "DimensionalInitialConditionDomains_Pressure",
    ),
    "DimensionalInitialConditionDomains_SpecificTurbulenceDissipationRate": (
        "simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__specific_turbulence_dissipation_rate",
        "DimensionalInitialConditionDomains_SpecificTurbulenceDissipationRate",
    ),
    "DimensionalInitialConditionDomains_Temperature": (
        "simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__temperature",
        "DimensionalInitialConditionDomains_Temperature",
    ),
    "DimensionalInitialConditionDomains_TurbulenceKineticEnergy": (
        "simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__turbulence_kinetic_energy",
        "DimensionalInitialConditionDomains_TurbulenceKineticEnergy",
    ),
    "DimensionalInitialConditionDomains_TurbulentDissipation": (
        "simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__turbulent_dissipation",
        "DimensionalInitialConditionDomains_TurbulentDissipation",
    ),
    "DimensionalPartialVectorFunction_Angle": (
        "simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__angle",
        "DimensionalPartialVectorFunction_Angle",
    ),
    "DimensionalPartialVectorFunction_Length": (
        "simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__length",
        "DimensionalPartialVectorFunction_Length",
    ),
    "DimensionalVector2d_Length": (
        "simscale_sdk_v1.models.simulation.dimensional_vector2d__length",
        "DimensionalVector2d_Length",
    ),
    "DimensionalVectorFunctionInitialConditionWithDomains_Acceleration": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__acceleration",
        "DimensionalVectorFunctionInitialConditionWithDomains_Acceleration",
    ),
    "DimensionalVectorFunctionInitialConditionWithDomains_Length": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__length",
        "DimensionalVectorFunctionInitialConditionWithDomains_Length",
    ),
    "DimensionalVectorFunctionInitialConditionWithDomains_Speed": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__speed",
        "DimensionalVectorFunctionInitialConditionWithDomains_Speed",
    ),
    "DimensionalVectorFunction_Acceleration": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function__acceleration",
        "DimensionalVectorFunction_Acceleration",
    ),
    "DimensionalVectorFunction_Force": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function__force",
        "DimensionalVectorFunction_Force",
    ),
    "DimensionalVectorFunction_Length": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function__length",
        "DimensionalVectorFunction_Length",
    ),
    "DimensionalVectorFunction_Pressure": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function__pressure",
        "DimensionalVectorFunction_Pressure",
    ),
    "DimensionalVectorFunction_Speed": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function__speed",
        "DimensionalVectorFunction_Speed",
    ),
    "DimensionalVectorFunction_Torque": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function__torque",
        "DimensionalVectorFunction_Torque",
    ),
    "DimensionalVectorFunction_VolumeForce": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_function__volume_force",
        "DimensionalVectorFunction_VolumeForce",
    ),
    "DimensionalVectorInitialConditionDomains_Speed": (
        "simscale_sdk_v1.models.simulation.dimensional_vector_initial_condition_domains__speed",
        "DimensionalVectorInitialConditionDomains_Speed",
    ),
    "DimensionalVector_Absorptivity": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__absorptivity",
        "DimensionalVector_Absorptivity",
    ),
    "DimensionalVector_Acceleration": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__acceleration",
        "DimensionalVector_Acceleration",
    ),
    "DimensionalVector_Angle": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__angle",
        "DimensionalVector_Angle",
    ),
    "DimensionalVector_Dimensionless": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless",
        "DimensionalVector_Dimensionless",
    ),
    "DimensionalVector_Length": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__length",
        "DimensionalVector_Length",
    ),
    "DimensionalVector_MomentOfInertia": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__moment_of_inertia",
        "DimensionalVector_MomentOfInertia",
    ),
    "DimensionalVector_ReciprocalPermeability": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__reciprocal_permeability",
        "DimensionalVector_ReciprocalPermeability",
    ),
    "DimensionalVector_RotationSpeed": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__rotation_speed",
        "DimensionalVector_RotationSpeed",
    ),
    "DimensionalVector_SpecificTurbulenceDissipationRate": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__specific_turbulence_dissipation_rate",
        "DimensionalVector_SpecificTurbulenceDissipationRate",
    ),
    "DimensionalVector_Speed": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__speed",
        "DimensionalVector_Speed",
    ),
    "DimensionalVector_SurfaceTension": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__surface_tension",
        "DimensionalVector_SurfaceTension",
    ),
    "DimensionalVector_VolumeForce": (
        "simscale_sdk_v1.models.simulation.dimensional_vector__volume_force",
        "DimensionalVector_VolumeForce",
    ),
    "Dimensional_AbsoluteHumidityRate": (
        "simscale_sdk_v1.models.simulation.dimensional__absolute_humidity_rate",
        "Dimensional_AbsoluteHumidityRate",
    ),
    "Dimensional_Absorptivity": (
        "simscale_sdk_v1.models.simulation.dimensional__absorptivity",
        "Dimensional_Absorptivity",
    ),
    "Dimensional_Acceleration": (
        "simscale_sdk_v1.models.simulation.dimensional__acceleration",
        "Dimensional_Acceleration",
    ),
    "Dimensional_Angle": ("simscale_sdk_v1.models.simulation.dimensional__angle", "Dimensional_Angle"),
    "Dimensional_Area": ("simscale_sdk_v1.models.simulation.dimensional__area", "Dimensional_Area"),
    "Dimensional_Charge": ("simscale_sdk_v1.models.simulation.dimensional__charge", "Dimensional_Charge"),
    "Dimensional_ChargeDensity": (
        "simscale_sdk_v1.models.simulation.dimensional__charge_density",
        "Dimensional_ChargeDensity",
    ),
    "Dimensional_ContactResistance": (
        "simscale_sdk_v1.models.simulation.dimensional__contact_resistance",
        "Dimensional_ContactResistance",
    ),
    "Dimensional_Density": ("simscale_sdk_v1.models.simulation.dimensional__density", "Dimensional_Density"),
    "Dimensional_Dimensionless": (
        "simscale_sdk_v1.models.simulation.dimensional__dimensionless",
        "Dimensional_Dimensionless",
    ),
    "Dimensional_DynamicViscosity": (
        "simscale_sdk_v1.models.simulation.dimensional__dynamic_viscosity",
        "Dimensional_DynamicViscosity",
    ),
    "Dimensional_EddyViscosityGradient": (
        "simscale_sdk_v1.models.simulation.dimensional__eddy_viscosity_gradient",
        "Dimensional_EddyViscosityGradient",
    ),
    "Dimensional_ElectricConductance": (
        "simscale_sdk_v1.models.simulation.dimensional__electric_conductance",
        "Dimensional_ElectricConductance",
    ),
    "Dimensional_ElectricCurrent": (
        "simscale_sdk_v1.models.simulation.dimensional__electric_current",
        "Dimensional_ElectricCurrent",
    ),
    "Dimensional_ElectricPotential": (
        "simscale_sdk_v1.models.simulation.dimensional__electric_potential",
        "Dimensional_ElectricPotential",
    ),
    "Dimensional_ElectricResistance": (
        "simscale_sdk_v1.models.simulation.dimensional__electric_resistance",
        "Dimensional_ElectricResistance",
    ),
    "Dimensional_ElectricResistivity": (
        "simscale_sdk_v1.models.simulation.dimensional__electric_resistivity",
        "Dimensional_ElectricResistivity",
    ),
    "Dimensional_EnergyDensity": (
        "simscale_sdk_v1.models.simulation.dimensional__energy_density",
        "Dimensional_EnergyDensity",
    ),
    "Dimensional_EpsilonGradient": (
        "simscale_sdk_v1.models.simulation.dimensional__epsilon_gradient",
        "Dimensional_EpsilonGradient",
    ),
    "Dimensional_Force": ("simscale_sdk_v1.models.simulation.dimensional__force", "Dimensional_Force"),
    "Dimensional_ForceDensity": (
        "simscale_sdk_v1.models.simulation.dimensional__force_density",
        "Dimensional_ForceDensity",
    ),
    "Dimensional_Frequency": ("simscale_sdk_v1.models.simulation.dimensional__frequency", "Dimensional_Frequency"),
    "Dimensional_FrictionAugmentation": (
        "simscale_sdk_v1.models.simulation.dimensional__friction_augmentation",
        "Dimensional_FrictionAugmentation",
    ),
    "Dimensional_HeatFlux": ("simscale_sdk_v1.models.simulation.dimensional__heat_flux", "Dimensional_HeatFlux"),
    "Dimensional_InvPressure": (
        "simscale_sdk_v1.models.simulation.dimensional__inv_pressure",
        "Dimensional_InvPressure",
    ),
    "Dimensional_KinematicViscosity": (
        "simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity",
        "Dimensional_KinematicViscosity",
    ),
    "Dimensional_Length": ("simscale_sdk_v1.models.simulation.dimensional__length", "Dimensional_Length"),
    "Dimensional_MagneticFluxDensity": (
        "simscale_sdk_v1.models.simulation.dimensional__magnetic_flux_density",
        "Dimensional_MagneticFluxDensity",
    ),
    "Dimensional_Mass": ("simscale_sdk_v1.models.simulation.dimensional__mass", "Dimensional_Mass"),
    "Dimensional_MassAreaDensity": (
        "simscale_sdk_v1.models.simulation.dimensional__mass_area_density",
        "Dimensional_MassAreaDensity",
    ),
    "Dimensional_MassFlowRate": (
        "simscale_sdk_v1.models.simulation.dimensional__mass_flow_rate",
        "Dimensional_MassFlowRate",
    ),
    "Dimensional_MassFraction": (
        "simscale_sdk_v1.models.simulation.dimensional__mass_fraction",
        "Dimensional_MassFraction",
    ),
    "Dimensional_MolarMass": ("simscale_sdk_v1.models.simulation.dimensional__molar_mass", "Dimensional_MolarMass"),
    "Dimensional_PassiveScalarSourceRate": (
        "simscale_sdk_v1.models.simulation.dimensional__passive_scalar_source_rate",
        "Dimensional_PassiveScalarSourceRate",
    ),
    "Dimensional_PhaseFractionGradient": (
        "simscale_sdk_v1.models.simulation.dimensional__phase_fraction_gradient",
        "Dimensional_PhaseFractionGradient",
    ),
    "Dimensional_Power": ("simscale_sdk_v1.models.simulation.dimensional__power", "Dimensional_Power"),
    "Dimensional_Pressure": ("simscale_sdk_v1.models.simulation.dimensional__pressure", "Dimensional_Pressure"),
    "Dimensional_RotationSpeed": (
        "simscale_sdk_v1.models.simulation.dimensional__rotation_speed",
        "Dimensional_RotationSpeed",
    ),
    "Dimensional_RotationalStiffness": (
        "simscale_sdk_v1.models.simulation.dimensional__rotational_stiffness",
        "Dimensional_RotationalStiffness",
    ),
    "Dimensional_SpecificContactResistance": (
        "simscale_sdk_v1.models.simulation.dimensional__specific_contact_resistance",
        "Dimensional_SpecificContactResistance",
    ),
    "Dimensional_SpecificElectricConductance": (
        "simscale_sdk_v1.models.simulation.dimensional__specific_electric_conductance",
        "Dimensional_SpecificElectricConductance",
    ),
    "Dimensional_SpecificElectricResistance": (
        "simscale_sdk_v1.models.simulation.dimensional__specific_electric_resistance",
        "Dimensional_SpecificElectricResistance",
    ),
    "Dimensional_SpecificHeat": (
        "simscale_sdk_v1.models.simulation.dimensional__specific_heat",
        "Dimensional_SpecificHeat",
    ),
    "Dimensional_SpecificTurbulenceDissipationRate": (
        "simscale_sdk_v1.models.simulation.dimensional__specific_turbulence_dissipation_rate",
        "Dimensional_SpecificTurbulenceDissipationRate",
    ),
    "Dimensional_SpecificTurbulenceDissipationRateGradient": (
        "simscale_sdk_v1.models.simulation.dimensional__specific_turbulence_dissipation_rate_gradient",
        "Dimensional_SpecificTurbulenceDissipationRateGradient",
    ),
    "Dimensional_Speed": ("simscale_sdk_v1.models.simulation.dimensional__speed", "Dimensional_Speed"),
    "Dimensional_Stiffness": ("simscale_sdk_v1.models.simulation.dimensional__stiffness", "Dimensional_Stiffness"),
    "Dimensional_StrainRate": ("simscale_sdk_v1.models.simulation.dimensional__strain_rate", "Dimensional_StrainRate"),
    "Dimensional_SurfaceTension": (
        "simscale_sdk_v1.models.simulation.dimensional__surface_tension",
        "Dimensional_SurfaceTension",
    ),
    "Dimensional_Temperature": (
        "simscale_sdk_v1.models.simulation.dimensional__temperature",
        "Dimensional_Temperature",
    ),
    "Dimensional_ThermalConductivity": (
        "simscale_sdk_v1.models.simulation.dimensional__thermal_conductivity",
        "Dimensional_ThermalConductivity",
    ),
    "Dimensional_ThermalExpansionRate": (
        "simscale_sdk_v1.models.simulation.dimensional__thermal_expansion_rate",
        "Dimensional_ThermalExpansionRate",
    ),
    "Dimensional_ThermalTransmittance": (
        "simscale_sdk_v1.models.simulation.dimensional__thermal_transmittance",
        "Dimensional_ThermalTransmittance",
    ),
    "Dimensional_Time": ("simscale_sdk_v1.models.simulation.dimensional__time", "Dimensional_Time"),
    "Dimensional_Torque": ("simscale_sdk_v1.models.simulation.dimensional__torque", "Dimensional_Torque"),
    "Dimensional_TotalThermalTransmittance": (
        "simscale_sdk_v1.models.simulation.dimensional__total_thermal_transmittance",
        "Dimensional_TotalThermalTransmittance",
    ),
    "Dimensional_TurbulenceKineticEnergy": (
        "simscale_sdk_v1.models.simulation.dimensional__turbulence_kinetic_energy",
        "Dimensional_TurbulenceKineticEnergy",
    ),
    "Dimensional_TurbulentDissipation": (
        "simscale_sdk_v1.models.simulation.dimensional__turbulent_dissipation",
        "Dimensional_TurbulentDissipation",
    ),
    "Dimensional_VolumeForce": (
        "simscale_sdk_v1.models.simulation.dimensional__volume_force",
        "Dimensional_VolumeForce",
    ),
    "Dimensional_VolumetricPassiveScalarSourceRate": (
        "simscale_sdk_v1.models.simulation.dimensional__volumetric_passive_scalar_source_rate",
        "Dimensional_VolumetricPassiveScalarSourceRate",
    ),
    "DimensionlessInitialConditionDomains": (
        "simscale_sdk_v1.models.simulation.dimensionless_initial_condition_domains",
        "DimensionlessInitialConditionDomains",
    ),
    "DirectionalDependency": ("simscale_sdk_v1.models.simulation.directional_dependency", "DirectionalDependency"),
    "DirectionalMaterialStructure": (
        "simscale_sdk_v1.models.simulation.directional_material_structure",
        "DirectionalMaterialStructure",
    ),
    "DisplacementField": ("simscale_sdk_v1.models.simulation.displacement_field", "DisplacementField"),
    "DisplacementFieldSelection": (
        "simscale_sdk_v1.models.simulation.displacement_field_selection",
        "DisplacementFieldSelection",
    ),
    "DisplacementResultControlItem": (
        "simscale_sdk_v1.models.simulation.displacement_result_control_item",
        "DisplacementResultControlItem",
    ),
    "DisplacementsConvergenceMethod": (
        "simscale_sdk_v1.models.simulation.displacements_convergence_method",
        "DisplacementsConvergenceMethod",
    ),
    "DistanceRegionRefinementWithLength": (
        "simscale_sdk_v1.models.simulation.distance_region_refinement_with_length",
        "DistanceRegionRefinementWithLength",
    ),
    "DistributedIsotropicStiffnessDefinition": (
        "simscale_sdk_v1.models.simulation.distributed_isotropic_stiffness_definition",
        "DistributedIsotropicStiffnessDefinition",
    ),
    "DistributedMassBC": ("simscale_sdk_v1.models.simulation.distributed_mass_bc", "DistributedMassBC"),
    "DistributedOrthotropicStiffnessDefinition": (
        "simscale_sdk_v1.models.simulation.distributed_orthotropic_stiffness_definition",
        "DistributedOrthotropicStiffnessDefinition",
    ),
    "DivergenceSchemes": ("simscale_sdk_v1.models.simulation.divergence_schemes", "DivergenceSchemes"),
    "DynamicAnalysis": ("simscale_sdk_v1.models.simulation.dynamic_analysis", "DynamicAnalysis"),
    "DynamicContactAnglePFBC": (
        "simscale_sdk_v1.models.simulation.dynamic_contact_angle_pfbc",
        "DynamicContactAnglePFBC",
    ),
    "EConstThermo": ("simscale_sdk_v1.models.simulation.e_const_thermo", "EConstThermo"),
    "ERPCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.erp_calculation_result_control_item",
        "ERPCalculationResultControlItem",
    ),
    "ERPDensityResultControlItem": (
        "simscale_sdk_v1.models.simulation.erp_density_result_control_item",
        "ERPDensityResultControlItem",
    ),
    "EffectiveConductivityHeatTransfer": (
        "simscale_sdk_v1.models.simulation.effective_conductivity_heat_transfer",
        "EffectiveConductivityHeatTransfer",
    ),
    "EigenModeVerification": ("simscale_sdk_v1.models.simulation.eigen_mode_verification", "EigenModeVerification"),
    "ElasticJacobianMatrix": ("simscale_sdk_v1.models.simulation.elastic_jacobian_matrix", "ElasticJacobianMatrix"),
    "ElasticStrain": ("simscale_sdk_v1.models.simulation.elastic_strain", "ElasticStrain"),
    "ElasticSupportBC": ("simscale_sdk_v1.models.simulation.elastic_support_bc", "ElasticSupportBC"),
    "ElasticityMarc": ("simscale_sdk_v1.models.simulation.elasticity_marc", "ElasticityMarc"),
    "ElastoplasticMarcMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.elastoplastic_marc_material_behavior",
        "ElastoplasticMarcMaterialBehavior",
    ),
    "ElastoplasticNetwork": ("simscale_sdk_v1.models.simulation.elastoplastic_network", "ElastoplasticNetwork"),
    "ElectricCurrentDensityFieldSelection": (
        "simscale_sdk_v1.models.simulation.electric_current_density_field_selection",
        "ElectricCurrentDensityFieldSelection",
    ),
    "ElectricDisplacementFieldFieldSelection": (
        "simscale_sdk_v1.models.simulation.electric_displacement_field_field_selection",
        "ElectricDisplacementFieldFieldSelection",
    ),
    "ElectricFieldFieldSelection": (
        "simscale_sdk_v1.models.simulation.electric_field_field_selection",
        "ElectricFieldFieldSelection",
    ),
    "ElectricPotentialFieldSelection": (
        "simscale_sdk_v1.models.simulation.electric_potential_field_selection",
        "ElectricPotentialFieldSelection",
    ),
    "ElectricalSteelCoreLoss": (
        "simscale_sdk_v1.models.simulation.electrical_steel_core_loss",
        "ElectricalSteelCoreLoss",
    ),
    "ElectromagneticAdvancedConcepts": (
        "simscale_sdk_v1.models.simulation.electromagnetic_advanced_concepts",
        "ElectromagneticAdvancedConcepts",
    ),
    "ElectromagneticAnalysis": (
        "simscale_sdk_v1.models.simulation.electromagnetic_analysis",
        "ElectromagneticAnalysis",
    ),
    "ElectromagneticCircuit": ("simscale_sdk_v1.models.simulation.electromagnetic_circuit", "ElectromagneticCircuit"),
    "ElectromagneticCurrentTypeConstant": (
        "simscale_sdk_v1.models.simulation.electromagnetic_current_type_constant",
        "ElectromagneticCurrentTypeConstant",
    ),
    "ElectromagneticCurrentTypeSinusoidal": (
        "simscale_sdk_v1.models.simulation.electromagnetic_current_type_sinusoidal",
        "ElectromagneticCurrentTypeSinusoidal",
    ),
    "ElectromagneticCurrentTypeTable": (
        "simscale_sdk_v1.models.simulation.electromagnetic_current_type_table",
        "ElectromagneticCurrentTypeTable",
    ),
    "ElectromagneticInitialConditions": (
        "simscale_sdk_v1.models.simulation.electromagnetic_initial_conditions",
        "ElectromagneticInitialConditions",
    ),
    "ElectromagneticMaterial": (
        "simscale_sdk_v1.models.simulation.electromagnetic_material",
        "ElectromagneticMaterial",
    ),
    "ElectromagneticNumerics": (
        "simscale_sdk_v1.models.simulation.electromagnetic_numerics",
        "ElectromagneticNumerics",
    ),
    "ElectromagneticResistanceSet": (
        "simscale_sdk_v1.models.simulation.electromagnetic_resistance_set",
        "ElectromagneticResistanceSet",
    ),
    "ElectromagneticResultControl": (
        "simscale_sdk_v1.models.simulation.electromagnetic_result_control",
        "ElectromagneticResultControl",
    ),
    "ElectromagneticResultControlProbePoint": (
        "simscale_sdk_v1.models.simulation.electromagnetic_result_control_probe_point",
        "ElectromagneticResultControlProbePoint",
    ),
    "ElectromagneticSimulationControl": (
        "simscale_sdk_v1.models.simulation.electromagnetic_simulation_control",
        "ElectromagneticSimulationControl",
    ),
    "ElectromagneticTransientControl": (
        "simscale_sdk_v1.models.simulation.electromagnetic_transient_control",
        "ElectromagneticTransientControl",
    ),
    "ElectromagneticVoltageTypeConstant": (
        "simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_constant",
        "ElectromagneticVoltageTypeConstant",
    ),
    "ElectromagneticVoltageTypeSinusoidal": (
        "simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_sinusoidal",
        "ElectromagneticVoltageTypeSinusoidal",
    ),
    "ElectromagneticVoltageTypeTable": (
        "simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_table",
        "ElectromagneticVoltageTypeTable",
    ),
    "Electrostatics": ("simscale_sdk_v1.models.simulation.electrostatics", "Electrostatics"),
    "ElementGroupsDomainDecomposition": (
        "simscale_sdk_v1.models.simulation.element_groups_domain_decomposition",
        "ElementGroupsDomainDecomposition",
    ),
    "ElementTechnology": ("simscale_sdk_v1.models.simulation.element_technology", "ElementTechnology"),
    "ElementTechnologyDefinition": (
        "simscale_sdk_v1.models.simulation.element_technology_definition",
        "ElementTechnologyDefinition",
    ),
    "EmbeddedBoundary": ("simscale_sdk_v1.models.simulation.embedded_boundary", "EmbeddedBoundary"),
    "EmbeddedBoundaryMeshing": (
        "simscale_sdk_v1.models.simulation.embedded_boundary_meshing",
        "EmbeddedBoundaryMeshing",
    ),
    "Empty2DBC": ("simscale_sdk_v1.models.simulation.empty2_dbc", "Empty2DBC"),
    "EquivalentElasticStrain": (
        "simscale_sdk_v1.models.simulation.equivalent_elastic_strain",
        "EquivalentElasticStrain",
    ),
    "EquivalentPlasticStrain": (
        "simscale_sdk_v1.models.simulation.equivalent_plastic_strain",
        "EquivalentPlasticStrain",
    ),
    "EquivalentRadiatedPowerDensityType": (
        "simscale_sdk_v1.models.simulation.equivalent_radiated_power_density_type",
        "EquivalentRadiatedPowerDensityType",
    ),
    "EquivalentSandGrainRoughness": (
        "simscale_sdk_v1.models.simulation.equivalent_sand_grain_roughness",
        "EquivalentSandGrainRoughness",
    ),
    "ErrorRetimingEvent": ("simscale_sdk_v1.models.simulation.error_retiming_event", "ErrorRetimingEvent"),
    "EulerTimeDifferentiationScheme": (
        "simscale_sdk_v1.models.simulation.euler_time_differentiation_scheme",
        "EulerTimeDifferentiationScheme",
    ),
    "ExplicitTimeIntegrationType": (
        "simscale_sdk_v1.models.simulation.explicit_time_integration_type",
        "ExplicitTimeIntegrationType",
    ),
    "ExpressionFunction": ("simscale_sdk_v1.models.simulation.expression_function", "ExpressionFunction"),
    "ExternalForce": ("simscale_sdk_v1.models.simulation.external_force", "ExternalForce"),
    "ExternalPressure": ("simscale_sdk_v1.models.simulation.external_pressure", "ExternalPressure"),
    "ExternalWallHeatFluxTBC": (
        "simscale_sdk_v1.models.simulation.external_wall_heat_flux_tbc",
        "ExternalWallHeatFluxTBC",
    ),
    "FaceNormalMagnetizationDirectionMethod": (
        "simscale_sdk_v1.models.simulation.face_normal_magnetization_direction_method",
        "FaceNormalMagnetizationDirectionMethod",
    ),
    "FairWeatherConditions": ("simscale_sdk_v1.models.simulation.fair_weather_conditions", "FairWeatherConditions"),
    "FalseChangeJacobianMatrix": (
        "simscale_sdk_v1.models.simulation.false_change_jacobian_matrix",
        "FalseChangeJacobianMatrix",
    ),
    "FalseLineSearch": ("simscale_sdk_v1.models.simulation.false_line_search", "FalseLineSearch"),
    "FalseSemiImplicit": ("simscale_sdk_v1.models.simulation.false_semi_implicit", "FalseSemiImplicit"),
    "FanBC": ("simscale_sdk_v1.models.simulation.fan_bc", "FanBC"),
    "FanPBC": ("simscale_sdk_v1.models.simulation.fan_pbc", "FanPBC"),
    "FanPressureDropMomentumSource": (
        "simscale_sdk_v1.models.simulation.fan_pressure_drop_momentum_source",
        "FanPressureDropMomentumSource",
    ),
    "FieldCalculationsAdjointSensitivitiesResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_adjoint_sensitivities_result_control",
        "FieldCalculationsAdjointSensitivitiesResultControl",
    ),
    "FieldCalculationsFrictionVelocityResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_friction_velocity_result_control",
        "FieldCalculationsFrictionVelocityResultControl",
    ),
    "FieldCalculationsMeanAgeOfFluidResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_mean_age_of_fluid_result_control",
        "FieldCalculationsMeanAgeOfFluidResultControl",
    ),
    "FieldCalculationsMeanRadiantTemperatureResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_mean_radiant_temperature_result_control",
        "FieldCalculationsMeanRadiantTemperatureResultControl",
    ),
    "FieldCalculationsModeledTIResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_modeled_ti_result_control",
        "FieldCalculationsModeledTIResultControl",
    ),
    "FieldCalculationsOperativeTemperatureResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_operative_temperature_result_control",
        "FieldCalculationsOperativeTemperatureResultControl",
    ),
    "FieldCalculationsPressureResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_pressure_result_control",
        "FieldCalculationsPressureResultControl",
    ),
    "FieldCalculationsResolvedTIResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_resolved_ti_result_control",
        "FieldCalculationsResolvedTIResultControl",
    ),
    "FieldCalculationsResolvedTKEResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_resolved_tke_result_control",
        "FieldCalculationsResolvedTKEResultControl",
    ),
    "FieldCalculationsSurfaceNormalsResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_surface_normals_result_control",
        "FieldCalculationsSurfaceNormalsResultControl",
    ),
    "FieldCalculationsThermalComfortResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_thermal_comfort_result_control",
        "FieldCalculationsThermalComfortResultControl",
    ),
    "FieldCalculationsTotalTIResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_total_ti_result_control",
        "FieldCalculationsTotalTIResultControl",
    ),
    "FieldCalculationsTotalTKEResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_total_tke_result_control",
        "FieldCalculationsTotalTKEResultControl",
    ),
    "FieldCalculationsTurbulenceResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_turbulence_result_control",
        "FieldCalculationsTurbulenceResultControl",
    ),
    "FieldCalculationsVelocityResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_velocity_result_control",
        "FieldCalculationsVelocityResultControl",
    ),
    "FieldCalculationsWallFluxesResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_wall_fluxes_result_control",
        "FieldCalculationsWallFluxesResultControl",
    ),
    "FieldCalculationsWallHeatFluxResultControl": (
        "simscale_sdk_v1.models.simulation.field_calculations_wall_heat_flux_result_control",
        "FieldCalculationsWallHeatFluxResultControl",
    ),
    "FieldChangeRetimingEvent": (
        "simscale_sdk_v1.models.simulation.field_change_retiming_event",
        "FieldChangeRetimingEvent",
    ),
    "FieldChangeTargetCalculationType": (
        "simscale_sdk_v1.models.simulation.field_change_target_calculation_type",
        "FieldChangeTargetCalculationType",
    ),
    "FieldLimits": ("simscale_sdk_v1.models.simulation.field_limits", "FieldLimits"),
    "FirstMode": ("simscale_sdk_v1.models.simulation.first_mode", "FirstMode"),
    "FirstOrderOgden": ("simscale_sdk_v1.models.simulation.first_order_ogden", "FirstOrderOgden"),
    "FirstOrderUpwindSpatialScheme": (
        "simscale_sdk_v1.models.simulation.first_order_upwind_spatial_scheme",
        "FirstOrderUpwindSpatialScheme",
    ),
    "FixedAugmentation": ("simscale_sdk_v1.models.simulation.fixed_augmentation", "FixedAugmentation"),
    "FixedCoeffMedium": ("simscale_sdk_v1.models.simulation.fixed_coeff_medium", "FixedCoeffMedium"),
    "FixedElectricPotentialEBC": (
        "simscale_sdk_v1.models.simulation.fixed_electric_potential_ebc",
        "FixedElectricPotentialEBC",
    ),
    "FixedFluxPBC": ("simscale_sdk_v1.models.simulation.fixed_flux_pbc", "FixedFluxPBC"),
    "FixedGradientDVBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_dvbc", "FixedGradientDVBC"),
    "FixedGradientEBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_ebc", "FixedGradientEBC"),
    "FixedGradientEVBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_evbc", "FixedGradientEVBC"),
    "FixedGradientEVCBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_evcbc", "FixedGradientEVCBC"),
    "FixedGradientNBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_nbc", "FixedGradientNBC"),
    "FixedGradientOBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_obc", "FixedGradientOBC"),
    "FixedGradientPBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_pbc", "FixedGradientPBC"),
    "FixedGradientPFBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_pfbc", "FixedGradientPFBC"),
    "FixedGradientPSBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_psbc", "FixedGradientPSBC"),
    "FixedGradientTBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_tbc", "FixedGradientTBC"),
    "FixedGradientTDBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_tdbc", "FixedGradientTDBC"),
    "FixedGradientTDCBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_tdcbc", "FixedGradientTDCBC"),
    "FixedGradientTKEBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_tkebc", "FixedGradientTKEBC"),
    "FixedGradientVBC": ("simscale_sdk_v1.models.simulation.fixed_gradient_vbc", "FixedGradientVBC"),
    "FixedHeatFlux": ("simscale_sdk_v1.models.simulation.fixed_heat_flux", "FixedHeatFlux"),
    "FixedMagnitudeVBC": ("simscale_sdk_v1.models.simulation.fixed_magnitude_vbc", "FixedMagnitudeVBC"),
    "FixedPointContactNonLinearityResolution": (
        "simscale_sdk_v1.models.simulation.fixed_point_contact_non_linearity_resolution",
        "FixedPointContactNonLinearityResolution",
    ),
    "FixedPointFrictionNonLinearityResolution": (
        "simscale_sdk_v1.models.simulation.fixed_point_friction_non_linearity_resolution",
        "FixedPointFrictionNonLinearityResolution",
    ),
    "FixedPointNonLinearityResolution": (
        "simscale_sdk_v1.models.simulation.fixed_point_non_linearity_resolution",
        "FixedPointNonLinearityResolution",
    ),
    "FixedPotential": ("simscale_sdk_v1.models.simulation.fixed_potential", "FixedPotential"),
    "FixedPowerHeatFlux": ("simscale_sdk_v1.models.simulation.fixed_power_heat_flux", "FixedPowerHeatFlux"),
    "FixedSubdivision": ("simscale_sdk_v1.models.simulation.fixed_subdivision", "FixedSubdivision"),
    "FixedSupportBC": ("simscale_sdk_v1.models.simulation.fixed_support_bc", "FixedSupportBC"),
    "FixedTemperature": ("simscale_sdk_v1.models.simulation.fixed_temperature", "FixedTemperature"),
    "FixedTemperatureHeatTransferCoefficientResultType": (
        "simscale_sdk_v1.models.simulation.fixed_temperature_heat_transfer_coefficient_result_type",
        "FixedTemperatureHeatTransferCoefficientResultType",
    ),
    "FixedTemperatureValueBC": (
        "simscale_sdk_v1.models.simulation.fixed_temperature_value_bc",
        "FixedTemperatureValueBC",
    ),
    "FixedValueBC": ("simscale_sdk_v1.models.simulation.fixed_value_bc", "FixedValueBC"),
    "FixedValueBCMarc": ("simscale_sdk_v1.models.simulation.fixed_value_bc_marc", "FixedValueBCMarc"),
    "FixedValueDVBC": ("simscale_sdk_v1.models.simulation.fixed_value_dvbc", "FixedValueDVBC"),
    "FixedValueEBC": ("simscale_sdk_v1.models.simulation.fixed_value_ebc", "FixedValueEBC"),
    "FixedValueEVBC": ("simscale_sdk_v1.models.simulation.fixed_value_evbc", "FixedValueEVBC"),
    "FixedValueEVCBC": ("simscale_sdk_v1.models.simulation.fixed_value_evcbc", "FixedValueEVCBC"),
    "FixedValueMassFractionBC": (
        "simscale_sdk_v1.models.simulation.fixed_value_mass_fraction_bc",
        "FixedValueMassFractionBC",
    ),
    "FixedValueNBC": ("simscale_sdk_v1.models.simulation.fixed_value_nbc", "FixedValueNBC"),
    "FixedValueOBC": ("simscale_sdk_v1.models.simulation.fixed_value_obc", "FixedValueOBC"),
    "FixedValuePBC": ("simscale_sdk_v1.models.simulation.fixed_value_pbc", "FixedValuePBC"),
    "FixedValuePFBC": ("simscale_sdk_v1.models.simulation.fixed_value_pfbc", "FixedValuePFBC"),
    "FixedValuePSBC": ("simscale_sdk_v1.models.simulation.fixed_value_psbc", "FixedValuePSBC"),
    "FixedValuePhaseFractionBC": (
        "simscale_sdk_v1.models.simulation.fixed_value_phase_fraction_bc",
        "FixedValuePhaseFractionBC",
    ),
    "FixedValueRHBC": ("simscale_sdk_v1.models.simulation.fixed_value_rhbc", "FixedValueRHBC"),
    "FixedValueTBC": ("simscale_sdk_v1.models.simulation.fixed_value_tbc", "FixedValueTBC"),
    "FixedValueTDBC": ("simscale_sdk_v1.models.simulation.fixed_value_tdbc", "FixedValueTDBC"),
    "FixedValueTDCBC": ("simscale_sdk_v1.models.simulation.fixed_value_tdcbc", "FixedValueTDCBC"),
    "FixedValueTKEBC": ("simscale_sdk_v1.models.simulation.fixed_value_tkebc", "FixedValueTKEBC"),
    "FixedValueTurbulence": ("simscale_sdk_v1.models.simulation.fixed_value_turbulence", "FixedValueTurbulence"),
    "FixedValueVBC": ("simscale_sdk_v1.models.simulation.fixed_value_vbc", "FixedValueVBC"),
    "FlexibleAxialTranslation": (
        "simscale_sdk_v1.models.simulation.flexible_axial_translation",
        "FlexibleAxialTranslation",
    ),
    "FloatingPotential": ("simscale_sdk_v1.models.simulation.floating_potential", "FloatingPotential"),
    "FlowDependentValuePFBC": ("simscale_sdk_v1.models.simulation.flow_dependent_value_pfbc", "FlowDependentValuePFBC"),
    "FlowDomainBoundaries": ("simscale_sdk_v1.models.simulation.flow_domain_boundaries", "FlowDomainBoundaries"),
    "FlowRateInletVBC": ("simscale_sdk_v1.models.simulation.flow_rate_inlet_vbc", "FlowRateInletVBC"),
    "FlowRateMeanInletVBC": ("simscale_sdk_v1.models.simulation.flow_rate_mean_inlet_vbc", "FlowRateMeanInletVBC"),
    "FlowRateMeanOutletVBC": ("simscale_sdk_v1.models.simulation.flow_rate_mean_outlet_vbc", "FlowRateMeanOutletVBC"),
    "FlowRateOutletVBC": ("simscale_sdk_v1.models.simulation.flow_rate_outlet_vbc", "FlowRateOutletVBC"),
    "FlowRateStableOutletVBC": (
        "simscale_sdk_v1.models.simulation.flow_rate_stable_outlet_vbc",
        "FlowRateStableOutletVBC",
    ),
    "FluidCompressibleMaterial": (
        "simscale_sdk_v1.models.simulation.fluid_compressible_material",
        "FluidCompressibleMaterial",
    ),
    "FluidInitialConditions": ("simscale_sdk_v1.models.simulation.fluid_initial_conditions", "FluidInitialConditions"),
    "FluidInterface": ("simscale_sdk_v1.models.simulation.fluid_interface", "FluidInterface"),
    "FluidModel": ("simscale_sdk_v1.models.simulation.fluid_model", "FluidModel"),
    "FluidNumerics": ("simscale_sdk_v1.models.simulation.fluid_numerics", "FluidNumerics"),
    "FluidOnlyHeatTransfer": ("simscale_sdk_v1.models.simulation.fluid_only_heat_transfer", "FluidOnlyHeatTransfer"),
    "FluidResultControls": ("simscale_sdk_v1.models.simulation.fluid_result_controls", "FluidResultControls"),
    "FluidSimulationControl": ("simscale_sdk_v1.models.simulation.fluid_simulation_control", "FluidSimulationControl"),
    "FluidSolvers": ("simscale_sdk_v1.models.simulation.fluid_solvers", "FluidSolvers"),
    "FluidTypeGas": ("simscale_sdk_v1.models.simulation.fluid_type_gas", "FluidTypeGas"),
    "FluidTypeLiquid": ("simscale_sdk_v1.models.simulation.fluid_type_liquid", "FluidTypeLiquid"),
    "FluxHeatSource": ("simscale_sdk_v1.models.simulation.flux_heat_source", "FluxHeatSource"),
    "FluxSchemes": ("simscale_sdk_v1.models.simulation.flux_schemes", "FluxSchemes"),
    "FollowerPressureBC": ("simscale_sdk_v1.models.simulation.follower_pressure_bc", "FollowerPressureBC"),
    "ForceAndTorque": ("simscale_sdk_v1.models.simulation.force_and_torque", "ForceAndTorque"),
    "ForceFieldSelection": ("simscale_sdk_v1.models.simulation.force_field_selection", "ForceFieldSelection"),
    "ForceLoadBC": ("simscale_sdk_v1.models.simulation.force_load_bc", "ForceLoadBC"),
    "ForceMomentCoefficientsResultControl": (
        "simscale_sdk_v1.models.simulation.force_moment_coefficients_result_control",
        "ForceMomentCoefficientsResultControl",
    ),
    "ForcePreload": ("simscale_sdk_v1.models.simulation.force_preload", "ForcePreload"),
    "ForceResultControlItem": ("simscale_sdk_v1.models.simulation.force_result_control_item", "ForceResultControlItem"),
    "ForcesMomentsResultControl": (
        "simscale_sdk_v1.models.simulation.forces_moments_result_control",
        "ForcesMomentsResultControl",
    ),
    "FourthGradientScheme": ("simscale_sdk_v1.models.simulation.fourth_gradient_scheme", "FourthGradientScheme"),
    "FractionValueInitialCondition": (
        "simscale_sdk_v1.models.simulation.fraction_value_initial_condition",
        "FractionValueInitialCondition",
    ),
    "FractionValuesInitialConditions": (
        "simscale_sdk_v1.models.simulation.fraction_values_initial_conditions",
        "FractionValuesInitialConditions",
    ),
    "FreeAxialRotation": ("simscale_sdk_v1.models.simulation.free_axial_rotation", "FreeAxialRotation"),
    "FreeAxialTranslation": ("simscale_sdk_v1.models.simulation.free_axial_translation", "FreeAxialTranslation"),
    "FreestreamPBC": ("simscale_sdk_v1.models.simulation.freestream_pbc", "FreestreamPBC"),
    "FreestreamVBC": ("simscale_sdk_v1.models.simulation.freestream_vbc", "FreestreamVBC"),
    "FrequencyAnalysis": ("simscale_sdk_v1.models.simulation.frequency_analysis", "FrequencyAnalysis"),
    "FrequencyList": ("simscale_sdk_v1.models.simulation.frequency_list", "FrequencyList"),
    "FrequencyRange": ("simscale_sdk_v1.models.simulation.frequency_range", "FrequencyRange"),
    "FrictionAugmentedLagrangeCoef": (
        "simscale_sdk_v1.models.simulation.friction_augmented_lagrange_coef",
        "FrictionAugmentedLagrangeCoef",
    ),
    "FrictionContact": ("simscale_sdk_v1.models.simulation.friction_contact", "FrictionContact"),
    "FrictionPenaltyCoef": ("simscale_sdk_v1.models.simulation.friction_penalty_coef", "FrictionPenaltyCoef"),
    "FrictionVelocityMomentumSource": (
        "simscale_sdk_v1.models.simulation.friction_velocity_momentum_source",
        "FrictionVelocityMomentumSource",
    ),
    "FrictionVelocityResultType": (
        "simscale_sdk_v1.models.simulation.friction_velocity_result_type",
        "FrictionVelocityResultType",
    ),
    "FrictionlessContact": ("simscale_sdk_v1.models.simulation.frictionless_contact", "FrictionlessContact"),
    "FullRankAcceleration": ("simscale_sdk_v1.models.simulation.full_rank_acceleration", "FullRankAcceleration"),
    "FullResolutionDVBC": ("simscale_sdk_v1.models.simulation.full_resolution_dvbc", "FullResolutionDVBC"),
    "FullResolutionEBC": ("simscale_sdk_v1.models.simulation.full_resolution_ebc", "FullResolutionEBC"),
    "FullResolutionEVBC": ("simscale_sdk_v1.models.simulation.full_resolution_evbc", "FullResolutionEVBC"),
    "FullResolutionEVCBC": ("simscale_sdk_v1.models.simulation.full_resolution_evcbc", "FullResolutionEVCBC"),
    "FullResolutionNBC": ("simscale_sdk_v1.models.simulation.full_resolution_nbc", "FullResolutionNBC"),
    "FullResolutionOBC": ("simscale_sdk_v1.models.simulation.full_resolution_obc", "FullResolutionOBC"),
    "FullResolutionTDBC": ("simscale_sdk_v1.models.simulation.full_resolution_tdbc", "FullResolutionTDBC"),
    "FullResolutionTDCBC": ("simscale_sdk_v1.models.simulation.full_resolution_tdcbc", "FullResolutionTDCBC"),
    "FullResolutionTKEBC": ("simscale_sdk_v1.models.simulation.full_resolution_tkebc", "FullResolutionTKEBC"),
    "FunctionParameter": ("simscale_sdk_v1.models.simulation.function_parameter", "FunctionParameter"),
    "GAMGSolver": ("simscale_sdk_v1.models.simulation.gamg_solver", "GAMGSolver"),
    "GaussInterfaceCompressionDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_interface_compression_divergence_scheme",
        "GaussInterfaceCompressionDivergenceScheme",
    ),
    "GaussLimitedLinear1DivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_limited_linear1_divergence_scheme",
        "GaussLimitedLinear1DivergenceScheme",
    ),
    "GaussLimitedLinearV1DivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_limited_linear_v1_divergence_scheme",
        "GaussLimitedLinearV1DivergenceScheme",
    ),
    "GaussLinearCorrectedLaplacianScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_corrected_laplacian_scheme",
        "GaussLinearCorrectedLaplacianScheme",
    ),
    "GaussLinearDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_divergence_scheme",
        "GaussLinearDivergenceScheme",
    ),
    "GaussLinearGradientScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_gradient_scheme",
        "GaussLinearGradientScheme",
    ),
    "GaussLinearLimitedCorrectedLaplacianScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_limited_corrected_laplacian_scheme",
        "GaussLinearLimitedCorrectedLaplacianScheme",
    ),
    "GaussLinearUncorrectedLaplacianScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_uncorrected_laplacian_scheme",
        "GaussLinearUncorrectedLaplacianScheme",
    ),
    "GaussLinearUpwindLimitedGradDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_upwind_limited_grad_divergence_scheme",
        "GaussLinearUpwindLimitedGradDivergenceScheme",
    ),
    "GaussLinearUpwindUnlimitedDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_upwind_unlimited_divergence_scheme",
        "GaussLinearUpwindUnlimitedDivergenceScheme",
    ),
    "GaussLinearUpwindVGradUDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_upwind_v_grad_u_divergence_scheme",
        "GaussLinearUpwindVGradUDivergenceScheme",
    ),
    "GaussLinearUpwindVUnlimitedDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_linear_upwind_v_unlimited_divergence_scheme",
        "GaussLinearUpwindVUnlimitedDivergenceScheme",
    ),
    "GaussUpwindDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_upwind_divergence_scheme",
        "GaussUpwindDivergenceScheme",
    ),
    "GaussVanleerDivergenceScheme": (
        "simscale_sdk_v1.models.simulation.gauss_vanleer_divergence_scheme",
        "GaussVanleerDivergenceScheme",
    ),
    "GeneralDarcyForchheimerPacefish": (
        "simscale_sdk_v1.models.simulation.general_darcy_forchheimer_pacefish",
        "GeneralDarcyForchheimerPacefish",
    ),
    "GeneralHoleShape": ("simscale_sdk_v1.models.simulation.general_hole_shape", "GeneralHoleShape"),
    "GeographicalLocation": ("simscale_sdk_v1.models.simulation.geographical_location", "GeographicalLocation"),
    "GlobalAccelerationType": ("simscale_sdk_v1.models.simulation.global_acceleration_type", "GlobalAccelerationType"),
    "GlobalCartesianMagnetizationDirectionMethod": (
        "simscale_sdk_v1.models.simulation.global_cartesian_magnetization_direction_method",
        "GlobalCartesianMagnetizationDirectionMethod",
    ),
    "GlobalCauchyStressType": ("simscale_sdk_v1.models.simulation.global_cauchy_stress_type", "GlobalCauchyStressType"),
    "GlobalDampingValue": ("simscale_sdk_v1.models.simulation.global_damping_value", "GlobalDampingValue"),
    "GlobalDisplacement": ("simscale_sdk_v1.models.simulation.global_displacement", "GlobalDisplacement"),
    "GlobalDisplacementType": ("simscale_sdk_v1.models.simulation.global_displacement_type", "GlobalDisplacementType"),
    "GlobalMaxOverPhaseVonMisesStressType": (
        "simscale_sdk_v1.models.simulation.global_max_over_phase_von_mises_stress_type",
        "GlobalMaxOverPhaseVonMisesStressType",
    ),
    "GlobalNodalForceType": ("simscale_sdk_v1.models.simulation.global_nodal_force_type", "GlobalNodalForceType"),
    "GlobalPrincipalGreenLagrangeStrainType": (
        "simscale_sdk_v1.models.simulation.global_principal_green_lagrange_strain_type",
        "GlobalPrincipalGreenLagrangeStrainType",
    ),
    "GlobalPrincipalStrainType": (
        "simscale_sdk_v1.models.simulation.global_principal_strain_type",
        "GlobalPrincipalStrainType",
    ),
    "GlobalPrincipalStressType": (
        "simscale_sdk_v1.models.simulation.global_principal_stress_type",
        "GlobalPrincipalStressType",
    ),
    "GlobalReactionForceType": (
        "simscale_sdk_v1.models.simulation.global_reaction_force_type",
        "GlobalReactionForceType",
    ),
    "GlobalSignedVonMisesStressType": (
        "simscale_sdk_v1.models.simulation.global_signed_von_mises_stress_type",
        "GlobalSignedVonMisesStressType",
    ),
    "GlobalTotalEquivalentPlasticStrainType": (
        "simscale_sdk_v1.models.simulation.global_total_equivalent_plastic_strain_type",
        "GlobalTotalEquivalentPlasticStrainType",
    ),
    "GlobalTotalNonlinearStrainType": (
        "simscale_sdk_v1.models.simulation.global_total_nonlinear_strain_type",
        "GlobalTotalNonlinearStrainType",
    ),
    "GlobalTotalStrainType": ("simscale_sdk_v1.models.simulation.global_total_strain_type", "GlobalTotalStrainType"),
    "GlobalTrescaStressType": ("simscale_sdk_v1.models.simulation.global_tresca_stress_type", "GlobalTrescaStressType"),
    "GlobalUnelasticStrainType": (
        "simscale_sdk_v1.models.simulation.global_unelastic_strain_type",
        "GlobalUnelasticStrainType",
    ),
    "GlobalVelocityType": ("simscale_sdk_v1.models.simulation.global_velocity_type", "GlobalVelocityType"),
    "GlobalVonMisesStressType": (
        "simscale_sdk_v1.models.simulation.global_von_mises_stress_type",
        "GlobalVonMisesStressType",
    ),
    "GradientSchemes": ("simscale_sdk_v1.models.simulation.gradient_schemes", "GradientSchemes"),
    "GreybodyDiffusiveRSBC": ("simscale_sdk_v1.models.simulation.greybody_diffusive_rsbc", "GreybodyDiffusiveRSBC"),
    "GreybodyDiffusiveRayBC": ("simscale_sdk_v1.models.simulation.greybody_diffusive_ray_bc", "GreybodyDiffusiveRayBC"),
    "GroundAbsolute": ("simscale_sdk_v1.models.simulation.ground_absolute", "GroundAbsolute"),
    "GroundRelative": ("simscale_sdk_v1.models.simulation.ground_relative", "GroundRelative"),
    "HConstThermo": ("simscale_sdk_v1.models.simulation.h_const_thermo", "HConstThermo"),
    "HarmonicAccelerationResultControlItem": (
        "simscale_sdk_v1.models.simulation.harmonic_acceleration_result_control_item",
        "HarmonicAccelerationResultControlItem",
    ),
    "HarmonicAnalysis": ("simscale_sdk_v1.models.simulation.harmonic_analysis", "HarmonicAnalysis"),
    "HarmonicDisplacementResultControlItem": (
        "simscale_sdk_v1.models.simulation.harmonic_displacement_result_control_item",
        "HarmonicDisplacementResultControlItem",
    ),
    "HarmonicResponse": ("simscale_sdk_v1.models.simulation.harmonic_response", "HarmonicResponse"),
    "HarmonicResponseControl": (
        "simscale_sdk_v1.models.simulation.harmonic_response_control",
        "HarmonicResponseControl",
    ),
    "HarmonicResponseResultControlItem": (
        "simscale_sdk_v1.models.simulation.harmonic_response_result_control_item",
        "HarmonicResponseResultControlItem",
    ),
    "HarmonicVelocityResultControlItem": (
        "simscale_sdk_v1.models.simulation.harmonic_velocity_result_control_item",
        "HarmonicVelocityResultControlItem",
    ),
    "HeatExchangerPerformance": (
        "simscale_sdk_v1.models.simulation.heat_exchanger_performance",
        "HeatExchangerPerformance",
    ),
    "HeatExchangerSource": ("simscale_sdk_v1.models.simulation.heat_exchanger_source", "HeatExchangerSource"),
    "HeatFlowCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.heat_flow_calculation_result_control_item",
        "HeatFlowCalculationResultControlItem",
    ),
    "HeatFluxFieldSelection": ("simscale_sdk_v1.models.simulation.heat_flux_field_selection", "HeatFluxFieldSelection"),
    "HeatFluxResultControlItem": (
        "simscale_sdk_v1.models.simulation.heat_flux_result_control_item",
        "HeatFluxResultControlItem",
    ),
    "HeatTransfer": ("simscale_sdk_v1.models.simulation.heat_transfer", "HeatTransfer"),
    "HeatTransferCoefficients": (
        "simscale_sdk_v1.models.simulation.heat_transfer_coefficients",
        "HeatTransferCoefficients",
    ),
    "HerschelBulkleyTransport": (
        "simscale_sdk_v1.models.simulation.herschel_bulkley_transport",
        "HerschelBulkleyTransport",
    ),
    "HerschelBulkleyViscosityModel": (
        "simscale_sdk_v1.models.simulation.herschel_bulkley_viscosity_model",
        "HerschelBulkleyViscosityModel",
    ),
    "HhtTimeIntegrationScheme": (
        "simscale_sdk_v1.models.simulation.hht_time_integration_scheme",
        "HhtTimeIntegrationScheme",
    ),
    "HierarchicalDecomposeAlgorithm": (
        "simscale_sdk_v1.models.simulation.hierarchical_decompose_algorithm",
        "HierarchicalDecomposeAlgorithm",
    ),
    "HighContactStiffness": ("simscale_sdk_v1.models.simulation.high_contact_stiffness", "HighContactStiffness"),
    "HighResolution": ("simscale_sdk_v1.models.simulation.high_resolution", "HighResolution"),
    "HighResolutionSpatialScheme": (
        "simscale_sdk_v1.models.simulation.high_resolution_spatial_scheme",
        "HighResolutionSpatialScheme",
    ),
    "HingeConstraintBC": ("simscale_sdk_v1.models.simulation.hinge_constraint_bc", "HingeConstraintBC"),
    "HomogeneousMaterialStructure": (
        "simscale_sdk_v1.models.simulation.homogeneous_material_structure",
        "HomogeneousMaterialStructure",
    ),
    "HydrostaticFanPBC": ("simscale_sdk_v1.models.simulation.hydrostatic_fan_pbc", "HydrostaticFanPBC"),
    "HydrostaticIsothermalFreestreamPBC": (
        "simscale_sdk_v1.models.simulation.hydrostatic_isothermal_freestream_pbc",
        "HydrostaticIsothermalFreestreamPBC",
    ),
    "HydrostaticIsothermalPBC": (
        "simscale_sdk_v1.models.simulation.hydrostatic_isothermal_pbc",
        "HydrostaticIsothermalPBC",
    ),
    "HydrostaticIsothermalTotalPBC": (
        "simscale_sdk_v1.models.simulation.hydrostatic_isothermal_total_pbc",
        "HydrostaticIsothermalTotalPBC",
    ),
    "HydrostaticPressure": ("simscale_sdk_v1.models.simulation.hydrostatic_pressure", "HydrostaticPressure"),
    "HyperElasticMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.hyper_elastic_material_behavior",
        "HyperElasticMaterialBehavior",
    ),
    "HyperelasticMarcMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.hyperelastic_marc_material_behavior",
        "HyperelasticMarcMaterialBehavior",
    ),
    "Hyperelasticity": ("simscale_sdk_v1.models.simulation.hyperelasticity", "Hyperelasticity"),
    "HystereticDamping": ("simscale_sdk_v1.models.simulation.hysteretic_damping", "HystereticDamping"),
    "ILUCpPreconditioner": ("simscale_sdk_v1.models.simulation.ilu_cp_preconditioner", "ILUCpPreconditioner"),
    "IRAMSorensen": ("simscale_sdk_v1.models.simulation.iram_sorensen", "IRAMSorensen"),
    "ImplicitTimeIntegrationType": (
        "simscale_sdk_v1.models.simulation.implicit_time_integration_type",
        "ImplicitTimeIntegrationType",
    ),
    "InactiveAdjustableTimestep": (
        "simscale_sdk_v1.models.simulation.inactive_adjustable_timestep",
        "InactiveAdjustableTimestep",
    ),
    "InactivePreconditioner": ("simscale_sdk_v1.models.simulation.inactive_preconditioner", "InactivePreconditioner"),
    "IncompletePreconditionerV33": (
        "simscale_sdk_v1.models.simulation.incomplete_preconditioner_v33",
        "IncompletePreconditionerV33",
    ),
    "Incompressible": ("simscale_sdk_v1.models.simulation.incompressible", "Incompressible"),
    "IncompressibleFluidMaterials": (
        "simscale_sdk_v1.models.simulation.incompressible_fluid_materials",
        "IncompressibleFluidMaterials",
    ),
    "IncompressibleMaterial": ("simscale_sdk_v1.models.simulation.incompressible_material", "IncompressibleMaterial"),
    "IncompressiblePacefish": ("simscale_sdk_v1.models.simulation.incompressible_pacefish", "IncompressiblePacefish"),
    "IncompressiblePerfectGasEquationOfState": (
        "simscale_sdk_v1.models.simulation.incompressible_perfect_gas_equation_of_state",
        "IncompressiblePerfectGasEquationOfState",
    ),
    "InitialTimestepsWriteControl": (
        "simscale_sdk_v1.models.simulation.initial_timesteps_write_control",
        "InitialTimestepsWriteControl",
    ),
    "InletFixedMFValues": ("simscale_sdk_v1.models.simulation.inlet_fixed_mf_values", "InletFixedMFValues"),
    "InletFixedPFValues": ("simscale_sdk_v1.models.simulation.inlet_fixed_pf_values", "InletFixedPFValues"),
    "InletOutletDVBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_dvbc", "InletOutletDVBC"),
    "InletOutletEBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_ebc", "InletOutletEBC"),
    "InletOutletEVBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_evbc", "InletOutletEVBC"),
    "InletOutletEVCBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_evcbc", "InletOutletEVCBC"),
    "InletOutletNBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_nbc", "InletOutletNBC"),
    "InletOutletOBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_obc", "InletOutletOBC"),
    "InletOutletPFBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_pfbc", "InletOutletPFBC"),
    "InletOutletPSBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_psbc", "InletOutletPSBC"),
    "InletOutletRHBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_rhbc", "InletOutletRHBC"),
    "InletOutletTBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_tbc", "InletOutletTBC"),
    "InletOutletTKEBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_tkebc", "InletOutletTKEBC"),
    "InletOutletVBC": ("simscale_sdk_v1.models.simulation.inlet_outlet_vbc", "InletOutletVBC"),
    "InsideRegionRefinementWithLength": (
        "simscale_sdk_v1.models.simulation.inside_region_refinement_with_length",
        "InsideRegionRefinementWithLength",
    ),
    "IntensityKineticEnergyInletTKEBC": (
        "simscale_sdk_v1.models.simulation.intensity_kinetic_energy_inlet_tkebc",
        "IntensityKineticEnergyInletTKEBC",
    ),
    "InterferenceFit": ("simscale_sdk_v1.models.simulation.interference_fit", "InterferenceFit"),
    "InternVariablesField": ("simscale_sdk_v1.models.simulation.intern_variables_field", "InternVariablesField"),
    "InterpolationParameter": ("simscale_sdk_v1.models.simulation.interpolation_parameter", "InterpolationParameter"),
    "InterpolationSchemes": ("simscale_sdk_v1.models.simulation.interpolation_schemes", "InterpolationSchemes"),
    "IsotropicConductivity": ("simscale_sdk_v1.models.simulation.isotropic_conductivity", "IsotropicConductivity"),
    "IsotropicDarcyForchheimer": (
        "simscale_sdk_v1.models.simulation.isotropic_darcy_forchheimer",
        "IsotropicDarcyForchheimer",
    ),
    "IsotropicDensityMethod": ("simscale_sdk_v1.models.simulation.isotropic_density_method", "IsotropicDensityMethod"),
    "IsotropicDielectricStrength": (
        "simscale_sdk_v1.models.simulation.isotropic_dielectric_strength",
        "IsotropicDielectricStrength",
    ),
    "IsotropicDirectionalDependency": (
        "simscale_sdk_v1.models.simulation.isotropic_directional_dependency",
        "IsotropicDirectionalDependency",
    ),
    "IsotropicElectricConductivity": (
        "simscale_sdk_v1.models.simulation.isotropic_electric_conductivity",
        "IsotropicElectricConductivity",
    ),
    "IsotropicElectricConductivityMethod": (
        "simscale_sdk_v1.models.simulation.isotropic_electric_conductivity_method",
        "IsotropicElectricConductivityMethod",
    ),
    "IsotropicExpansion": ("simscale_sdk_v1.models.simulation.isotropic_expansion", "IsotropicExpansion"),
    "IsotropicLossTangent": ("simscale_sdk_v1.models.simulation.isotropic_loss_tangent", "IsotropicLossTangent"),
    "IsotropicPlasticHardening": (
        "simscale_sdk_v1.models.simulation.isotropic_plastic_hardening",
        "IsotropicPlasticHardening",
    ),
    "IsotropicPlasticHardeningMarc": (
        "simscale_sdk_v1.models.simulation.isotropic_plastic_hardening_marc",
        "IsotropicPlasticHardeningMarc",
    ),
    "IsotropicRelativePermeabilityMethod": (
        "simscale_sdk_v1.models.simulation.isotropic_relative_permeability_method",
        "IsotropicRelativePermeabilityMethod",
    ),
    "IsotropicSpecificHeatMethod": (
        "simscale_sdk_v1.models.simulation.isotropic_specific_heat_method",
        "IsotropicSpecificHeatMethod",
    ),
    "IsotropicSpringStiffness": (
        "simscale_sdk_v1.models.simulation.isotropic_spring_stiffness",
        "IsotropicSpringStiffness",
    ),
    "IsotropicThermalConductivityMethod": (
        "simscale_sdk_v1.models.simulation.isotropic_thermal_conductivity_method",
        "IsotropicThermalConductivityMethod",
    ),
    "JacobiPreconditioner": ("simscale_sdk_v1.models.simulation.jacobi_preconditioner", "JacobiPreconditioner"),
    "JohnsonCookElastoPlasticModel": (
        "simscale_sdk_v1.models.simulation.johnson_cook_elasto_plastic_model",
        "JohnsonCookElastoPlasticModel",
    ),
    "KinematicPlasticHardeningMarc": (
        "simscale_sdk_v1.models.simulation.kinematic_plastic_hardening_marc",
        "KinematicPlasticHardeningMarc",
    ),
    "KurganovFluxScheme": ("simscale_sdk_v1.models.simulation.kurganov_flux_scheme", "KurganovFluxScheme"),
    "Lanczos": ("simscale_sdk_v1.models.simulation.lanczos", "Lanczos"),
    "LaplacianSchemes": ("simscale_sdk_v1.models.simulation.laplacian_schemes", "LaplacianSchemes"),
    "LayerWallThermal": ("simscale_sdk_v1.models.simulation.layer_wall_thermal", "LayerWallThermal"),
    "LeastsquaresGradientScheme": (
        "simscale_sdk_v1.models.simulation.leastsquares_gradient_scheme",
        "LeastsquaresGradientScheme",
    ),
    "LimitedSurfaceNormalGradientScheme": (
        "simscale_sdk_v1.models.simulation.limited_surface_normal_gradient_scheme",
        "LimitedSurfaceNormalGradientScheme",
    ),
    "LinearElasticMarcMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.linear_elastic_marc_material_behavior",
        "LinearElasticMarcMaterialBehavior",
    ),
    "LinearElasticMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.linear_elastic_material_behavior",
        "LinearElasticMaterialBehavior",
    ),
    "LinearInterpolationScheme": (
        "simscale_sdk_v1.models.simulation.linear_interpolation_scheme",
        "LinearInterpolationScheme",
    ),
    "LinearIsotropicPermittivityMethod": (
        "simscale_sdk_v1.models.simulation.linear_isotropic_permittivity_method",
        "LinearIsotropicPermittivityMethod",
    ),
    "LinearSBM": ("simscale_sdk_v1.models.simulation.linear_sbm", "LinearSBM"),
    "LitzWireCoil": ("simscale_sdk_v1.models.simulation.litz_wire_coil", "LitzWireCoil"),
    "LoadStep": ("simscale_sdk_v1.models.simulation.load_step", "LoadStep"),
    "LocalElementSizeEBM": ("simscale_sdk_v1.models.simulation.local_element_size_ebm", "LocalElementSizeEBM"),
    "LocalEulerTimeDifferentiationScheme": (
        "simscale_sdk_v1.models.simulation.local_euler_time_differentiation_scheme",
        "LocalEulerTimeDifferentiationScheme",
    ),
    "LowContactStiffness": ("simscale_sdk_v1.models.simulation.low_contact_stiffness", "LowContactStiffness"),
    "LowRankAcceleration": ("simscale_sdk_v1.models.simulation.low_rank_acceleration", "LowRankAcceleration"),
    "MRFRotatingZone": ("simscale_sdk_v1.models.simulation.mrf_rotating_zone", "MRFRotatingZone"),
    "MULESSolver": ("simscale_sdk_v1.models.simulation.mules_solver", "MULESSolver"),
    "MUMPSPreconditoner": ("simscale_sdk_v1.models.simulation.mumps_preconditoner", "MUMPSPreconditoner"),
    "MUMPSSolver": ("simscale_sdk_v1.models.simulation.mumps_solver", "MUMPSSolver"),
    "MagneticFieldFieldSelection": (
        "simscale_sdk_v1.models.simulation.magnetic_field_field_selection",
        "MagneticFieldFieldSelection",
    ),
    "MagneticFieldNormal": ("simscale_sdk_v1.models.simulation.magnetic_field_normal", "MagneticFieldNormal"),
    "MagneticFluxDensityFieldSelection": (
        "simscale_sdk_v1.models.simulation.magnetic_flux_density_field_selection",
        "MagneticFluxDensityFieldSelection",
    ),
    "MagneticFluxTangential": ("simscale_sdk_v1.models.simulation.magnetic_flux_tangential", "MagneticFluxTangential"),
    "Magnetostatics": ("simscale_sdk_v1.models.simulation.magnetostatics", "Magnetostatics"),
    "ManualEmbeddedBoundaryMeshSizing": (
        "simscale_sdk_v1.models.simulation.manual_embedded_boundary_mesh_sizing",
        "ManualEmbeddedBoundaryMeshSizing",
    ),
    "ManualReactualization": ("simscale_sdk_v1.models.simulation.manual_reactualization", "ManualReactualization"),
    "ManualReferenceLength": ("simscale_sdk_v1.models.simulation.manual_reference_length", "ManualReferenceLength"),
    "ManualRegionSizingPacefish": (
        "simscale_sdk_v1.models.simulation.manual_region_sizing_pacefish",
        "ManualRegionSizingPacefish",
    ),
    "ManualReynoldsScaling": ("simscale_sdk_v1.models.simulation.manual_reynolds_scaling", "ManualReynoldsScaling"),
    "ManualSimericsMeshSettings": (
        "simscale_sdk_v1.models.simulation.manual_simerics_mesh_settings",
        "ManualSimericsMeshSettings",
    ),
    "ManualSurfaceSizingPacefish": (
        "simscale_sdk_v1.models.simulation.manual_surface_sizing_pacefish",
        "ManualSurfaceSizingPacefish",
    ),
    "ManualTimeStepDefintion": (
        "simscale_sdk_v1.models.simulation.manual_time_step_defintion",
        "ManualTimeStepDefintion",
    ),
    "ManualTimestepCalculationType": (
        "simscale_sdk_v1.models.simulation.manual_timestep_calculation_type",
        "ManualTimestepCalculationType",
    ),
    "ManualTimestepDefinition": (
        "simscale_sdk_v1.models.simulation.manual_timestep_definition",
        "ManualTimestepDefinition",
    ),
    "MarcAnalysis": ("simscale_sdk_v1.models.simulation.marc_analysis", "MarcAnalysis"),
    "MarcAverageFieldsCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_average_fields_calculation_result_control_item",
        "MarcAverageFieldsCalculationResultControlItem",
    ),
    "MarcBondedAndTouchingContactConnection": (
        "simscale_sdk_v1.models.simulation.marc_bonded_and_touching_contact_connection",
        "MarcBondedAndTouchingContactConnection",
    ),
    "MarcBondedContactConnection": (
        "simscale_sdk_v1.models.simulation.marc_bonded_contact_connection",
        "MarcBondedContactConnection",
    ),
    "MarcCauchyStressType": ("simscale_sdk_v1.models.simulation.marc_cauchy_stress_type", "MarcCauchyStressType"),
    "MarcConnectionGroup": ("simscale_sdk_v1.models.simulation.marc_connection_group", "MarcConnectionGroup"),
    "MarcConnectorPointDataItem": (
        "simscale_sdk_v1.models.simulation.marc_connector_point_data_item",
        "MarcConnectorPointDataItem",
    ),
    "MarcContactBodyForceType": (
        "simscale_sdk_v1.models.simulation.marc_contact_body_force_type",
        "MarcContactBodyForceType",
    ),
    "MarcContactFieldSelection": (
        "simscale_sdk_v1.models.simulation.marc_contact_field_selection",
        "MarcContactFieldSelection",
    ),
    "MarcContactForceFieldSelection": (
        "simscale_sdk_v1.models.simulation.marc_contact_force_field_selection",
        "MarcContactForceFieldSelection",
    ),
    "MarcContactFrictionForce": (
        "simscale_sdk_v1.models.simulation.marc_contact_friction_force",
        "MarcContactFrictionForce",
    ),
    "MarcContactFrictionForceType": (
        "simscale_sdk_v1.models.simulation.marc_contact_friction_force_type",
        "MarcContactFrictionForceType",
    ),
    "MarcContactFrictionStress": (
        "simscale_sdk_v1.models.simulation.marc_contact_friction_stress",
        "MarcContactFrictionStress",
    ),
    "MarcContactFrictionStressType": (
        "simscale_sdk_v1.models.simulation.marc_contact_friction_stress_type",
        "MarcContactFrictionStressType",
    ),
    "MarcContactGap": ("simscale_sdk_v1.models.simulation.marc_contact_gap", "MarcContactGap"),
    "MarcContactGapType": ("simscale_sdk_v1.models.simulation.marc_contact_gap_type", "MarcContactGapType"),
    "MarcContactNormalForce": ("simscale_sdk_v1.models.simulation.marc_contact_normal_force", "MarcContactNormalForce"),
    "MarcContactNormalForceType": (
        "simscale_sdk_v1.models.simulation.marc_contact_normal_force_type",
        "MarcContactNormalForceType",
    ),
    "MarcContactNormalStress": (
        "simscale_sdk_v1.models.simulation.marc_contact_normal_stress",
        "MarcContactNormalStress",
    ),
    "MarcContactNormalStressType": (
        "simscale_sdk_v1.models.simulation.marc_contact_normal_stress_type",
        "MarcContactNormalStressType",
    ),
    "MarcContactPressure": ("simscale_sdk_v1.models.simulation.marc_contact_pressure", "MarcContactPressure"),
    "MarcContactPressureType": (
        "simscale_sdk_v1.models.simulation.marc_contact_pressure_type",
        "MarcContactPressureType",
    ),
    "MarcContactResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_contact_result_control_item",
        "MarcContactResultControlItem",
    ),
    "MarcContactStatus": ("simscale_sdk_v1.models.simulation.marc_contact_status", "MarcContactStatus"),
    "MarcContactStatusType": ("simscale_sdk_v1.models.simulation.marc_contact_status_type", "MarcContactStatusType"),
    "MarcDisplacementFieldSelection": (
        "simscale_sdk_v1.models.simulation.marc_displacement_field_selection",
        "MarcDisplacementFieldSelection",
    ),
    "MarcDisplacementResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_displacement_result_control_item",
        "MarcDisplacementResultControlItem",
    ),
    "MarcElasticStrainType": ("simscale_sdk_v1.models.simulation.marc_elastic_strain_type", "MarcElasticStrainType"),
    "MarcElementTechnology": ("simscale_sdk_v1.models.simulation.marc_element_technology", "MarcElementTechnology"),
    "MarcEquivalentElasticStrainType": (
        "simscale_sdk_v1.models.simulation.marc_equivalent_elastic_strain_type",
        "MarcEquivalentElasticStrainType",
    ),
    "MarcEquivalentPlasticStrainType": (
        "simscale_sdk_v1.models.simulation.marc_equivalent_plastic_strain_type",
        "MarcEquivalentPlasticStrainType",
    ),
    "MarcExternalForceType": ("simscale_sdk_v1.models.simulation.marc_external_force_type", "MarcExternalForceType"),
    "MarcExternalPressureType": (
        "simscale_sdk_v1.models.simulation.marc_external_pressure_type",
        "MarcExternalPressureType",
    ),
    "MarcForceFieldSelection": (
        "simscale_sdk_v1.models.simulation.marc_force_field_selection",
        "MarcForceFieldSelection",
    ),
    "MarcForceResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_force_result_control_item",
        "MarcForceResultControlItem",
    ),
    "MarcGlobalDisplacementFieldType": (
        "simscale_sdk_v1.models.simulation.marc_global_displacement_field_type",
        "MarcGlobalDisplacementFieldType",
    ),
    "MarcHeatFluxResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_heat_flux_result_control_item",
        "MarcHeatFluxResultControlItem",
    ),
    "MarcLinearSolverSettings": (
        "simscale_sdk_v1.models.simulation.marc_linear_solver_settings",
        "MarcLinearSolverSettings",
    ),
    "MarcMaterial": ("simscale_sdk_v1.models.simulation.marc_material", "MarcMaterial"),
    "MarcMinMaxFieldsCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_min_max_fields_calculation_result_control_item",
        "MarcMinMaxFieldsCalculationResultControlItem",
    ),
    "MarcNonlinearSolverSettings": (
        "simscale_sdk_v1.models.simulation.marc_nonlinear_solver_settings",
        "MarcNonlinearSolverSettings",
    ),
    "MarcNumerics": ("simscale_sdk_v1.models.simulation.marc_numerics", "MarcNumerics"),
    "MarcOutputWritingContainer": (
        "simscale_sdk_v1.models.simulation.marc_output_writing_container",
        "MarcOutputWritingContainer",
    ),
    "MarcPlasticStrainType": ("simscale_sdk_v1.models.simulation.marc_plastic_strain_type", "MarcPlasticStrainType"),
    "MarcPressureFieldSelection": (
        "simscale_sdk_v1.models.simulation.marc_pressure_field_selection",
        "MarcPressureFieldSelection",
    ),
    "MarcPressureResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_pressure_result_control_item",
        "MarcPressureResultControlItem",
    ),
    "MarcPrincipalElasticStrainType": (
        "simscale_sdk_v1.models.simulation.marc_principal_elastic_strain_type",
        "MarcPrincipalElasticStrainType",
    ),
    "MarcPrincipalPlasticStrainType": (
        "simscale_sdk_v1.models.simulation.marc_principal_plastic_strain_type",
        "MarcPrincipalPlasticStrainType",
    ),
    "MarcPrincipalStressType": (
        "simscale_sdk_v1.models.simulation.marc_principal_stress_type",
        "MarcPrincipalStressType",
    ),
    "MarcPrincipalTotalStrainType": (
        "simscale_sdk_v1.models.simulation.marc_principal_total_strain_type",
        "MarcPrincipalTotalStrainType",
    ),
    "MarcReactionForceType": ("simscale_sdk_v1.models.simulation.marc_reaction_force_type", "MarcReactionForceType"),
    "MarcResultControl": ("simscale_sdk_v1.models.simulation.marc_result_control", "MarcResultControl"),
    "MarcSimulationControl": ("simscale_sdk_v1.models.simulation.marc_simulation_control", "MarcSimulationControl"),
    "MarcStrainFieldSelection": (
        "simscale_sdk_v1.models.simulation.marc_strain_field_selection",
        "MarcStrainFieldSelection",
    ),
    "MarcStrainResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_strain_result_control_item",
        "MarcStrainResultControlItem",
    ),
    "MarcStressFieldSelection": (
        "simscale_sdk_v1.models.simulation.marc_stress_field_selection",
        "MarcStressFieldSelection",
    ),
    "MarcStressResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_stress_result_control_item",
        "MarcStressResultControlItem",
    ),
    "MarcSumFieldsCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_sum_fields_calculation_result_control_item",
        "MarcSumFieldsCalculationResultControlItem",
    ),
    "MarcTemperatureResultControlItem": (
        "simscale_sdk_v1.models.simulation.marc_temperature_result_control_item",
        "MarcTemperatureResultControlItem",
    ),
    "MarcTotalStrainType": ("simscale_sdk_v1.models.simulation.marc_total_strain_type", "MarcTotalStrainType"),
    "MarcTouchingContactConnection": (
        "simscale_sdk_v1.models.simulation.marc_touching_contact_connection",
        "MarcTouchingContactConnection",
    ),
    "MarcVonMisesStressType": (
        "simscale_sdk_v1.models.simulation.marc_von_mises_stress_type",
        "MarcVonMisesStressType",
    ),
    "MarlowHyperelasticModelMarc": (
        "simscale_sdk_v1.models.simulation.marlow_hyperelastic_model_marc",
        "MarlowHyperelasticModelMarc",
    ),
    "MassFlow": ("simscale_sdk_v1.models.simulation.mass_flow", "MassFlow"),
    "MaterialLibraryReference": (
        "simscale_sdk_v1.models.simulation.material_library_reference",
        "MaterialLibraryReference",
    ),
    "MaximumNumberIterationControl": (
        "simscale_sdk_v1.models.simulation.maximum_number_iteration_control",
        "MaximumNumberIterationControl",
    ),
    "MeanAgeOfFluidResultType": (
        "simscale_sdk_v1.models.simulation.mean_age_of_fluid_result_type",
        "MeanAgeOfFluidResultType",
    ),
    "MeanRadiantTemperatureResultType": (
        "simscale_sdk_v1.models.simulation.mean_radiant_temperature_result_type",
        "MeanRadiantTemperatureResultType",
    ),
    "MeanValueOutletVBC": ("simscale_sdk_v1.models.simulation.mean_value_outlet_vbc", "MeanValueOutletVBC"),
    "MeanValuePBC": ("simscale_sdk_v1.models.simulation.mean_value_pbc", "MeanValuePBC"),
    "MeanValueVBC": ("simscale_sdk_v1.models.simulation.mean_value_vbc", "MeanValueVBC"),
    "MinMaxFieldsCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.min_max_fields_calculation_result_control_item",
        "MinMaxFieldsCalculationResultControlItem",
    ),
    "MinimumGapSize": ("simscale_sdk_v1.models.simulation.minimum_gap_size", "MinimumGapSize"),
    "MixedTimestepCalculationType": (
        "simscale_sdk_v1.models.simulation.mixed_timestep_calculation_type",
        "MixedTimestepCalculationType",
    ),
    "MixingLengthInletEBC": ("simscale_sdk_v1.models.simulation.mixing_length_inlet_ebc", "MixingLengthInletEBC"),
    "ModalBaseControl": ("simscale_sdk_v1.models.simulation.modal_base_control", "ModalBaseControl"),
    "ModalSolver": ("simscale_sdk_v1.models.simulation.modal_solver", "ModalSolver"),
    "ModeledTurbulenceIntensity": (
        "simscale_sdk_v1.models.simulation.modeled_turbulence_intensity",
        "ModeledTurbulenceIntensity",
    ),
    "ModerateContactStiffness": (
        "simscale_sdk_v1.models.simulation.moderate_contact_stiffness",
        "ModerateContactStiffness",
    ),
    "ModerateResolution": ("simscale_sdk_v1.models.simulation.moderate_resolution", "ModerateResolution"),
    "MomentFieldSelection": ("simscale_sdk_v1.models.simulation.moment_field_selection", "MomentFieldSelection"),
    "MooneyRivlinHyperElasticModel": (
        "simscale_sdk_v1.models.simulation.mooney_rivlin_hyper_elastic_model",
        "MooneyRivlinHyperElasticModel",
    ),
    "MooneyTypeHyperelasticModelMarc": (
        "simscale_sdk_v1.models.simulation.mooney_type_hyperelastic_model_marc",
        "MooneyTypeHyperelasticModelMarc",
    ),
    "MovingWallVBC": ("simscale_sdk_v1.models.simulation.moving_wall_vbc", "MovingWallVBC"),
    "MrtSolarParameters": ("simscale_sdk_v1.models.simulation.mrt_solar_parameters", "MrtSolarParameters"),
    "MultifrontalSolver": ("simscale_sdk_v1.models.simulation.multifrontal_solver", "MultifrontalSolver"),
    "MultilinearElastoPlasticModel": (
        "simscale_sdk_v1.models.simulation.multilinear_elasto_plastic_model",
        "MultilinearElastoPlasticModel",
    ),
    "MultilinearModelMarc": ("simscale_sdk_v1.models.simulation.multilinear_model_marc", "MultilinearModelMarc"),
    "Multiphase": ("simscale_sdk_v1.models.simulation.multiphase", "Multiphase"),
    "MultipliedSlaveNodesIterationControl": (
        "simscale_sdk_v1.models.simulation.multiplied_slave_nodes_iteration_control",
        "MultipliedSlaveNodesIterationControl",
    ),
    "MumpsDirectSolver": ("simscale_sdk_v1.models.simulation.mumps_direct_solver", "MumpsDirectSolver"),
    "NaturalConvectionInletOutletBC": (
        "simscale_sdk_v1.models.simulation.natural_convection_inlet_outlet_bc",
        "NaturalConvectionInletOutletBC",
    ),
    "NeoHookeHyperElasticModel": (
        "simscale_sdk_v1.models.simulation.neo_hooke_hyper_elastic_model",
        "NeoHookeHyperElasticModel",
    ),
    "NewRegionRefinementPacefishV38": (
        "simscale_sdk_v1.models.simulation.new_region_refinement_pacefish_v38",
        "NewRegionRefinementPacefishV38",
    ),
    "NewSurfaceRefinementPacefishV38": (
        "simscale_sdk_v1.models.simulation.new_surface_refinement_pacefish_v38",
        "NewSurfaceRefinementPacefishV38",
    ),
    "NewmarkTimeIntegrationScheme": (
        "simscale_sdk_v1.models.simulation.newmark_time_integration_scheme",
        "NewmarkTimeIntegrationScheme",
    ),
    "NewtonContactNonLinearityResolution": (
        "simscale_sdk_v1.models.simulation.newton_contact_non_linearity_resolution",
        "NewtonContactNonLinearityResolution",
    ),
    "NewtonFrictionNonLinearityResolution": (
        "simscale_sdk_v1.models.simulation.newton_friction_non_linearity_resolution",
        "NewtonFrictionNonLinearityResolution",
    ),
    "NewtonIterationTimestepCalculationType": (
        "simscale_sdk_v1.models.simulation.newton_iteration_timestep_calculation_type",
        "NewtonIterationTimestepCalculationType",
    ),
    "NewtonKrylovResolutionType": (
        "simscale_sdk_v1.models.simulation.newton_krylov_resolution_type",
        "NewtonKrylovResolutionType",
    ),
    "NewtonNonLinearityResolution": (
        "simscale_sdk_v1.models.simulation.newton_non_linearity_resolution",
        "NewtonNonLinearityResolution",
    ),
    "NewtonResolutionType": ("simscale_sdk_v1.models.simulation.newton_resolution_type", "NewtonResolutionType"),
    "NewtonianViscosityModel": (
        "simscale_sdk_v1.models.simulation.newtonian_viscosity_model",
        "NewtonianViscosityModel",
    ),
    "NoCoreLoss": ("simscale_sdk_v1.models.simulation.no_core_loss", "NoCoreLoss"),
    "NoCreep": ("simscale_sdk_v1.models.simulation.no_creep", "NoCreep"),
    "NoCreepFormulation": ("simscale_sdk_v1.models.simulation.no_creep_formulation", "NoCreepFormulation"),
    "NoCurrentEBC": ("simscale_sdk_v1.models.simulation.no_current_ebc", "NoCurrentEBC"),
    "NoDamage": ("simscale_sdk_v1.models.simulation.no_damage", "NoDamage"),
    "NoDielectricLosses": ("simscale_sdk_v1.models.simulation.no_dielectric_losses", "NoDielectricLosses"),
    "NoDielectricStrength": ("simscale_sdk_v1.models.simulation.no_dielectric_strength", "NoDielectricStrength"),
    "NoElastoplasticity": ("simscale_sdk_v1.models.simulation.no_elastoplasticity", "NoElastoplasticity"),
    "NoFictitiousClearance": ("simscale_sdk_v1.models.simulation.no_fictitious_clearance", "NoFictitiousClearance"),
    "NoFriction": ("simscale_sdk_v1.models.simulation.no_friction", "NoFriction"),
    "NoSlipVBC": ("simscale_sdk_v1.models.simulation.no_slip_vbc", "NoSlipVBC"),
    "NoSlipWallAerodynamicRoughness": (
        "simscale_sdk_v1.models.simulation.no_slip_wall_aerodynamic_roughness",
        "NoSlipWallAerodynamicRoughness",
    ),
    "NoSlipWallEquivalentSandRoughness": (
        "simscale_sdk_v1.models.simulation.no_slip_wall_equivalent_sand_roughness",
        "NoSlipWallEquivalentSandRoughness",
    ),
    "NoWallThermal": ("simscale_sdk_v1.models.simulation.no_wall_thermal", "NoWallThermal"),
    "NodalForceType": ("simscale_sdk_v1.models.simulation.nodal_force_type", "NodalForceType"),
    "NodalLoadBC": ("simscale_sdk_v1.models.simulation.nodal_load_bc", "NodalLoadBC"),
    "NodalMomentType": ("simscale_sdk_v1.models.simulation.nodal_moment_type", "NodalMomentType"),
    "NonMonotomousResidualRetimingEvent": (
        "simscale_sdk_v1.models.simulation.non_monotomous_residual_retiming_event",
        "NonMonotomousResidualRetimingEvent",
    ),
    "NoneDamping": ("simscale_sdk_v1.models.simulation.none_damping", "NoneDamping"),
    "NoneReactualization": ("simscale_sdk_v1.models.simulation.none_reactualization", "NoneReactualization"),
    "NonlinearIsotropicPermeability": (
        "simscale_sdk_v1.models.simulation.nonlinear_isotropic_permeability",
        "NonlinearIsotropicPermeability",
    ),
    "NormalizedDisplacementResultControlItem": (
        "simscale_sdk_v1.models.simulation.normalized_displacement_result_control_item",
        "NormalizedDisplacementResultControlItem",
    ),
    "NormalizedDisplacementType": (
        "simscale_sdk_v1.models.simulation.normalized_displacement_type",
        "NormalizedDisplacementType",
    ),
    "NortonCreepFormulation": ("simscale_sdk_v1.models.simulation.norton_creep_formulation", "NortonCreepFormulation"),
    "NumberIterationsWriteControl": (
        "simscale_sdk_v1.models.simulation.number_iterations_write_control",
        "NumberIterationsWriteControl",
    ),
    "NumberOfCellsPerDirection": (
        "simscale_sdk_v1.models.simulation.number_of_cells_per_direction",
        "NumberOfCellsPerDirection",
    ),
    "Oak": ("simscale_sdk_v1.models.simulation.oak", "Oak"),
    "OffPositionTolerance": ("simscale_sdk_v1.models.simulation.off_position_tolerance", "OffPositionTolerance"),
    "OgdenHyperElasticModel": ("simscale_sdk_v1.models.simulation.ogden_hyper_elastic_model", "OgdenHyperElasticModel"),
    "OgdenHyperelasticModelMarc": (
        "simscale_sdk_v1.models.simulation.ogden_hyperelastic_model_marc",
        "OgdenHyperelasticModelMarc",
    ),
    "OgdenRoxburgh": ("simscale_sdk_v1.models.simulation.ogden_roxburgh", "OgdenRoxburgh"),
    "OneOf_AMIRotatingZoneMotionType": (
        "simscale_sdk_v1.models.simulation.one_of_ami_rotating_zone_motion_type",
        "OneOf_AMIRotatingZoneMotionType",
    ),
    "OneOf_AccelerationFieldSelectionAccelerationType": (
        "simscale_sdk_v1.models.simulation.one_of__acceleration_field_selection_acceleration_type",
        "OneOf_AccelerationFieldSelectionAccelerationType",
    ),
    "OneOf_AdvancedConceptsHumiditySources": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_humidity_sources",
        "OneOf_AdvancedConceptsHumiditySources",
    ),
    "OneOf_AdvancedConceptsMomentumSources": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_momentum_sources",
        "OneOf_AdvancedConceptsMomentumSources",
    ),
    "OneOf_AdvancedConceptsPassiveScalarSources": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_passive_scalar_sources",
        "OneOf_AdvancedConceptsPassiveScalarSources",
    ),
    "OneOf_AdvancedConceptsPorousMediums": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_porous_mediums",
        "OneOf_AdvancedConceptsPorousMediums",
    ),
    "OneOf_AdvancedConceptsPowerSources": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_power_sources",
        "OneOf_AdvancedConceptsPowerSources",
    ),
    "OneOf_AdvancedConceptsRotatingZones": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_rotating_zones",
        "OneOf_AdvancedConceptsRotatingZones",
    ),
    "OneOf_AdvancedConceptsSolidBodyMotions": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_solid_body_motions",
        "OneOf_AdvancedConceptsSolidBodyMotions",
    ),
    "OneOf_AdvancedConceptsThermalContactResistance": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_thermal_contact_resistance",
        "OneOf_AdvancedConceptsThermalContactResistance",
    ),
    "OneOf_AdvancedConceptsThermalResistanceNetworks": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_concepts_thermal_resistance_networks",
        "OneOf_AdvancedConceptsThermalResistanceNetworks",
    ),
    "OneOf_AdvancedMUMPSSettingsMumpsAcceleration": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_mumps_settings_mumps_acceleration",
        "OneOf_AdvancedMUMPSSettingsMumpsAcceleration",
    ),
    "OneOf_AdvancedModellingPorousObjects": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_modelling_porous_objects",
        "OneOf_AdvancedModellingPorousObjects",
    ),
    "OneOf_AdvancedPETSCSettingsPreconditioner": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_petsc_settings_preconditioner",
        "OneOf_AdvancedPETSCSettingsPreconditioner",
    ),
    "OneOf_AdvancedROISettingsWindTunnelSize": (
        "simscale_sdk_v1.models.simulation.one_of__advanced_roi_settings_wind_tunnel_size",
        "OneOf_AdvancedROISettingsWindTunnelSize",
    ),
    "OneOf_AreaAverageResultControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__area_average_result_control_write_control",
        "OneOf_AreaAverageResultControlWriteControl",
    ),
    "OneOf_AreaIntegralResultControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__area_integral_result_control_write_control",
        "OneOf_AreaIntegralResultControlWriteControl",
    ),
    "OneOf_AutoTimestepDefinitionRetimingEvent": (
        "simscale_sdk_v1.models.simulation.one_of__auto_timestep_definition_retiming_event",
        "OneOf_AutoTimestepDefinitionRetimingEvent",
    ),
    "OneOf_AutomaticSimericsMeshSettingsRefinements": (
        "simscale_sdk_v1.models.simulation.one_of__automatic_simerics_mesh_settings_refinements",
        "OneOf_AutomaticSimericsMeshSettingsRefinements",
    ),
    "OneOf_AverageFieldsCalculationResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__average_fields_calculation_result_control_item_field_selection",
        "OneOf_AverageFieldsCalculationResultControlItemFieldSelection",
    ),
    "OneOf_BatheWilsonSubspaceSettings": (
        "simscale_sdk_v1.models.simulation.one_of__bathe_wilson_subspace_settings",
        "OneOf_BatheWilsonSubspaceSettings",
    ),
    "OneOf_BilinearElastoPlasticModelHardeningModel": (
        "simscale_sdk_v1.models.simulation.one_of__bilinear_elasto_plastic_model_hardening_model",
        "OneOf_BilinearElastoPlasticModelHardeningModel",
    ),
    "OneOf_BilinearElastoPlasticModelPoissonsRatio": (
        "simscale_sdk_v1.models.simulation.one_of__bilinear_elasto_plastic_model_poissons_ratio",
        "OneOf_BilinearElastoPlasticModelPoissonsRatio",
    ),
    "OneOf_BilinearModelMarcHardeningModel": (
        "simscale_sdk_v1.models.simulation.one_of__bilinear_model_marc_hardening_model",
        "OneOf_BilinearModelMarcHardeningModel",
    ),
    "OneOf_BilinearModelMarcHardeningRule": (
        "simscale_sdk_v1.models.simulation.one_of__bilinear_model_marc_hardening_rule",
        "OneOf_BilinearModelMarcHardeningRule",
    ),
    "OneOf_BondedContactPositionTolerance": (
        "simscale_sdk_v1.models.simulation.one_of__bonded_contact_position_tolerance",
        "OneOf_BondedContactPositionTolerance",
    ),
    "OneOf_CoilCoilType": ("simscale_sdk_v1.models.simulation.one_of__coil_coil_type", "OneOf_CoilCoilType"),
    "OneOf_CoilExcitation": ("simscale_sdk_v1.models.simulation.one_of__coil_excitation", "OneOf_CoilExcitation"),
    "OneOf_CoilTopology": ("simscale_sdk_v1.models.simulation.one_of__coil_topology", "OneOf_CoilTopology"),
    "OneOf_ComponentVectorFunctionX": (
        "simscale_sdk_v1.models.simulation.one_of__component_vector_function_x",
        "OneOf_ComponentVectorFunctionX",
    ),
    "OneOf_ComponentVectorFunctionY": (
        "simscale_sdk_v1.models.simulation.one_of__component_vector_function_y",
        "OneOf_ComponentVectorFunctionY",
    ),
    "OneOf_ComponentVectorFunctionZ": (
        "simscale_sdk_v1.models.simulation.one_of__component_vector_function_z",
        "OneOf_ComponentVectorFunctionZ",
    ),
    "OneOf_CompressibleBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__compressible_boundary_conditions",
        "OneOf_CompressibleBoundaryConditions",
    ),
    "OneOf_CompressibleTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__compressible_time_dependency",
        "OneOf_CompressibleTimeDependency",
    ),
    "OneOf_ComputingCoreDomainDecomposition": (
        "simscale_sdk_v1.models.simulation.one_of__computing_core_domain_decomposition",
        "OneOf_ComputingCoreDomainDecomposition",
    ),
    "OneOf_ConjugateHeatTransferBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__conjugate_heat_transfer_boundary_conditions",
        "OneOf_ConjugateHeatTransferBoundaryConditions",
    ),
    "OneOf_ConjugateHeatTransferTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__conjugate_heat_transfer_time_dependency",
        "OneOf_ConjugateHeatTransferTimeDependency",
    ),
    "OneOf_ConnectionSettingsV36ContactNonLinearityResolution": (
        "simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_contact_non_linearity_resolution",
        "OneOf_ConnectionSettingsV36ContactNonLinearityResolution",
    ),
    "OneOf_ConnectionSettingsV36Friction": (
        "simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_friction",
        "OneOf_ConnectionSettingsV36Friction",
    ),
    "OneOf_ConnectionSettingsV36NonlinearityResolution": (
        "simscale_sdk_v1.models.simulation.one_of__connection_settings_v36_nonlinearity_resolution",
        "OneOf_ConnectionSettingsV36NonlinearityResolution",
    ),
    "OneOf_ConstAnIsoTransportOrientation": (
        "simscale_sdk_v1.models.simulation.one_of__const_an_iso_transport_orientation",
        "OneOf_ConstAnIsoTransportOrientation",
    ),
    "OneOf_ConstCrossPlaneOrthotropicTransportOrientation": (
        "simscale_sdk_v1.models.simulation.one_of__const_cross_plane_orthotropic_transport_orientation",
        "OneOf_ConstCrossPlaneOrthotropicTransportOrientation",
    ),
    "OneOf_ConstTransportThermo": (
        "simscale_sdk_v1.models.simulation.one_of__const_transport_thermo",
        "OneOf_ConstTransportThermo",
    ),
    "OneOf_ContactConductanceLayerInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.one_of__contact_conductance_layer_interface_thermal",
        "OneOf_ContactConductanceLayerInterfaceThermal",
    ),
    "OneOf_ContactConnections": (
        "simscale_sdk_v1.models.simulation.one_of__contact_connections",
        "OneOf_ContactConnections",
    ),
    "OneOf_ContactFieldSelectionContactType": (
        "simscale_sdk_v1.models.simulation.one_of__contact_field_selection_contact_type",
        "OneOf_ContactFieldSelectionContactType",
    ),
    "OneOf_ContactResistanceLayerInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.one_of__contact_resistance_layer_interface_thermal",
        "OneOf_ContactResistanceLayerInterfaceThermal",
    ),
    "OneOf_ConvectiveHeatTransferBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_boundary_conditions",
        "OneOf_ConvectiveHeatTransferBoundaryConditions",
    ),
    "OneOf_ConvectiveHeatTransferMaterialsFluids": (
        "simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_materials_fluids",
        "OneOf_ConvectiveHeatTransferMaterialsFluids",
    ),
    "OneOf_ConvectiveHeatTransferTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_time_dependency",
        "OneOf_ConvectiveHeatTransferTimeDependency",
    ),
    "OneOf_CoulombFrictionNonlinearityResolution": (
        "simscale_sdk_v1.models.simulation.one_of__coulomb_friction_nonlinearity_resolution",
        "OneOf_CoulombFrictionNonlinearityResolution",
    ),
    "OneOf_CoupledConjugateHeatTransferBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__coupled_conjugate_heat_transfer_boundary_conditions",
        "OneOf_CoupledConjugateHeatTransferBoundaryConditions",
    ),
    "OneOf_CoupledConjugateHeatTransferMaterialsFluids": (
        "simscale_sdk_v1.models.simulation.one_of__coupled_conjugate_heat_transfer_materials_fluids",
        "OneOf_CoupledConjugateHeatTransferMaterialsFluids",
    ),
    "OneOf_CoupledConjugateHeatTransferTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__coupled_conjugate_heat_transfer_time_dependency",
        "OneOf_CoupledConjugateHeatTransferTimeDependency",
    ),
    "OneOf_CurrentExcitationCurrentType": (
        "simscale_sdk_v1.models.simulation.one_of__current_excitation_current_type",
        "OneOf_CurrentExcitationCurrentType",
    ),
    "OneOf_CustomFluidBCEddyViscosity": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_eddy_viscosity",
        "OneOf_CustomFluidBCEddyViscosity",
    ),
    "OneOf_CustomFluidBCEddyViscosityCompressible": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_eddy_viscosity_compressible",
        "OneOf_CustomFluidBCEddyViscosityCompressible",
    ),
    "OneOf_CustomFluidBCEpsilonDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_epsilon_dissipation_rate",
        "OneOf_CustomFluidBCEpsilonDissipationRate",
    ),
    "OneOf_CustomFluidBCGaugePressure": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_gauge_pressure",
        "OneOf_CustomFluidBCGaugePressure",
    ),
    "OneOf_CustomFluidBCGaugePressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_gauge_pressure_rgh",
        "OneOf_CustomFluidBCGaugePressureRgh",
    ),
    "OneOf_CustomFluidBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_net_radiative_heat_flux",
        "OneOf_CustomFluidBCNetRadiativeHeatFlux",
    ),
    "OneOf_CustomFluidBCNuTilda": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_nu_tilda",
        "OneOf_CustomFluidBCNuTilda",
    ),
    "OneOf_CustomFluidBCOmegaDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_omega_dissipation_rate",
        "OneOf_CustomFluidBCOmegaDissipationRate",
    ),
    "OneOf_CustomFluidBCPassiveScalars": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_passive_scalars",
        "OneOf_CustomFluidBCPassiveScalars",
    ),
    "OneOf_CustomFluidBCPhaseFraction": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_phase_fraction",
        "OneOf_CustomFluidBCPhaseFraction",
    ),
    "OneOf_CustomFluidBCPressure": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_pressure",
        "OneOf_CustomFluidBCPressure",
    ),
    "OneOf_CustomFluidBCPressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_pressure_rgh",
        "OneOf_CustomFluidBCPressureRgh",
    ),
    "OneOf_CustomFluidBCTemperature": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_temperature",
        "OneOf_CustomFluidBCTemperature",
    ),
    "OneOf_CustomFluidBCTurbulentDynamicViscosity": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_dynamic_viscosity",
        "OneOf_CustomFluidBCTurbulentDynamicViscosity",
    ),
    "OneOf_CustomFluidBCTurbulentKineticEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_kinetic_energy",
        "OneOf_CustomFluidBCTurbulentKineticEnergy",
    ),
    "OneOf_CustomFluidBCTurbulentThermalDiffusivity": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_thermal_diffusivity",
        "OneOf_CustomFluidBCTurbulentThermalDiffusivity",
    ),
    "OneOf_CustomFluidBCTurbulentThermalDiffusivityCompressible": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_thermal_diffusivity_compressible",
        "OneOf_CustomFluidBCTurbulentThermalDiffusivityCompressible",
    ),
    "OneOf_CustomFluidBCVelocity": (
        "simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_velocity",
        "OneOf_CustomFluidBCVelocity",
    ),
    "OneOf_DarcyForchheimerMediumOrientation": (
        "simscale_sdk_v1.models.simulation.one_of__darcy_forchheimer_medium_orientation",
        "OneOf_DarcyForchheimerMediumOrientation",
    ),
    "OneOf_DarcyForchheimerMediumPorousMediaHeatTransfer": (
        "simscale_sdk_v1.models.simulation.one_of__darcy_forchheimer_medium_porous_media_heat_transfer",
        "OneOf_DarcyForchheimerMediumPorousMediaHeatTransfer",
    ),
    "OneOf_DarcyMediumPorousMaterialType": (
        "simscale_sdk_v1.models.simulation.one_of__darcy_medium_porous_material_type",
        "OneOf_DarcyMediumPorousMaterialType",
    ),
    "OneOf_DerivedHeatFluxWallThermal": (
        "simscale_sdk_v1.models.simulation.one_of__derived_heat_flux_wall_thermal",
        "OneOf_DerivedHeatFluxWallThermal",
    ),
    "OneOf_DimensionalFunction_AccelerationValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__acceleration_value",
        "OneOf_DimensionalFunction_AccelerationValue",
    ),
    "OneOf_DimensionalFunction_AngleValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__angle_value",
        "OneOf_DimensionalFunction_AngleValue",
    ),
    "OneOf_DimensionalFunction_DensityValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__density_value",
        "OneOf_DimensionalFunction_DensityValue",
    ),
    "OneOf_DimensionalFunction_DimensionlessValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__dimensionless_value",
        "OneOf_DimensionalFunction_DimensionlessValue",
    ),
    "OneOf_DimensionalFunction_DynamicViscosityValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__dynamic_viscosity_value",
        "OneOf_DimensionalFunction_DynamicViscosityValue",
    ),
    "OneOf_DimensionalFunction_ElectricConductivityValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_conductivity_value",
        "OneOf_DimensionalFunction_ElectricConductivityValue",
    ),
    "OneOf_DimensionalFunction_ElectricCurrentValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_current_value",
        "OneOf_DimensionalFunction_ElectricCurrentValue",
    ),
    "OneOf_DimensionalFunction_ElectricFieldStrengthValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_field_strength_value",
        "OneOf_DimensionalFunction_ElectricFieldStrengthValue",
    ),
    "OneOf_DimensionalFunction_ElectricPotentialValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_potential_value",
        "OneOf_DimensionalFunction_ElectricPotentialValue",
    ),
    "OneOf_DimensionalFunction_ElectricResistivityValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_resistivity_value",
        "OneOf_DimensionalFunction_ElectricResistivityValue",
    ),
    "OneOf_DimensionalFunction_HeatFluxValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__heat_flux_value",
        "OneOf_DimensionalFunction_HeatFluxValue",
    ),
    "OneOf_DimensionalFunction_KinematicViscosityValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__kinematic_viscosity_value",
        "OneOf_DimensionalFunction_KinematicViscosityValue",
    ),
    "OneOf_DimensionalFunction_LengthValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__length_value",
        "OneOf_DimensionalFunction_LengthValue",
    ),
    "OneOf_DimensionalFunction_MagneticFluxDensityValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__magnetic_flux_density_value",
        "OneOf_DimensionalFunction_MagneticFluxDensityValue",
    ),
    "OneOf_DimensionalFunction_MassFlowRateValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__mass_flow_rate_value",
        "OneOf_DimensionalFunction_MassFlowRateValue",
    ),
    "OneOf_DimensionalFunction_PowerValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__power_value",
        "OneOf_DimensionalFunction_PowerValue",
    ),
    "OneOf_DimensionalFunction_PressureValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__pressure_value",
        "OneOf_DimensionalFunction_PressureValue",
    ),
    "OneOf_DimensionalFunction_RotationSpeedValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__rotation_speed_value",
        "OneOf_DimensionalFunction_RotationSpeedValue",
    ),
    "OneOf_DimensionalFunction_SpecificEnergyValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_energy_value",
        "OneOf_DimensionalFunction_SpecificEnergyValue",
    ),
    "OneOf_DimensionalFunction_SpecificHeatValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_heat_value",
        "OneOf_DimensionalFunction_SpecificHeatValue",
    ),
    "OneOf_DimensionalFunction_SpecificTurbulenceDissipationRateValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_turbulence_dissipation_rate_value",
        "OneOf_DimensionalFunction_SpecificTurbulenceDissipationRateValue",
    ),
    "OneOf_DimensionalFunction_SpeedValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__speed_value",
        "OneOf_DimensionalFunction_SpeedValue",
    ),
    "OneOf_DimensionalFunction_TemperatureGradientValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__temperature_gradient_value",
        "OneOf_DimensionalFunction_TemperatureGradientValue",
    ),
    "OneOf_DimensionalFunction_TemperatureValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__temperature_value",
        "OneOf_DimensionalFunction_TemperatureValue",
    ),
    "OneOf_DimensionalFunction_ThermalConductivityValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_conductivity_value",
        "OneOf_DimensionalFunction_ThermalConductivityValue",
    ),
    "OneOf_DimensionalFunction_ThermalExpansionRateValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_expansion_rate_value",
        "OneOf_DimensionalFunction_ThermalExpansionRateValue",
    ),
    "OneOf_DimensionalFunction_ThermalTransmittanceValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_transmittance_value",
        "OneOf_DimensionalFunction_ThermalTransmittanceValue",
    ),
    "OneOf_DimensionalFunction_TimeValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__time_value",
        "OneOf_DimensionalFunction_TimeValue",
    ),
    "OneOf_DimensionalFunction_TotalThermalTransmittanceValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__total_thermal_transmittance_value",
        "OneOf_DimensionalFunction_TotalThermalTransmittanceValue",
    ),
    "OneOf_DimensionalFunction_TurbulenceKineticEnergyValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__turbulence_kinetic_energy_value",
        "OneOf_DimensionalFunction_TurbulenceKineticEnergyValue",
    ),
    "OneOf_DimensionalFunction_TurbulentDissipationValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__turbulent_dissipation_value",
        "OneOf_DimensionalFunction_TurbulentDissipationValue",
    ),
    "OneOf_DimensionalFunction_VolumetricFlowRateValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__volumetric_flow_rate_value",
        "OneOf_DimensionalFunction_VolumetricFlowRateValue",
    ),
    "OneOf_DimensionalFunction_VolumetricPowerValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_function__volumetric_power_value",
        "OneOf_DimensionalFunction_VolumetricPowerValue",
    ),
    "OneOf_DimensionalVectorFunction_AccelerationValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__acceleration_value",
        "OneOf_DimensionalVectorFunction_AccelerationValue",
    ),
    "OneOf_DimensionalVectorFunction_ForceValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__force_value",
        "OneOf_DimensionalVectorFunction_ForceValue",
    ),
    "OneOf_DimensionalVectorFunction_LengthValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__length_value",
        "OneOf_DimensionalVectorFunction_LengthValue",
    ),
    "OneOf_DimensionalVectorFunction_PressureValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__pressure_value",
        "OneOf_DimensionalVectorFunction_PressureValue",
    ),
    "OneOf_DimensionalVectorFunction_SpeedValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__speed_value",
        "OneOf_DimensionalVectorFunction_SpeedValue",
    ),
    "OneOf_DimensionalVectorFunction_TorqueValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__torque_value",
        "OneOf_DimensionalVectorFunction_TorqueValue",
    ),
    "OneOf_DimensionalVectorFunction_VolumeForceValue": (
        "simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__volume_force_value",
        "OneOf_DimensionalVectorFunction_VolumeForceValue",
    ),
    "OneOf_DirectionalDependencyDarcyForchheimerType": (
        "simscale_sdk_v1.models.simulation.one_of__directional_dependency_darcy_forchheimer_type",
        "OneOf_DirectionalDependencyDarcyForchheimerType",
    ),
    "OneOf_DirectionalMaterialStructureMode": (
        "simscale_sdk_v1.models.simulation.one_of__directional_material_structure_mode",
        "OneOf_DirectionalMaterialStructureMode",
    ),
    "OneOf_DirectionalMaterialStructureOrientation": (
        "simscale_sdk_v1.models.simulation.one_of__directional_material_structure_orientation",
        "OneOf_DirectionalMaterialStructureOrientation",
    ),
    "OneOf_DisplacementFieldSelectionDisplacementType": (
        "simscale_sdk_v1.models.simulation.one_of__displacement_field_selection_displacement_type",
        "OneOf_DisplacementFieldSelectionDisplacementType",
    ),
    "OneOf_DisplacementsConvergenceMethodConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.one_of__displacements_convergence_method_convergence_criteria",
        "OneOf_DisplacementsConvergenceMethodConvergenceCriteria",
    ),
    "OneOf_DistributedMassBCMassDefinition": (
        "simscale_sdk_v1.models.simulation.one_of__distributed_mass_bc_mass_definition",
        "OneOf_DistributedMassBCMassDefinition",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_R": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_r",
        "OneOf_DivergenceSchemesDiv_Phi_R",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_enthalpy": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_enthalpy",
        "OneOf_DivergenceSchemesDiv_Phi_enthalpy",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_epsilonDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_epsilon_dissipation_rate",
        "OneOf_DivergenceSchemesDiv_Phi_epsilonDissipationRate",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_internalEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_internal_energy",
        "OneOf_DivergenceSchemesDiv_Phi_internalEnergy",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_kineticEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_kinetic_energy",
        "OneOf_DivergenceSchemesDiv_Phi_kineticEnergy",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_nuTilda": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_nu_tilda",
        "OneOf_DivergenceSchemesDiv_Phi_nuTilda",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_omegaDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_omega_dissipation_rate",
        "OneOf_DivergenceSchemesDiv_Phi_omegaDissipationRate",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_passiveScalar": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_passive_scalar",
        "OneOf_DivergenceSchemesDiv_Phi_passiveScalar",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_temperature": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_temperature",
        "OneOf_DivergenceSchemesDiv_Phi_temperature",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_turbulentKineticEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_turbulent_kinetic_energy",
        "OneOf_DivergenceSchemesDiv_Phi_turbulentKineticEnergy",
    ),
    "OneOf_DivergenceSchemesDiv_Phi_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_velocity",
        "OneOf_DivergenceSchemesDiv_Phi_velocity",
    ),
    "OneOf_DivergenceSchemesDiv_Phiv_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phiv_pressure",
        "OneOf_DivergenceSchemesDiv_Phiv_pressure",
    ),
    "OneOf_DivergenceSchemesDiv_R": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_r",
        "OneOf_DivergenceSchemesDiv_R",
    ),
    "OneOf_DivergenceSchemesDiv_phi_Ekp": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phi__ekp",
        "OneOf_DivergenceSchemesDiv_phi_Ekp",
    ),
    "OneOf_DivergenceSchemesDiv_phi_alpha": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phi_alpha",
        "OneOf_DivergenceSchemesDiv_phi_alpha",
    ),
    "OneOf_DivergenceSchemesDiv_phid_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phid_pressure",
        "OneOf_DivergenceSchemesDiv_phid_pressure",
    ),
    "OneOf_DivergenceSchemesDiv_phirb_alpha": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phirb_alpha",
        "OneOf_DivergenceSchemesDiv_phirb_alpha",
    ),
    "OneOf_DivergenceSchemesDiv_rhoPhi_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_rho_phi_velocity",
        "OneOf_DivergenceSchemesDiv_rhoPhi_velocity",
    ),
    "OneOf_DivergenceSchemesDiv_tauMC": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_tau_mc",
        "OneOf_DivergenceSchemesDiv_tauMC",
    ),
    "OneOf_DivergenceSchemesDiv_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_velocity",
        "OneOf_DivergenceSchemesDiv_velocity",
    ),
    "OneOf_DivergenceSchemesForDefault": (
        "simscale_sdk_v1.models.simulation.one_of__divergence_schemes_for_default",
        "OneOf_DivergenceSchemesForDefault",
    ),
    "OneOf_DynamicAnalysisBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_boundary_conditions",
        "OneOf_DynamicAnalysisBoundaryConditions",
    ),
    "OneOf_DynamicAnalysisConnectionGroups": (
        "simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_connection_groups",
        "OneOf_DynamicAnalysisConnectionGroups",
    ),
    "OneOf_DynamicAnalysisConnectors": (
        "simscale_sdk_v1.models.simulation.one_of__dynamic_analysis_connectors",
        "OneOf_DynamicAnalysisConnectors",
    ),
    "OneOf_ERPCalculationResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of_erp_calculation_result_control_item_field_selection",
        "OneOf_ERPCalculationResultControlItemFieldSelection",
    ),
    "OneOf_ElasticSupportBCSpringStiffness": (
        "simscale_sdk_v1.models.simulation.one_of__elastic_support_bc_spring_stiffness",
        "OneOf_ElasticSupportBCSpringStiffness",
    ),
    "OneOf_ElasticityMarcPoissonsRatio": (
        "simscale_sdk_v1.models.simulation.one_of__elasticity_marc_poissons_ratio",
        "OneOf_ElasticityMarcPoissonsRatio",
    ),
    "OneOf_ElastoplasticNetworkPlasticityModelElastoplasticNetwork": (
        "simscale_sdk_v1.models.simulation.one_of__elastoplastic_network_plasticity_model_elastoplastic_network",
        "OneOf_ElastoplasticNetworkPlasticityModelElastoplasticNetwork",
    ),
    "OneOf_ElectromagneticAnalysisBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_analysis_boundary_conditions",
        "OneOf_ElectromagneticAnalysisBoundaryConditions",
    ),
    "OneOf_ElectromagneticAnalysisModel": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_analysis_model",
        "OneOf_ElectromagneticAnalysisModel",
    ),
    "OneOf_ElectromagneticMaterialCoreLossesType": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_core_losses_type",
        "OneOf_ElectromagneticMaterialCoreLossesType",
    ),
    "OneOf_ElectromagneticMaterialDielectricLossType": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_dielectric_loss_type",
        "OneOf_ElectromagneticMaterialDielectricLossType",
    ),
    "OneOf_ElectromagneticMaterialDielectricStrengthType": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_dielectric_strength_type",
        "OneOf_ElectromagneticMaterialDielectricStrengthType",
    ),
    "OneOf_ElectromagneticMaterialElectricConductivityType": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_electric_conductivity_type",
        "OneOf_ElectromagneticMaterialElectricConductivityType",
    ),
    "OneOf_ElectromagneticMaterialMagneticPermeabilityType": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_magnetic_permeability_type",
        "OneOf_ElectromagneticMaterialMagneticPermeabilityType",
    ),
    "OneOf_ElectromagneticMaterialMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_material_material_behavior",
        "OneOf_ElectromagneticMaterialMaterialBehavior",
    ),
    "OneOf_ElectromagneticResultControlProbePointFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__electromagnetic_result_control_probe_point_field_selection",
        "OneOf_ElectromagneticResultControlProbePointFieldSelection",
    ),
    "OneOf_ElementTechnologyDefinitionMethod": (
        "simscale_sdk_v1.models.simulation.one_of__element_technology_definition_method",
        "OneOf_ElementTechnologyDefinitionMethod",
    ),
    "OneOf_EmbeddedBoundaryBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__embedded_boundary_boundary_conditions",
        "OneOf_EmbeddedBoundaryBoundaryConditions",
    ),
    "OneOf_EmbeddedBoundaryExternalFlowBoundaryCondition": (
        "simscale_sdk_v1.models.simulation.one_of__embedded_boundary_external_flow_boundary_condition",
        "OneOf_EmbeddedBoundaryExternalFlowBoundaryCondition",
    ),
    "OneOf_EmbeddedBoundaryMeshingRefinements": (
        "simscale_sdk_v1.models.simulation.one_of__embedded_boundary_meshing_refinements",
        "OneOf_EmbeddedBoundaryMeshingRefinements",
    ),
    "OneOf_EmbeddedBoundaryMeshingSizing": (
        "simscale_sdk_v1.models.simulation.one_of__embedded_boundary_meshing_sizing",
        "OneOf_EmbeddedBoundaryMeshingSizing",
    ),
    "OneOf_EmbeddedBoundaryTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__embedded_boundary_time_dependency",
        "OneOf_EmbeddedBoundaryTimeDependency",
    ),
    "OneOf_ErrorRetimingEventTimestepCalculationType": (
        "simscale_sdk_v1.models.simulation.one_of__error_retiming_event_timestep_calculation_type",
        "OneOf_ErrorRetimingEventTimestepCalculationType",
    ),
    "OneOf_ExplicitTimeIntegrationTypeScheme": (
        "simscale_sdk_v1.models.simulation.one_of__explicit_time_integration_type_scheme",
        "OneOf_ExplicitTimeIntegrationTypeScheme",
    ),
    "OneOf_ExternalWallHeatFluxTBCHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__external_wall_heat_flux_tbc_heat_flux",
        "OneOf_ExternalWallHeatFluxTBCHeatFlux",
    ),
    "OneOf_FanBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__fan_bc_net_radiative_heat_flux",
        "OneOf_FanBCNetRadiativeHeatFlux",
    ),
    "OneOf_FanBCPressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__fan_bc_pressure_rgh",
        "OneOf_FanBCPressureRgh",
    ),
    "OneOf_FanBCRadiativeIntensityRay": (
        "simscale_sdk_v1.models.simulation.one_of__fan_bc_radiative_intensity_ray",
        "OneOf_FanBCRadiativeIntensityRay",
    ),
    "OneOf_FanBCTemperature": (
        "simscale_sdk_v1.models.simulation.one_of__fan_bc_temperature",
        "OneOf_FanBCTemperature",
    ),
    "OneOf_FanBCTurbulence": ("simscale_sdk_v1.models.simulation.one_of__fan_bc_turbulence", "OneOf_FanBCTurbulence"),
    "OneOf_FieldCalculationsPressureResultControlPressureType": (
        "simscale_sdk_v1.models.simulation.one_of__field_calculations_pressure_result_control_pressure_type",
        "OneOf_FieldCalculationsPressureResultControlPressureType",
    ),
    "OneOf_FieldCalculationsPressureResultControlResultType": (
        "simscale_sdk_v1.models.simulation.one_of__field_calculations_pressure_result_control_result_type",
        "OneOf_FieldCalculationsPressureResultControlResultType",
    ),
    "OneOf_FieldCalculationsTurbulenceResultControlResultType": (
        "simscale_sdk_v1.models.simulation.one_of__field_calculations_turbulence_result_control_result_type",
        "OneOf_FieldCalculationsTurbulenceResultControlResultType",
    ),
    "OneOf_FieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType": (
        "simscale_sdk_v1.models.simulation.one_of__field_calculations_wall_heat_flux_result_control_reference_temperature_result_type",
        "OneOf_FieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType",
    ),
    "OneOf_FieldChangeRetimingEventFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__field_change_retiming_event_field_selection",
        "OneOf_FieldChangeRetimingEventFieldSelection",
    ),
    "OneOf_FieldChangeRetimingEventTimestepCalculationType": (
        "simscale_sdk_v1.models.simulation.one_of__field_change_retiming_event_timestep_calculation_type",
        "OneOf_FieldChangeRetimingEventTimestepCalculationType",
    ),
    "OneOf_FixedCoeffMediumOrientation": (
        "simscale_sdk_v1.models.simulation.one_of__fixed_coeff_medium_orientation",
        "OneOf_FixedCoeffMediumOrientation",
    ),
    "OneOf_FixedCoeffMediumPorousMediaHeatTransfer": (
        "simscale_sdk_v1.models.simulation.one_of__fixed_coeff_medium_porous_media_heat_transfer",
        "OneOf_FixedCoeffMediumPorousMediaHeatTransfer",
    ),
    "OneOf_FixedPointContactNonLinearityResolutionIterationControl": (
        "simscale_sdk_v1.models.simulation.one_of__fixed_point_contact_non_linearity_resolution_iteration_control",
        "OneOf_FixedPointContactNonLinearityResolutionIterationControl",
    ),
    "OneOf_FixedPointNonLinearityResolutionGeometryReactualization": (
        "simscale_sdk_v1.models.simulation.one_of__fixed_point_non_linearity_resolution_geometry_reactualization",
        "OneOf_FixedPointNonLinearityResolutionGeometryReactualization",
    ),
    "OneOf_FixedValueRHBCHumidityValue": (
        "simscale_sdk_v1.models.simulation.one_of__fixed_value_rhbc_humidity_value",
        "OneOf_FixedValueRHBCHumidityValue",
    ),
    "OneOf_FlowDomainBoundariesXMAX": (
        "simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_xmax",
        "OneOf_FlowDomainBoundariesXMAX",
    ),
    "OneOf_FlowDomainBoundariesXMIN": (
        "simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_xmin",
        "OneOf_FlowDomainBoundariesXMIN",
    ),
    "OneOf_FlowDomainBoundariesYMAX": (
        "simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_ymax",
        "OneOf_FlowDomainBoundariesYMAX",
    ),
    "OneOf_FlowDomainBoundariesYMIN": (
        "simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_ymin",
        "OneOf_FlowDomainBoundariesYMIN",
    ),
    "OneOf_FlowDomainBoundariesZMAX": (
        "simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_zmax",
        "OneOf_FlowDomainBoundariesZMAX",
    ),
    "OneOf_FlowDomainBoundariesZMIN": (
        "simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_zmin",
        "OneOf_FlowDomainBoundariesZMIN",
    ),
    "OneOf_FlowRateInletVBCFlowRate": (
        "simscale_sdk_v1.models.simulation.one_of__flow_rate_inlet_vbc_flow_rate",
        "OneOf_FlowRateInletVBCFlowRate",
    ),
    "OneOf_FlowRateMeanInletVBCFlowRate": (
        "simscale_sdk_v1.models.simulation.one_of__flow_rate_mean_inlet_vbc_flow_rate",
        "OneOf_FlowRateMeanInletVBCFlowRate",
    ),
    "OneOf_FlowRateMeanOutletVBCFlowRate": (
        "simscale_sdk_v1.models.simulation.one_of__flow_rate_mean_outlet_vbc_flow_rate",
        "OneOf_FlowRateMeanOutletVBCFlowRate",
    ),
    "OneOf_FlowRateOutletVBCFlowRate": (
        "simscale_sdk_v1.models.simulation.one_of__flow_rate_outlet_vbc_flow_rate",
        "OneOf_FlowRateOutletVBCFlowRate",
    ),
    "OneOf_FlowRateStableOutletVBCFlowRate": (
        "simscale_sdk_v1.models.simulation.one_of__flow_rate_stable_outlet_vbc_flow_rate",
        "OneOf_FlowRateStableOutletVBCFlowRate",
    ),
    "OneOf_FluidCompressibleMaterialEquationOfState": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_equation_of_state",
        "OneOf_FluidCompressibleMaterialEquationOfState",
    ),
    "OneOf_FluidCompressibleMaterialFluidType": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_fluid_type",
        "OneOf_FluidCompressibleMaterialFluidType",
    ),
    "OneOf_FluidCompressibleMaterialTransport": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_transport",
        "OneOf_FluidCompressibleMaterialTransport",
    ),
    "OneOf_FluidCompressibleMaterialViscosityModel": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_compressible_material_viscosity_model",
        "OneOf_FluidCompressibleMaterialViscosityModel",
    ),
    "OneOf_FluidModelDeltaCoefficient": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_model_delta_coefficient",
        "OneOf_FluidModelDeltaCoefficient",
    ),
    "OneOf_FluidResultControlsFieldCalculations": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_field_calculations",
        "OneOf_FluidResultControlsFieldCalculations",
    ),
    "OneOf_FluidResultControlsForcesMoments": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_forces_moments",
        "OneOf_FluidResultControlsForcesMoments",
    ),
    "OneOf_FluidResultControlsSurfaceData": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_surface_data",
        "OneOf_FluidResultControlsSurfaceData",
    ),
    "OneOf_FluidSimulationControlAdjustableTimestep": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_adjustable_timestep",
        "OneOf_FluidSimulationControlAdjustableTimestep",
    ),
    "OneOf_FluidSimulationControlDecomposeAlgorithm": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_decompose_algorithm",
        "OneOf_FluidSimulationControlDecomposeAlgorithm",
    ),
    "OneOf_FluidSimulationControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_simulation_control_write_control",
        "OneOf_FluidSimulationControlWriteControl",
    ),
    "OneOf_FluidSolversDensityFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_density_final_solver",
        "OneOf_FluidSolversDensityFinalSolver",
    ),
    "OneOf_FluidSolversDensitySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_density_solver",
        "OneOf_FluidSolversDensitySolver",
    ),
    "OneOf_FluidSolversEnthalpyFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_enthalpy_final_solver",
        "OneOf_FluidSolversEnthalpyFinalSolver",
    ),
    "OneOf_FluidSolversEnthalpySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_enthalpy_solver",
        "OneOf_FluidSolversEnthalpySolver",
    ),
    "OneOf_FluidSolversEpsilonDissipationRateFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_epsilon_dissipation_rate_final_solver",
        "OneOf_FluidSolversEpsilonDissipationRateFinalSolver",
    ),
    "OneOf_FluidSolversEpsilonDissipationRateSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_epsilon_dissipation_rate_solver",
        "OneOf_FluidSolversEpsilonDissipationRateSolver",
    ),
    "OneOf_FluidSolversInternalEnergyFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_internal_energy_final_solver",
        "OneOf_FluidSolversInternalEnergyFinalSolver",
    ),
    "OneOf_FluidSolversInternalEnergySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_internal_energy_solver",
        "OneOf_FluidSolversInternalEnergySolver",
    ),
    "OneOf_FluidSolversNuTildaFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_nu_tilda_final_solver",
        "OneOf_FluidSolversNuTildaFinalSolver",
    ),
    "OneOf_FluidSolversNuTildaSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_nu_tilda_solver",
        "OneOf_FluidSolversNuTildaSolver",
    ),
    "OneOf_FluidSolversOmegaDissipationRateFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_omega_dissipation_rate_final_solver",
        "OneOf_FluidSolversOmegaDissipationRateFinalSolver",
    ),
    "OneOf_FluidSolversOmegaDissipationRateSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_omega_dissipation_rate_solver",
        "OneOf_FluidSolversOmegaDissipationRateSolver",
    ),
    "OneOf_FluidSolversPassiveScalarSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_passive_scalar_solver",
        "OneOf_FluidSolversPassiveScalarSolver",
    ),
    "OneOf_FluidSolversPressureFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_final_solver",
        "OneOf_FluidSolversPressureFinalSolver",
    ),
    "OneOf_FluidSolversPressureRghFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_rgh_final_solver",
        "OneOf_FluidSolversPressureRghFinalSolver",
    ),
    "OneOf_FluidSolversPressureRghSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_rgh_solver",
        "OneOf_FluidSolversPressureRghSolver",
    ),
    "OneOf_FluidSolversPressureSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_solver",
        "OneOf_FluidSolversPressureSolver",
    ),
    "OneOf_FluidSolversRadiativeIntensityRaySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_radiative_intensity_ray_solver",
        "OneOf_FluidSolversRadiativeIntensityRaySolver",
    ),
    "OneOf_FluidSolversSolidEnthalpyFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_solid_enthalpy_final_solver",
        "OneOf_FluidSolversSolidEnthalpyFinalSolver",
    ),
    "OneOf_FluidSolversSolidEnthalpySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_solid_enthalpy_solver",
        "OneOf_FluidSolversSolidEnthalpySolver",
    ),
    "OneOf_FluidSolversSpecificHumiditySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_specific_humidity_solver",
        "OneOf_FluidSolversSpecificHumiditySolver",
    ),
    "OneOf_FluidSolversTemperatureFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_temperature_final_solver",
        "OneOf_FluidSolversTemperatureFinalSolver",
    ),
    "OneOf_FluidSolversTemperatureSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_temperature_solver",
        "OneOf_FluidSolversTemperatureSolver",
    ),
    "OneOf_FluidSolversTurbulentKineticEnergyFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_turbulent_kinetic_energy_final_solver",
        "OneOf_FluidSolversTurbulentKineticEnergyFinalSolver",
    ),
    "OneOf_FluidSolversTurbulentKineticEnergySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_turbulent_kinetic_energy_solver",
        "OneOf_FluidSolversTurbulentKineticEnergySolver",
    ),
    "OneOf_FluidSolversVelocityFinalSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_velocity_final_solver",
        "OneOf_FluidSolversVelocityFinalSolver",
    ),
    "OneOf_FluidSolversVelocitySolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_velocity_solver",
        "OneOf_FluidSolversVelocitySolver",
    ),
    "OneOf_FluidSolversVoltageSolver": (
        "simscale_sdk_v1.models.simulation.one_of__fluid_solvers_voltage_solver",
        "OneOf_FluidSolversVoltageSolver",
    ),
    "OneOf_FluxSchemesForDefault": (
        "simscale_sdk_v1.models.simulation.one_of__flux_schemes_for_default",
        "OneOf_FluxSchemesForDefault",
    ),
    "OneOf_ForceFieldSelectionForceType": (
        "simscale_sdk_v1.models.simulation.one_of__force_field_selection_force_type",
        "OneOf_ForceFieldSelectionForceType",
    ),
    "OneOf_ForceMomentCoefficientsResultControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__force_moment_coefficients_result_control_write_control",
        "OneOf_ForceMomentCoefficientsResultControlWriteControl",
    ),
    "OneOf_ForceResultControlItemForceType": (
        "simscale_sdk_v1.models.simulation.one_of__force_result_control_item_force_type",
        "OneOf_ForceResultControlItemForceType",
    ),
    "OneOf_ForcesMomentsResultControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__forces_moments_result_control_write_control",
        "OneOf_ForcesMomentsResultControlWriteControl",
    ),
    "OneOf_FreestreamVBCAmbientPressure": (
        "simscale_sdk_v1.models.simulation.one_of__freestream_vbc_ambient_pressure",
        "OneOf_FreestreamVBCAmbientPressure",
    ),
    "OneOf_FrequencyAnalysisBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__frequency_analysis_boundary_conditions",
        "OneOf_FrequencyAnalysisBoundaryConditions",
    ),
    "OneOf_FrequencyAnalysisConnectors": (
        "simscale_sdk_v1.models.simulation.one_of__frequency_analysis_connectors",
        "OneOf_FrequencyAnalysisConnectors",
    ),
    "OneOf_FrictionContactContactSolutionMethod": (
        "simscale_sdk_v1.models.simulation.one_of__friction_contact_contact_solution_method",
        "OneOf_FrictionContactContactSolutionMethod",
    ),
    "OneOf_FrictionContactFictitiousClearance": (
        "simscale_sdk_v1.models.simulation.one_of__friction_contact_fictitious_clearance",
        "OneOf_FrictionContactFictitiousClearance",
    ),
    "OneOf_FrictionContactFrictionCoefficient": (
        "simscale_sdk_v1.models.simulation.one_of__friction_contact_friction_coefficient",
        "OneOf_FrictionContactFrictionCoefficient",
    ),
    "OneOf_FrictionlessContactContactSolutionMethod": (
        "simscale_sdk_v1.models.simulation.one_of__frictionless_contact_contact_solution_method",
        "OneOf_FrictionlessContactContactSolutionMethod",
    ),
    "OneOf_FrictionlessContactFictitiousClearance": (
        "simscale_sdk_v1.models.simulation.one_of__frictionless_contact_fictitious_clearance",
        "OneOf_FrictionlessContactFictitiousClearance",
    ),
    "OneOf_GeneralDarcyForchheimerPacefishDarcyForchheimerType": (
        "simscale_sdk_v1.models.simulation.one_of__general_darcy_forchheimer_pacefish_darcy_forchheimer_type",
        "OneOf_GeneralDarcyForchheimerPacefishDarcyForchheimerType",
    ),
    "OneOf_GradientSchemesForDefault": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_for_default",
        "OneOf_GradientSchemesForDefault",
    ),
    "OneOf_GradientSchemesGrad_density": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_density",
        "OneOf_GradientSchemesGrad_density",
    ),
    "OneOf_GradientSchemesGrad_enthalpy": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_enthalpy",
        "OneOf_GradientSchemesGrad_enthalpy",
    ),
    "OneOf_GradientSchemesGrad_epsilonDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_epsilon_dissipation_rate",
        "OneOf_GradientSchemesGrad_epsilonDissipationRate",
    ),
    "OneOf_GradientSchemesGrad_internalEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_internal_energy",
        "OneOf_GradientSchemesGrad_internalEnergy",
    ),
    "OneOf_GradientSchemesGrad_nuTilda": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_nu_tilda",
        "OneOf_GradientSchemesGrad_nuTilda",
    ),
    "OneOf_GradientSchemesGrad_omegaDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_omega_dissipation_rate",
        "OneOf_GradientSchemesGrad_omegaDissipationRate",
    ),
    "OneOf_GradientSchemesGrad_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_pressure",
        "OneOf_GradientSchemesGrad_pressure",
    ),
    "OneOf_GradientSchemesGrad_pressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_pressure_rgh",
        "OneOf_GradientSchemesGrad_pressureRgh",
    ),
    "OneOf_GradientSchemesGrad_rhok": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_rhok",
        "OneOf_GradientSchemesGrad_rhok",
    ),
    "OneOf_GradientSchemesGrad_temperature": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_temperature",
        "OneOf_GradientSchemesGrad_temperature",
    ),
    "OneOf_GradientSchemesGrad_turbulentKineticEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_turbulent_kinetic_energy",
        "OneOf_GradientSchemesGrad_turbulentKineticEnergy",
    ),
    "OneOf_GradientSchemesGrad_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_velocity",
        "OneOf_GradientSchemesGrad_velocity",
    ),
    "OneOf_HConstThermoEquationOfState": (
        "simscale_sdk_v1.models.simulation.one_of_h_const_thermo_equation_of_state",
        "OneOf_HConstThermoEquationOfState",
    ),
    "OneOf_HarmonicAccelerationResultControlItemHarmonicAccelerationType": (
        "simscale_sdk_v1.models.simulation.one_of__harmonic_acceleration_result_control_item_harmonic_acceleration_type",
        "OneOf_HarmonicAccelerationResultControlItemHarmonicAccelerationType",
    ),
    "OneOf_HarmonicAnalysisBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__harmonic_analysis_boundary_conditions",
        "OneOf_HarmonicAnalysisBoundaryConditions",
    ),
    "OneOf_HarmonicAnalysisConnectors": (
        "simscale_sdk_v1.models.simulation.one_of__harmonic_analysis_connectors",
        "OneOf_HarmonicAnalysisConnectors",
    ),
    "OneOf_HarmonicDisplacementResultControlItemHarmonicDisplacementType": (
        "simscale_sdk_v1.models.simulation.one_of__harmonic_displacement_result_control_item_harmonic_displacement_type",
        "OneOf_HarmonicDisplacementResultControlItemHarmonicDisplacementType",
    ),
    "OneOf_HarmonicResponseControlExcitationFrequencies": (
        "simscale_sdk_v1.models.simulation.one_of__harmonic_response_control_excitation_frequencies",
        "OneOf_HarmonicResponseControlExcitationFrequencies",
    ),
    "OneOf_HarmonicResponseResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__harmonic_response_result_control_item_field_selection",
        "OneOf_HarmonicResponseResultControlItemFieldSelection",
    ),
    "OneOf_HarmonicVelocityResultControlItemHarmonicVelocityType": (
        "simscale_sdk_v1.models.simulation.one_of__harmonic_velocity_result_control_item_harmonic_velocity_type",
        "OneOf_HarmonicVelocityResultControlItemHarmonicVelocityType",
    ),
    "OneOf_HeatExchangerSourceHeatExchangerMode": (
        "simscale_sdk_v1.models.simulation.one_of__heat_exchanger_source_heat_exchanger_mode",
        "OneOf_HeatExchangerSourceHeatExchangerMode",
    ),
    "OneOf_HeatTransferBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__heat_transfer_boundary_conditions",
        "OneOf_HeatTransferBoundaryConditions",
    ),
    "OneOf_HeatTransferTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__heat_transfer_time_dependency",
        "OneOf_HeatTransferTimeDependency",
    ),
    "OneOf_HingeConstraintBCAxisDefinition": (
        "simscale_sdk_v1.models.simulation.one_of__hinge_constraint_bc_axis_definition",
        "OneOf_HingeConstraintBCAxisDefinition",
    ),
    "OneOf_HyperElasticMaterialBehaviorHyperElasticModel": (
        "simscale_sdk_v1.models.simulation.one_of__hyper_elastic_material_behavior_hyper_elastic_model",
        "OneOf_HyperElasticMaterialBehaviorHyperElasticModel",
    ),
    "OneOf_HyperelasticityHyperelasticModelMarc": (
        "simscale_sdk_v1.models.simulation.one_of__hyperelasticity_hyperelastic_model_marc",
        "OneOf_HyperelasticityHyperelasticModelMarc",
    ),
    "OneOf_IRAMSorensenSubspaceSettings": (
        "simscale_sdk_v1.models.simulation.one_of_iram_sorensen_subspace_settings",
        "OneOf_IRAMSorensenSubspaceSettings",
    ),
    "OneOf_ImplicitTimeIntegrationTypeScheme": (
        "simscale_sdk_v1.models.simulation.one_of__implicit_time_integration_type_scheme",
        "OneOf_ImplicitTimeIntegrationTypeScheme",
    ),
    "OneOf_IncompressibleBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__incompressible_boundary_conditions",
        "OneOf_IncompressibleBoundaryConditions",
    ),
    "OneOf_IncompressibleMaterialFluidType": (
        "simscale_sdk_v1.models.simulation.one_of__incompressible_material_fluid_type",
        "OneOf_IncompressibleMaterialFluidType",
    ),
    "OneOf_IncompressibleMaterialViscosityModel": (
        "simscale_sdk_v1.models.simulation.one_of__incompressible_material_viscosity_model",
        "OneOf_IncompressibleMaterialViscosityModel",
    ),
    "OneOf_IncompressiblePacefishMeshSettingsNew": (
        "simscale_sdk_v1.models.simulation.one_of__incompressible_pacefish_mesh_settings_new",
        "OneOf_IncompressiblePacefishMeshSettingsNew",
    ),
    "OneOf_IncompressibleTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__incompressible_time_dependency",
        "OneOf_IncompressibleTimeDependency",
    ),
    "OneOf_InletOutletRHBCHumidityValue": (
        "simscale_sdk_v1.models.simulation.one_of__inlet_outlet_rhbc_humidity_value",
        "OneOf_InletOutletRHBCHumidityValue",
    ),
    "OneOf_InterpolationSchemesForDefault": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_for_default",
        "OneOf_InterpolationSchemesForDefault",
    ),
    "OneOf_InterpolationSchemesInterpolate_HbyA": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate__hby_a",
        "OneOf_InterpolationSchemesInterpolate_HbyA",
    ),
    "OneOf_InterpolationSchemesInterpolate_grad_enthalpy": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_grad_enthalpy",
        "OneOf_InterpolationSchemesInterpolate_grad_enthalpy",
    ),
    "OneOf_InterpolationSchemesInterpolate_kappa": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_kappa",
        "OneOf_InterpolationSchemesInterpolate_kappa",
    ),
    "OneOf_InterpolationSchemesInterpolate_map_Kappa": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_map__kappa",
        "OneOf_InterpolationSchemesInterpolate_map_Kappa",
    ),
    "OneOf_InterpolationSchemesInterpolate_rAU": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_r_au",
        "OneOf_InterpolationSchemesInterpolate_rAU",
    ),
    "OneOf_InterpolationSchemesInterpolate_rho": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho",
        "OneOf_InterpolationSchemesInterpolate_rho",
    ),
    "OneOf_InterpolationSchemesInterpolate_rho_0_velocity0": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho_0_velocity0",
        "OneOf_InterpolationSchemesInterpolate_rho_0_velocity0",
    ),
    "OneOf_InterpolationSchemesInterpolate_rho_Hbya": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho__hbya",
        "OneOf_InterpolationSchemesInterpolate_rho_Hbya",
    ),
    "OneOf_InterpolationSchemesInterpolate_rho_rAU": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho_r_au",
        "OneOf_InterpolationSchemesInterpolate_rho_rAU",
    ),
    "OneOf_InterpolationSchemesInterpolate_thermo_rho_Cp": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_thermo_rho__cp",
        "OneOf_InterpolationSchemesInterpolate_thermo_rho_Cp",
    ),
    "OneOf_InterpolationSchemesInterpolate_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_velocity",
        "OneOf_InterpolationSchemesInterpolate_velocity",
    ),
    "OneOf_InterpolationSchemesInterpolate_velocity0": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_velocity0",
        "OneOf_InterpolationSchemesInterpolate_velocity0",
    ),
    "OneOf_InterpolationSchemesReconstruct_rho": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_rho",
        "OneOf_InterpolationSchemesReconstruct_rho",
    ),
    "OneOf_InterpolationSchemesReconstruct_temperature": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_temperature",
        "OneOf_InterpolationSchemesReconstruct_temperature",
    ),
    "OneOf_InterpolationSchemesReconstruct_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_velocity",
        "OneOf_InterpolationSchemesReconstruct_velocity",
    ),
    "OneOf_IsotropicDirectionalDependencyPoissonsRatio": (
        "simscale_sdk_v1.models.simulation.one_of__isotropic_directional_dependency_poissons_ratio",
        "OneOf_IsotropicDirectionalDependencyPoissonsRatio",
    ),
    "OneOf_IsotropicPlasticHardeningPoissonsRatio": (
        "simscale_sdk_v1.models.simulation.one_of__isotropic_plastic_hardening_poissons_ratio",
        "OneOf_IsotropicPlasticHardeningPoissonsRatio",
    ),
    "OneOf_IsotropicSpringStiffnessStiffnessDefinition": (
        "simscale_sdk_v1.models.simulation.one_of__isotropic_spring_stiffness_stiffness_definition",
        "OneOf_IsotropicSpringStiffnessStiffnessDefinition",
    ),
    "OneOf_JohnsonCookElastoPlasticModelPoissonsRatio": (
        "simscale_sdk_v1.models.simulation.one_of__johnson_cook_elasto_plastic_model_poissons_ratio",
        "OneOf_JohnsonCookElastoPlasticModelPoissonsRatio",
    ),
    "OneOf_LanczosSubspaceSettings": (
        "simscale_sdk_v1.models.simulation.one_of__lanczos_subspace_settings",
        "OneOf_LanczosSubspaceSettings",
    ),
    "OneOf_LaplacianSchemesForDefault": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_for_default",
        "OneOf_LaplacianSchemesForDefault",
    ),
    "OneOf_LaplacianSchemesLaplacian_1A_U_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_1_a_u_pressure",
        "OneOf_LaplacianSchemesLaplacian_1A_U_pressure",
    ),
    "OneOf_LaplacianSchemesLaplacian_DREff_R": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_dr_eff_r",
        "OneOf_LaplacianSchemesLaplacian_DREff_R",
    ),
    "OneOf_LaplacianSchemesLaplacian_DT_passiveScalar": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_dt_passive_scalar",
        "OneOf_LaplacianSchemesLaplacian_DT_passiveScalar",
    ),
    "OneOf_LaplacianSchemesLaplacian_DepsilonEff_epsilonDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__depsilon_eff_epsilon_dissipation_rate",
        "OneOf_LaplacianSchemesLaplacian_DepsilonEff_epsilonDissipationRate",
    ),
    "OneOf_LaplacianSchemesLaplacian_DkEff_turbulentKineticEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dk_eff_turbulent_kinetic_energy",
        "OneOf_LaplacianSchemesLaplacian_DkEff_turbulentKineticEnergy",
    ),
    "OneOf_LaplacianSchemesLaplacian_DnuTildaEff_nuTilda": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dnu_tilda_eff_nu_tilda",
        "OneOf_LaplacianSchemesLaplacian_DnuTildaEff_nuTilda",
    ),
    "OneOf_LaplacianSchemesLaplacian_DomegaEff_omegaDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__domega_eff_omega_dissipation_rate",
        "OneOf_LaplacianSchemesLaplacian_DomegaEff_omegaDissipationRate",
    ),
    "OneOf_LaplacianSchemesLaplacian_Dp_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dp_pressure",
        "OneOf_LaplacianSchemesLaplacian_Dp_pressure",
    ),
    "OneOf_LaplacianSchemesLaplacian_NuEff_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__nu_eff_velocity",
        "OneOf_LaplacianSchemesLaplacian_NuEff_velocity",
    ),
    "OneOf_LaplacianSchemesLaplacian_Nu_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__nu_velocity",
        "OneOf_LaplacianSchemesLaplacian_Nu_velocity",
    ),
    "OneOf_LaplacianSchemesLaplacian_alphaEff_enthalpy": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_enthalpy",
        "OneOf_LaplacianSchemesLaplacian_alphaEff_enthalpy",
    ),
    "OneOf_LaplacianSchemesLaplacian_alphaEff_internalEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_internal_energy",
        "OneOf_LaplacianSchemesLaplacian_alphaEff_internalEnergy",
    ),
    "OneOf_LaplacianSchemesLaplacian_alphaEff_temperature": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_temperature",
        "OneOf_LaplacianSchemesLaplacian_alphaEff_temperature",
    ),
    "OneOf_LaplacianSchemesLaplacian_alpha_enthalpy": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_enthalpy",
        "OneOf_LaplacianSchemesLaplacian_alpha_enthalpy",
    ),
    "OneOf_LaplacianSchemesLaplacian_muEff_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_mu_eff_velocity",
        "OneOf_LaplacianSchemesLaplacian_muEff_velocity",
    ),
    "OneOf_LaplacianSchemesLaplacian_mut_velocity": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_mut_velocity",
        "OneOf_LaplacianSchemesLaplacian_mut_velocity",
    ),
    "OneOf_LaplacianSchemesLaplacian_rAUf_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_r_a_uf_pressure",
        "OneOf_LaplacianSchemesLaplacian_rAUf_pressure",
    ),
    "OneOf_LaplacianSchemesLaplacian_rAUf_pressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_r_a_uf_pressure_rgh",
        "OneOf_LaplacianSchemesLaplacian_rAUf_pressureRgh",
    ),
    "OneOf_LaplacianSchemesLaplacian_rho_1_A_U_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rho_1_a_u_pressure",
        "OneOf_LaplacianSchemesLaplacian_rho_1_A_U_pressure",
    ),
    "OneOf_LaplacianSchemesLaplacian_rhorAUf_pressure": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rhor_a_uf_pressure",
        "OneOf_LaplacianSchemesLaplacian_rhorAUf_pressure",
    ),
    "OneOf_LaplacianSchemesLaplacian_rhorAUf_pressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rhor_a_uf_pressure_rgh",
        "OneOf_LaplacianSchemesLaplacian_rhorAUf_pressureRgh",
    ),
    "OneOf_LinearElasticMarcMaterialBehaviorPoissonsRatio": (
        "simscale_sdk_v1.models.simulation.one_of__linear_elastic_marc_material_behavior_poissons_ratio",
        "OneOf_LinearElasticMarcMaterialBehaviorPoissonsRatio",
    ),
    "OneOf_LinearElasticMaterialBehaviorCreepFormulation": (
        "simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_creep_formulation",
        "OneOf_LinearElasticMaterialBehaviorCreepFormulation",
    ),
    "OneOf_LinearElasticMaterialBehaviorDamping": (
        "simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_damping",
        "OneOf_LinearElasticMaterialBehaviorDamping",
    ),
    "OneOf_LinearElasticMaterialBehaviorDirectionalDependency": (
        "simscale_sdk_v1.models.simulation.one_of__linear_elastic_material_behavior_directional_dependency",
        "OneOf_LinearElasticMaterialBehaviorDirectionalDependency",
    ),
    "OneOf_LitzWireCoilStrandCrossSectionType": (
        "simscale_sdk_v1.models.simulation.one_of__litz_wire_coil_strand_cross_section_type",
        "OneOf_LitzWireCoilStrandCrossSectionType",
    ),
    "OneOf_MULESSolverSemiImplicit": (
        "simscale_sdk_v1.models.simulation.one_of_mules_solver_semi_implicit",
        "OneOf_MULESSolverSemiImplicit",
    ),
    "OneOf_ManualSimericsMeshSettingsCellSizeSpecification": (
        "simscale_sdk_v1.models.simulation.one_of__manual_simerics_mesh_settings_cell_size_specification",
        "OneOf_ManualSimericsMeshSettingsCellSizeSpecification",
    ),
    "OneOf_ManualSimericsMeshSettingsRefinements": (
        "simscale_sdk_v1.models.simulation.one_of__manual_simerics_mesh_settings_refinements",
        "OneOf_ManualSimericsMeshSettingsRefinements",
    ),
    "OneOf_MarcAnalysisBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__marc_analysis_boundary_conditions",
        "OneOf_MarcAnalysisBoundaryConditions",
    ),
    "OneOf_MarcAverageFieldsCalculationResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__marc_average_fields_calculation_result_control_item_field_selection",
        "OneOf_MarcAverageFieldsCalculationResultControlItemFieldSelection",
    ),
    "OneOf_MarcBondedAndTouchingContactConnectionPositionTolerance": (
        "simscale_sdk_v1.models.simulation.one_of__marc_bonded_and_touching_contact_connection_position_tolerance",
        "OneOf_MarcBondedAndTouchingContactConnectionPositionTolerance",
    ),
    "OneOf_MarcBondedContactConnectionPositionTolerance": (
        "simscale_sdk_v1.models.simulation.one_of__marc_bonded_contact_connection_position_tolerance",
        "OneOf_MarcBondedContactConnectionPositionTolerance",
    ),
    "OneOf_MarcConnectionGroupConnections": (
        "simscale_sdk_v1.models.simulation.one_of__marc_connection_group_connections",
        "OneOf_MarcConnectionGroupConnections",
    ),
    "OneOf_MarcConnectorPointDataItemResults": (
        "simscale_sdk_v1.models.simulation.one_of__marc_connector_point_data_item_results",
        "OneOf_MarcConnectorPointDataItemResults",
    ),
    "OneOf_MarcContactFieldSelectionContactType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_contact_field_selection_contact_type",
        "OneOf_MarcContactFieldSelectionContactType",
    ),
    "OneOf_MarcContactForceFieldSelectionContactType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_contact_force_field_selection_contact_type",
        "OneOf_MarcContactForceFieldSelectionContactType",
    ),
    "OneOf_MarcContactResultControlItemContactType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_contact_result_control_item_contact_type",
        "OneOf_MarcContactResultControlItemContactType",
    ),
    "OneOf_MarcForceFieldSelectionForceType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_force_field_selection_force_type",
        "OneOf_MarcForceFieldSelectionForceType",
    ),
    "OneOf_MarcForceResultControlItemForceType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_force_result_control_item_force_type",
        "OneOf_MarcForceResultControlItemForceType",
    ),
    "OneOf_MarcLinearSolverSettingsLinearSolver": (
        "simscale_sdk_v1.models.simulation.one_of__marc_linear_solver_settings_linear_solver",
        "OneOf_MarcLinearSolverSettingsLinearSolver",
    ),
    "OneOf_MarcMaterialMarcMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.one_of__marc_material_marc_material_behavior",
        "OneOf_MarcMaterialMarcMaterialBehavior",
    ),
    "OneOf_MarcMinMaxFieldsCalculationResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__marc_min_max_fields_calculation_result_control_item_field_selection",
        "OneOf_MarcMinMaxFieldsCalculationResultControlItemFieldSelection",
    ),
    "OneOf_MarcNonlinearSolverSettingsConvergenceMethod": (
        "simscale_sdk_v1.models.simulation.one_of__marc_nonlinear_solver_settings_convergence_method",
        "OneOf_MarcNonlinearSolverSettingsConvergenceMethod",
    ),
    "OneOf_MarcOutputWritingContainerOutputWriting": (
        "simscale_sdk_v1.models.simulation.one_of__marc_output_writing_container_output_writing",
        "OneOf_MarcOutputWritingContainerOutputWriting",
    ),
    "OneOf_MarcResultControlAreaCalculation": (
        "simscale_sdk_v1.models.simulation.one_of__marc_result_control_area_calculation",
        "OneOf_MarcResultControlAreaCalculation",
    ),
    "OneOf_MarcResultControlSolutionFields": (
        "simscale_sdk_v1.models.simulation.one_of__marc_result_control_solution_fields",
        "OneOf_MarcResultControlSolutionFields",
    ),
    "OneOf_MarcResultControlVolumeCalculation": (
        "simscale_sdk_v1.models.simulation.one_of__marc_result_control_volume_calculation",
        "OneOf_MarcResultControlVolumeCalculation",
    ),
    "OneOf_MarcSimulationControlTimestepDefinition": (
        "simscale_sdk_v1.models.simulation.one_of__marc_simulation_control_timestep_definition",
        "OneOf_MarcSimulationControlTimestepDefinition",
    ),
    "OneOf_MarcStrainFieldSelectionStrainType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_strain_field_selection_strain_type",
        "OneOf_MarcStrainFieldSelectionStrainType",
    ),
    "OneOf_MarcStrainResultControlItemStrainType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_strain_result_control_item_strain_type",
        "OneOf_MarcStrainResultControlItemStrainType",
    ),
    "OneOf_MarcStressFieldSelectionStressType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_stress_field_selection_stress_type",
        "OneOf_MarcStressFieldSelectionStressType",
    ),
    "OneOf_MarcStressResultControlItemStressType": (
        "simscale_sdk_v1.models.simulation.one_of__marc_stress_result_control_item_stress_type",
        "OneOf_MarcStressResultControlItemStressType",
    ),
    "OneOf_MarcSumFieldsCalculationResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__marc_sum_fields_calculation_result_control_item_field_selection",
        "OneOf_MarcSumFieldsCalculationResultControlItemFieldSelection",
    ),
    "OneOf_MinMaxFieldsCalculationResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__min_max_fields_calculation_result_control_item_field_selection",
        "OneOf_MinMaxFieldsCalculationResultControlItemFieldSelection",
    ),
    "OneOf_ModalBaseControlEigenfrequencyScope": (
        "simscale_sdk_v1.models.simulation.one_of__modal_base_control_eigenfrequency_scope",
        "OneOf_ModalBaseControlEigenfrequencyScope",
    ),
    "OneOf_ModalSolverEigenSolver": (
        "simscale_sdk_v1.models.simulation.one_of__modal_solver_eigen_solver",
        "OneOf_ModalSolverEigenSolver",
    ),
    "OneOf_ModalSolverSolver": (
        "simscale_sdk_v1.models.simulation.one_of__modal_solver_solver",
        "OneOf_ModalSolverSolver",
    ),
    "OneOf_MomentFieldSelectionMomentType": (
        "simscale_sdk_v1.models.simulation.one_of__moment_field_selection_moment_type",
        "OneOf_MomentFieldSelectionMomentType",
    ),
    "OneOf_MrtSolarParametersFractionBodySurface": (
        "simscale_sdk_v1.models.simulation.one_of__mrt_solar_parameters_fraction_body_surface",
        "OneOf_MrtSolarParametersFractionBodySurface",
    ),
    "OneOf_MultilinearModelMarcHardeningRule": (
        "simscale_sdk_v1.models.simulation.one_of__multilinear_model_marc_hardening_rule",
        "OneOf_MultilinearModelMarcHardeningRule",
    ),
    "OneOf_MultiphaseBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__multiphase_boundary_conditions",
        "OneOf_MultiphaseBoundaryConditions",
    ),
    "OneOf_NaturalConvectionInletOutletBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_net_radiative_heat_flux",
        "OneOf_NaturalConvectionInletOutletBCNetRadiativeHeatFlux",
    ),
    "OneOf_NaturalConvectionInletOutletBCPressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_pressure_rgh",
        "OneOf_NaturalConvectionInletOutletBCPressureRgh",
    ),
    "OneOf_NaturalConvectionInletOutletBCTurbulence": (
        "simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_turbulence",
        "OneOf_NaturalConvectionInletOutletBCTurbulence",
    ),
    "OneOf_NewRegionRefinementPacefishV38MeshSizing": (
        "simscale_sdk_v1.models.simulation.one_of__new_region_refinement_pacefish_v38_mesh_sizing",
        "OneOf_NewRegionRefinementPacefishV38MeshSizing",
    ),
    "OneOf_NewSurfaceRefinementPacefishV38MeshSizing": (
        "simscale_sdk_v1.models.simulation.one_of__new_surface_refinement_pacefish_v38_mesh_sizing",
        "OneOf_NewSurfaceRefinementPacefishV38MeshSizing",
    ),
    "OneOf_NewtonKrylovResolutionTypeConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.one_of__newton_krylov_resolution_type_convergence_criteria",
        "OneOf_NewtonKrylovResolutionTypeConvergenceCriteria",
    ),
    "OneOf_NewtonKrylovResolutionTypeJacobianMatrix": (
        "simscale_sdk_v1.models.simulation.one_of__newton_krylov_resolution_type_jacobian_matrix",
        "OneOf_NewtonKrylovResolutionTypeJacobianMatrix",
    ),
    "OneOf_NewtonResolutionTypeConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.one_of__newton_resolution_type_convergence_criteria",
        "OneOf_NewtonResolutionTypeConvergenceCriteria",
    ),
    "OneOf_NewtonResolutionTypeJacobianMatrix": (
        "simscale_sdk_v1.models.simulation.one_of__newton_resolution_type_jacobian_matrix",
        "OneOf_NewtonResolutionTypeJacobianMatrix",
    ),
    "OneOf_NoSlipVBCNoSlipWallRoughnessType": (
        "simscale_sdk_v1.models.simulation.one_of__no_slip_vbc_no_slip_wall_roughness_type",
        "OneOf_NoSlipVBCNoSlipWallRoughnessType",
    ),
    "OneOf_NonMonotomousResidualRetimingEventTimestepCalculationType": (
        "simscale_sdk_v1.models.simulation.one_of__non_monotomous_residual_retiming_event_timestep_calculation_type",
        "OneOf_NonMonotomousResidualRetimingEventTimestepCalculationType",
    ),
    "OneOf_OgdenHyperElasticModelOrder": (
        "simscale_sdk_v1.models.simulation.one_of__ogden_hyper_elastic_model_order",
        "OneOf_OgdenHyperElasticModelOrder",
    ),
    "OneOf_OgdenHyperelasticModelMarcNumberOfTerms": (
        "simscale_sdk_v1.models.simulation.one_of__ogden_hyperelastic_model_marc_number_of_terms",
        "OneOf_OgdenHyperelasticModelMarcNumberOfTerms",
    ),
    "OneOf_OrthotropicDirectionalDependencyPoissonsRatioXY": (
        "simscale_sdk_v1.models.simulation.one_of__orthotropic_directional_dependency_poissons_ratio_xy",
        "OneOf_OrthotropicDirectionalDependencyPoissonsRatioXY",
    ),
    "OneOf_OrthotropicDirectionalDependencyPoissonsRatioXZ": (
        "simscale_sdk_v1.models.simulation.one_of__orthotropic_directional_dependency_poissons_ratio_xz",
        "OneOf_OrthotropicDirectionalDependencyPoissonsRatioXZ",
    ),
    "OneOf_OrthotropicDirectionalDependencyPoissonsRatioYZ": (
        "simscale_sdk_v1.models.simulation.one_of__orthotropic_directional_dependency_poissons_ratio_yz",
        "OneOf_OrthotropicDirectionalDependencyPoissonsRatioYZ",
    ),
    "OneOf_OrthotropicSpringStiffnessStiffnessDefinition": (
        "simscale_sdk_v1.models.simulation.one_of__orthotropic_spring_stiffness_stiffness_definition",
        "OneOf_OrthotropicSpringStiffnessStiffnessDefinition",
    ),
    "OneOf_PBICGSolverPreconditioner": (
        "simscale_sdk_v1.models.simulation.one_of_pbicg_solver_preconditioner",
        "OneOf_PBICGSolverPreconditioner",
    ),
    "OneOf_PBICGStabSolverPreconditioner": (
        "simscale_sdk_v1.models.simulation.one_of_pbicg_stab_solver_preconditioner",
        "OneOf_PBICGStabSolverPreconditioner",
    ),
    "OneOf_PCGSolverPreconditioner": (
        "simscale_sdk_v1.models.simulation.one_of_pcg_solver_preconditioner",
        "OneOf_PCGSolverPreconditioner",
    ),
    "OneOf_PacefishAutomeshAutomaticGapClosing": (
        "simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_automatic_gap_closing",
        "OneOf_PacefishAutomeshAutomaticGapClosing",
    ),
    "OneOf_PacefishAutomeshNewFineness": (
        "simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_new_fineness",
        "OneOf_PacefishAutomeshNewFineness",
    ),
    "OneOf_PacefishAutomeshPrimaryTopology": (
        "simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_primary_topology",
        "OneOf_PacefishAutomeshPrimaryTopology",
    ),
    "OneOf_PacefishAutomeshReferenceLengthComputation": (
        "simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_reference_length_computation",
        "OneOf_PacefishAutomeshReferenceLengthComputation",
    ),
    "OneOf_PacefishAutomeshRefinements": (
        "simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_refinements",
        "OneOf_PacefishAutomeshRefinements",
    ),
    "OneOf_PacefishAutomeshReynoldsScalingType": (
        "simscale_sdk_v1.models.simulation.one_of__pacefish_automesh_reynolds_scaling_type",
        "OneOf_PacefishAutomeshReynoldsScalingType",
    ),
    "OneOf_PacefishMeshLegacyRefinements": (
        "simscale_sdk_v1.models.simulation.one_of__pacefish_mesh_legacy_refinements",
        "OneOf_PacefishMeshLegacyRefinements",
    ),
    "OneOf_PartialVectorFunctionX": (
        "simscale_sdk_v1.models.simulation.one_of__partial_vector_function_x",
        "OneOf_PartialVectorFunctionX",
    ),
    "OneOf_PartialVectorFunctionY": (
        "simscale_sdk_v1.models.simulation.one_of__partial_vector_function_y",
        "OneOf_PartialVectorFunctionY",
    ),
    "OneOf_PartialVectorFunctionZ": (
        "simscale_sdk_v1.models.simulation.one_of__partial_vector_function_z",
        "OneOf_PartialVectorFunctionZ",
    ),
    "OneOf_PedestrianComfortSurfaceGround": (
        "simscale_sdk_v1.models.simulation.one_of__pedestrian_comfort_surface_ground",
        "OneOf_PedestrianComfortSurfaceGround",
    ),
    "OneOf_PenaltyMethodContactStiffness": (
        "simscale_sdk_v1.models.simulation.one_of__penalty_method_contact_stiffness",
        "OneOf_PenaltyMethodContactStiffness",
    ),
    "OneOf_PerforatedPlatePorousMediaHeatTransfer": (
        "simscale_sdk_v1.models.simulation.one_of__perforated_plate_porous_media_heat_transfer",
        "OneOf_PerforatedPlatePorousMediaHeatTransfer",
    ),
    "OneOf_PermanentMagnetMaterialMagnetizationDirectionType": (
        "simscale_sdk_v1.models.simulation.one_of__permanent_magnet_material_magnetization_direction_type",
        "OneOf_PermanentMagnetMaterialMagnetizationDirectionType",
    ),
    "OneOf_PhysicalContactConnections": (
        "simscale_sdk_v1.models.simulation.one_of__physical_contact_connections",
        "OneOf_PhysicalContactConnections",
    ),
    "OneOf_PinKinematicBehaviorAxialTranslation": (
        "simscale_sdk_v1.models.simulation.one_of__pin_kinematic_behavior_axial_translation",
        "OneOf_PinKinematicBehaviorAxialTranslation",
    ),
    "OneOf_PinKinematicBehaviorRotation": (
        "simscale_sdk_v1.models.simulation.one_of__pin_kinematic_behavior_rotation",
        "OneOf_PinKinematicBehaviorRotation",
    ),
    "OneOf_PlasticMaterialBehaviorElastoPlasticModel": (
        "simscale_sdk_v1.models.simulation.one_of__plastic_material_behavior_elasto_plastic_model",
        "OneOf_PlasticMaterialBehaviorElastoPlasticModel",
    ),
    "OneOf_PlasticityMarcPlasticityModel": (
        "simscale_sdk_v1.models.simulation.one_of__plasticity_marc_plasticity_model",
        "OneOf_PlasticityMarcPlasticityModel",
    ),
    "OneOf_PlateDataHoleShape": (
        "simscale_sdk_v1.models.simulation.one_of__plate_data_hole_shape",
        "OneOf_PlateDataHoleShape",
    ),
    "OneOf_PorousTreeTreeType": (
        "simscale_sdk_v1.models.simulation.one_of__porous_tree_tree_type",
        "OneOf_PorousTreeTreeType",
    ),
    "OneOf_PowerLawMediumPorousMediaHeatTransfer": (
        "simscale_sdk_v1.models.simulation.one_of__power_law_medium_porous_media_heat_transfer",
        "OneOf_PowerLawMediumPorousMediaHeatTransfer",
    ),
    "OneOf_PrandtlLesDeltaDeltaCoefficient": (
        "simscale_sdk_v1.models.simulation.one_of__prandtl_les_delta_delta_coefficient",
        "OneOf_PrandtlLesDeltaDeltaCoefficient",
    ),
    "OneOf_PrescribedOptionalFunctionValue": (
        "simscale_sdk_v1.models.simulation.one_of__prescribed_optional_function_value",
        "OneOf_PrescribedOptionalFunctionValue",
    ),
    "OneOf_PressureInletBCGaugePressure": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_gauge_pressure",
        "OneOf_PressureInletBCGaugePressure",
    ),
    "OneOf_PressureInletBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_net_radiative_heat_flux",
        "OneOf_PressureInletBCNetRadiativeHeatFlux",
    ),
    "OneOf_PressureInletBCPressure": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_pressure",
        "OneOf_PressureInletBCPressure",
    ),
    "OneOf_PressureInletBCPressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_pressure_rgh",
        "OneOf_PressureInletBCPressureRgh",
    ),
    "OneOf_PressureInletBCRadiativeIntensityRay": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_radiative_intensity_ray",
        "OneOf_PressureInletBCRadiativeIntensityRay",
    ),
    "OneOf_PressureInletBCTemperature": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_temperature",
        "OneOf_PressureInletBCTemperature",
    ),
    "OneOf_PressureInletBCTurbulence": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_turbulence",
        "OneOf_PressureInletBCTurbulence",
    ),
    "OneOf_PressureLossCurvePorousMediaHeatTransfer": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_loss_curve_porous_media_heat_transfer",
        "OneOf_PressureLossCurvePorousMediaHeatTransfer",
    ),
    "OneOf_PressureLossFunctionMediumPorousMaterialType": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_loss_function_medium_porous_material_type",
        "OneOf_PressureLossFunctionMediumPorousMaterialType",
    ),
    "OneOf_PressureOutletBCGaugePressure": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_gauge_pressure",
        "OneOf_PressureOutletBCGaugePressure",
    ),
    "OneOf_PressureOutletBCGaugePressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_gauge_pressure_rgh",
        "OneOf_PressureOutletBCGaugePressureRgh",
    ),
    "OneOf_PressureOutletBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_net_radiative_heat_flux",
        "OneOf_PressureOutletBCNetRadiativeHeatFlux",
    ),
    "OneOf_PressureOutletBCPhaseFractionsV2": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_phase_fractions_v2",
        "OneOf_PressureOutletBCPhaseFractionsV2",
    ),
    "OneOf_PressureOutletBCPressure": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_pressure",
        "OneOf_PressureOutletBCPressure",
    ),
    "OneOf_PressureOutletBCPressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_pressure_rgh",
        "OneOf_PressureOutletBCPressureRgh",
    ),
    "OneOf_PressureOutletBCRadiativeIntensityRay": (
        "simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_radiative_intensity_ray",
        "OneOf_PressureOutletBCRadiativeIntensityRay",
    ),
    "OneOf_PrimaryNetworkDamageModelPrimaryNetwork": (
        "simscale_sdk_v1.models.simulation.one_of__primary_network_damage_model_primary_network",
        "OneOf_PrimaryNetworkDamageModelPrimaryNetwork",
    ),
    "OneOf_ProbePointsResultControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__probe_points_result_control_write_control",
        "OneOf_ProbePointsResultControlWriteControl",
    ),
    "OneOf_RegionInterfaceInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.one_of__region_interface_interface_thermal",
        "OneOf_RegionInterfaceInterfaceThermal",
    ),
    "OneOf_RegionRefinementEBMRefinement": (
        "simscale_sdk_v1.models.simulation.one_of__region_refinement_ebm_refinement",
        "OneOf_RegionRefinementEBMRefinement",
    ),
    "OneOf_RegionRefinementWindComfortNewFineness": (
        "simscale_sdk_v1.models.simulation.one_of__region_refinement_wind_comfort_new_fineness",
        "OneOf_RegionRefinementWindComfortNewFineness",
    ),
    "OneOf_ResidualsConvergenceMethodConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.one_of__residuals_convergence_method_convergence_criteria",
        "OneOf_ResidualsConvergenceMethodConvergenceCriteria",
    ),
    "OneOf_ResidualsOrDisplacementsConvergenceMethodConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.one_of__residuals_or_displacements_convergence_method_convergence_criteria",
        "OneOf_ResidualsOrDisplacementsConvergenceMethodConvergenceCriteria",
    ),
    "OneOf_RestrictedDimensionalFunction_FrequencyValue": (
        "simscale_sdk_v1.models.simulation.one_of__restricted_dimensional_function__frequency_value",
        "OneOf_RestrictedDimensionalFunction_FrequencyValue",
    ),
    "OneOf_RestrictedDimensionalFunction_TimeValue": (
        "simscale_sdk_v1.models.simulation.one_of__restricted_dimensional_function__time_value",
        "OneOf_RestrictedDimensionalFunction_TimeValue",
    ),
    "OneOf_RotatingMotionTypeRotation": (
        "simscale_sdk_v1.models.simulation.one_of__rotating_motion_type_rotation",
        "OneOf_RotatingMotionTypeRotation",
    ),
    "OneOf_RotatingSBMRotation": (
        "simscale_sdk_v1.models.simulation.one_of__rotating_sbm_rotation",
        "OneOf_RotatingSBMRotation",
    ),
    "OneOf_ScalarTransportResultControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__scalar_transport_result_control_write_control",
        "OneOf_ScalarTransportResultControlWriteControl",
    ),
    "OneOf_SimericsAnalysisBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__simerics_analysis_boundary_conditions",
        "OneOf_SimericsAnalysisBoundaryConditions",
    ),
    "OneOf_SimericsAnalysisMeshSettings": (
        "simscale_sdk_v1.models.simulation.one_of__simerics_analysis_mesh_settings",
        "OneOf_SimericsAnalysisMeshSettings",
    ),
    "OneOf_SimericsAnalysisTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__simerics_analysis_time_dependency",
        "OneOf_SimericsAnalysisTimeDependency",
    ),
    "OneOf_SimericsMaterialsFluids": (
        "simscale_sdk_v1.models.simulation.one_of__simerics_materials_fluids",
        "OneOf_SimericsMaterialsFluids",
    ),
    "OneOf_SlidingContactPositionTolerance": (
        "simscale_sdk_v1.models.simulation.one_of__sliding_contact_position_tolerance",
        "OneOf_SlidingContactPositionTolerance",
    ),
    "OneOf_SolarCalculatorSolarLoad": (
        "simscale_sdk_v1.models.simulation.one_of__solar_calculator_solar_load",
        "OneOf_SolarCalculatorSolarLoad",
    ),
    "OneOf_SolarCalculatorSunDirection": (
        "simscale_sdk_v1.models.simulation.one_of__solar_calculator_sun_direction",
        "OneOf_SolarCalculatorSunDirection",
    ),
    "OneOf_SolidCompressibleMaterialElectricConductivityType": (
        "simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_electric_conductivity_type",
        "OneOf_SolidCompressibleMaterialElectricConductivityType",
    ),
    "OneOf_SolidCompressibleMaterialRadiativeBehavior": (
        "simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_radiative_behavior",
        "OneOf_SolidCompressibleMaterialRadiativeBehavior",
    ),
    "OneOf_SolidCompressibleMaterialTransport": (
        "simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_transport",
        "OneOf_SolidCompressibleMaterialTransport",
    ),
    "OneOf_SolidMaterialConductivity": (
        "simscale_sdk_v1.models.simulation.one_of__solid_material_conductivity",
        "OneOf_SolidMaterialConductivity",
    ),
    "OneOf_SolidMaterialMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.one_of__solid_material_material_behavior",
        "OneOf_SolidMaterialMaterialBehavior",
    ),
    "OneOf_SolidNumericsEigenSolver": (
        "simscale_sdk_v1.models.simulation.one_of__solid_numerics_eigen_solver",
        "OneOf_SolidNumericsEigenSolver",
    ),
    "OneOf_SolidNumericsMechanicalLineSearch": (
        "simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_line_search",
        "OneOf_SolidNumericsMechanicalLineSearch",
    ),
    "OneOf_SolidNumericsMechanicalResolutionType": (
        "simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_resolution_type",
        "OneOf_SolidNumericsMechanicalResolutionType",
    ),
    "OneOf_SolidNumericsMechanicalTimeIntegrationType": (
        "simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_time_integration_type",
        "OneOf_SolidNumericsMechanicalTimeIntegrationType",
    ),
    "OneOf_SolidNumericsSolver": (
        "simscale_sdk_v1.models.simulation.one_of__solid_numerics_solver",
        "OneOf_SolidNumericsSolver",
    ),
    "OneOf_SolidNumericsThermalLineSearch": (
        "simscale_sdk_v1.models.simulation.one_of__solid_numerics_thermal_line_search",
        "OneOf_SolidNumericsThermalLineSearch",
    ),
    "OneOf_SolidNumericsThermalResolutionType": (
        "simscale_sdk_v1.models.simulation.one_of__solid_numerics_thermal_resolution_type",
        "OneOf_SolidNumericsThermalResolutionType",
    ),
    "OneOf_SolidResultControlAreaCalculation": (
        "simscale_sdk_v1.models.simulation.one_of__solid_result_control_area_calculation",
        "OneOf_SolidResultControlAreaCalculation",
    ),
    "OneOf_SolidResultControlEdgeCalculation": (
        "simscale_sdk_v1.models.simulation.one_of__solid_result_control_edge_calculation",
        "OneOf_SolidResultControlEdgeCalculation",
    ),
    "OneOf_SolidResultControlPointData": (
        "simscale_sdk_v1.models.simulation.one_of__solid_result_control_point_data",
        "OneOf_SolidResultControlPointData",
    ),
    "OneOf_SolidResultControlSolutionFields": (
        "simscale_sdk_v1.models.simulation.one_of__solid_result_control_solution_fields",
        "OneOf_SolidResultControlSolutionFields",
    ),
    "OneOf_SolidResultControlVolumeCalculation": (
        "simscale_sdk_v1.models.simulation.one_of__solid_result_control_volume_calculation",
        "OneOf_SolidResultControlVolumeCalculation",
    ),
    "OneOf_SolidSimulationControlEigenfrequencyScope": (
        "simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_eigenfrequency_scope",
        "OneOf_SolidSimulationControlEigenfrequencyScope",
    ),
    "OneOf_SolidSimulationControlExcitationFrequencies": (
        "simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_excitation_frequencies",
        "OneOf_SolidSimulationControlExcitationFrequencies",
    ),
    "OneOf_SolidSimulationControlPseudoTimeStepping": (
        "simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_pseudo_time_stepping",
        "OneOf_SolidSimulationControlPseudoTimeStepping",
    ),
    "OneOf_SolidSimulationControlTimestepDefinition": (
        "simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_timestep_definition",
        "OneOf_SolidSimulationControlTimestepDefinition",
    ),
    "OneOf_SolidSimulationControlWriteControlDefinition": (
        "simscale_sdk_v1.models.simulation.one_of__solid_simulation_control_write_control_definition",
        "OneOf_SolidSimulationControlWriteControlDefinition",
    ),
    "OneOf_SpatialDiscretizationSchemesDensity": (
        "simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_density",
        "OneOf_SpatialDiscretizationSchemesDensity",
    ),
    "OneOf_SpatialDiscretizationSchemesGasMixtureTransport": (
        "simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_gas_mixture_transport",
        "OneOf_SpatialDiscretizationSchemesGasMixtureTransport",
    ),
    "OneOf_SpatialDiscretizationSchemesInternalEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_internal_energy",
        "OneOf_SpatialDiscretizationSchemesInternalEnergy",
    ),
    "OneOf_SpatialDiscretizationSchemesTurbulentEnergyDissipationRate": (
        "simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_turbulent_energy_dissipation_rate",
        "OneOf_SpatialDiscretizationSchemesTurbulentEnergyDissipationRate",
    ),
    "OneOf_SpatialDiscretizationSchemesTurbulentKineticEnergy": (
        "simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_turbulent_kinetic_energy",
        "OneOf_SpatialDiscretizationSchemesTurbulentKineticEnergy",
    ),
    "OneOf_SpatialDiscretizationSchemesVelocity": (
        "simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_velocity",
        "OneOf_SpatialDiscretizationSchemesVelocity",
    ),
    "OneOf_SpatialDiscretizationSchemesVolumeOfFluid": (
        "simscale_sdk_v1.models.simulation.one_of__spatial_discretization_schemes_volume_of_fluid",
        "OneOf_SpatialDiscretizationSchemesVolumeOfFluid",
    ),
    "OneOf_StaticAnalysisBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__static_analysis_boundary_conditions",
        "OneOf_StaticAnalysisBoundaryConditions",
    ),
    "OneOf_StaticAnalysisConnectionGroups": (
        "simscale_sdk_v1.models.simulation.one_of__static_analysis_connection_groups",
        "OneOf_StaticAnalysisConnectionGroups",
    ),
    "OneOf_StaticAnalysisConnectors": (
        "simscale_sdk_v1.models.simulation.one_of__static_analysis_connectors",
        "OneOf_StaticAnalysisConnectors",
    ),
    "OneOf_StatisticalAveragingResultControlV2SamplingInterval": (
        "simscale_sdk_v1.models.simulation.one_of__statistical_averaging_result_control_v2_sampling_interval",
        "OneOf_StatisticalAveragingResultControlV2SamplingInterval",
    ),
    "OneOf_StrainFieldSelectionStrainType": (
        "simscale_sdk_v1.models.simulation.one_of__strain_field_selection_strain_type",
        "OneOf_StrainFieldSelectionStrainType",
    ),
    "OneOf_StrainResultControlItemStrainType": (
        "simscale_sdk_v1.models.simulation.one_of__strain_result_control_item_strain_type",
        "OneOf_StrainResultControlItemStrainType",
    ),
    "OneOf_StressFieldSelectionStressType": (
        "simscale_sdk_v1.models.simulation.one_of__stress_field_selection_stress_type",
        "OneOf_StressFieldSelectionStressType",
    ),
    "OneOf_StressResultControlItemStressType": (
        "simscale_sdk_v1.models.simulation.one_of__stress_result_control_item_stress_type",
        "OneOf_StressResultControlItemStressType",
    ),
    "OneOf_StressTensor_PressureSigmaXX": (
        "simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xx",
        "OneOf_StressTensor_PressureSigmaXX",
    ),
    "OneOf_StressTensor_PressureSigmaXY": (
        "simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xy",
        "OneOf_StressTensor_PressureSigmaXY",
    ),
    "OneOf_StressTensor_PressureSigmaXZ": (
        "simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_xz",
        "OneOf_StressTensor_PressureSigmaXZ",
    ),
    "OneOf_StressTensor_PressureSigmaYY": (
        "simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_yy",
        "OneOf_StressTensor_PressureSigmaYY",
    ),
    "OneOf_StressTensor_PressureSigmaYZ": (
        "simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_yz",
        "OneOf_StressTensor_PressureSigmaYZ",
    ),
    "OneOf_StressTensor_PressureSigmaZZ": (
        "simscale_sdk_v1.models.simulation.one_of__stress_tensor__pressure_sigma_zz",
        "OneOf_StressTensor_PressureSigmaZZ",
    ),
    "OneOf_SumFieldsCalculationResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__sum_fields_calculation_result_control_item_field_selection",
        "OneOf_SumFieldsCalculationResultControlItemFieldSelection",
    ),
    "OneOf_SurfaceNormalGradientSchemesForDefault": (
        "simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_for_default",
        "OneOf_SurfaceNormalGradientSchemesForDefault",
    ),
    "OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_pressureRgh": (
        "simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_pressure_rgh",
        "OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_pressureRgh",
    ),
    "OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rho": (
        "simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_rho",
        "OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rho",
    ),
    "OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rhok": (
        "simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_rhok",
        "OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rhok",
    ),
    "OneOf_SurfaceRefinementWindComfortNewFineness": (
        "simscale_sdk_v1.models.simulation.one_of__surface_refinement_wind_comfort_new_fineness",
        "OneOf_SurfaceRefinementWindComfortNewFineness",
    ),
    "OneOf_SurfaceRoughnessModelSurfaceRoughnessType": (
        "simscale_sdk_v1.models.simulation.one_of__surface_roughness_model_surface_roughness_type",
        "OneOf_SurfaceRoughnessModelSurfaceRoughnessType",
    ),
    "OneOf_SutherlandTransportThermo": (
        "simscale_sdk_v1.models.simulation.one_of__sutherland_transport_thermo",
        "OneOf_SutherlandTransportThermo",
    ),
    "OneOf_TangentJacobianMatrixChangeJacobianMatrix": (
        "simscale_sdk_v1.models.simulation.one_of__tangent_jacobian_matrix_change_jacobian_matrix",
        "OneOf_TangentJacobianMatrixChangeJacobianMatrix",
    ),
    "OneOf_TemporalResponseResultControlItemFieldSelection": (
        "simscale_sdk_v1.models.simulation.one_of__temporal_response_result_control_item_field_selection",
        "OneOf_TemporalResponseResultControlItemFieldSelection",
    ),
    "OneOf_ThermalMechanicalBoundaryConditions": (
        "simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_boundary_conditions",
        "OneOf_ThermalMechanicalBoundaryConditions",
    ),
    "OneOf_ThermalMechanicalConnectionGroups": (
        "simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_connection_groups",
        "OneOf_ThermalMechanicalConnectionGroups",
    ),
    "OneOf_ThermalMechanicalTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__thermal_mechanical_time_dependency",
        "OneOf_ThermalMechanicalTimeDependency",
    ),
    "OneOf_TimeDifferentiationSchemesForDefault": (
        "simscale_sdk_v1.models.simulation.one_of__time_differentiation_schemes_for_default",
        "OneOf_TimeDifferentiationSchemesForDefault",
    ),
    "OneOf_TimeHarmonicMagneticsTimeDependency": (
        "simscale_sdk_v1.models.simulation.one_of__time_harmonic_magnetics_time_dependency",
        "OneOf_TimeHarmonicMagneticsTimeDependency",
    ),
    "OneOf_TransientResultControlWriteControl": (
        "simscale_sdk_v1.models.simulation.one_of__transient_result_control_write_control",
        "OneOf_TransientResultControlWriteControl",
    ),
    "OneOf_TrueSemiImplicitSolver": (
        "simscale_sdk_v1.models.simulation.one_of__true_semi_implicit_solver",
        "OneOf_TrueSemiImplicitSolver",
    ),
    "OneOf_TurbulentHeatFluxTBCHeatSource": (
        "simscale_sdk_v1.models.simulation.one_of__turbulent_heat_flux_tbc_heat_source",
        "OneOf_TurbulentHeatFluxTBCHeatSource",
    ),
    "OneOf_VelocityFieldSelectionVelocityType": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_field_selection_velocity_type",
        "OneOf_VelocityFieldSelectionVelocityType",
    ),
    "OneOf_VelocityInletBCDissipationType": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_dissipation_type",
        "OneOf_VelocityInletBCDissipationType",
    ),
    "OneOf_VelocityInletBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_net_radiative_heat_flux",
        "OneOf_VelocityInletBCNetRadiativeHeatFlux",
    ),
    "OneOf_VelocityInletBCRadiativeIntensityRay": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_radiative_intensity_ray",
        "OneOf_VelocityInletBCRadiativeIntensityRay",
    ),
    "OneOf_VelocityInletBCTemperature": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_temperature",
        "OneOf_VelocityInletBCTemperature",
    ),
    "OneOf_VelocityInletBCTurbulence": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_turbulence",
        "OneOf_VelocityInletBCTurbulence",
    ),
    "OneOf_VelocityInletBCTurbulenceIntensity": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_turbulence_intensity",
        "OneOf_VelocityInletBCTurbulenceIntensity",
    ),
    "OneOf_VelocityInletBCVelocity": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_velocity",
        "OneOf_VelocityInletBCVelocity",
    ),
    "OneOf_VelocityOutletBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_net_radiative_heat_flux",
        "OneOf_VelocityOutletBCNetRadiativeHeatFlux",
    ),
    "OneOf_VelocityOutletBCPhaseFraction": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_phase_fraction",
        "OneOf_VelocityOutletBCPhaseFraction",
    ),
    "OneOf_VelocityOutletBCPhaseFractionsV2": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_phase_fractions_v2",
        "OneOf_VelocityOutletBCPhaseFractionsV2",
    ),
    "OneOf_VelocityOutletBCRadiativeIntensityRay": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_radiative_intensity_ray",
        "OneOf_VelocityOutletBCRadiativeIntensityRay",
    ),
    "OneOf_VelocityOutletBCVelocity": (
        "simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_velocity",
        "OneOf_VelocityOutletBCVelocity",
    ),
    "OneOf_ViscoelasticNetworkCreepModelViscoelasticNetwork": (
        "simscale_sdk_v1.models.simulation.one_of__viscoelastic_network_creep_model_viscoelastic_network",
        "OneOf_ViscoelasticNetworkCreepModelViscoelasticNetwork",
    ),
    "OneOf_VoltageExcitationVoltageType": (
        "simscale_sdk_v1.models.simulation.one_of__voltage_excitation_voltage_type",
        "OneOf_VoltageExcitationVoltageType",
    ),
    "OneOf_WallBCElectricBoundaryCondition": (
        "simscale_sdk_v1.models.simulation.one_of__wall_bc_electric_boundary_condition",
        "OneOf_WallBCElectricBoundaryCondition",
    ),
    "OneOf_WallBCNetRadiativeHeatFlux": (
        "simscale_sdk_v1.models.simulation.one_of__wall_bc_net_radiative_heat_flux",
        "OneOf_WallBCNetRadiativeHeatFlux",
    ),
    "OneOf_WallBCPhaseFraction": (
        "simscale_sdk_v1.models.simulation.one_of__wall_bc_phase_fraction",
        "OneOf_WallBCPhaseFraction",
    ),
    "OneOf_WallBCRadiativeIntensityRay": (
        "simscale_sdk_v1.models.simulation.one_of__wall_bc_radiative_intensity_ray",
        "OneOf_WallBCRadiativeIntensityRay",
    ),
    "OneOf_WallBCRelativeHumidity": (
        "simscale_sdk_v1.models.simulation.one_of__wall_bc_relative_humidity",
        "OneOf_WallBCRelativeHumidity",
    ),
    "OneOf_WallBCTemperature": (
        "simscale_sdk_v1.models.simulation.one_of__wall_bc_temperature",
        "OneOf_WallBCTemperature",
    ),
    "OneOf_WallBCVelocity": ("simscale_sdk_v1.models.simulation.one_of__wall_bc_velocity", "OneOf_WallBCVelocity"),
    "OneOf_WindComfortMeshAutomaticGapClosing": (
        "simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_automatic_gap_closing",
        "OneOf_WindComfortMeshAutomaticGapClosing",
    ),
    "OneOf_WindComfortMeshRefinements": (
        "simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_refinements",
        "OneOf_WindComfortMeshRefinements",
    ),
    "OneOf_WindComfortMeshReynoldsScalingType": (
        "simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_reynolds_scaling_type",
        "OneOf_WindComfortMeshReynoldsScalingType",
    ),
    "OneOf_WindComfortMeshWindComfortFineness": (
        "simscale_sdk_v1.models.simulation.one_of__wind_comfort_mesh_wind_comfort_fineness",
        "OneOf_WindComfortMeshWindComfortFineness",
    ),
    "OneTerm": ("simscale_sdk_v1.models.simulation.one_term", "OneTerm"),
    "OpaqueMaterial": ("simscale_sdk_v1.models.simulation.opaque_material", "OpaqueMaterial"),
    "OpenBoundaryRayBC": ("simscale_sdk_v1.models.simulation.open_boundary_ray_bc", "OpenBoundaryRayBC"),
    "OpenCoil": ("simscale_sdk_v1.models.simulation.open_coil", "OpenCoil"),
    "OpenWindowRSBC": ("simscale_sdk_v1.models.simulation.open_window_rsbc", "OpenWindowRSBC"),
    "OperativeTemperatureResultType": (
        "simscale_sdk_v1.models.simulation.operative_temperature_result_type",
        "OperativeTemperatureResultType",
    ),
    "OrthotropicConductivity": (
        "simscale_sdk_v1.models.simulation.orthotropic_conductivity",
        "OrthotropicConductivity",
    ),
    "OrthotropicDirectionalDependency": (
        "simscale_sdk_v1.models.simulation.orthotropic_directional_dependency",
        "OrthotropicDirectionalDependency",
    ),
    "OrthotropicElectricConductivity": (
        "simscale_sdk_v1.models.simulation.orthotropic_electric_conductivity",
        "OrthotropicElectricConductivity",
    ),
    "OrthotropicSpringStiffness": (
        "simscale_sdk_v1.models.simulation.orthotropic_spring_stiffness",
        "OrthotropicSpringStiffness",
    ),
    "OscillatingLinearSBM": ("simscale_sdk_v1.models.simulation.oscillating_linear_sbm", "OscillatingLinearSBM"),
    "OscillatingRotatingMotionType": (
        "simscale_sdk_v1.models.simulation.oscillating_rotating_motion_type",
        "OscillatingRotatingMotionType",
    ),
    "OscillatingRotatingSBM": ("simscale_sdk_v1.models.simulation.oscillating_rotating_sbm", "OscillatingRotatingSBM"),
    "OutletBackFlowMFValues": (
        "simscale_sdk_v1.models.simulation.outlet_back_flow_mf_values",
        "OutletBackFlowMFValues",
    ),
    "OutletBackFlowPFValues": (
        "simscale_sdk_v1.models.simulation.outlet_back_flow_pf_values",
        "OutletBackFlowPFValues",
    ),
    "OutletFlowDrivenPF": ("simscale_sdk_v1.models.simulation.outlet_flow_driven_pf", "OutletFlowDrivenPF"),
    "OutletMeanPhaseVBC": ("simscale_sdk_v1.models.simulation.outlet_mean_phase_vbc", "OutletMeanPhaseVBC"),
    "OutputSteps": ("simscale_sdk_v1.models.simulation.output_steps", "OutputSteps"),
    "PBICGSolver": ("simscale_sdk_v1.models.simulation.pbicg_solver", "PBICGSolver"),
    "PBICGStabSolver": ("simscale_sdk_v1.models.simulation.pbicg_stab_solver", "PBICGStabSolver"),
    "PCGSolver": ("simscale_sdk_v1.models.simulation.pcg_solver", "PCGSolver"),
    "PETSCSolver": ("simscale_sdk_v1.models.simulation.petsc_solver", "PETSCSolver"),
    "PacefishAutomesh": ("simscale_sdk_v1.models.simulation.pacefish_automesh", "PacefishAutomesh"),
    "PacefishFinenessCoarse": ("simscale_sdk_v1.models.simulation.pacefish_fineness_coarse", "PacefishFinenessCoarse"),
    "PacefishFinenessFine": ("simscale_sdk_v1.models.simulation.pacefish_fineness_fine", "PacefishFinenessFine"),
    "PacefishFinenessModerate": (
        "simscale_sdk_v1.models.simulation.pacefish_fineness_moderate",
        "PacefishFinenessModerate",
    ),
    "PacefishFinenessTargetSize": (
        "simscale_sdk_v1.models.simulation.pacefish_fineness_target_size",
        "PacefishFinenessTargetSize",
    ),
    "PacefishFinenessVeryCoarse": (
        "simscale_sdk_v1.models.simulation.pacefish_fineness_very_coarse",
        "PacefishFinenessVeryCoarse",
    ),
    "PacefishFinenessVeryFine": (
        "simscale_sdk_v1.models.simulation.pacefish_fineness_very_fine",
        "PacefishFinenessVeryFine",
    ),
    "PacefishMeshLegacy": ("simscale_sdk_v1.models.simulation.pacefish_mesh_legacy", "PacefishMeshLegacy"),
    "PardisoDirectSolver": ("simscale_sdk_v1.models.simulation.pardiso_direct_solver", "PardisoDirectSolver"),
    "PartialVectorFunction": ("simscale_sdk_v1.models.simulation.partial_vector_function", "PartialVectorFunction"),
    "PedestrianComfortSurface": (
        "simscale_sdk_v1.models.simulation.pedestrian_comfort_surface",
        "PedestrianComfortSurface",
    ),
    "PenaltyMethod": ("simscale_sdk_v1.models.simulation.penalty_method", "PenaltyMethod"),
    "PengRobinsonGasEquationOfState": (
        "simscale_sdk_v1.models.simulation.peng_robinson_gas_equation_of_state",
        "PengRobinsonGasEquationOfState",
    ),
    "PerfectFluidEquationOfState": (
        "simscale_sdk_v1.models.simulation.perfect_fluid_equation_of_state",
        "PerfectFluidEquationOfState",
    ),
    "PerfectGasEquationOfState": (
        "simscale_sdk_v1.models.simulation.perfect_gas_equation_of_state",
        "PerfectGasEquationOfState",
    ),
    "PerfectPlasticityModel": ("simscale_sdk_v1.models.simulation.perfect_plasticity_model", "PerfectPlasticityModel"),
    "PerfectPlasticityModelMarc": (
        "simscale_sdk_v1.models.simulation.perfect_plasticity_model_marc",
        "PerfectPlasticityModelMarc",
    ),
    "PerforatedPlate": ("simscale_sdk_v1.models.simulation.perforated_plate", "PerforatedPlate"),
    "PeriodicBC": ("simscale_sdk_v1.models.simulation.periodic_bc", "PeriodicBC"),
    "PermanentMagnetMaterial": (
        "simscale_sdk_v1.models.simulation.permanent_magnet_material",
        "PermanentMagnetMaterial",
    ),
    "PhaseFractionIC": ("simscale_sdk_v1.models.simulation.phase_fraction_ic", "PhaseFractionIC"),
    "PhaseFractionsIC": ("simscale_sdk_v1.models.simulation.phase_fractions_ic", "PhaseFractionsIC"),
    "PhysicalContact": ("simscale_sdk_v1.models.simulation.physical_contact", "PhysicalContact"),
    "PinConnector": ("simscale_sdk_v1.models.simulation.pin_connector", "PinConnector"),
    "PinKinematicBehavior": ("simscale_sdk_v1.models.simulation.pin_kinematic_behavior", "PinKinematicBehavior"),
    "PlaneTree": ("simscale_sdk_v1.models.simulation.plane_tree", "PlaneTree"),
    "PlasticMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.plastic_material_behavior",
        "PlasticMaterialBehavior",
    ),
    "PlasticStrain": ("simscale_sdk_v1.models.simulation.plastic_strain", "PlasticStrain"),
    "PlasticityMarc": ("simscale_sdk_v1.models.simulation.plasticity_marc", "PlasticityMarc"),
    "PlateData": ("simscale_sdk_v1.models.simulation.plate_data", "PlateData"),
    "PointDisplacementBCMarc": (
        "simscale_sdk_v1.models.simulation.point_displacement_bc_marc",
        "PointDisplacementBCMarc",
    ),
    "PointLoadBCMarc": ("simscale_sdk_v1.models.simulation.point_load_bc_marc", "PointLoadBCMarc"),
    "PointMassBC": ("simscale_sdk_v1.models.simulation.point_mass_bc", "PointMassBC"),
    "PolynomialFunction": ("simscale_sdk_v1.models.simulation.polynomial_function", "PolynomialFunction"),
    "PorousTree": ("simscale_sdk_v1.models.simulation.porous_tree", "PorousTree"),
    "PowerFerriteCoreLoss": ("simscale_sdk_v1.models.simulation.power_ferrite_core_loss", "PowerFerriteCoreLoss"),
    "PowerHeatSource": ("simscale_sdk_v1.models.simulation.power_heat_source", "PowerHeatSource"),
    "PowerLawMedium": ("simscale_sdk_v1.models.simulation.power_law_medium", "PowerLawMedium"),
    "PowerLawViscosityModel": ("simscale_sdk_v1.models.simulation.power_law_viscosity_model", "PowerLawViscosityModel"),
    "PrandtlLesDelta": ("simscale_sdk_v1.models.simulation.prandtl_les_delta", "PrandtlLesDelta"),
    "PredefinedRotationalMotion": (
        "simscale_sdk_v1.models.simulation.predefined_rotational_motion",
        "PredefinedRotationalMotion",
    ),
    "PrescribedOptionalFunction": (
        "simscale_sdk_v1.models.simulation.prescribed_optional_function",
        "PrescribedOptionalFunction",
    ),
    "PressureBC": ("simscale_sdk_v1.models.simulation.pressure_bc", "PressureBC"),
    "PressureBCMarc": ("simscale_sdk_v1.models.simulation.pressure_bc_marc", "PressureBCMarc"),
    "PressureCoefficientResultType": (
        "simscale_sdk_v1.models.simulation.pressure_coefficient_result_type",
        "PressureCoefficientResultType",
    ),
    "PressureDifferenceResultControl": (
        "simscale_sdk_v1.models.simulation.pressure_difference_result_control",
        "PressureDifferenceResultControl",
    ),
    "PressureInletBC": ("simscale_sdk_v1.models.simulation.pressure_inlet_bc", "PressureInletBC"),
    "PressureInletOutletVBC": ("simscale_sdk_v1.models.simulation.pressure_inlet_outlet_vbc", "PressureInletOutletVBC"),
    "PressureInletVBC": ("simscale_sdk_v1.models.simulation.pressure_inlet_vbc", "PressureInletVBC"),
    "PressureLossCurve": ("simscale_sdk_v1.models.simulation.pressure_loss_curve", "PressureLossCurve"),
    "PressureLossData": ("simscale_sdk_v1.models.simulation.pressure_loss_data", "PressureLossData"),
    "PressureLossFunctionMedium": (
        "simscale_sdk_v1.models.simulation.pressure_loss_function_medium",
        "PressureLossFunctionMedium",
    ),
    "PressureOutletBC": ("simscale_sdk_v1.models.simulation.pressure_outlet_bc", "PressureOutletBC"),
    "PressureValueResultType": (
        "simscale_sdk_v1.models.simulation.pressure_value_result_type",
        "PressureValueResultType",
    ),
    "PrimaryNetwork": ("simscale_sdk_v1.models.simulation.primary_network", "PrimaryNetwork"),
    "PrincipalElasticStrain": ("simscale_sdk_v1.models.simulation.principal_elastic_strain", "PrincipalElasticStrain"),
    "PrincipalGreenLagrangeStrainType": (
        "simscale_sdk_v1.models.simulation.principal_green_lagrange_strain_type",
        "PrincipalGreenLagrangeStrainType",
    ),
    "PrincipalPlasticStrain": ("simscale_sdk_v1.models.simulation.principal_plastic_strain", "PrincipalPlasticStrain"),
    "PrincipalStrainType": ("simscale_sdk_v1.models.simulation.principal_strain_type", "PrincipalStrainType"),
    "PrincipalStress": ("simscale_sdk_v1.models.simulation.principal_stress", "PrincipalStress"),
    "PrincipalStressType": ("simscale_sdk_v1.models.simulation.principal_stress_type", "PrincipalStressType"),
    "PrincipalTotalStrain": ("simscale_sdk_v1.models.simulation.principal_total_strain", "PrincipalTotalStrain"),
    "ProbePointsResultControl": (
        "simscale_sdk_v1.models.simulation.probe_points_result_control",
        "ProbePointsResultControl",
    ),
    "ProgressiveRefinement": ("simscale_sdk_v1.models.simulation.progressive_refinement", "ProgressiveRefinement"),
    "PronySeries": ("simscale_sdk_v1.models.simulation.prony_series", "PronySeries"),
    "QZ": ("simscale_sdk_v1.models.simulation.qz", "QZ"),
    "RadiationHeatFlux": ("simscale_sdk_v1.models.simulation.radiation_heat_flux", "RadiationHeatFlux"),
    "RadiationTBC": ("simscale_sdk_v1.models.simulation.radiation_tbc", "RadiationTBC"),
    "RayleighDamping": ("simscale_sdk_v1.models.simulation.rayleigh_damping", "RayleighDamping"),
    "ReactionForce": ("simscale_sdk_v1.models.simulation.reaction_force", "ReactionForce"),
    "ReactionForceType": ("simscale_sdk_v1.models.simulation.reaction_force_type", "ReactionForceType"),
    "ReactionMomentType": ("simscale_sdk_v1.models.simulation.reaction_moment_type", "ReactionMomentType"),
    "RealGasEquationOfState": (
        "simscale_sdk_v1.models.simulation.real_gas_equation_of_state",
        "RealGasEquationOfState",
    ),
    "RectifyingDarcyForchheimer": (
        "simscale_sdk_v1.models.simulation.rectifying_darcy_forchheimer",
        "RectifyingDarcyForchheimer",
    ),
    "RefinementLength": ("simscale_sdk_v1.models.simulation.refinement_length", "RefinementLength"),
    "Region": ("simscale_sdk_v1.models.simulation.region", "Region"),
    "RegionInterface": ("simscale_sdk_v1.models.simulation.region_interface", "RegionInterface"),
    "RegionOfInterest": ("simscale_sdk_v1.models.simulation.region_of_interest", "RegionOfInterest"),
    "RegionRefinementEBM": ("simscale_sdk_v1.models.simulation.region_refinement_ebm", "RegionRefinementEBM"),
    "RegionRefinementPacefish": (
        "simscale_sdk_v1.models.simulation.region_refinement_pacefish",
        "RegionRefinementPacefish",
    ),
    "RegionRefinementSimerics": (
        "simscale_sdk_v1.models.simulation.region_refinement_simerics",
        "RegionRefinementSimerics",
    ),
    "RegionRefinementWindComfort": (
        "simscale_sdk_v1.models.simulation.region_refinement_wind_comfort",
        "RegionRefinementWindComfort",
    ),
    "RelativeConvergenceCriteria": (
        "simscale_sdk_v1.models.simulation.relative_convergence_criteria",
        "RelativeConvergenceCriteria",
    ),
    "RelativeConvergenceDisplacements": (
        "simscale_sdk_v1.models.simulation.relative_convergence_displacements",
        "RelativeConvergenceDisplacements",
    ),
    "RelativeConvergenceResiduals": (
        "simscale_sdk_v1.models.simulation.relative_convergence_residuals",
        "RelativeConvergenceResiduals",
    ),
    "RelativeConvergenceResidualsOrDisplacements": (
        "simscale_sdk_v1.models.simulation.relative_convergence_residuals_or_displacements",
        "RelativeConvergenceResidualsOrDisplacements",
    ),
    "RelativeERPFieldSelection": (
        "simscale_sdk_v1.models.simulation.relative_erp_field_selection",
        "RelativeERPFieldSelection",
    ),
    "RelativeHarmonicAccelerationFieldType": (
        "simscale_sdk_v1.models.simulation.relative_harmonic_acceleration_field_type",
        "RelativeHarmonicAccelerationFieldType",
    ),
    "RelativeHarmonicAccelerationType": (
        "simscale_sdk_v1.models.simulation.relative_harmonic_acceleration_type",
        "RelativeHarmonicAccelerationType",
    ),
    "RelativeHarmonicDisplacementFieldType": (
        "simscale_sdk_v1.models.simulation.relative_harmonic_displacement_field_type",
        "RelativeHarmonicDisplacementFieldType",
    ),
    "RelativeHarmonicDisplacementType": (
        "simscale_sdk_v1.models.simulation.relative_harmonic_displacement_type",
        "RelativeHarmonicDisplacementType",
    ),
    "RelativeHarmonicVelocityFieldType": (
        "simscale_sdk_v1.models.simulation.relative_harmonic_velocity_field_type",
        "RelativeHarmonicVelocityFieldType",
    ),
    "RelativeHarmonicVelocityType": (
        "simscale_sdk_v1.models.simulation.relative_harmonic_velocity_type",
        "RelativeHarmonicVelocityType",
    ),
    "RelativeHumidityValue": ("simscale_sdk_v1.models.simulation.relative_humidity_value", "RelativeHumidityValue"),
    "RelativeToAllCadSurfacesSettings": (
        "simscale_sdk_v1.models.simulation.relative_to_all_cad_surfaces_settings",
        "RelativeToAllCadSurfacesSettings",
    ),
    "RelaxationFactor": ("simscale_sdk_v1.models.simulation.relaxation_factor", "RelaxationFactor"),
    "RemoteDisplacementLoadBC": (
        "simscale_sdk_v1.models.simulation.remote_displacement_load_bc",
        "RemoteDisplacementLoadBC",
    ),
    "RemoteForceLoadBC": ("simscale_sdk_v1.models.simulation.remote_force_load_bc", "RemoteForceLoadBC"),
    "RemotePointConnectionMarc": (
        "simscale_sdk_v1.models.simulation.remote_point_connection_marc",
        "RemotePointConnectionMarc",
    ),
    "ResidualControls": ("simscale_sdk_v1.models.simulation.residual_controls", "ResidualControls"),
    "ResidualsConvergenceMethod": (
        "simscale_sdk_v1.models.simulation.residuals_convergence_method",
        "ResidualsConvergenceMethod",
    ),
    "ResidualsOrDisplacementsConvergenceMethod": (
        "simscale_sdk_v1.models.simulation.residuals_or_displacements_convergence_method",
        "ResidualsOrDisplacementsConvergenceMethod",
    ),
    "ResolvedTurbulenceIntensity": (
        "simscale_sdk_v1.models.simulation.resolved_turbulence_intensity",
        "ResolvedTurbulenceIntensity",
    ),
    "ResolvedTurbulentKineticEnergy": (
        "simscale_sdk_v1.models.simulation.resolved_turbulent_kinetic_energy",
        "ResolvedTurbulentKineticEnergy",
    ),
    "RestrictedDimensionalFunction_Frequency": (
        "simscale_sdk_v1.models.simulation.restricted_dimensional_function__frequency",
        "RestrictedDimensionalFunction_Frequency",
    ),
    "RestrictedDimensionalFunction_Time": (
        "simscale_sdk_v1.models.simulation.restricted_dimensional_function__time",
        "RestrictedDimensionalFunction_Time",
    ),
    "RestrictedTableDefinedFunction": (
        "simscale_sdk_v1.models.simulation.restricted_table_defined_function",
        "RestrictedTableDefinedFunction",
    ),
    "ReynoldsStressResultType": (
        "simscale_sdk_v1.models.simulation.reynolds_stress_result_type",
        "ReynoldsStressResultType",
    ),
    "RhoConstEquationOfState": (
        "simscale_sdk_v1.models.simulation.rho_const_equation_of_state",
        "RhoConstEquationOfState",
    ),
    "RigidAxialRotation": ("simscale_sdk_v1.models.simulation.rigid_axial_rotation", "RigidAxialRotation"),
    "RigidAxialTranslation": ("simscale_sdk_v1.models.simulation.rigid_axial_translation", "RigidAxialTranslation"),
    "RotatingMotionBC": ("simscale_sdk_v1.models.simulation.rotating_motion_bc", "RotatingMotionBC"),
    "RotatingMotionType": ("simscale_sdk_v1.models.simulation.rotating_motion_type", "RotatingMotionType"),
    "RotatingSBM": ("simscale_sdk_v1.models.simulation.rotating_sbm", "RotatingSBM"),
    "RotatingWall": ("simscale_sdk_v1.models.simulation.rotating_wall", "RotatingWall"),
    "RotatingWallVBC": ("simscale_sdk_v1.models.simulation.rotating_wall_vbc", "RotatingWallVBC"),
    "Round": ("simscale_sdk_v1.models.simulation.round", "Round"),
    "RunTimeWriteControl": ("simscale_sdk_v1.models.simulation.run_time_write_control", "RunTimeWriteControl"),
    "ScalarTransportResultControl": (
        "simscale_sdk_v1.models.simulation.scalar_transport_result_control",
        "ScalarTransportResultControl",
    ),
    "Schemes": ("simscale_sdk_v1.models.simulation.schemes", "Schemes"),
    "ScotchDecomposeAlgorithm": (
        "simscale_sdk_v1.models.simulation.scotch_decompose_algorithm",
        "ScotchDecomposeAlgorithm",
    ),
    "SecondOrderOgden": ("simscale_sdk_v1.models.simulation.second_order_ogden", "SecondOrderOgden"),
    "SecondOrderUpwindSpatialScheme": (
        "simscale_sdk_v1.models.simulation.second_order_upwind_spatial_scheme",
        "SecondOrderUpwindSpatialScheme",
    ),
    "SemiOpenBoundaryRayBC": ("simscale_sdk_v1.models.simulation.semi_open_boundary_ray_bc", "SemiOpenBoundaryRayBC"),
    "SemiTransparentMaterial": (
        "simscale_sdk_v1.models.simulation.semi_transparent_material",
        "SemiTransparentMaterial",
    ),
    "SetValuePositionTolerance": (
        "simscale_sdk_v1.models.simulation.set_value_position_tolerance",
        "SetValuePositionTolerance",
    ),
    "ShipDesignAnalysisSBM": ("simscale_sdk_v1.models.simulation.ship_design_analysis_sbm", "ShipDesignAnalysisSBM"),
    "SignedVonMisesStressType": (
        "simscale_sdk_v1.models.simulation.signed_von_mises_stress_type",
        "SignedVonMisesStressType",
    ),
    "SignoriniHyperElasticModel": (
        "simscale_sdk_v1.models.simulation.signorini_hyper_elastic_model",
        "SignoriniHyperElasticModel",
    ),
    "SilverBirch": ("simscale_sdk_v1.models.simulation.silver_birch", "SilverBirch"),
    "SimericsAnalysis": ("simscale_sdk_v1.models.simulation.simerics_analysis", "SimericsAnalysis"),
    "SimericsMaterials": ("simscale_sdk_v1.models.simulation.simerics_materials", "SimericsMaterials"),
    "SimpleDecomposeAlgorithm": (
        "simscale_sdk_v1.models.simulation.simple_decompose_algorithm",
        "SimpleDecomposeAlgorithm",
    ),
    "SingleFrequency": ("simscale_sdk_v1.models.simulation.single_frequency", "SingleFrequency"),
    "SingleStepPseudoTimeStepping": (
        "simscale_sdk_v1.models.simulation.single_step_pseudo_time_stepping",
        "SingleStepPseudoTimeStepping",
    ),
    "SittingFractionBodySurface": (
        "simscale_sdk_v1.models.simulation.sitting_fraction_body_surface",
        "SittingFractionBodySurface",
    ),
    "SlidingContact": ("simscale_sdk_v1.models.simulation.sliding_contact", "SlidingContact"),
    "SlipVBC": ("simscale_sdk_v1.models.simulation.slip_vbc", "SlipVBC"),
    "SmallestCell": ("simscale_sdk_v1.models.simulation.smallest_cell", "SmallestCell"),
    "SmoothLesDelta": ("simscale_sdk_v1.models.simulation.smooth_les_delta", "SmoothLesDelta"),
    "SmoothSolver": ("simscale_sdk_v1.models.simulation.smooth_solver", "SmoothSolver"),
    "SnapshotResultControl": ("simscale_sdk_v1.models.simulation.snapshot_result_control", "SnapshotResultControl"),
    "SoftMagneticMaterial": ("simscale_sdk_v1.models.simulation.soft_magnetic_material", "SoftMagneticMaterial"),
    "SolarCalculator": ("simscale_sdk_v1.models.simulation.solar_calculator", "SolarCalculator"),
    "SolidCoil": ("simscale_sdk_v1.models.simulation.solid_coil", "SolidCoil"),
    "SolidCompressibleMaterial": (
        "simscale_sdk_v1.models.simulation.solid_compressible_material",
        "SolidCompressibleMaterial",
    ),
    "SolidElementTechnology": ("simscale_sdk_v1.models.simulation.solid_element_technology", "SolidElementTechnology"),
    "SolidGlobalPhysics": ("simscale_sdk_v1.models.simulation.solid_global_physics", "SolidGlobalPhysics"),
    "SolidInitialConditions": ("simscale_sdk_v1.models.simulation.solid_initial_conditions", "SolidInitialConditions"),
    "SolidMaterial": ("simscale_sdk_v1.models.simulation.solid_material", "SolidMaterial"),
    "SolidModel": ("simscale_sdk_v1.models.simulation.solid_model", "SolidModel"),
    "SolidNumerics": ("simscale_sdk_v1.models.simulation.solid_numerics", "SolidNumerics"),
    "SolidResultControl": ("simscale_sdk_v1.models.simulation.solid_result_control", "SolidResultControl"),
    "SolidSimulationControl": ("simscale_sdk_v1.models.simulation.solid_simulation_control", "SolidSimulationControl"),
    "SolverModel": ("simscale_sdk_v1.models.simulation.solver_model", "SolverModel"),
    "SorPreconditioner": ("simscale_sdk_v1.models.simulation.sor_preconditioner", "SorPreconditioner"),
    "SparseIterative": ("simscale_sdk_v1.models.simulation.sparse_iterative", "SparseIterative"),
    "SpatialDiscretizationSchemes": (
        "simscale_sdk_v1.models.simulation.spatial_discretization_schemes",
        "SpatialDiscretizationSchemes",
    ),
    "SpecieDefault": ("simscale_sdk_v1.models.simulation.specie_default", "SpecieDefault"),
    "SpeciesHumiditySource": ("simscale_sdk_v1.models.simulation.species_humidity_source", "SpeciesHumiditySource"),
    "SpecificConductanceInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.specific_conductance_interface_thermal",
        "SpecificConductanceInterfaceThermal",
    ),
    "SpecificConductanceWallThermal": (
        "simscale_sdk_v1.models.simulation.specific_conductance_wall_thermal",
        "SpecificConductanceWallThermal",
    ),
    "SpecificHumidityValue": ("simscale_sdk_v1.models.simulation.specific_humidity_value", "SpecificHumidityValue"),
    "SpecificPassiveScalarSource": (
        "simscale_sdk_v1.models.simulation.specific_passive_scalar_source",
        "SpecificPassiveScalarSource",
    ),
    "SpecificPowerSource": ("simscale_sdk_v1.models.simulation.specific_power_source", "SpecificPowerSource"),
    "SpecificResistanceInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.specific_resistance_interface_thermal",
        "SpecificResistanceInterfaceThermal",
    ),
    "Square": ("simscale_sdk_v1.models.simulation.square", "Square"),
    "Stabilization": ("simscale_sdk_v1.models.simulation.stabilization", "Stabilization"),
    "StandardHerschelBulkleyViscosityModel": (
        "simscale_sdk_v1.models.simulation.standard_herschel_bulkley_viscosity_model",
        "StandardHerschelBulkleyViscosityModel",
    ),
    "StandingFractionBodySurface": (
        "simscale_sdk_v1.models.simulation.standing_fraction_body_surface",
        "StandingFractionBodySurface",
    ),
    "StarThermalResistanceNetwork": (
        "simscale_sdk_v1.models.simulation.star_thermal_resistance_network",
        "StarThermalResistanceNetwork",
    ),
    "StaticAnalysis": ("simscale_sdk_v1.models.simulation.static_analysis", "StaticAnalysis"),
    "StaticPressurePressureType": (
        "simscale_sdk_v1.models.simulation.static_pressure_pressure_type",
        "StaticPressurePressureType",
    ),
    "StationaryTimeDependency": (
        "simscale_sdk_v1.models.simulation.stationary_time_dependency",
        "StationaryTimeDependency",
    ),
    "StatisticalAveragingResultControlV2": (
        "simscale_sdk_v1.models.simulation.statistical_averaging_result_control_v2",
        "StatisticalAveragingResultControlV2",
    ),
    "SteadystateTimeDifferentiationScheme": (
        "simscale_sdk_v1.models.simulation.steadystate_time_differentiation_scheme",
        "SteadystateTimeDifferentiationScheme",
    ),
    "SteppingListPseudoTimeStepping": (
        "simscale_sdk_v1.models.simulation.stepping_list_pseudo_time_stepping",
        "SteppingListPseudoTimeStepping",
    ),
    "StrainEnergyConvergenceMethod": (
        "simscale_sdk_v1.models.simulation.strain_energy_convergence_method",
        "StrainEnergyConvergenceMethod",
    ),
    "StrainFieldSelection": ("simscale_sdk_v1.models.simulation.strain_field_selection", "StrainFieldSelection"),
    "StrainHardeningCreepFormulation": (
        "simscale_sdk_v1.models.simulation.strain_hardening_creep_formulation",
        "StrainHardeningCreepFormulation",
    ),
    "StrainHardeningModel": ("simscale_sdk_v1.models.simulation.strain_hardening_model", "StrainHardeningModel"),
    "StrainHardeningModelMarc": (
        "simscale_sdk_v1.models.simulation.strain_hardening_model_marc",
        "StrainHardeningModelMarc",
    ),
    "StrainResultControlItem": (
        "simscale_sdk_v1.models.simulation.strain_result_control_item",
        "StrainResultControlItem",
    ),
    "StrandedCoil": ("simscale_sdk_v1.models.simulation.stranded_coil", "StrandedCoil"),
    "StressFieldSelection": ("simscale_sdk_v1.models.simulation.stress_field_selection", "StressFieldSelection"),
    "StressInitialConditionDomains": (
        "simscale_sdk_v1.models.simulation.stress_initial_condition_domains",
        "StressInitialConditionDomains",
    ),
    "StressResultControlItem": (
        "simscale_sdk_v1.models.simulation.stress_result_control_item",
        "StressResultControlItem",
    ),
    "StressTensor_Pressure": ("simscale_sdk_v1.models.simulation.stress_tensor__pressure", "StressTensor_Pressure"),
    "SubdomainBasedDimensionalVectorFunctionInitialCondition_Acceleration": (
        "simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__acceleration",
        "SubdomainBasedDimensionalVectorFunctionInitialCondition_Acceleration",
    ),
    "SubdomainBasedDimensionalVectorFunctionInitialCondition_Length": (
        "simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__length",
        "SubdomainBasedDimensionalVectorFunctionInitialCondition_Length",
    ),
    "SubdomainBasedDimensionalVectorFunctionInitialCondition_Speed": (
        "simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__speed",
        "SubdomainBasedDimensionalVectorFunctionInitialCondition_Speed",
    ),
    "SubdomainDimensionalFunctionInitialCondition_Temperature": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_function_initial_condition__temperature",
        "SubdomainDimensionalFunctionInitialCondition_Temperature",
    ),
    "SubdomainDimensionalInitialCondition_Dimensionless": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__dimensionless",
        "SubdomainDimensionalInitialCondition_Dimensionless",
    ),
    "SubdomainDimensionalInitialCondition_KinematicViscosity": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__kinematic_viscosity",
        "SubdomainDimensionalInitialCondition_KinematicViscosity",
    ),
    "SubdomainDimensionalInitialCondition_Pressure": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__pressure",
        "SubdomainDimensionalInitialCondition_Pressure",
    ),
    "SubdomainDimensionalInitialCondition_SpecificTurbulenceDissipationRate": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__specific_turbulence_dissipation_rate",
        "SubdomainDimensionalInitialCondition_SpecificTurbulenceDissipationRate",
    ),
    "SubdomainDimensionalInitialCondition_Temperature": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__temperature",
        "SubdomainDimensionalInitialCondition_Temperature",
    ),
    "SubdomainDimensionalInitialCondition_TurbulenceKineticEnergy": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__turbulence_kinetic_energy",
        "SubdomainDimensionalInitialCondition_TurbulenceKineticEnergy",
    ),
    "SubdomainDimensionalInitialCondition_TurbulentDissipation": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__turbulent_dissipation",
        "SubdomainDimensionalInitialCondition_TurbulentDissipation",
    ),
    "SubdomainDimensionalVectorInitialCondition_Speed": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensional_vector_initial_condition__speed",
        "SubdomainDimensionalVectorInitialCondition_Speed",
    ),
    "SubdomainDimensionlessInitialCondition": (
        "simscale_sdk_v1.models.simulation.subdomain_dimensionless_initial_condition",
        "SubdomainDimensionlessInitialCondition",
    ),
    "SubdomainFractionValueInitialCondition": (
        "simscale_sdk_v1.models.simulation.subdomain_fraction_value_initial_condition",
        "SubdomainFractionValueInitialCondition",
    ),
    "SubdomainStressInitialCondition": (
        "simscale_sdk_v1.models.simulation.subdomain_stress_initial_condition",
        "SubdomainStressInitialCondition",
    ),
    "SubspaceCoefficient": ("simscale_sdk_v1.models.simulation.subspace_coefficient", "SubspaceCoefficient"),
    "SubspaceDimension": ("simscale_sdk_v1.models.simulation.subspace_dimension", "SubspaceDimension"),
    "SumFieldsCalculationResultControlItem": (
        "simscale_sdk_v1.models.simulation.sum_fields_calculation_result_control_item",
        "SumFieldsCalculationResultControlItem",
    ),
    "SurfaceHeatFlux": ("simscale_sdk_v1.models.simulation.surface_heat_flux", "SurfaceHeatFlux"),
    "SurfaceHeatFluxBC": ("simscale_sdk_v1.models.simulation.surface_heat_flux_bc", "SurfaceHeatFluxBC"),
    "SurfaceLoadBC": ("simscale_sdk_v1.models.simulation.surface_load_bc", "SurfaceLoadBC"),
    "SurfaceNormalGradientSchemes": (
        "simscale_sdk_v1.models.simulation.surface_normal_gradient_schemes",
        "SurfaceNormalGradientSchemes",
    ),
    "SurfaceNormalsResultType": (
        "simscale_sdk_v1.models.simulation.surface_normals_result_type",
        "SurfaceNormalsResultType",
    ),
    "SurfaceRefinementPacefish": (
        "simscale_sdk_v1.models.simulation.surface_refinement_pacefish",
        "SurfaceRefinementPacefish",
    ),
    "SurfaceRefinementSimerics": (
        "simscale_sdk_v1.models.simulation.surface_refinement_simerics",
        "SurfaceRefinementSimerics",
    ),
    "SurfaceRefinementWindComfort": (
        "simscale_sdk_v1.models.simulation.surface_refinement_wind_comfort",
        "SurfaceRefinementWindComfort",
    ),
    "SurfaceRoughnessModel": ("simscale_sdk_v1.models.simulation.surface_roughness_model", "SurfaceRoughnessModel"),
    "SurfaceWaterVaporFluxHumidityBC": (
        "simscale_sdk_v1.models.simulation.surface_water_vapor_flux_humidity_bc",
        "SurfaceWaterVaporFluxHumidityBC",
    ),
    "SutherlandTransport": ("simscale_sdk_v1.models.simulation.sutherland_transport", "SutherlandTransport"),
    "SutherlandViscosity": ("simscale_sdk_v1.models.simulation.sutherland_viscosity", "SutherlandViscosity"),
    "Sycamore": ("simscale_sdk_v1.models.simulation.sycamore", "Sycamore"),
    "SymmetryBC": ("simscale_sdk_v1.models.simulation.symmetry_bc", "SymmetryBC"),
    "SymmetryBCMarc": ("simscale_sdk_v1.models.simulation.symmetry_bc_marc", "SymmetryBCMarc"),
    "SymmetryDVBC": ("simscale_sdk_v1.models.simulation.symmetry_dvbc", "SymmetryDVBC"),
    "SymmetryEBC": ("simscale_sdk_v1.models.simulation.symmetry_ebc", "SymmetryEBC"),
    "SymmetryEVBC": ("simscale_sdk_v1.models.simulation.symmetry_evbc", "SymmetryEVBC"),
    "SymmetryEVCBC": ("simscale_sdk_v1.models.simulation.symmetry_evcbc", "SymmetryEVCBC"),
    "SymmetryNBC": ("simscale_sdk_v1.models.simulation.symmetry_nbc", "SymmetryNBC"),
    "SymmetryOBC": ("simscale_sdk_v1.models.simulation.symmetry_obc", "SymmetryOBC"),
    "SymmetryPBC": ("simscale_sdk_v1.models.simulation.symmetry_pbc", "SymmetryPBC"),
    "SymmetryPFBC": ("simscale_sdk_v1.models.simulation.symmetry_pfbc", "SymmetryPFBC"),
    "SymmetryPSBC": ("simscale_sdk_v1.models.simulation.symmetry_psbc", "SymmetryPSBC"),
    "SymmetryPlaneBC": ("simscale_sdk_v1.models.simulation.symmetry_plane_bc", "SymmetryPlaneBC"),
    "SymmetryTBC": ("simscale_sdk_v1.models.simulation.symmetry_tbc", "SymmetryTBC"),
    "SymmetryTDBC": ("simscale_sdk_v1.models.simulation.symmetry_tdbc", "SymmetryTDBC"),
    "SymmetryTDCBC": ("simscale_sdk_v1.models.simulation.symmetry_tdcbc", "SymmetryTDCBC"),
    "SymmetryTKEBC": ("simscale_sdk_v1.models.simulation.symmetry_tkebc", "SymmetryTKEBC"),
    "SymmetryVBC": ("simscale_sdk_v1.models.simulation.symmetry_vbc", "SymmetryVBC"),
    "SynchronizeWithFieldOutputWriteControl": (
        "simscale_sdk_v1.models.simulation.synchronize_with_field_output_write_control",
        "SynchronizeWithFieldOutputWriteControl",
    ),
    "TableDefinedFunction": ("simscale_sdk_v1.models.simulation.table_defined_function", "TableDefinedFunction"),
    "TableDefinedProbeLocations": (
        "simscale_sdk_v1.models.simulation.table_defined_probe_locations",
        "TableDefinedProbeLocations",
    ),
    "TableDefinedVectorFunction": (
        "simscale_sdk_v1.models.simulation.table_defined_vector_function",
        "TableDefinedVectorFunction",
    ),
    "TableFunctionParameter": ("simscale_sdk_v1.models.simulation.table_function_parameter", "TableFunctionParameter"),
    "TadmorFluxScheme": ("simscale_sdk_v1.models.simulation.tadmor_flux_scheme", "TadmorFluxScheme"),
    "TangentJacobianMatrix": ("simscale_sdk_v1.models.simulation.tangent_jacobian_matrix", "TangentJacobianMatrix"),
    "TchamwaTimeIntegrationScheme": (
        "simscale_sdk_v1.models.simulation.tchamwa_time_integration_scheme",
        "TchamwaTimeIntegrationScheme",
    ),
    "TemperatureBCMarc": ("simscale_sdk_v1.models.simulation.temperature_bc_marc", "TemperatureBCMarc"),
    "TemperatureFieldSelection": (
        "simscale_sdk_v1.models.simulation.temperature_field_selection",
        "TemperatureFieldSelection",
    ),
    "TemperatureResultControlItem": (
        "simscale_sdk_v1.models.simulation.temperature_result_control_item",
        "TemperatureResultControlItem",
    ),
    "TemporalResponseResultControlItem": (
        "simscale_sdk_v1.models.simulation.temporal_response_result_control_item",
        "TemporalResponseResultControlItem",
    ),
    "TestsolverSimulationControl": (
        "simscale_sdk_v1.models.simulation.testsolver_simulation_control",
        "TestsolverSimulationControl",
    ),
    "ThermalMechanical": ("simscale_sdk_v1.models.simulation.thermal_mechanical", "ThermalMechanical"),
    "ThetaMethodTimeIntegrationType": (
        "simscale_sdk_v1.models.simulation.theta_method_time_integration_type",
        "ThetaMethodTimeIntegrationType",
    ),
    "ThinResistanceLayer": ("simscale_sdk_v1.models.simulation.thin_resistance_layer", "ThinResistanceLayer"),
    "ThirdOrderOgden": ("simscale_sdk_v1.models.simulation.third_order_ogden", "ThirdOrderOgden"),
    "ThreeTerms": ("simscale_sdk_v1.models.simulation.three_terms", "ThreeTerms"),
    "TimeAndPlaceSunDirection": (
        "simscale_sdk_v1.models.simulation.time_and_place_sun_direction",
        "TimeAndPlaceSunDirection",
    ),
    "TimeDifferentiationSchemes": (
        "simscale_sdk_v1.models.simulation.time_differentiation_schemes",
        "TimeDifferentiationSchemes",
    ),
    "TimeHardeningCreepFormulation": (
        "simscale_sdk_v1.models.simulation.time_hardening_creep_formulation",
        "TimeHardeningCreepFormulation",
    ),
    "TimeHarmonicElectrics": ("simscale_sdk_v1.models.simulation.time_harmonic_electrics", "TimeHarmonicElectrics"),
    "TimeHarmonicMagnetics": ("simscale_sdk_v1.models.simulation.time_harmonic_magnetics", "TimeHarmonicMagnetics"),
    "TimeStepWriteControl": ("simscale_sdk_v1.models.simulation.time_step_write_control", "TimeStepWriteControl"),
    "TimeTransientMagnetics": ("simscale_sdk_v1.models.simulation.time_transient_magnetics", "TimeTransientMagnetics"),
    "Tolerance": ("simscale_sdk_v1.models.simulation.tolerance", "Tolerance"),
    "TopologicalReference": ("simscale_sdk_v1.models.simulation.topological_reference", "TopologicalReference"),
    "TorsionalAxialRotation": ("simscale_sdk_v1.models.simulation.torsional_axial_rotation", "TorsionalAxialRotation"),
    "TotalCharge": ("simscale_sdk_v1.models.simulation.total_charge", "TotalCharge"),
    "TotalConductanceInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.total_conductance_interface_thermal",
        "TotalConductanceInterfaceThermal",
    ),
    "TotalEquivalentPlasticStrainType": (
        "simscale_sdk_v1.models.simulation.total_equivalent_plastic_strain_type",
        "TotalEquivalentPlasticStrainType",
    ),
    "TotalIsotropicStiffnessDefinition": (
        "simscale_sdk_v1.models.simulation.total_isotropic_stiffness_definition",
        "TotalIsotropicStiffnessDefinition",
    ),
    "TotalLinearStrainType": ("simscale_sdk_v1.models.simulation.total_linear_strain_type", "TotalLinearStrainType"),
    "TotalMass": ("simscale_sdk_v1.models.simulation.total_mass", "TotalMass"),
    "TotalNonLinearStrainType": (
        "simscale_sdk_v1.models.simulation.total_non_linear_strain_type",
        "TotalNonLinearStrainType",
    ),
    "TotalOrthotropicStiffnessDefinition": (
        "simscale_sdk_v1.models.simulation.total_orthotropic_stiffness_definition",
        "TotalOrthotropicStiffnessDefinition",
    ),
    "TotalPBC": ("simscale_sdk_v1.models.simulation.total_pbc", "TotalPBC"),
    "TotalPressurePressureType": (
        "simscale_sdk_v1.models.simulation.total_pressure_pressure_type",
        "TotalPressurePressureType",
    ),
    "TotalResistanceInterfaceThermal": (
        "simscale_sdk_v1.models.simulation.total_resistance_interface_thermal",
        "TotalResistanceInterfaceThermal",
    ),
    "TotalResistanceWallThermal": (
        "simscale_sdk_v1.models.simulation.total_resistance_wall_thermal",
        "TotalResistanceWallThermal",
    ),
    "TotalStrain": ("simscale_sdk_v1.models.simulation.total_strain", "TotalStrain"),
    "TotalTBC": ("simscale_sdk_v1.models.simulation.total_tbc", "TotalTBC"),
    "TotalTurbulenceIntensity": (
        "simscale_sdk_v1.models.simulation.total_turbulence_intensity",
        "TotalTurbulenceIntensity",
    ),
    "TotalTurbulentKineticEnergy": (
        "simscale_sdk_v1.models.simulation.total_turbulent_kinetic_energy",
        "TotalTurbulentKineticEnergy",
    ),
    "TrAbsolutePowerSource": ("simscale_sdk_v1.models.simulation.tr_absolute_power_source", "TrAbsolutePowerSource"),
    "TrSpecificPowerSource": ("simscale_sdk_v1.models.simulation.tr_specific_power_source", "TrSpecificPowerSource"),
    "TransientResultControl": ("simscale_sdk_v1.models.simulation.transient_result_control", "TransientResultControl"),
    "TransientTimeDependency": (
        "simscale_sdk_v1.models.simulation.transient_time_dependency",
        "TransientTimeDependency",
    ),
    "TransparentMaterial": ("simscale_sdk_v1.models.simulation.transparent_material", "TransparentMaterial"),
    "TrescaStressType": ("simscale_sdk_v1.models.simulation.tresca_stress_type", "TrescaStressType"),
    "TrueChangeJacobianMatrix": (
        "simscale_sdk_v1.models.simulation.true_change_jacobian_matrix",
        "TrueChangeJacobianMatrix",
    ),
    "TrueLineSearch": ("simscale_sdk_v1.models.simulation.true_line_search", "TrueLineSearch"),
    "TrueSemiImplicit": ("simscale_sdk_v1.models.simulation.true_semi_implicit", "TrueSemiImplicit"),
    "TurbulenceIntensityTIBC": (
        "simscale_sdk_v1.models.simulation.turbulence_intensity_tibc",
        "TurbulenceIntensityTIBC",
    ),
    "TurbulenceKineticEnergyTIBC": (
        "simscale_sdk_v1.models.simulation.turbulence_kinetic_energy_tibc",
        "TurbulenceKineticEnergyTIBC",
    ),
    "TurbulentHeatFluxTBC": ("simscale_sdk_v1.models.simulation.turbulent_heat_flux_tbc", "TurbulentHeatFluxTBC"),
    "TurbulentIntensityAndReferenceLengthTurbulence": (
        "simscale_sdk_v1.models.simulation.turbulent_intensity_and_reference_length_turbulence",
        "TurbulentIntensityAndReferenceLengthTurbulence",
    ),
    "TwiceMaxLoadingFrequency": (
        "simscale_sdk_v1.models.simulation.twice_max_loading_frequency",
        "TwiceMaxLoadingFrequency",
    ),
    "TwoResistorNetwork": ("simscale_sdk_v1.models.simulation.two_resistor_network", "TwoResistorNetwork"),
    "TwoTerms": ("simscale_sdk_v1.models.simulation.two_terms", "TwoTerms"),
    "UnconstrainedOptionalFunction": (
        "simscale_sdk_v1.models.simulation.unconstrained_optional_function",
        "UnconstrainedOptionalFunction",
    ),
    "UncorrectedSurfaceNormalGradientScheme": (
        "simscale_sdk_v1.models.simulation.uncorrected_surface_normal_gradient_scheme",
        "UncorrectedSurfaceNormalGradientScheme",
    ),
    "UnelasticStrainType": ("simscale_sdk_v1.models.simulation.unelastic_strain_type", "UnelasticStrainType"),
    "Unit_Dimensionless": ("simscale_sdk_v1.models.simulation.unit__dimensionless", "Unit_Dimensionless"),
    "Unit_Frequency": ("simscale_sdk_v1.models.simulation.unit__frequency", "Unit_Frequency"),
    "Unit_Length": ("simscale_sdk_v1.models.simulation.unit__length", "Unit_Length"),
    "Unit_MagneticFieldStrength": (
        "simscale_sdk_v1.models.simulation.unit__magnetic_field_strength",
        "Unit_MagneticFieldStrength",
    ),
    "Unit_Pressure": ("simscale_sdk_v1.models.simulation.unit__pressure", "Unit_Pressure"),
    "Unit_Speed": ("simscale_sdk_v1.models.simulation.unit__speed", "Unit_Speed"),
    "Unit_Temperature": ("simscale_sdk_v1.models.simulation.unit__temperature", "Unit_Temperature"),
    "Unit_Text": ("simscale_sdk_v1.models.simulation.unit__text", "Unit_Text"),
    "Unit_Time": ("simscale_sdk_v1.models.simulation.unit__time", "Unit_Time"),
    "Unit_VolumetricFlowRate": (
        "simscale_sdk_v1.models.simulation.unit__volumetric_flow_rate",
        "Unit_VolumetricFlowRate",
    ),
    "UserDefinedWriteControl": (
        "simscale_sdk_v1.models.simulation.user_defined_write_control",
        "UserDefinedWriteControl",
    ),
    "VariableGroup_EMPTY": ("simscale_sdk_v1.models.simulation.variable_group_empty", "VariableGroup_EMPTY"),
    "VariableGroup_ENGINEERING_STRAIN": (
        "simscale_sdk_v1.models.simulation.variable_group_engineering_strain",
        "VariableGroup_ENGINEERING_STRAIN",
    ),
    "VariableGroup_F": ("simscale_sdk_v1.models.simulation.variable_group_f", "VariableGroup_F"),
    "VariableGroup_HEIGHT": ("simscale_sdk_v1.models.simulation.variable_group_height", "VariableGroup_HEIGHT"),
    "VariableGroup_LEGEND_PROBABILITY": (
        "simscale_sdk_v1.models.simulation.variable_group_legend_probability",
        "VariableGroup_LEGEND_PROBABILITY",
    ),
    "VariableGroup_MAGNETIC_FIELD_STRENGTH": (
        "simscale_sdk_v1.models.simulation.variable_group_magnetic_field_strength",
        "VariableGroup_MAGNETIC_FIELD_STRENGTH",
    ),
    "VariableGroup_PLASTIC_STRAIN": (
        "simscale_sdk_v1.models.simulation.variable_group_plastic_strain",
        "VariableGroup_PLASTIC_STRAIN",
    ),
    "VariableGroup_RELAXATION_TIME": (
        "simscale_sdk_v1.models.simulation.variable_group_relaxation_time",
        "VariableGroup_RELAXATION_TIME",
    ),
    "VariableGroup_STRAIN": ("simscale_sdk_v1.models.simulation.variable_group_strain", "VariableGroup_STRAIN"),
    "VariableGroup_TEMP": ("simscale_sdk_v1.models.simulation.variable_group_temp", "VariableGroup_TEMP"),
    "VariableGroup_TEMP_ENGINEERING_STRAIN": (
        "simscale_sdk_v1.models.simulation.variable_group_temp_engineering_strain",
        "VariableGroup_TEMP_ENGINEERING_STRAIN",
    ),
    "VariableGroup_TEMP_PLASTIC_STRAIN": (
        "simscale_sdk_v1.models.simulation.variable_group_temp_plastic_strain",
        "VariableGroup_TEMP_PLASTIC_STRAIN",
    ),
    "VariableGroup_TEMP_PRESSURE": (
        "simscale_sdk_v1.models.simulation.variable_group_temp_pressure",
        "VariableGroup_TEMP_PRESSURE",
    ),
    "VariableGroup_TEMP_STRAIN": (
        "simscale_sdk_v1.models.simulation.variable_group_temp_strain",
        "VariableGroup_TEMP_STRAIN",
    ),
    "VariableGroup_TIME": ("simscale_sdk_v1.models.simulation.variable_group_time", "VariableGroup_TIME"),
    "VariableGroup_VELOCITY": ("simscale_sdk_v1.models.simulation.variable_group_velocity", "VariableGroup_VELOCITY"),
    "VariableGroup_V_DOT": ("simscale_sdk_v1.models.simulation.variable_group_v_dot", "VariableGroup_V_DOT"),
    "VariableGroup_X_Y_Z": ("simscale_sdk_v1.models.simulation.variable_group_x_y_z", "VariableGroup_X_Y_Z"),
    "VariableGroup_X_Y_Z_TIME": (
        "simscale_sdk_v1.models.simulation.variable_group_x_y_z_time",
        "VariableGroup_X_Y_Z_TIME",
    ),
    "VariableGroup_X_Y_Z_TIME_TEMP": (
        "simscale_sdk_v1.models.simulation.variable_group_x_y_z_time_temp",
        "VariableGroup_X_Y_Z_TIME_TEMP",
    ),
    "VectorRotation": ("simscale_sdk_v1.models.simulation.vector_rotation", "VectorRotation"),
    "VelocityFieldSelection": ("simscale_sdk_v1.models.simulation.velocity_field_selection", "VelocityFieldSelection"),
    "VelocityInletBC": ("simscale_sdk_v1.models.simulation.velocity_inlet_bc", "VelocityInletBC"),
    "VelocityOutletBC": ("simscale_sdk_v1.models.simulation.velocity_outlet_bc", "VelocityOutletBC"),
    "VelocityResultControlItem": (
        "simscale_sdk_v1.models.simulation.velocity_result_control_item",
        "VelocityResultControlItem",
    ),
    "ViscoelasticNetwork": ("simscale_sdk_v1.models.simulation.viscoelastic_network", "ViscoelasticNetwork"),
    "ViscoplasticMarcMaterialBehavior": (
        "simscale_sdk_v1.models.simulation.viscoplastic_marc_material_behavior",
        "ViscoplasticMarcMaterialBehavior",
    ),
    "VoltageExcitation": ("simscale_sdk_v1.models.simulation.voltage_excitation", "VoltageExcitation"),
    "VolumeHeatFlux": ("simscale_sdk_v1.models.simulation.volume_heat_flux", "VolumeHeatFlux"),
    "VolumeHeatFluxBC": ("simscale_sdk_v1.models.simulation.volume_heat_flux_bc", "VolumeHeatFluxBC"),
    "VolumeLoadBC": ("simscale_sdk_v1.models.simulation.volume_load_bc", "VolumeLoadBC"),
    "VolumetricFlow": ("simscale_sdk_v1.models.simulation.volumetric_flow", "VolumetricFlow"),
    "VolumetricSpeciesHumiditySource": (
        "simscale_sdk_v1.models.simulation.volumetric_species_humidity_source",
        "VolumetricSpeciesHumiditySource",
    ),
    "VonMisesStress": ("simscale_sdk_v1.models.simulation.von_mises_stress", "VonMisesStress"),
    "VonMisesStressType": ("simscale_sdk_v1.models.simulation.von_mises_stress_type", "VonMisesStressType"),
    "VorticityResultType": ("simscale_sdk_v1.models.simulation.vorticity_result_type", "VorticityResultType"),
    "WallBC": ("simscale_sdk_v1.models.simulation.wall_bc", "WallBC"),
    "WallContactAngle": ("simscale_sdk_v1.models.simulation.wall_contact_angle", "WallContactAngle"),
    "WallConvectionModel": ("simscale_sdk_v1.models.simulation.wall_convection_model", "WallConvectionModel"),
    "WallFunctionDVBC": ("simscale_sdk_v1.models.simulation.wall_function_dvbc", "WallFunctionDVBC"),
    "WallFunctionEBC": ("simscale_sdk_v1.models.simulation.wall_function_ebc", "WallFunctionEBC"),
    "WallFunctionEVBC": ("simscale_sdk_v1.models.simulation.wall_function_evbc", "WallFunctionEVBC"),
    "WallFunctionEVCBC": ("simscale_sdk_v1.models.simulation.wall_function_evcbc", "WallFunctionEVCBC"),
    "WallFunctionNBC": ("simscale_sdk_v1.models.simulation.wall_function_nbc", "WallFunctionNBC"),
    "WallFunctionOBC": ("simscale_sdk_v1.models.simulation.wall_function_obc", "WallFunctionOBC"),
    "WallFunctionTDBC": ("simscale_sdk_v1.models.simulation.wall_function_tdbc", "WallFunctionTDBC"),
    "WallFunctionTDCBC": ("simscale_sdk_v1.models.simulation.wall_function_tdcbc", "WallFunctionTDCBC"),
    "WallFunctionTKEBC": ("simscale_sdk_v1.models.simulation.wall_function_tkebc", "WallFunctionTKEBC"),
    "WallHeatFluxResultType": (
        "simscale_sdk_v1.models.simulation.wall_heat_flux_result_type",
        "WallHeatFluxResultType",
    ),
    "WallHeatTransferTBC": ("simscale_sdk_v1.models.simulation.wall_heat_transfer_tbc", "WallHeatTransferTBC"),
    "WallNextCellHeatTransferCoefficientResultType": (
        "simscale_sdk_v1.models.simulation.wall_next_cell_heat_transfer_coefficient_result_type",
        "WallNextCellHeatTransferCoefficientResultType",
    ),
    "WallRadiationModel": ("simscale_sdk_v1.models.simulation.wall_radiation_model", "WallRadiationModel"),
    "WallShearStressResultType": (
        "simscale_sdk_v1.models.simulation.wall_shear_stress_result_type",
        "WallShearStressResultType",
    ),
    "WaterVaporFluxHumidityBC": (
        "simscale_sdk_v1.models.simulation.water_vapor_flux_humidity_bc",
        "WaterVaporFluxHumidityBC",
    ),
    "WaveTransmissivePBC": ("simscale_sdk_v1.models.simulation.wave_transmissive_pbc", "WaveTransmissivePBC"),
    "WedgeBC": ("simscale_sdk_v1.models.simulation.wedge_bc", "WedgeBC"),
    "WindComfort": ("simscale_sdk_v1.models.simulation.wind_comfort", "WindComfort"),
    "WindComfortMesh": ("simscale_sdk_v1.models.simulation.wind_comfort_mesh", "WindComfortMesh"),
    "WindComfortSimulationControl": (
        "simscale_sdk_v1.models.simulation.wind_comfort_simulation_control",
        "WindComfortSimulationControl",
    ),
    "WindConditions": ("simscale_sdk_v1.models.simulation.wind_conditions", "WindConditions"),
    "WindExposureRoughness": ("simscale_sdk_v1.models.simulation.wind_exposure_roughness", "WindExposureRoughness"),
    "WindRose": ("simscale_sdk_v1.models.simulation.wind_rose", "WindRose"),
    "WindRoseVelocityBucket": ("simscale_sdk_v1.models.simulation.wind_rose_velocity_bucket", "WindRoseVelocityBucket"),
    "WindTunnelSizeCustom": ("simscale_sdk_v1.models.simulation.wind_tunnel_size_custom", "WindTunnelSizeCustom"),
    "WindTunnelSizeLarge": ("simscale_sdk_v1.models.simulation.wind_tunnel_size_large", "WindTunnelSizeLarge"),
    "WindTunnelSizeModerate": ("simscale_sdk_v1.models.simulation.wind_tunnel_size_moderate", "WindTunnelSizeModerate"),
    "WithFictitiousClearance": (
        "simscale_sdk_v1.models.simulation.with_fictitious_clearance",
        "WithFictitiousClearance",
    ),
    "WriteInterval": ("simscale_sdk_v1.models.simulation.write_interval", "WriteInterval"),
    "WriteIntervalWriteControl": (
        "simscale_sdk_v1.models.simulation.write_interval_write_control",
        "WriteIntervalWriteControl",
    ),
    "XAxis": ("simscale_sdk_v1.models.simulation.x_axis", "XAxis"),
    "YAxis": ("simscale_sdk_v1.models.simulation.y_axis", "YAxis"),
    "YPlusRASResultType": ("simscale_sdk_v1.models.simulation.y_plus_ras_result_type", "YPlusRASResultType"),
    "YeohHyperElasticModel": ("simscale_sdk_v1.models.simulation.yeoh_hyper_elastic_model", "YeohHyperElasticModel"),
    "YeohPrimaryNetwork": ("simscale_sdk_v1.models.simulation.yeoh_primary_network", "YeohPrimaryNetwork"),
    "ZAxis": ("simscale_sdk_v1.models.simulation.z_axis", "ZAxis"),
    "ZeroGradientDVBC": ("simscale_sdk_v1.models.simulation.zero_gradient_dvbc", "ZeroGradientDVBC"),
    "ZeroGradientEBC": ("simscale_sdk_v1.models.simulation.zero_gradient_ebc", "ZeroGradientEBC"),
    "ZeroGradientEVBC": ("simscale_sdk_v1.models.simulation.zero_gradient_evbc", "ZeroGradientEVBC"),
    "ZeroGradientEVCBC": ("simscale_sdk_v1.models.simulation.zero_gradient_evcbc", "ZeroGradientEVCBC"),
    "ZeroGradientHumidityBC": ("simscale_sdk_v1.models.simulation.zero_gradient_humidity_bc", "ZeroGradientHumidityBC"),
    "ZeroGradientNBC": ("simscale_sdk_v1.models.simulation.zero_gradient_nbc", "ZeroGradientNBC"),
    "ZeroGradientOBC": ("simscale_sdk_v1.models.simulation.zero_gradient_obc", "ZeroGradientOBC"),
    "ZeroGradientPBC": ("simscale_sdk_v1.models.simulation.zero_gradient_pbc", "ZeroGradientPBC"),
    "ZeroGradientPFBC": ("simscale_sdk_v1.models.simulation.zero_gradient_pfbc", "ZeroGradientPFBC"),
    "ZeroGradientPSBC": ("simscale_sdk_v1.models.simulation.zero_gradient_psbc", "ZeroGradientPSBC"),
    "ZeroGradientTDBC": ("simscale_sdk_v1.models.simulation.zero_gradient_tdbc", "ZeroGradientTDBC"),
    "ZeroGradientTDCBC": ("simscale_sdk_v1.models.simulation.zero_gradient_tdcbc", "ZeroGradientTDCBC"),
    "ZeroGradientTKEBC": ("simscale_sdk_v1.models.simulation.zero_gradient_tkebc", "ZeroGradientTKEBC"),
    "ZeroGradientVBC": ("simscale_sdk_v1.models.simulation.zero_gradient_vbc", "ZeroGradientVBC"),
    "Simulation": ("simscale_sdk_v1.models.simulation._root", "Simulation"),
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
