from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.cavitation import Cavitation
from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density
from simscale_sdk_v1.models.simulation.dimensional__molar_mass import Dimensional_MolarMass
from simscale_sdk_v1.models.simulation.dimensional__specific_heat import Dimensional_SpecificHeat
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional__thermal_expansion_rate import Dimensional_ThermalExpansionRate
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_function__specific_heat import DimensionalFunction_SpecificHeat
from simscale_sdk_v1.models.simulation.material_library_reference import MaterialLibraryReference
from simscale_sdk_v1.models.simulation.one_of__incompressible_material_fluid_type import (
    OneOf_IncompressibleMaterialFluidType,
)
from simscale_sdk_v1.models.simulation.one_of__incompressible_material_viscosity_model import (
    OneOf_IncompressibleMaterialViscosityModel,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference
from simscale_sdk_v1.models.simulation.transparent_material import TransparentMaterial


class IncompressibleMaterial(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INCOMPRESSIBLE",
        description="Schema name: IncompressibleMaterial",
    )
    name: str | None = Field(default=None)
    fluid_type: OneOf_IncompressibleMaterialFluidType | None = Field(
        validation_alias="fluidType", serialization_alias="fluidType", default=None
    )
    associated_phase: Literal["PHASE_0", "PHASE_1"] | None = Field(
        validation_alias="associatedPhase",
        serialization_alias="associatedPhase",
        default="PHASE_0",
        description="Select the corresponding phase for this material:Phase 0 would mean this material is represented by the phase fraction value of 0. Hence, a phase fraction of '0' in your setup corresponds to 100% of this fluid material.Phase 1 would mean this material is represented by the phase fraction value of 1. Hence, a phase fraction of '1' in your setup corresponds to 100% of this fluid material.",
    )
    viscosity_model: OneOf_IncompressibleMaterialViscosityModel | None = Field(
        validation_alias="viscosityModel", serialization_alias="viscosityModel", default=None
    )
    density: Dimensional_Density | None = Field(default=None)
    thermal_expansion_coefficient: Dimensional_ThermalExpansionRate | None = Field(
        validation_alias="thermalExpansionCoefficient", serialization_alias="thermalExpansionCoefficient", default=None
    )
    reference_temperature: Dimensional_Temperature | None = Field(
        validation_alias="referenceTemperature", serialization_alias="referenceTemperature", default=None
    )
    laminar_prandtl_number: float | None = Field(
        validation_alias="laminarPrandtlNumber",
        serialization_alias="laminarPrandtlNumber",
        default=None,
        description="Laminar Prandtl number is used to calculate the heat transfer in the domain.",
    )
    laminar_prandtl_number_function: DimensionalFunction_Dimensionless | None = Field(
        validation_alias="laminarPrandtlNumberFunction",
        serialization_alias="laminarPrandtlNumberFunction",
        default=None,
    )
    turbulent_prandtl_number: float | None = Field(
        validation_alias="turbulentPrandtlNumber",
        serialization_alias="turbulentPrandtlNumber",
        default=None,
        description="Turbulent Prandtl number is used to calculate the heat transfer due to turbulent effects in the domain.",
    )
    specific_heat: Dimensional_SpecificHeat | None = Field(
        validation_alias="specificHeat", serialization_alias="specificHeat", default=None
    )
    specific_heat_function: DimensionalFunction_SpecificHeat | None = Field(
        validation_alias="specificHeatFunction", serialization_alias="specificHeatFunction", default=None
    )
    molar_weight: Dimensional_MolarMass | None = Field(
        validation_alias="molarWeight", serialization_alias="molarWeight", default=None
    )
    cavitation: Cavitation | None = Field(default=None)
    radiative_behavior: TransparentMaterial | None = Field(
        validation_alias="radiativeBehavior", serialization_alias="radiativeBehavior", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
    built_in_material: str | None = Field(
        validation_alias="builtInMaterial", serialization_alias="builtInMaterial", default=None
    )
    material_library_reference: MaterialLibraryReference | None = Field(
        validation_alias="materialLibraryReference", serialization_alias="materialLibraryReference", default=None
    )
