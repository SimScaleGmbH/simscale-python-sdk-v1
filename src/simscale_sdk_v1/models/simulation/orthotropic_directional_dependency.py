from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_expansion_rate import (
    DimensionalFunction_ThermalExpansionRate,
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


class OrthotropicDirectionalDependency(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ORTHOTROPIC",
        description="Schema name: OrthotropicDirectionalDependency",
    )
    youngs_modulus_x: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulusX", serialization_alias="youngsModulusX", default=None
    )
    youngs_modulus_y: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulusY", serialization_alias="youngsModulusY", default=None
    )
    youngs_modulus_z: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulusZ", serialization_alias="youngsModulusZ", default=None
    )
    poissons_ratio_xy: OneOf_OrthotropicDirectionalDependencyPoissonsRatioXY | None = Field(
        validation_alias="poissonsRatioXY", serialization_alias="poissonsRatioXY", default=None
    )
    poissons_ratio_yz: OneOf_OrthotropicDirectionalDependencyPoissonsRatioYZ | None = Field(
        validation_alias="poissonsRatioYZ", serialization_alias="poissonsRatioYZ", default=None
    )
    poissons_ratio_xz: OneOf_OrthotropicDirectionalDependencyPoissonsRatioXZ | None = Field(
        validation_alias="poissonsRatioXZ", serialization_alias="poissonsRatioXZ", default=None
    )
    shear_modulus_xy: DimensionalFunction_Pressure | None = Field(
        validation_alias="shearModulusXY", serialization_alias="shearModulusXY", default=None
    )
    shear_modulus_yz: DimensionalFunction_Pressure | None = Field(
        validation_alias="shearModulusYZ", serialization_alias="shearModulusYZ", default=None
    )
    shear_modulus_xz: DimensionalFunction_Pressure | None = Field(
        validation_alias="shearModulusXZ", serialization_alias="shearModulusXZ", default=None
    )
    expansion_coefficient_x: DimensionalFunction_ThermalExpansionRate | None = Field(
        validation_alias="expansionCoefficientX", serialization_alias="expansionCoefficientX", default=None
    )
    expansion_coefficient_y: DimensionalFunction_ThermalExpansionRate | None = Field(
        validation_alias="expansionCoefficientY", serialization_alias="expansionCoefficientY", default=None
    )
    expansion_coefficient_z: DimensionalFunction_ThermalExpansionRate | None = Field(
        validation_alias="expansionCoefficientZ", serialization_alias="expansionCoefficientZ", default=None
    )
    reference_temperature: Dimensional_Temperature | None = Field(
        validation_alias="referenceTemperature", serialization_alias="referenceTemperature", default=None
    )
