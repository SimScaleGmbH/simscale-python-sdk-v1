from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.comets_visualization_style import CometsVisualizationStyle
from simscale_sdk_v1.models.reporting.cylinders_visualization_style import CylindersVisualizationStyle
from simscale_sdk_v1.models.reporting.spheres_visualization_style import SpheresVisualizationStyle

_ONE_OF_VISUALIZATION_STYLE_VARIANTS: dict[str, type] = {
    "CYLINDERS": CylindersVisualizationStyle,
    "SPHERES": SpheresVisualizationStyle,
    "COMETS": CometsVisualizationStyle,
}

OneOfVisualizationStyle = Annotated[
    Union[CylindersVisualizationStyle, SpheresVisualizationStyle, CometsVisualizationStyle],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="representation",
            variants=_ONE_OF_VISUALIZATION_STYLE_VARIANTS,
        )
    ),
]
