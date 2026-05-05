from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.electrical_steel_core_loss import ElectricalSteelCoreLoss
from simscale_sdk_v1.models.simulation.no_core_loss import NoCoreLoss
from simscale_sdk_v1.models.simulation.power_ferrite_core_loss import PowerFerriteCoreLoss

# Core losses calculate the losses in magnetic materials, including hysteresis and eddy current losses. Note: Once a core loss model is enabled, eddy currents are suppressed within that body.  For more information on each model, please refer to our documentation.
_ONE_OF__ELECTROMAGNETIC_MATERIAL_CORE_LOSSES_TYPE_VARIANTS: dict[str, type] = {
    "NONE": NoCoreLoss,
    "ELECTRICAL_STEEL": ElectricalSteelCoreLoss,
    "POWER_FERRITE": PowerFerriteCoreLoss,
}

OneOf_ElectromagneticMaterialCoreLossesType = Annotated[
    Union[NoCoreLoss, ElectricalSteelCoreLoss, PowerFerriteCoreLoss],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_MATERIAL_CORE_LOSSES_TYPE_VARIANTS,
        )
    ),
]
