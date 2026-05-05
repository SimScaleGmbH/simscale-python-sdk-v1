from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation_run_result_convergence_plot import SimulationRunResultConvergencePlot
from simscale_sdk_v1.models.simulation_run_result_plot import SimulationRunResultPlot
from simscale_sdk_v1.models.simulation_run_result_solution import SimulationRunResultSolution
from simscale_sdk_v1.models.simulation_run_result_table import SimulationRunResultTable

_ONE_OF_SIMULATION_RUN_RESULT_VARIANTS: dict[str, type] = {
    "SOLUTION_FIELD": SimulationRunResultSolution,
    "CONVERGENCE_PLOT": SimulationRunResultConvergencePlot,
    "PLOT": SimulationRunResultPlot,
    "TABLE": SimulationRunResultTable,
}

OneOfSimulationRunResult = Annotated[
    Union[
        SimulationRunResultSolution,
        SimulationRunResultConvergencePlot,
        SimulationRunResultPlot,
        SimulationRunResultTable,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_SIMULATION_RUN_RESULT_VARIANTS,
        )
    ),
]
