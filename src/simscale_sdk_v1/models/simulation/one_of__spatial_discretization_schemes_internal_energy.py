from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.central_difference_spatial_scheme import CentralDifferenceSpatialScheme
from simscale_sdk_v1.models.simulation.first_order_upwind_spatial_scheme import FirstOrderUpwindSpatialScheme
from simscale_sdk_v1.models.simulation.second_order_upwind_spatial_scheme import SecondOrderUpwindSpatialScheme

_ONE_OF__SPATIAL_DISCRETIZATION_SCHEMES_INTERNAL_ENERGY_VARIANTS: dict[str, type] = {
    "UPWIND_1ST": FirstOrderUpwindSpatialScheme,
    "UPWIND_2ND": SecondOrderUpwindSpatialScheme,
    "CENTRAL_DIFFERENCE": CentralDifferenceSpatialScheme,
}

OneOf_SpatialDiscretizationSchemesInternalEnergy = Annotated[
    Union[FirstOrderUpwindSpatialScheme, SecondOrderUpwindSpatialScheme, CentralDifferenceSpatialScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SPATIAL_DISCRETIZATION_SCHEMES_INTERNAL_ENERGY_VARIANTS,
        )
    ),
]
