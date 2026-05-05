from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.natural_convection_inlet_outlet_bc import NaturalConvectionInletOutletBC
from simscale_sdk_v1.models.simulation.wall_bc import WallBC

_ONE_OF__EMBEDDED_BOUNDARY_EXTERNAL_FLOW_BOUNDARY_CONDITION_VARIANTS: dict[str, type] = {
    "WALL_V34": WallBC,
    "NATURAL_CONVECTION_INLET_OUTLET": NaturalConvectionInletOutletBC,
}

OneOf_EmbeddedBoundaryExternalFlowBoundaryCondition = Annotated[
    Union[WallBC, NaturalConvectionInletOutletBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__EMBEDDED_BOUNDARY_EXTERNAL_FLOW_BOUNDARY_CONDITION_VARIANTS,
        )
    ),
]
