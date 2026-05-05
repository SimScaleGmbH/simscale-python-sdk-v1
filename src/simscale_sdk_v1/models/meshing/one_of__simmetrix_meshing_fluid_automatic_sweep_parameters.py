from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.automatic_sweep_off import AutomaticSweepOff
from simscale_sdk_v1.models.meshing.automatic_sweep_on import AutomaticSweepOn

# This toggle enables the automatic detection and meshing of sweepable bodies.
_ONE_OF__SIMMETRIX_MESHING_FLUID_AUTOMATIC_SWEEP_PARAMETERS_VARIANTS: dict[str, type] = {
    "AUTOMATIC_SWEEP_MESHING_ON": AutomaticSweepOn,
    "AUTOMATIC_SWEEP_MESHING_OFF": AutomaticSweepOff,
}

OneOf_SimmetrixMeshingFluidAutomaticSweepParameters = Annotated[
    Union[AutomaticSweepOn, AutomaticSweepOff],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_MESHING_FLUID_AUTOMATIC_SWEEP_PARAMETERS_VARIANTS,
        )
    ),
]
