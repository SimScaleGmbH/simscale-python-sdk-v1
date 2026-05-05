from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CustomContactStiffness(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_CONTACT_STIFFNESS",
        description="Schema name: CustomContactStiffness",
    )
    penalty_coefficient: float | None = Field(
        validation_alias="penaltyCoefficient",
        serialization_alias="penaltyCoefficient",
        default=100000000000,
        description="Define the penalty coefficient for the contact pair. As a good starting point this value should be about 5-50 times as high as the softest of the materials in this contact definition and below 1e16. A higher value reduces interpenetration but may also lead to numerical instabilities and divergence. The independence of the results from this parameter should be checked.",
    )
