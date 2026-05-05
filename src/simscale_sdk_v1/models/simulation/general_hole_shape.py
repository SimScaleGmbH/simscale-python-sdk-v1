from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GeneralHoleShape(SimScaleModel):
    """General formulation that does not depend on the shape of the holes. Valid only for thin plates where thickness to hole ratio is less than 0.015 and Reynolds number is greater than 10000."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GENERAL",
        description="General formulation that does not depend on the shape of the holes. Valid only for thin plates where thickness to hole ratio is less than 0.015 and Reynolds number is greater than 10000.  Schema name: GeneralHoleShape",
    )
