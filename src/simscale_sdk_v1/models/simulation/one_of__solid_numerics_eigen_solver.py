from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bathe_wilson import BatheWilson
from simscale_sdk_v1.models.simulation.iram_sorensen import IRAMSorensen
from simscale_sdk_v1.models.simulation.lanczos import Lanczos
from simscale_sdk_v1.models.simulation.qz import QZ

_ONE_OF__SOLID_NUMERICS_EIGEN_SOLVER_VARIANTS: dict[str, type] = {
    "SORENSEN": IRAMSorensen,
    "TRI_DIAG": Lanczos,
    "JACOBI": BatheWilson,
    "QZ": QZ,
}

OneOf_SolidNumericsEigenSolver = Annotated[
    Union[IRAMSorensen, Lanczos, BatheWilson, QZ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_NUMERICS_EIGEN_SOLVER_VARIANTS,
        )
    ),
]
