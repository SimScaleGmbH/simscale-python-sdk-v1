from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class SecondOrderOgden(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SECOND_ORDER_OGDEN",
        description="Schema name: SecondOrderOgden",
    )
    mu1: Dimensional_Pressure | None = Field(default=None)
    alpha1: float | None = Field(
        default=None, description="Provide a parameter value for the Ogden coefficient &alpha;1."
    )
    mu2: Dimensional_Pressure | None = Field(default=None)
    alpha2: float | None = Field(
        default=None, description="Provide a parameter value for the Ogden coefficient &alpha;2."
    )
