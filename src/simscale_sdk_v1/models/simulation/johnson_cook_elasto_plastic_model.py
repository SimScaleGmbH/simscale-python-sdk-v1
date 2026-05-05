from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__strain_rate import Dimensional_StrainRate
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__johnson_cook_elasto_plastic_model_poissons_ratio import (
    OneOf_JohnsonCookElastoPlasticModelPoissonsRatio,
)


class JohnsonCookElastoPlasticModel(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="JOHNSON_COOK",
        description="Schema name: JohnsonCookElastoPlasticModel",
    )
    youngs_modulus: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulus", serialization_alias="youngsModulus", default=None
    )
    poissons_ratio: OneOf_JohnsonCookElastoPlasticModelPoissonsRatio | None = Field(
        validation_alias="poissonsRatio", serialization_alias="poissonsRatio", default=None
    )
    initial_yield_stress: DimensionalFunction_Pressure | None = Field(
        validation_alias="initialYieldStress", serialization_alias="initialYieldStress", default=None
    )
    hardening_coefficient: DimensionalFunction_Pressure | None = Field(
        validation_alias="hardeningCoefficient", serialization_alias="hardeningCoefficient", default=None
    )
    hardening_exponent: float | None = Field(
        validation_alias="hardeningExponent",
        serialization_alias="hardeningExponent",
        default=None,
        description="The strain hardening exponent describes the rate at which the material hardens with respect to plastic strain.",
    )
    strain_rate_effect: bool | None = Field(
        validation_alias="strainRateEffect",
        serialization_alias="strainRateEffect",
        default=False,
        description="This term indicates how the flow stress increases with increasing strain rate.",
    )
    strain_rate_hardening_coefficient: float | None = Field(
        validation_alias="strainRateHardeningCoefficient",
        serialization_alias="strainRateHardeningCoefficient",
        default=0.0,
        description="The strain rate hardening coefficient describes the sensitivity of the material's flow stress to changes in the strain rate.",
    )
    reference_strain_rate: Dimensional_StrainRate | None = Field(
        validation_alias="referenceStrainRate", serialization_alias="referenceStrainRate", default=None
    )
    thermal_softening_effect: bool | None = Field(
        validation_alias="thermalSofteningEffect",
        serialization_alias="thermalSofteningEffect",
        default=False,
        description="This term indicates how the material softens with increasing temperature.",
    )
    thermal_softening_exponent: float | None = Field(
        validation_alias="thermalSofteningExponent",
        serialization_alias="thermalSofteningExponent",
        default=None,
        description="The thermal softening exponent describes the rate at which the material's strength decreases with increasing temperature.",
    )
    reference_temperature_jc: Dimensional_Temperature | None = Field(
        validation_alias="referenceTemperatureJC", serialization_alias="referenceTemperatureJC", default=None
    )
    melting_temperature_jc: Dimensional_Temperature | None = Field(
        validation_alias="meltingTemperatureJC", serialization_alias="meltingTemperatureJC", default=None
    )
