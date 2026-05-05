from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.minimum_gap_size import MinimumGapSize
from simscale_sdk_v1.models.simulation.smallest_cell import SmallestCell

_ONE_OF__PACEFISH_AUTOMESH_AUTOMATIC_GAP_CLOSING_VARIANTS: dict[str, type] = {
    "SMALLEST_CELL_SIZE": SmallestCell,
    "MINIMUM_GAP_SIZE": MinimumGapSize,
}

OneOf_PacefishAutomeshAutomaticGapClosing = Annotated[
    Union[SmallestCell, MinimumGapSize],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PACEFISH_AUTOMESH_AUTOMATIC_GAP_CLOSING_VARIANTS,
        )
    ),
]
