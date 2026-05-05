from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_turbulence import AutomaticTurbulence
from simscale_sdk_v1.models.simulation.fixed_value_turbulence import FixedValueTurbulence
from simscale_sdk_v1.models.simulation.turbulent_intensity_and_reference_length_turbulence import (
    TurbulentIntensityAndReferenceLengthTurbulence,
)

# These options specify inlet boundary conditions for turbulence quantities: Automatic considers a value of 0.05 for turbulent intensity (I). The turbulent mixing length (L) is calculated as 0.07Dh, where Dh is the hydraulic diameter of the boundary face.Turbulent intensity and mixing length allows to specify these values directly.Fixed value allows to specify the values of the turbulent kinetic energy (k) and the turbulent dissipation rate (&#120656) or the specific dissipation rate (&#969).
_ONE_OF__NATURAL_CONVECTION_INLET_OUTLET_BC_TURBULENCE_VARIANTS: dict[str, type] = {
    "AUTOMATIC_TURBULENCE": AutomaticTurbulence,
    "TURBULENT_INTENSITY_AND_REFERENCE_LENGTH_TURBULENCE": TurbulentIntensityAndReferenceLengthTurbulence,
    "FIXED_VALUE_TURBULENCE": FixedValueTurbulence,
}

OneOf_NaturalConvectionInletOutletBCTurbulence = Annotated[
    Union[AutomaticTurbulence, TurbulentIntensityAndReferenceLengthTurbulence, FixedValueTurbulence],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__NATURAL_CONVECTION_INLET_OUTLET_BC_TURBULENCE_VARIANTS,
        )
    ),
]
