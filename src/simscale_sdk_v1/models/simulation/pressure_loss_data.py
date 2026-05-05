from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__area import Dimensional_Area
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class PressureLossData(SimScaleModel):
    pressure_loss_curve: DimensionalFunction_Pressure | None = Field(
        validation_alias="pressureLossCurve", serialization_alias="pressureLossCurve", default=None
    )
    flow_direction_length: Dimensional_Length | None = Field(
        validation_alias="flowDirectionLength", serialization_alias="flowDirectionLength", default=None
    )
    cross_section_area: Dimensional_Area | None = Field(
        validation_alias="crossSectionArea", serialization_alias="crossSectionArea", default=None
    )
