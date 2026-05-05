from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.one_of__field_calculations_wall_heat_flux_result_control_reference_temperature_result_type import (
    OneOf_FieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType,
)
from simscale_sdk_v1.models.simulation.wall_heat_flux_result_type import WallHeatFluxResultType


class FieldCalculationsWallHeatFluxResultControl(SimScaleModel):
    """Computes the heat flux [W/m²] at every wall based on the surface normal gradient of the temperature. Radiation effects are not included."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WALL_HEAT_FLUX",
        description="Computes the heat flux [W/m²] at every wall based on the surface normal gradient of the temperature. Radiation effects are not included.  Schema name: FieldCalculationsWallHeatFluxResultControl",
    )
    name: str | None = Field(default=None)
    result_type: WallHeatFluxResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
    compute_heat_transfer_coefficient: bool | None = Field(
        validation_alias="computeHeatTransferCoefficient",
        serialization_alias="computeHeatTransferCoefficient",
        default=False,
        description="Computes the heat transfer coefficient [W/(m²K)] at every wall. Radiation effects are not included. Two modes are available for the reference temperature calculation:  Wall adjacent cell: Uses the temperature of the first adjacent cell.  Fixed: Uses a custom value.",
    )
    reference_temperature_result_type: (
        OneOf_FieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType | None
    ) = Field(
        validation_alias="referenceTemperatureResultType",
        serialization_alias="referenceTemperatureResultType",
        default=None,
    )
    compute_nusselt_number: bool | None = Field(
        validation_alias="computeNusseltNumber",
        serialization_alias="computeNusseltNumber",
        default=False,
        description="Computes the Nusselt Number at every wall. The specified heat transfer coefficient mode will be used.",
    )
    reference_nusselt_number_length: Dimensional_Length | None = Field(
        validation_alias="referenceNusseltNumberLength",
        serialization_alias="referenceNusseltNumberLength",
        default=None,
    )
