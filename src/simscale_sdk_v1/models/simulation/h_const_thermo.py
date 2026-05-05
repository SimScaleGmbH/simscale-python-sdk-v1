from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__specific_heat import Dimensional_SpecificHeat
from simscale_sdk_v1.models.simulation.dimensional_function__specific_heat import DimensionalFunction_SpecificHeat
from simscale_sdk_v1.models.simulation.one_of_h_const_thermo_equation_of_state import OneOf_HConstThermoEquationOfState


class HConstThermo(SimScaleModel):
    """The Thermo models are used to calculate the specific heat at constant pressure (Cp) for the fluid. The available models are:hConst: This model assumes a constant value for specific heat at fixed pressure (Cp). eConst: This model assumes a constant value for the specific heat at fixed volume (Cv)."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HCONST",
        description="The Thermo models are used to calculate the specific heat at constant pressure (Cp) for the fluid. The available models are:hConst: This model assumes a constant value for specific heat at fixed pressure (Cp). eConst: This model assumes a constant value for the specific heat at fixed volume (Cv).   Schema name: HConstThermo",
    )
    specific_heat: Dimensional_SpecificHeat | None = Field(
        validation_alias="specificHeat", serialization_alias="specificHeat", default=None
    )
    specific_heat_function: DimensionalFunction_SpecificHeat | None = Field(
        validation_alias="specificHeatFunction", serialization_alias="specificHeatFunction", default=None
    )
    equation_of_state: OneOf_HConstThermoEquationOfState | None = Field(
        validation_alias="equationOfState", serialization_alias="equationOfState", default=None
    )
