from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.area_density_mass import AreaDensityMass
from simscale_sdk_v1.models.simulation.total_mass import TotalMass

# Define how the distributed mass is specified: either as a total mass that will be distributed across the selected surface, or as an area density that represents mass per unit area.
_ONE_OF__DISTRIBUTED_MASS_BC_MASS_DEFINITION_VARIANTS: dict[str, type] = {
    "TOTAL_MASS": TotalMass,
    "AREA_DENSITY_MASS": AreaDensityMass,
}

OneOf_DistributedMassBCMassDefinition = Annotated[
    Union[TotalMass, AreaDensityMass],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DISTRIBUTED_MASS_BC_MASS_DEFINITION_VARIANTS,
        )
    ),
]
