from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_relative_permeability_method import IsotropicRelativePermeabilityMethod
from simscale_sdk_v1.models.simulation.nonlinear_isotropic_permeability import NonlinearIsotropicPermeability

_ONE_OF__ELECTROMAGNETIC_MATERIAL_MAGNETIC_PERMEABILITY_TYPE_VARIANTS: dict[str, type] = {
    "ISOTROPIC_RELATIVE_MAGNETIC_PERMEABILITY": IsotropicRelativePermeabilityMethod,
    "NONLINEAR_ISOTROPIC": NonlinearIsotropicPermeability,
}

OneOf_ElectromagneticMaterialMagneticPermeabilityType = Annotated[
    Union[IsotropicRelativePermeabilityMethod, NonlinearIsotropicPermeability],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_MATERIAL_MAGNETIC_PERMEABILITY_TYPE_VARIANTS,
        )
    ),
]
