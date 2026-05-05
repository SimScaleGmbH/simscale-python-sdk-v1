from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.off_position_tolerance import OffPositionTolerance
from simscale_sdk_v1.models.simulation.set_value_position_tolerance import SetValuePositionTolerance

# Define how gaps and small interferences should be treated:Set Value: Define a numerical distance (tolerance) below which contact is established. If the gap between a contacting node and its target body is larger than the tolerance, the glued contact constraint will not be activated on this node. This check happens on each iteration. For this option the &quot;stress-free projection&quot; of contact nodes on the target surfaces is activated. Small gaps will be closed without adding stresses.Use this option for cases where small CAD inaccuracies, manufacturing tolerances or mesh discretization errors might appear.Off: No specific contact tolerance is used. The program uses an automatic value based on element size (1/10th of the typical element size) to overcome small gaps or penetrations due to mesh approximations on curved surfaces. No &quot;stress-free projection&quot; is active for this setting.
_ONE_OF__MARC_BONDED_CONTACT_CONNECTION_POSITION_TOLERANCE_VARIANTS: dict[str, type] = {
    "SET_VALUE": SetValuePositionTolerance,
    "OFF": OffPositionTolerance,
}

OneOf_MarcBondedContactConnectionPositionTolerance = Annotated[
    Union[SetValuePositionTolerance, OffPositionTolerance],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_BONDED_CONTACT_CONNECTION_POSITION_TOLERANCE_VARIANTS,
        )
    ),
]
