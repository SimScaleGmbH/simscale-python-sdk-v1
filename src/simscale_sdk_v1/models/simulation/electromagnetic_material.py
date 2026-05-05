from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.isotropic_density_method import IsotropicDensityMethod
from simscale_sdk_v1.models.simulation.isotropic_specific_heat_method import IsotropicSpecificHeatMethod
from simscale_sdk_v1.models.simulation.isotropic_thermal_conductivity_method import IsotropicThermalConductivityMethod
from simscale_sdk_v1.models.simulation.linear_isotropic_permittivity_method import LinearIsotropicPermittivityMethod
from simscale_sdk_v1.models.simulation.material_library_reference import MaterialLibraryReference
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
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ElectromagneticMaterial(SimScaleModel):
    name: str | None = Field(default=None)
    material_behavior: OneOf_ElectromagneticMaterialMaterialBehavior | None = Field(
        validation_alias="materialBehavior", serialization_alias="materialBehavior", default=None
    )
    electric_conductivity_type: OneOf_ElectromagneticMaterialElectricConductivityType | None = Field(
        validation_alias="electricConductivityType", serialization_alias="electricConductivityType", default=None
    )
    magnetic_permeability_type: OneOf_ElectromagneticMaterialMagneticPermeabilityType | None = Field(
        validation_alias="magneticPermeabilityType", serialization_alias="magneticPermeabilityType", default=None
    )
    electric_permittivity_type: LinearIsotropicPermittivityMethod | None = Field(
        validation_alias="electricPermittivityType", serialization_alias="electricPermittivityType", default=None
    )
    density_type: IsotropicDensityMethod | None = Field(
        validation_alias="densityType", serialization_alias="densityType", default=None
    )
    specific_heat_type: IsotropicSpecificHeatMethod | None = Field(
        validation_alias="specificHeatType", serialization_alias="specificHeatType", default=None
    )
    thermal_conductivity: IsotropicThermalConductivityMethod | None = Field(
        validation_alias="thermalConductivity", serialization_alias="thermalConductivity", default=None
    )
    dielectric_strength_type: OneOf_ElectromagneticMaterialDielectricStrengthType | None = Field(
        validation_alias="dielectricStrengthType", serialization_alias="dielectricStrengthType", default=None
    )
    core_losses_type: OneOf_ElectromagneticMaterialCoreLossesType | None = Field(
        validation_alias="coreLossesType", serialization_alias="coreLossesType", default=None
    )
    dielectric_loss_type: OneOf_ElectromagneticMaterialDielectricLossType | None = Field(
        validation_alias="dielectricLossType", serialization_alias="dielectricLossType", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    built_in_material: str | None = Field(
        validation_alias="builtInMaterial", serialization_alias="builtInMaterial", default=None
    )
    material_library_reference: MaterialLibraryReference | None = Field(
        validation_alias="materialLibraryReference", serialization_alias="materialLibraryReference", default=None
    )
