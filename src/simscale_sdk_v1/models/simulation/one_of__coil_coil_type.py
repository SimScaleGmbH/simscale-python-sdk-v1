from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.litz_wire_coil import LitzWireCoil
from simscale_sdk_v1.models.simulation.solid_coil import SolidCoil
from simscale_sdk_v1.models.simulation.stranded_coil import StrandedCoil

# Solid Coil: Is used for coils with usually only a few turns and large-diameter wire which requires explicit meshing. Eddy current effects are significant due to the wire's large diameter where skin depth is about the same or smaller than the wire diameter. Example of a solid coil where each wire is meshed explictly.   Stranded Coil: Employed when wires are closely packed, thin, and eddy currents can be neglected. This model represents multiple wires without the need of explicit meshing them, which save significant computational time.Example of a stranded coil where wires are not meshed explicitly.
_ONE_OF__COIL_COIL_TYPE_VARIANTS: dict[str, type] = {
    "STRANDED_COIL": StrandedCoil,
    "SOLID_COIL": SolidCoil,
    "LITZ_WIRE_COIL": LitzWireCoil,
}

OneOf_CoilCoilType = Annotated[
    Union[StrandedCoil, SolidCoil, LitzWireCoil],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__COIL_COIL_TYPE_VARIANTS,
        )
    ),
]
