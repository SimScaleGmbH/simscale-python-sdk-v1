from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_convergence_residuals import AbsoluteConvergenceResiduals
from simscale_sdk_v1.models.simulation.adaptive_convergence_residuals import AdaptiveConvergenceResiduals
from simscale_sdk_v1.models.simulation.relative_convergence_residuals import RelativeConvergenceResiduals

# Defines whether the tolerances are measured relative to the overall solution, as absolute values, or dynamically adjusted.Relative: Standard for general use. Tolerances are measured as a fraction of the current reference value (e.g., maximum applied force or displacement).Absolute: Necessary when the reference forces are near zero (e.g., free expansion). Tolerances are defined as fixed values in model units.Adaptive: Allows Marc to dynamically loosen or tighten tolerances based on solution progress, balancing robustness and computational efficiency.
_ONE_OF__RESIDUALS_CONVERGENCE_METHOD_CONVERGENCE_CRITERIA_VARIANTS: dict[str, type] = {
    "RELATIVE": RelativeConvergenceResiduals,
    "ABSOLUTE": AbsoluteConvergenceResiduals,
    "ADAPTIVE": AdaptiveConvergenceResiduals,
}

OneOf_ResidualsConvergenceMethodConvergenceCriteria = Annotated[
    Union[RelativeConvergenceResiduals, AbsoluteConvergenceResiduals, AdaptiveConvergenceResiduals],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__RESIDUALS_CONVERGENCE_METHOD_CONVERGENCE_CRITERIA_VARIANTS,
        )
    ),
]
