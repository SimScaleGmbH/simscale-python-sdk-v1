from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.heat_exchanger_performance import HeatExchangerPerformance
from simscale_sdk_v1.models.simulation.heat_transfer_coefficients import HeatTransferCoefficients

# The overall conductance (U) of the heat exchanger can be modelled in two different ways:Heat transfer coefficients: In this model the overall conductance (U) is computed using the heat transfer coefficient (h), the surface area density or surface to volume ratio (&rho;) and the exchanger volume (V) as U = h &rho; V. Heat exchanger performance: This model takes the overall conductance (U) as the heat exchanger performance (P).
_ONE_OF__HEAT_EXCHANGER_SOURCE_HEAT_EXCHANGER_MODE_VARIANTS: dict[str, type] = {
    "HEAT_TRANSFER_COEFFICIENTS": HeatTransferCoefficients,
    "HEAT_EXCHANGER_PERFORMANCE": HeatExchangerPerformance,
}

OneOf_HeatExchangerSourceHeatExchangerMode = Annotated[
    Union[HeatTransferCoefficients, HeatExchangerPerformance],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HEAT_EXCHANGER_SOURCE_HEAT_EXCHANGER_MODE_VARIANTS,
        )
    ),
]
