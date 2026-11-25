from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.minimum_gap_size import MinimumGapSize
from simscale_sdk_v1.models.simulation.smallest_cell import SmallestCell

# Automatic gap closing has two purposes:Closing gaps: Openings (such as doors or windows) smaller than the Automatic gap closing value are closed. Select Minimum gap size to set the value manually.Memory efficiency: An Automatic gap closing value above the Smallest cell size, typically 4x, greatly reduces memory demand.Note: Make sure openings relevant to the flow are larger than this value.
_ONE_OF__WIND_COMFORT_MESH_AUTOMATIC_GAP_CLOSING_VARIANTS: dict[str, type] = {
    "SMALLEST_CELL_SIZE": SmallestCell,
    "MINIMUM_GAP_SIZE": MinimumGapSize,
}

OneOf_WindComfortMeshAutomaticGapClosing = Annotated[
    Union[SmallestCell, MinimumGapSize],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WIND_COMFORT_MESH_AUTOMATIC_GAP_CLOSING_VARIANTS,
        )
    ),
]
