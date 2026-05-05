from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__density import DimensionalFunction_Density
from simscale_sdk_v1.models.simulation.dimensional_function__specific_energy import DimensionalFunction_SpecificEnergy


class RealGasEquationOfState(SimScaleModel):
    """The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REAL_GAS",
        description="The Equation of state describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:Rho const: Fluid density is assumed constant.Incompressibel perfect gas: The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.Perfect gas: Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.Perfect fluid: Fluid density can change due to pressure and temperature with respect to a base value.Adiabatic perfect fluid: The fluid is a perfect fluid which is adiabatic in nature. Learn more.  Schema name: RealGasEquationOfState",
    )
    density: DimensionalFunction_Density | None = Field(default=None)
    specific_enthalpy: DimensionalFunction_SpecificEnergy | None = Field(
        validation_alias="specificEnthalpy", serialization_alias="specificEnthalpy", default=None
    )
