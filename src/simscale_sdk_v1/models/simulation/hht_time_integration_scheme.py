from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class HhtTimeIntegrationScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HHT",
        description="Schema name: HhtTimeIntegrationScheme",
    )
    alpha: float | None = Field(
        default=-0.1,
        description="The parameter &alpha; is given by a negative value. The larger |&alpha;| is, the more numerical damping is induced.",
    )
    method: Literal["AVERAGE_ACCELERATION", "ALPHA_METHOD"] | None = Field(
        default="ALPHA_METHOD",
        description="Choose the mode of the HHT method. Compared to the average acceleration scheme the induced numerical damping of the alpha method is more selective: it is weaker for low frequencies and it will increase with the frequencies.",
    )
