from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.hierarchical_decompose_algorithm import HierarchicalDecomposeAlgorithm
from simscale_sdk_v1.models.simulation.scotch_decompose_algorithm import ScotchDecomposeAlgorithm
from simscale_sdk_v1.models.simulation.simple_decompose_algorithm import SimpleDecomposeAlgorithm

_ONE_OF__FLUID_SIMULATION_CONTROL_DECOMPOSE_ALGORITHM_VARIANTS: dict[str, type] = {
    "SCOTCH": ScotchDecomposeAlgorithm,
    "HIERARCHICAL": HierarchicalDecomposeAlgorithm,
    "SIMPLE": SimpleDecomposeAlgorithm,
}

OneOf_FluidSimulationControlDecomposeAlgorithm = Annotated[
    Union[ScotchDecomposeAlgorithm, HierarchicalDecomposeAlgorithm, SimpleDecomposeAlgorithm],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_SIMULATION_CONTROL_DECOMPOSE_ALGORITHM_VARIANTS,
        )
    ),
]
