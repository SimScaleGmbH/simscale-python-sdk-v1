from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.chestnut import Chestnut
from simscale_sdk_v1.models.simulation.custom_tree import CustomTree
from simscale_sdk_v1.models.simulation.oak import Oak
from simscale_sdk_v1.models.simulation.plane_tree import PlaneTree
from simscale_sdk_v1.models.simulation.silver_birch import SilverBirch
from simscale_sdk_v1.models.simulation.sycamore import Sycamore

_ONE_OF__POROUS_TREE_TREE_TYPE_VARIANTS: dict[str, type] = {
    "CUSTOM_TREE": CustomTree,
    "PLANE_TREE": PlaneTree,
    "OAK": Oak,
    "SYCAMORE": Sycamore,
    "SILVER_BIRCH": SilverBirch,
    "CHESTNUT": Chestnut,
}

OneOf_PorousTreeTreeType = Annotated[
    Union[CustomTree, PlaneTree, Oak, Sycamore, SilverBirch, Chestnut],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__POROUS_TREE_TREE_TYPE_VARIANTS,
        )
    ),
]
