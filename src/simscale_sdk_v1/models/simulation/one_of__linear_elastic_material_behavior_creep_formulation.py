from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.no_creep_formulation import NoCreepFormulation
from simscale_sdk_v1.models.simulation.norton_creep_formulation import NortonCreepFormulation
from simscale_sdk_v1.models.simulation.strain_hardening_creep_formulation import StrainHardeningCreepFormulation
from simscale_sdk_v1.models.simulation.time_hardening_creep_formulation import TimeHardeningCreepFormulation

# Define the Creep formulation. Three different formulations are available: Norton, Strain Hardening or Time Hardening.They are based on the Power Law:&epsilon;&#775 = m*A*&sigma;n*tm-1
_ONE_OF__LINEAR_ELASTIC_MATERIAL_BEHAVIOR_CREEP_FORMULATION_VARIANTS: dict[str, type] = {
    "NORTON": NortonCreepFormulation,
    "NO_CREEP": NoCreepFormulation,
    "STRAIN_HARDENING": StrainHardeningCreepFormulation,
    "TIME_HARDENING": TimeHardeningCreepFormulation,
}

OneOf_LinearElasticMaterialBehaviorCreepFormulation = Annotated[
    Union[NortonCreepFormulation, NoCreepFormulation, StrainHardeningCreepFormulation, TimeHardeningCreepFormulation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__LINEAR_ELASTIC_MATERIAL_BEHAVIOR_CREEP_FORMULATION_VARIANTS,
        )
    ),
]
