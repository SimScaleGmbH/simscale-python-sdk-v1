from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.advective_vbc import AdvectiveVBC
from simscale_sdk_v1.models.simulation.fixed_gradient_vbc import FixedGradientVBC
from simscale_sdk_v1.models.simulation.fixed_value_vbc import FixedValueVBC
from simscale_sdk_v1.models.simulation.flow_rate_inlet_vbc import FlowRateInletVBC
from simscale_sdk_v1.models.simulation.flow_rate_mean_inlet_vbc import FlowRateMeanInletVBC
from simscale_sdk_v1.models.simulation.freestream_vbc import FreestreamVBC
from simscale_sdk_v1.models.simulation.inlet_outlet_vbc import InletOutletVBC
from simscale_sdk_v1.models.simulation.mean_value_vbc import MeanValueVBC
from simscale_sdk_v1.models.simulation.moving_wall_vbc import MovingWallVBC
from simscale_sdk_v1.models.simulation.no_slip_vbc import NoSlipVBC
from simscale_sdk_v1.models.simulation.outlet_mean_phase_vbc import OutletMeanPhaseVBC
from simscale_sdk_v1.models.simulation.pressure_inlet_outlet_vbc import PressureInletOutletVBC
from simscale_sdk_v1.models.simulation.pressure_inlet_vbc import PressureInletVBC
from simscale_sdk_v1.models.simulation.rotating_wall_vbc import RotatingWallVBC
from simscale_sdk_v1.models.simulation.slip_vbc import SlipVBC
from simscale_sdk_v1.models.simulation.symmetry_vbc import SymmetryVBC
from simscale_sdk_v1.models.simulation.zero_gradient_vbc import ZeroGradientVBC

_ONE_OF__CUSTOM_FLUID_BC_VELOCITY_VARIANTS: dict[str, type] = {
    "ADVECTIVE": AdvectiveVBC,
    "SYMMETRY": SymmetryVBC,
    "FIXED_GRADIENT": FixedGradientVBC,
    "FIXED_VALUE": FixedValueVBC,
    "FIXED_MEAN": MeanValueVBC,
    "FLOW_RATE_INLET_VELOCITY": FlowRateInletVBC,
    "FLOW_RATE_MEAN_INLET_VELOCITY": FlowRateMeanInletVBC,
    "FREESTREAM": FreestreamVBC,
    "INLET_OUTLET": InletOutletVBC,
    "MOVING_WALL_VELOCITY": MovingWallVBC,
    "NO_SLIP": NoSlipVBC,
    "OUTLET_MEAN_PHASE": OutletMeanPhaseVBC,
    "PRESSURE_INLET_VELOCITY": PressureInletVBC,
    "PRESSURE_INLET_OUTLET_VELOCITY": PressureInletOutletVBC,
    "ROTATING_WALL_VELOCITY": RotatingWallVBC,
    "ZERO_GRADIENT": ZeroGradientVBC,
    "SLIP": SlipVBC,
}

OneOf_CustomFluidBCVelocity = Annotated[
    Union[
        AdvectiveVBC,
        SymmetryVBC,
        FixedGradientVBC,
        FixedValueVBC,
        MeanValueVBC,
        FlowRateInletVBC,
        FlowRateMeanInletVBC,
        FreestreamVBC,
        InletOutletVBC,
        MovingWallVBC,
        NoSlipVBC,
        OutletMeanPhaseVBC,
        PressureInletVBC,
        PressureInletOutletVBC,
        RotatingWallVBC,
        ZeroGradientVBC,
        SlipVBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_VELOCITY_VARIANTS,
        )
    ),
]
