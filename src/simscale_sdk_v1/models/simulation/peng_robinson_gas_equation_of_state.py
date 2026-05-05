from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__molar_mass import Dimensional_MolarMass
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class PengRobinsonGasEquationOfState(SimScaleModel):
    """The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PENG_ROBINSON_GAS",
        description="The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more.  Schema name: PengRobinsonGasEquationOfState",
    )
    critical_temperature: Dimensional_Temperature | None = Field(
        validation_alias="criticalTemperature", serialization_alias="criticalTemperature", default=None
    )
    critical_volume: Dimensional_MolarMass | None = Field(
        validation_alias="criticalVolume", serialization_alias="criticalVolume", default=None
    )
    critical_pressure: Dimensional_Pressure | None = Field(
        validation_alias="criticalPressure", serialization_alias="criticalPressure", default=None
    )
    acentric_factor: float | None = Field(
        validation_alias="acentricFactor",
        serialization_alias="acentricFactor",
        default=None,
        description="Specify the acentric factor. It is a property of the material that characterized the changes in thermodynamic properties of the fluid due to non-spherical molecules.",
    )
    energy: Literal["SENSIBLE_ENTHALPY", "SENSIBLE_INTERNAL_ENERGY"] | None = Field(
        default="SENSIBLE_ENTHALPY",
        description="Energy provides the methods for the form of energy to be used. The options are:Sensible enthalpy: The enthalpy form of equation is used without the heat of formation. In most cases this is the recommended choice.Sensible internal Energy: The internal energy form of equation is used without the heat of formation but also incorporates energy change due to reactions.",
    )
