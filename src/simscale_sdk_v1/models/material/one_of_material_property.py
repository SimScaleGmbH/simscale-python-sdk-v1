from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.material.fixed_material_property import FixedMaterialProperty
from simscale_sdk_v1.models.material.parametric_material_property import ParametricMaterialProperty

_ONE_OF_MATERIAL_PROPERTY_VARIANTS: dict[str, type] = {
    "fixed": FixedMaterialProperty,
    "parametric": ParametricMaterialProperty,
}

OneOfMaterialProperty = Annotated[
    Union[FixedMaterialProperty, ParametricMaterialProperty],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="valueType",
            variants=_ONE_OF_MATERIAL_PROPERTY_VARIANTS,
        )
    ),
]
