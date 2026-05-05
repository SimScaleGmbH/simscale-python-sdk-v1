from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_function__acceleration import DimensionalFunction_Acceleration
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless


class BaseExcitationBC(SimScaleModel):
    """Base excitation boundary condition applies a uniform acceleration to all fixed surfaces in the model (zero displacement), e.g. faces assigned to the Fixed support boundary condition. Specify the direction vector, the acceleration magnitude and the delay in terms of a harmonic phase angle, from the load to the reference harmonic excitation.Learn more"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BASE_EXCITATION",
        description="Base excitation boundary condition applies a uniform acceleration to all fixed surfaces in the model (zero displacement), e.g. faces assigned to the Fixed support boundary condition. Specify the direction vector, the acceleration magnitude and the delay in terms of a harmonic phase angle, from the load to the reference harmonic excitation.Learn more  Schema name: BaseExcitationBC",
    )
    name: str | None = Field(default=None)
    direction: DimensionalVector_Dimensionless | None = Field(default=None)
    acceleration: DimensionalFunction_Acceleration | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
