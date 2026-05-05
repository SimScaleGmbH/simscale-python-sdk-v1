from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cartesian_orientation import CartesianOrientation
from simscale_sdk_v1.models.simulation.custom_orientation import CustomOrientation

# Defines the direction on which the thermal conductivity will act: Cartesian: the conductivities &kappa;x, &kappa;y, and &kappa;z are aligned with the X, Y, and Z-axis, respectively.Custom: the conductivities &kappa;x and &kappa;y are aligned with the unit vectors x and y, respectively, and the conductivity &kappa;z is aligned with the resultant of the cross product of unit vectors x and y.
_ONE_OF__CONST_AN_ISO_TRANSPORT_ORIENTATION_VARIANTS: dict[str, type] = {
    "CARTESIAN": CartesianOrientation,
    "CUSTOM": CustomOrientation,
}

OneOf_ConstAnIsoTransportOrientation = Annotated[
    Union[CartesianOrientation, CustomOrientation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONST_AN_ISO_TRANSPORT_ORIENTATION_VARIANTS,
        )
    ),
]
