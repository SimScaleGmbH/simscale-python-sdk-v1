"""Generated GeometryPrimitive models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.geometry_primitive.box import Box
    from simscale_sdk_v1.models.geometry_primitive.cartesian_box import CartesianBox
    from simscale_sdk_v1.models.geometry_primitive.cylinder import Cylinder
    from simscale_sdk_v1.models.geometry_primitive.decimal_vector import DecimalVector
    from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__angle import DimensionalVector_Angle
    from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length
    from simscale_sdk_v1.models.geometry_primitive.dimensional__angle import Dimensional_Angle
    from simscale_sdk_v1.models.geometry_primitive.dimensional__length import Dimensional_Length
    from simscale_sdk_v1.models.geometry_primitive.geometry_primitive import GeometryPrimitive
    from simscale_sdk_v1.models.geometry_primitive.half_space import HalfSpace
    from simscale_sdk_v1.models.geometry_primitive.local_cartesian_box import LocalCartesianBox
    from simscale_sdk_v1.models.geometry_primitive.local_half_space import LocalHalfSpace
    from simscale_sdk_v1.models.geometry_primitive.local_sphere import LocalSphere
    from simscale_sdk_v1.models.geometry_primitive.point import Point
    from simscale_sdk_v1.models.geometry_primitive.rotatable_cartesian_box import RotatableCartesianBox
    from simscale_sdk_v1.models.geometry_primitive.sphere import Sphere

_NAMES: dict[str, tuple[str, str]] = {
    "Box": ("simscale_sdk_v1.models.geometry_primitive.box", "Box"),
    "CartesianBox": ("simscale_sdk_v1.models.geometry_primitive.cartesian_box", "CartesianBox"),
    "Cylinder": ("simscale_sdk_v1.models.geometry_primitive.cylinder", "Cylinder"),
    "DecimalVector": ("simscale_sdk_v1.models.geometry_primitive.decimal_vector", "DecimalVector"),
    "DimensionalVector_Angle": (
        "simscale_sdk_v1.models.geometry_primitive.dimensional_vector__angle",
        "DimensionalVector_Angle",
    ),
    "DimensionalVector_Length": (
        "simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length",
        "DimensionalVector_Length",
    ),
    "Dimensional_Angle": ("simscale_sdk_v1.models.geometry_primitive.dimensional__angle", "Dimensional_Angle"),
    "Dimensional_Length": ("simscale_sdk_v1.models.geometry_primitive.dimensional__length", "Dimensional_Length"),
    "GeometryPrimitive": ("simscale_sdk_v1.models.geometry_primitive.geometry_primitive", "GeometryPrimitive"),
    "HalfSpace": ("simscale_sdk_v1.models.geometry_primitive.half_space", "HalfSpace"),
    "LocalCartesianBox": ("simscale_sdk_v1.models.geometry_primitive.local_cartesian_box", "LocalCartesianBox"),
    "LocalHalfSpace": ("simscale_sdk_v1.models.geometry_primitive.local_half_space", "LocalHalfSpace"),
    "LocalSphere": ("simscale_sdk_v1.models.geometry_primitive.local_sphere", "LocalSphere"),
    "Point": ("simscale_sdk_v1.models.geometry_primitive.point", "Point"),
    "RotatableCartesianBox": (
        "simscale_sdk_v1.models.geometry_primitive.rotatable_cartesian_box",
        "RotatableCartesianBox",
    ),
    "Sphere": ("simscale_sdk_v1.models.geometry_primitive.sphere", "Sphere"),
}


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys())
