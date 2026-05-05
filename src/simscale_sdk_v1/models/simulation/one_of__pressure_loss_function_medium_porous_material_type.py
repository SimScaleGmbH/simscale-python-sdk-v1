from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.directional_material_structure import DirectionalMaterialStructure
from simscale_sdk_v1.models.simulation.homogeneous_material_structure import HomogeneousMaterialStructure

# Select the porous material behavior: Homogeneous: Uniform resistance to fluid flow in all directions.Directional: Resistance to fluid flow in one or two directions.
_ONE_OF__PRESSURE_LOSS_FUNCTION_MEDIUM_POROUS_MATERIAL_TYPE_VARIANTS: dict[str, type] = {
    "HOMOGENEOUS": HomogeneousMaterialStructure,
    "DIRECTIONAL": DirectionalMaterialStructure,
}

OneOf_PressureLossFunctionMediumPorousMaterialType = Annotated[
    Union[HomogeneousMaterialStructure, DirectionalMaterialStructure],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PRESSURE_LOSS_FUNCTION_MEDIUM_POROUS_MATERIAL_TYPE_VARIANTS,
        )
    ),
]
