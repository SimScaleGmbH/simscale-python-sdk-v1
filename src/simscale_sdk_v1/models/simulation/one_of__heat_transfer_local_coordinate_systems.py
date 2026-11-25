from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cartesian_coordinate_system import CartesianCoordinateSystem
from simscale_sdk_v1.models.simulation.cylindrical_coordinate_system import CylindricalCoordinateSystem

_ONE_OF__HEAT_TRANSFER_LOCAL_COORDINATE_SYSTEMS_VARIANTS: dict[str, type] = {
    "CARTESIAN_COORDINATE_SYSTEM": CartesianCoordinateSystem,
    "CYLINDRICAL_COORDINATE_SYSTEM": CylindricalCoordinateSystem,
}

OneOf_HeatTransferLocalCoordinateSystems = Annotated[
    Union[CartesianCoordinateSystem, CylindricalCoordinateSystem],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HEAT_TRANSFER_LOCAL_COORDINATE_SYSTEMS_VARIANTS,
        )
    ),
]
