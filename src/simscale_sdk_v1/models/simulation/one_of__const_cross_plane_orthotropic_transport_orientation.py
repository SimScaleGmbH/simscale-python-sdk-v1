from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cross_plane_custom_orientation import CrossPlaneCustomOrientation
from simscale_sdk_v1.models.simulation.x_axis import XAxis
from simscale_sdk_v1.models.simulation.y_axis import YAxis
from simscale_sdk_v1.models.simulation.z_axis import ZAxis

# Defines the direction on which the thermal conductivity will act: x-, y-, z-Axis: the cross-plane conductivity acts along the selected coordinate axis and the in-plane conductivity acts on the plane orthogonal to that axis.Custom: the cross-plane conductivity is aligned with the cross-plane orientation defined by the X, Y, Z components, and the in-plane conductivity acts on the plane orthogonal to the cross-plane orientation.
_ONE_OF__CONST_CROSS_PLANE_ORTHOTROPIC_TRANSPORT_ORIENTATION_VARIANTS: dict[str, type] = {
    "XAXIS": XAxis,
    "YAXIS": YAxis,
    "ZAXIS": ZAxis,
    "CROSS_PLANE": CrossPlaneCustomOrientation,
}

OneOf_ConstCrossPlaneOrthotropicTransportOrientation = Annotated[
    Union[XAxis, YAxis, ZAxis, CrossPlaneCustomOrientation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONST_CROSS_PLANE_ORTHOTROPIC_TRANSPORT_ORIENTATION_VARIANTS,
        )
    ),
]
