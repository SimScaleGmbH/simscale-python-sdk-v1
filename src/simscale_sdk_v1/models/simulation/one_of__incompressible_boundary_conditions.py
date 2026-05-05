from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.custom_fluid_bc import CustomFluidBC
from simscale_sdk_v1.models.simulation.empty2_dbc import Empty2DBC
from simscale_sdk_v1.models.simulation.fan_bc import FanBC
from simscale_sdk_v1.models.simulation.periodic_bc import PeriodicBC
from simscale_sdk_v1.models.simulation.pressure_inlet_bc import PressureInletBC
from simscale_sdk_v1.models.simulation.pressure_outlet_bc import PressureOutletBC
from simscale_sdk_v1.models.simulation.symmetry_bc import SymmetryBC
from simscale_sdk_v1.models.simulation.velocity_inlet_bc import VelocityInletBC
from simscale_sdk_v1.models.simulation.velocity_outlet_bc import VelocityOutletBC
from simscale_sdk_v1.models.simulation.wall_bc import WallBC
from simscale_sdk_v1.models.simulation.wedge_bc import WedgeBC

_ONE_OF__INCOMPRESSIBLE_BOUNDARY_CONDITIONS_VARIANTS: dict[str, type] = {
    "VELOCITY_INLET_V3": VelocityInletBC,
    "VELOCITY_OUTLET_V7": VelocityOutletBC,
    "PRESSURE_INLET_V31": PressureInletBC,
    "PRESSURE_OUTLET_V30": PressureOutletBC,
    "WALL_V34": WallBC,
    "FAN": FanBC,
    "SYMMETRY": SymmetryBC,
    "PERIODIC": PeriodicBC,
    "WEDGE": WedgeBC,
    "CUSTOM_V37": CustomFluidBC,
    "EMPTY_2D": Empty2DBC,
}

OneOf_IncompressibleBoundaryConditions = Annotated[
    Union[
        VelocityInletBC,
        VelocityOutletBC,
        PressureInletBC,
        PressureOutletBC,
        WallBC,
        FanBC,
        SymmetryBC,
        PeriodicBC,
        WedgeBC,
        CustomFluidBC,
        Empty2DBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__INCOMPRESSIBLE_BOUNDARY_CONDITIONS_VARIANTS,
        )
    ),
]
