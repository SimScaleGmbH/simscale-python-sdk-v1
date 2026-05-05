from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_convergence_criteria import AbsoluteConvergenceCriteria
from simscale_sdk_v1.models.simulation.adaptive_convergence_criteria import AdaptiveConvergenceCriteria
from simscale_sdk_v1.models.simulation.relative_convergence_criteria import RelativeConvergenceCriteria

# Select the convergence criterion for the nonlinear solution method.Important remarks: When Absolute is selected, the convergence is reached if the maximum absolute residual of a given Newton iteration is lower than the defined tolerance.If Relative is chosen, then the maximum relative residual i.e. the maximum absolute residual divided by external loads and support reactions, is checked during the Newton iteration. Please note that using the Relative criterion leads to a failed convergence if no external load is present (e.g. two far objects coming into contact). In this case, the Adaptive criterion should be used.By selecting the Adaptive option, a combination of both Relative and Absolute criteria is used. That is, in each Newton iteration the Relative is used by default unless the external loads and support reactions have vanished, at which point we check the Absolute one instead.
_ONE_OF__NEWTON_KRYLOV_RESOLUTION_TYPE_CONVERGENCE_CRITERIA_VARIANTS: dict[str, type] = {
    "ADAPTIVE": AdaptiveConvergenceCriteria,
    "RELATIVE": RelativeConvergenceCriteria,
    "ABSOLUTE": AbsoluteConvergenceCriteria,
}

OneOf_NewtonKrylovResolutionTypeConvergenceCriteria = Annotated[
    Union[AdaptiveConvergenceCriteria, RelativeConvergenceCriteria, AbsoluteConvergenceCriteria],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__NEWTON_KRYLOV_RESOLUTION_TYPE_CONVERGENCE_CRITERIA_VARIANTS,
        )
    ),
]
