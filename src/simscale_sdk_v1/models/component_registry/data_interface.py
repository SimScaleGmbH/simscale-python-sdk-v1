from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.component_registry.data_description import DataDescription


class DataInterface(SimScaleModel):
    """Description of the input and output data of a method or a workflow."""

    input: list[DataDescription] | None = Field(default=None)
    output: list[DataDescription] | None = Field(default=None)
