from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.first_layer_growth import FirstLayerGrowth
from simscale_sdk_v1.models.meshing.fractional_height1 import FractionalHeight1
from simscale_sdk_v1.models.meshing.fractional_height2 import FractionalHeight2
from simscale_sdk_v1.models.meshing.geometric_growth import GeometricGrowth

# Define how the layers should be distributed within the overall layer thickness:Specify growth rate: Define the growth rate between adjacent layers.  Specify first layer thickness: Define the absolute thickness of the first layer. The remaining layers are distributed automatically. Choose this option for example to strictly control the y+ value.  Specify first layer and total absolute thickness: Define the absolute value of the first layer and the total layer thickness. The growth rate is computed automatically using a geometric progression.
_ONE_OF__SIMMETRIX_BOUNDARY_LAYER_REFINEMENT_LAYER_TYPE_VARIANTS: dict[str, type] = {
    "FRACTIONAL_HEIGHT_1": FractionalHeight1,
    "FRACTIONAL_HEIGHT_2": FractionalHeight2,
    "GEOMETRIC_GROWTH": GeometricGrowth,
    "FIRST_LAYER_GROWTH": FirstLayerGrowth,
}

OneOf_SimmetrixBoundaryLayerRefinementLayerType = Annotated[
    Union[FractionalHeight1, FractionalHeight2, GeometricGrowth, FirstLayerGrowth],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMMETRIX_BOUNDARY_LAYER_REFINEMENT_LAYER_TYPE_VARIANTS,
        )
    ),
]
