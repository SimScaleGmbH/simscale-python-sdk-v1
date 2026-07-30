from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CloseSheetV2Parameters(SimScaleModel):
    occurrences: list[str] | None = Field(default=None, description="List of sheet bodies.")
    heal_option: Literal["cap", "grow_from_child"] = Field(
        description="The `cap` healing option creates a surface to cover the existing holes. The `grow_from_child` healing option extends the faces around the holes in order to create a patch."
    )
