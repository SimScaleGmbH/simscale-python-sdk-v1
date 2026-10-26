from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.component_registry.documentation_page import DocumentationPage


class ComponentDocumentation(SimScaleModel):
    pages: list[DocumentationPage] | None = Field(default=None)
