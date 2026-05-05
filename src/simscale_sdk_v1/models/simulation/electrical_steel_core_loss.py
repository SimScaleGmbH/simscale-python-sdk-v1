from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ElectricalSteelCoreLoss(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ELECTRICAL_STEEL",
        description="Schema name: ElectricalSteelCoreLoss",
    )
    hysteresis_loss: float | None = Field(
        validation_alias="hysteresisLoss", serialization_alias="hysteresisLoss", default=0.0
    )
    eddy_loss: float | None = Field(validation_alias="eddyLoss", serialization_alias="eddyLoss", default=0.0)
    excess_loss: float | None = Field(validation_alias="excessLoss", serialization_alias="excessLoss", default=0.0)
