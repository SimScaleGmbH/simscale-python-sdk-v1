from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.with_cell_zone import WithCellZone
from simscale_sdk_v1.models.meshing.without_cell_zone import WithoutCellZone

# You can create cell zones in your mesh by assigning this option to one or more of your CAD bodies. They can be later defined as Rotating Zones or Porosity Volumes, among others. Check these options under “Advanced Concepts” in the simulation tree.
_ONE_OF__SURFACE_REFINEMENT_CELL_ZONE_VARIANTS: dict[str, type] = {
    "WITHOUT_CELL_ZONE": WithoutCellZone,
    "WITH_CELL_ZONE_V11": WithCellZone,
}

OneOf_SurfaceRefinementCellZone = Annotated[
    Union[WithoutCellZone, WithCellZone],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SURFACE_REFINEMENT_CELL_ZONE_VARIANTS,
        )
    ),
]
