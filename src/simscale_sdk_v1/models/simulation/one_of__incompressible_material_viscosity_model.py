from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bird_carreau_viscosity_model import BirdCarreauViscosityModel
from simscale_sdk_v1.models.simulation.cross_power_law_viscosity_model import CrossPowerLawViscosityModel
from simscale_sdk_v1.models.simulation.herschel_bulkley_viscosity_model import HerschelBulkleyViscosityModel
from simscale_sdk_v1.models.simulation.newtonian_viscosity_model import NewtonianViscosityModel
from simscale_sdk_v1.models.simulation.power_law_viscosity_model import PowerLawViscosityModel
from simscale_sdk_v1.models.simulation.standard_herschel_bulkley_viscosity_model import (
    StandardHerschelBulkleyViscosityModel,
)

_ONE_OF__INCOMPRESSIBLE_MATERIAL_VISCOSITY_MODEL_VARIANTS: dict[str, type] = {
    "NEWTONIAN": NewtonianViscosityModel,
    "POWER_LAW": PowerLawViscosityModel,
    "STD_HERSCHEL_BULKLEY": StandardHerschelBulkleyViscosityModel,
    "HERSCHEL_BULKLEY": HerschelBulkleyViscosityModel,
    "CROSS_POWER_LAW": CrossPowerLawViscosityModel,
    "BIRD_CARREAU": BirdCarreauViscosityModel,
}

OneOf_IncompressibleMaterialViscosityModel = Annotated[
    Union[
        NewtonianViscosityModel,
        PowerLawViscosityModel,
        StandardHerschelBulkleyViscosityModel,
        HerschelBulkleyViscosityModel,
        CrossPowerLawViscosityModel,
        BirdCarreauViscosityModel,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__INCOMPRESSIBLE_MATERIAL_VISCOSITY_MODEL_VARIANTS,
        )
    ),
]
