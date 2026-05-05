from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bolt_preload_bc import BoltPreloadBC
from simscale_sdk_v1.models.simulation.centrifugal_force_bc import CentrifugalForceBC
from simscale_sdk_v1.models.simulation.cyclic_symmetry_bc import CyclicSymmetryBC
from simscale_sdk_v1.models.simulation.distributed_mass_bc import DistributedMassBC
from simscale_sdk_v1.models.simulation.elastic_support_bc import ElasticSupportBC
from simscale_sdk_v1.models.simulation.fixed_support_bc import FixedSupportBC
from simscale_sdk_v1.models.simulation.fixed_value_bc import FixedValueBC
from simscale_sdk_v1.models.simulation.follower_pressure_bc import FollowerPressureBC
from simscale_sdk_v1.models.simulation.force_load_bc import ForceLoadBC
from simscale_sdk_v1.models.simulation.hinge_constraint_bc import HingeConstraintBC
from simscale_sdk_v1.models.simulation.nodal_load_bc import NodalLoadBC
from simscale_sdk_v1.models.simulation.point_mass_bc import PointMassBC
from simscale_sdk_v1.models.simulation.pressure_bc import PressureBC
from simscale_sdk_v1.models.simulation.remote_displacement_load_bc import RemoteDisplacementLoadBC
from simscale_sdk_v1.models.simulation.remote_force_load_bc import RemoteForceLoadBC
from simscale_sdk_v1.models.simulation.rotating_motion_bc import RotatingMotionBC
from simscale_sdk_v1.models.simulation.surface_load_bc import SurfaceLoadBC
from simscale_sdk_v1.models.simulation.symmetry_plane_bc import SymmetryPlaneBC
from simscale_sdk_v1.models.simulation.volume_load_bc import VolumeLoadBC

_ONE_OF__STATIC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS: dict[str, type] = {
    "BOLT_PRELOAD": BoltPreloadBC,
    "ELASTIC_SUPPORT": ElasticSupportBC,
    "FIXED_SUPPORT": FixedSupportBC,
    "FIXED_VALUE": FixedValueBC,
    "POINT_MASS": PointMassBC,
    "DISTRIBUTED_MASS": DistributedMassBC,
    "REMOTE_DISPLACEMENT_LOAD": RemoteDisplacementLoadBC,
    "ROTATING_MOTION": RotatingMotionBC,
    "SYMMETRY_PLANE": SymmetryPlaneBC,
    "CYCLIC_SYMMETRY": CyclicSymmetryBC,
    "CENTRIFUGAL_FORCE": CentrifugalForceBC,
    "FOLLOWER_PRESSURE": FollowerPressureBC,
    "FORCE_LOAD": ForceLoadBC,
    "NODAL_LOAD": NodalLoadBC,
    "PRESSURE": PressureBC,
    "REMOTE_FORCE_LOAD": RemoteForceLoadBC,
    "SURFACE_LOAD": SurfaceLoadBC,
    "VOLUME_LOAD": VolumeLoadBC,
    "HINGE_CONSTRAINT": HingeConstraintBC,
}

OneOf_StaticAnalysisBoundaryConditions = Annotated[
    Union[
        BoltPreloadBC,
        ElasticSupportBC,
        FixedSupportBC,
        FixedValueBC,
        PointMassBC,
        DistributedMassBC,
        RemoteDisplacementLoadBC,
        RotatingMotionBC,
        SymmetryPlaneBC,
        CyclicSymmetryBC,
        CentrifugalForceBC,
        FollowerPressureBC,
        ForceLoadBC,
        NodalLoadBC,
        PressureBC,
        RemoteForceLoadBC,
        SurfaceLoadBC,
        VolumeLoadBC,
        HingeConstraintBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__STATIC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS,
        )
    ),
]
