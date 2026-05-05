from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.all_computed import AllComputed
from simscale_sdk_v1.models.simulation.output_steps import OutputSteps
from simscale_sdk_v1.models.simulation.write_interval import WriteInterval

# Choose how to write the results for the simulation:All computed writes the results for every step. This can lead to a lot of output, especially in simulations with lots of time stepping cutbacks. That takes accordingly longer to post-process.Write interval allows to specify the interval at which results are written.Output steps is used to control the total number of steps for which output is written.
_ONE_OF__MARC_OUTPUT_WRITING_CONTAINER_OUTPUT_WRITING_VARIANTS: dict[str, type] = {
    "ALL_COMPUTED": AllComputed,
    "WRITE_INTERVAL": WriteInterval,
    "OUTPUT_STEPS": OutputSteps,
}

OneOf_MarcOutputWritingContainerOutputWriting = Annotated[
    Union[AllComputed, WriteInterval, OutputSteps],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_OUTPUT_WRITING_CONTAINER_OUTPUT_WRITING_VARIANTS,
        )
    ),
]
