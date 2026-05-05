from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.geometry_primitive.box import Box
from simscale_sdk_v1.models.geometry_primitive.cartesian_box import CartesianBox
from simscale_sdk_v1.models.geometry_primitive.cylinder import Cylinder
from simscale_sdk_v1.models.geometry_primitive.half_space import HalfSpace
from simscale_sdk_v1.models.geometry_primitive.local_cartesian_box import LocalCartesianBox
from simscale_sdk_v1.models.geometry_primitive.local_half_space import LocalHalfSpace
from simscale_sdk_v1.models.geometry_primitive.local_sphere import LocalSphere
from simscale_sdk_v1.models.geometry_primitive.point import Point
from simscale_sdk_v1.models.geometry_primitive.rotatable_cartesian_box import RotatableCartesianBox
from simscale_sdk_v1.models.geometry_primitive.sphere import Sphere

_GEOMETRY_PRIMITIVE_VARIANTS: dict[str, type] = {
    "CARTESIAN_BOX": CartesianBox,
    "ROTATABLE_CARTESIAN_BOX": RotatableCartesianBox,
    "LOCAL_CARTESIAN_BOX": LocalCartesianBox,
    "SPHERE": Sphere,
    "LOCAL_SPHERE": LocalSphere,
    "CYLINDER": Cylinder,
    "POINT": Point,
    "BOX": Box,
    "HALF_SPACE": HalfSpace,
    "LOCAL_HALF_SPACE": LocalHalfSpace,
}

GeometryPrimitive = Annotated[
    Union[
        CartesianBox,
        RotatableCartesianBox,
        LocalCartesianBox,
        Sphere,
        LocalSphere,
        Cylinder,
        Point,
        Box,
        HalfSpace,
        LocalHalfSpace,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_GEOMETRY_PRIMITIVE_VARIANTS,
        )
    ),
]
