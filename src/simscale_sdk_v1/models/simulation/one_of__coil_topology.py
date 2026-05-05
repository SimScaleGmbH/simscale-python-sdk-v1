from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.closed_coil import ClosedCoil
from simscale_sdk_v1.models.simulation.open_coil import OpenCoil

# Open Coil: This coil topology has an entry port and an exit port.Example of an open coil with an entry (blue) and exit (red) port. Note that an entry port and exit port should lie on an outer boundary with Magnetic flux tangential boundaries.  Closed Coil: This coil topology is a self-contained loop with no entry or exit ports. An internal port is used to specify the current flow surface within the coil. Example of a closed coil with an internal port (blue).
_ONE_OF__COIL_TOPOLOGY_VARIANTS: dict[str, type] = {
    "OPEN_COIL": OpenCoil,
    "CLOSED_COIL": ClosedCoil,
}

OneOf_CoilTopology = Annotated[
    Union[OpenCoil, ClosedCoil],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__COIL_TOPOLOGY_VARIANTS,
        )
    ),
]
