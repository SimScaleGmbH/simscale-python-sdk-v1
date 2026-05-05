from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.pressure_inlet_bc import PressureInletBC
from simscale_sdk_v1.models.simulation.pressure_outlet_bc import PressureOutletBC
from simscale_sdk_v1.models.simulation.symmetry_bc import SymmetryBC
from simscale_sdk_v1.models.simulation.velocity_inlet_bc import VelocityInletBC
from simscale_sdk_v1.models.simulation.velocity_outlet_bc import VelocityOutletBC
from simscale_sdk_v1.models.simulation.wall_bc import WallBC

_ONE_OF__SIMERICS_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS: dict[str, type] = {
    "VELOCITY_INLET_V3": VelocityInletBC,
    "VELOCITY_OUTLET_V7": VelocityOutletBC,
    "PRESSURE_INLET_V31": PressureInletBC,
    "PRESSURE_OUTLET_V30": PressureOutletBC,
    "WALL_V34": WallBC,
    "SYMMETRY": SymmetryBC,
}

OneOf_SimericsAnalysisBoundaryConditions = Annotated[
    Union[VelocityInletBC, VelocityOutletBC, PressureInletBC, PressureOutletBC, WallBC, SymmetryBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SIMERICS_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS,
        )
    ),
]
