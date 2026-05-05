from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density
from simscale_sdk_v1.models.simulation.dimensional__specific_heat import Dimensional_SpecificHeat


class PerfectFluidEquationOfState(SimScaleModel):
    """The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PERFECT_FLUID",
        description="The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more.  Schema name: PerfectFluidEquationOfState",
    )
    fluid_constant: Dimensional_SpecificHeat | None = Field(
        validation_alias="fluidConstant", serialization_alias="fluidConstant", default=None
    )
    reference_density: Dimensional_Density | None = Field(
        validation_alias="referenceDensity", serialization_alias="referenceDensity", default=None
    )
    energy: Literal["SENSIBLE_ENTHALPY", "SENSIBLE_INTERNAL_ENERGY"] | None = Field(
        default="SENSIBLE_ENTHALPY",
        description="Energy provides the methods for the form of energy to be used. The options are:Sensible enthalpy: The enthalpy form of equation is used without the heat of formation. In most cases this is the recommended choice.Sensible internal Energy: The internal energy form of equation is used without the heat of formation but also incorporates energy change due to reactions.",
    )
