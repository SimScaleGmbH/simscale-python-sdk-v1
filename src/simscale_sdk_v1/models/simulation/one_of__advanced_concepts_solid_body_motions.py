from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.linear_sbm import LinearSBM
from simscale_sdk_v1.models.simulation.oscillating_linear_sbm import OscillatingLinearSBM
from simscale_sdk_v1.models.simulation.oscillating_rotating_sbm import OscillatingRotatingSBM
from simscale_sdk_v1.models.simulation.rotating_sbm import RotatingSBM
from simscale_sdk_v1.models.simulation.ship_design_analysis_sbm import ShipDesignAnalysisSBM

_ONE_OF__ADVANCED_CONCEPTS_SOLID_BODY_MOTIONS_VARIANTS: dict[str, type] = {
    "LINEAR_MOTION": LinearSBM,
    "OSCILLATING_ROTATING_MOTION": OscillatingRotatingSBM,
    "OSCILLATING_LINEAR_MOTION": OscillatingLinearSBM,
    "ROTATING_MOTION": RotatingSBM,
    "SHIP_DESIGN_ANALYSIS": ShipDesignAnalysisSBM,
}

OneOf_AdvancedConceptsSolidBodyMotions = Annotated[
    Union[LinearSBM, OscillatingRotatingSBM, OscillatingLinearSBM, RotatingSBM, ShipDesignAnalysisSBM],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_SOLID_BODY_MOTIONS_VARIANTS,
        )
    ),
]
