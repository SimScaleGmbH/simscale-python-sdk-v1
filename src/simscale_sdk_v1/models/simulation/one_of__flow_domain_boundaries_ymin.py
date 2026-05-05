from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.atmospheric_boundary_layer_inlet_bc import AtmosphericBoundaryLayerInletBC
from simscale_sdk_v1.models.simulation.periodic_bc import PeriodicBC
from simscale_sdk_v1.models.simulation.pressure_outlet_bc import PressureOutletBC
from simscale_sdk_v1.models.simulation.velocity_inlet_bc import VelocityInletBC
from simscale_sdk_v1.models.simulation.wall_bc import WallBC

# This shows the face of the external flow domain to which this boundary condition is assigned. The name of the face reflects its alignment with respect to the orientation cube seen in the viewer.
_ONE_OF__FLOW_DOMAIN_BOUNDARIES_YMIN_VARIANTS: dict[str, type] = {
    "VELOCITY_INLET_V3": VelocityInletBC,
    "PRESSURE_OUTLET_V30": PressureOutletBC,
    "WALL_V34": WallBC,
    "PERIODIC": PeriodicBC,
    "ATMOSPHERIC_BOUNDARY_LAYER_INLET": AtmosphericBoundaryLayerInletBC,
}

OneOf_FlowDomainBoundariesYMIN = Annotated[
    Union[VelocityInletBC, PressureOutletBC, WallBC, PeriodicBC, AtmosphericBoundaryLayerInletBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLOW_DOMAIN_BOUNDARIES_YMIN_VARIANTS,
        )
    ),
]
