from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__specific_heat import Dimensional_SpecificHeat
from simscale_sdk_v1.models.simulation.perfect_gas_equation_of_state import PerfectGasEquationOfState


class EConstThermo(SimScaleModel):
    """The Thermo models are used to calculate the specific heat at constant pressure (Cp) for the fluid. The available models are:hConst: This model assumes a constant value for specific heat at fixed pressure (Cp). eConst: This model assumes a constant value for the specific heat at fixed volume (Cv)."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ECONST",
        description="The Thermo models are used to calculate the specific heat at constant pressure (Cp) for the fluid. The available models are:hConst: This model assumes a constant value for specific heat at fixed pressure (Cp). eConst: This model assumes a constant value for the specific heat at fixed volume (Cv).   Schema name: EConstThermo",
    )
    specific_heat: Dimensional_SpecificHeat | None = Field(
        validation_alias="specificHeat", serialization_alias="specificHeat", default=None
    )
    equation_of_state: PerfectGasEquationOfState | None = Field(
        validation_alias="equationOfState", serialization_alias="equationOfState", default=None
    )
