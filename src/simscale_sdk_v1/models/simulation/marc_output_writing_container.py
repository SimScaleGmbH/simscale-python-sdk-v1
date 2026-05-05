from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_output_writing_container_output_writing import (
    OneOf_MarcOutputWritingContainerOutputWriting,
)


class MarcOutputWritingContainer(SimScaleModel):
    output_writing: OneOf_MarcOutputWritingContainerOutputWriting | None = Field(
        validation_alias="outputWriting", serialization_alias="outputWriting", default=None
    )
