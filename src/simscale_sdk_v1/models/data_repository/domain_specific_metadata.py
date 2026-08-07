from __future__ import annotations

from pydantic import ConfigDict

from simscale_sdk_v1._base import SimScaleModel


class DomainSpecificMetadata(SimScaleModel):
    """Domain-specific metadata of a data object. A free-form JSON object whose shape is defined by the metadata schema of the data type."""

    model_config = ConfigDict(extra="allow")
