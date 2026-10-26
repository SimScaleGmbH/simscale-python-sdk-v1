from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.length import Length


class FindGapsParameters(SimScaleModel):
    max_size: Length = Field(validation_alias="maxSize", serialization_alias="maxSize")
    min_size: Length = Field(validation_alias="minSize", serialization_alias="minSize")
    max_angle: float = Field(
        validation_alias="maxAngle",
        serialization_alias="maxAngle",
        description="Maximum allowed angle between the normals of the opposing gap faces. Allowed values are between 0 and 90 degrees.",
    )
