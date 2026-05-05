from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class AdiabaticPerfectFluidEquationOfState(SimScaleModel):
    """The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ADIABATIC_PERFECT_FLUID",
        description="The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more.  Schema name: AdiabaticPerfectFluidEquationOfState",
    )
    reference_pressure: Dimensional_Pressure | None = Field(
        validation_alias="referencePressure", serialization_alias="referencePressure", default=None
    )
    reference_density: Dimensional_Density | None = Field(
        validation_alias="referenceDensity", serialization_alias="referenceDensity", default=None
    )
    isentropic_exponent: float | None = Field(
        validation_alias="isentropicExponent",
        serialization_alias="isentropicExponent",
        default=None,
        description="Specify the isentropic exponent. This parameter characterizes changes in density due to pressure. A Larger isentropic exponent results in less sensitivity of the density to reference pressure.",
    )
    pressure_offset: Dimensional_Pressure | None = Field(
        validation_alias="pressureOffset", serialization_alias="pressureOffset", default=None
    )
    energy: Literal["SENSIBLE_ENTHALPY", "SENSIBLE_INTERNAL_ENERGY"] | None = Field(
        default="SENSIBLE_ENTHALPY",
        description="Energy provides the methods for the form of energy to be used. The options are:Sensible enthalpy: The enthalpy form of equation is used without the heat of formation. In most cases this is the recommended choice.Sensible internal Energy: The internal energy form of equation is used without the heat of formation but also incorporates energy change due to reactions.",
    )
