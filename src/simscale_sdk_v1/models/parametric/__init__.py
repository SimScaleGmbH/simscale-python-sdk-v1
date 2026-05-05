"""Generated Parametric models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.parametric.any_of__parameter_with_values_values import AnyOf_ParameterWithValuesValues
    from simscale_sdk_v1.models.parametric.numerical_sequence_parameter_value_generator import (
        NumericalSequenceParameterValueGenerator,
    )
    from simscale_sdk_v1.models.parametric.one_of__parameters import OneOf_Parameters
    from simscale_sdk_v1.models.parametric.parameter_with_value_generator import ParameterWithValueGenerator
    from simscale_sdk_v1.models.parametric.parameter_with_values import ParameterWithValues
    from simscale_sdk_v1.models.parametric.parameters import Parameters

_NAMES: dict[str, tuple[str, str]] = {
    "AnyOf_ParameterWithValuesValues": (
        "simscale_sdk_v1.models.parametric.any_of__parameter_with_values_values",
        "AnyOf_ParameterWithValuesValues",
    ),
    "NumericalSequenceParameterValueGenerator": (
        "simscale_sdk_v1.models.parametric.numerical_sequence_parameter_value_generator",
        "NumericalSequenceParameterValueGenerator",
    ),
    "OneOf_Parameters": ("simscale_sdk_v1.models.parametric.one_of__parameters", "OneOf_Parameters"),
    "ParameterWithValueGenerator": (
        "simscale_sdk_v1.models.parametric.parameter_with_value_generator",
        "ParameterWithValueGenerator",
    ),
    "ParameterWithValues": ("simscale_sdk_v1.models.parametric.parameter_with_values", "ParameterWithValues"),
    "Parameters": ("simscale_sdk_v1.models.parametric.parameters", "Parameters"),
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
