from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_function__specific_heat import DimensionalFunction_SpecificHeat
from simscale_sdk_v1.models.simulation.material_library_reference import MaterialLibraryReference
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
from simscale_sdk_v1.models.simulation.specie_default import SpecieDefault
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference
from simscale_sdk_v1.models.simulation.transparent_material import TransparentMaterial


class FluidCompressibleMaterial(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COMPRESSIBLE",
        description="Schema name: FluidCompressibleMaterial",
    )
    name: str | None = Field(default=None)
    fluid_type: OneOf_FluidCompressibleMaterialFluidType | None = Field(
        validation_alias="fluidType", serialization_alias="fluidType", default=None
    )
    associated_phase: Literal["PHASE_0", "PHASE_1"] | None = Field(
        validation_alias="associatedPhase",
        serialization_alias="associatedPhase",
        default="PHASE_0",
        description="Select the corresponding phase for this material:Phase 0 would mean this material is represented by the phase fraction value of 0. Hence, a phase fraction of '0' in your setup corresponds to 100% of this fluid material.Phase 1 would mean this material is represented by the phase fraction value of 1. Hence, a phase fraction of '1' in your setup corresponds to 100% of this fluid material.",
    )
    specie: SpecieDefault | None = Field(default=None)
    transport: OneOf_FluidCompressibleMaterialTransport | None = Field(default=None)
    viscosity_model: OneOf_FluidCompressibleMaterialViscosityModel | None = Field(
        validation_alias="viscosityModel", serialization_alias="viscosityModel", default=None
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
    schmidt_number: float | None = Field(
        validation_alias="schmidtNumber",
        serialization_alias="schmidtNumber",
        default=0.8333,
        description="The Schmidt number is a dimensionless number defined as the ratio of viscous diffusion to molecular mass diffusion. In dilute flows where a dominant carrier gas advects other species, it is assumed to be constant and a typical value is Sc = 5/6.",
    )
    specific_heat_function: DimensionalFunction_SpecificHeat | None = Field(
        validation_alias="specificHeatFunction", serialization_alias="specificHeatFunction", default=None
    )
    equation_of_state: OneOf_FluidCompressibleMaterialEquationOfState | None = Field(
        validation_alias="equationOfState", serialization_alias="equationOfState", default=None
    )
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
