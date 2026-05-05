"""Generated Material models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.material.create_material_group_request import CreateMaterialGroupRequest
    from simscale_sdk_v1.models.material.create_material_request import CreateMaterialRequest
    from simscale_sdk_v1.models.material.create_nested_material_group_request import CreateNestedMaterialGroupRequest
    from simscale_sdk_v1.models.material.fixed_material_property import FixedMaterialProperty
    from simscale_sdk_v1.models.material.material_group_response import MaterialGroupResponse
    from simscale_sdk_v1.models.material.material_group_type import MaterialGroupType
    from simscale_sdk_v1.models.material.material_properties import MaterialProperties
    from simscale_sdk_v1.models.material.material_property_parameter import MaterialPropertyParameter
    from simscale_sdk_v1.models.material.material_response import MaterialResponse
    from simscale_sdk_v1.models.material.one_of_material_property import OneOfMaterialProperty
    from simscale_sdk_v1.models.material.parametric_material_property import ParametricMaterialProperty
    from simscale_sdk_v1.models.material.permission_dto import PermissionDto
    from simscale_sdk_v1.models.material.property_data_type import PropertyDataType
    from simscale_sdk_v1.models.material.update_material_group_request import UpdateMaterialGroupRequest

_NAMES: dict[str, tuple[str, str]] = {
    "CreateMaterialGroupRequest": (
        "simscale_sdk_v1.models.material.create_material_group_request",
        "CreateMaterialGroupRequest",
    ),
    "CreateMaterialRequest": ("simscale_sdk_v1.models.material.create_material_request", "CreateMaterialRequest"),
    "CreateNestedMaterialGroupRequest": (
        "simscale_sdk_v1.models.material.create_nested_material_group_request",
        "CreateNestedMaterialGroupRequest",
    ),
    "FixedMaterialProperty": ("simscale_sdk_v1.models.material.fixed_material_property", "FixedMaterialProperty"),
    "MaterialGroupResponse": ("simscale_sdk_v1.models.material.material_group_response", "MaterialGroupResponse"),
    "MaterialGroupType": ("simscale_sdk_v1.models.material.material_group_type", "MaterialGroupType"),
    "MaterialProperties": ("simscale_sdk_v1.models.material.material_properties", "MaterialProperties"),
    "MaterialPropertyParameter": (
        "simscale_sdk_v1.models.material.material_property_parameter",
        "MaterialPropertyParameter",
    ),
    "MaterialResponse": ("simscale_sdk_v1.models.material.material_response", "MaterialResponse"),
    "OneOfMaterialProperty": ("simscale_sdk_v1.models.material.one_of_material_property", "OneOfMaterialProperty"),
    "ParametricMaterialProperty": (
        "simscale_sdk_v1.models.material.parametric_material_property",
        "ParametricMaterialProperty",
    ),
    "PermissionDto": ("simscale_sdk_v1.models.material.permission_dto", "PermissionDto"),
    "PropertyDataType": ("simscale_sdk_v1.models.material.property_data_type", "PropertyDataType"),
    "UpdateMaterialGroupRequest": (
        "simscale_sdk_v1.models.material.update_material_group_request",
        "UpdateMaterialGroupRequest",
    ),
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
