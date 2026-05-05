from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_subspace_settings import AutomaticSubspaceSettings
from simscale_sdk_v1.models.simulation.subspace_coefficient import SubspaceCoefficient
from simscale_sdk_v1.models.simulation.subspace_dimension import SubspaceDimension

# Specify the subspace used by the eigensolver. This setting should only be changed if the errors during the solution procedure occur that recommend to change it. In general, the more frequencies are computed, the larger the subspace should be. Automatic: The solver selects an appropriate subspace itself based on the model and other inputs.Dimension: Directly specify the subspace dimension. This should be only done after checking the error log, which gives hints on selecting this setting.Coefficient: Multiplier for setting the subspace dimension proportional to the number of computed frequencies
_ONE_OF_IRAM_SORENSEN_SUBSPACE_SETTINGS_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticSubspaceSettings,
    "SUBSPACE_DIMENSION": SubspaceDimension,
    "SUBSPACE_COEFFICIENT": SubspaceCoefficient,
}

OneOf_IRAMSorensenSubspaceSettings = Annotated[
    Union[AutomaticSubspaceSettings, SubspaceDimension, SubspaceCoefficient],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_IRAM_SORENSEN_SUBSPACE_SETTINGS_VARIANTS,
        )
    ),
]
