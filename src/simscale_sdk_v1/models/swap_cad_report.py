from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SwapCadReport(SimScaleModel):
    """The report provides details on unsuccessful entity mappings found in the assignments.  Ideally, this section should be empty, indicating that all entities were mapped correctly. Please review the reported fields to verify and correct any discrepancies."""

    unmapped_paths: list[str] | None = Field(
        validation_alias="unmappedPaths",
        serialization_alias="unmappedPaths",
        default=None,
        description="List of unmapped assignments.",
    )
    partially_mapped_paths: list[str] | None = Field(
        validation_alias="partiallyMappedPaths",
        serialization_alias="partiallyMappedPaths",
        default=None,
        description="List of partially mapped assignments.",
    )
