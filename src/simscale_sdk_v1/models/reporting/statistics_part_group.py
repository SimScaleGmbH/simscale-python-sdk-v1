from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StatisticsPartGroup(SimScaleModel):
    """A named group of model parts whose bulk values are aggregated into a single result entry. All parts in the group are combined before computing statistics, so the result reflects the collective geometry rather than individual parts."""

    identifier: str = Field(
        description="Unique label for this group. Used as the key for this group's entry in the statisticsResult map returned when the report is finished."
    )
    part_names: list[str] = Field(
        validation_alias="partNames",
        serialization_alias="partNames",
        description="Names of the model parts to include in this group. Each name must exactly match a part name present in the simulation result. Parts not found in the model are skipped.",
    )
