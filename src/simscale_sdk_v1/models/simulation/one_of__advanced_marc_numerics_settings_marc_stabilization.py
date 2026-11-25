from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_marc_stabilization import AutomaticMarcStabilization
from simscale_sdk_v1.models.simulation.custom_marc_stabilization import CustomMarcStabilization

# Stabilization adds viscous forces that steady the solution, for example in buckling, snap-through, or contact that keeps opening and closing. Marc calls this artificial damping. It only acts with automatic time stepping.Automatic: Damping is added only if the time step reaches the minimum time step, to help the simulation continue.Custom: Damping acts in every increment (damping energy rate method in Marc). It replaces the automatic mode: the time step is then controlled by the damping energy instead of the number of recycles. Damping changes the result while the model is moving, so compare with a run without it.
_ONE_OF__ADVANCED_MARC_NUMERICS_SETTINGS_MARC_STABILIZATION_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticMarcStabilization,
    "CUSTOM": CustomMarcStabilization,
}

OneOf_AdvancedMarcNumericsSettingsMarcStabilization = Annotated[
    Union[AutomaticMarcStabilization, CustomMarcStabilization],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_MARC_NUMERICS_SETTINGS_MARC_STABILIZATION_VARIANTS,
        )
    ),
]
