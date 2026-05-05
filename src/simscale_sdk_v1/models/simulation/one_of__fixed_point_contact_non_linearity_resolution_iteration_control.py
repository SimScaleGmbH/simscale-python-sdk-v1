from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.maximum_number_iteration_control import MaximumNumberIterationControl
from simscale_sdk_v1.models.simulation.multiplied_slave_nodes_iteration_control import (
    MultipliedSlaveNodesIterationControl,
)

_ONE_OF__FIXED_POINT_CONTACT_NON_LINEARITY_RESOLUTION_ITERATION_CONTROL_VARIANTS: dict[str, type] = {
    "MAXIMUM_NUMBER": MaximumNumberIterationControl,
    "MULTIPLIED_SLAVE_NODE": MultipliedSlaveNodesIterationControl,
}

OneOf_FixedPointContactNonLinearityResolutionIterationControl = Annotated[
    Union[MaximumNumberIterationControl, MultipliedSlaveNodesIterationControl],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIXED_POINT_CONTACT_NON_LINEARITY_RESOLUTION_ITERATION_CONTROL_VARIANTS,
        )
    ),
]
