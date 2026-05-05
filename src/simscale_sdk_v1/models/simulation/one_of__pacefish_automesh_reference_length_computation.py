from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_reference_length import AutomaticReferenceLength
from simscale_sdk_v1.models.simulation.manual_reference_length import ManualReferenceLength

_ONE_OF__PACEFISH_AUTOMESH_REFERENCE_LENGTH_COMPUTATION_VARIANTS: dict[str, type] = {
    "AUTOMATIC_REFERENCE_LENGTH": AutomaticReferenceLength,
    "MANUAL_REFERENCE_LENGTH": ManualReferenceLength,
}

OneOf_PacefishAutomeshReferenceLengthComputation = Annotated[
    Union[AutomaticReferenceLength, ManualReferenceLength],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PACEFISH_AUTOMESH_REFERENCE_LENGTH_COMPUTATION_VARIANTS,
        )
    ),
]
