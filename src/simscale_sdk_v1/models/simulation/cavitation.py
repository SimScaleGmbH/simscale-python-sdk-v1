from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__molar_mass import Dimensional_MolarMass
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class Cavitation(SimScaleModel):
    vapor_molecular_weight: Dimensional_MolarMass | None = Field(
        validation_alias="vaporMolecularWeight", serialization_alias="vaporMolecularWeight", default=None
    )
    liquid_bulk_modulus: Dimensional_Pressure | None = Field(
        validation_alias="liquidBulkModulus", serialization_alias="liquidBulkModulus", default=None
    )
    liquid_bulk_modulus_coefficient: float | None = Field(
        validation_alias="liquidBulkModulusCoefficient",
        serialization_alias="liquidBulkModulusCoefficient",
        default=0,
        description="The liquid bulk modulus coefficient B1 accounts for a linear rate of change in the liquid bulk modulus with respect to pressure such that B = B0 + B1 (P - Pref), where B0 is the constant liquid bulk modulus. Typically only applicable in cases where pressure differences exceed 100 bar, otherwise a zero value should be specified.",
    )
    liquid_reference_pressure: Dimensional_Pressure | None = Field(
        validation_alias="liquidReferencePressure", serialization_alias="liquidReferencePressure", default=None
    )
    saturation_pressure: Dimensional_Pressure | None = Field(
        validation_alias="saturationPressure", serialization_alias="saturationPressure", default=None
    )
    liquid_temperature: Dimensional_Temperature | None = Field(
        validation_alias="liquidTemperature", serialization_alias="liquidTemperature", default=None
    )
