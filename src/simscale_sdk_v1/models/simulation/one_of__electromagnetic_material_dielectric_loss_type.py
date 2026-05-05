from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_loss_tangent import IsotropicLossTangent
from simscale_sdk_v1.models.simulation.no_dielectric_losses import NoDielectricLosses

# Specify the dielectric loss type. It models dielectric heating losses in insulating materials under time-varying electric fields. For details, see our documentation.
_ONE_OF__ELECTROMAGNETIC_MATERIAL_DIELECTRIC_LOSS_TYPE_VARIANTS: dict[str, type] = {
    "NONE": NoDielectricLosses,
    "ISOTROPIC_LOSS_TANGENT": IsotropicLossTangent,
}

OneOf_ElectromagneticMaterialDielectricLossType = Annotated[
    Union[NoDielectricLosses, IsotropicLossTangent],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_MATERIAL_DIELECTRIC_LOSS_TYPE_VARIANTS,
        )
    ),
]
