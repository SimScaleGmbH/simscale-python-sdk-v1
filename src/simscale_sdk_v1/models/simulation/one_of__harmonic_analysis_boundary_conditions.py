from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.base_excitation_bc import BaseExcitationBC
from simscale_sdk_v1.models.simulation.bolt_preload_bc import BoltPreloadBC
from simscale_sdk_v1.models.simulation.centrifugal_force_bc import CentrifugalForceBC
from simscale_sdk_v1.models.simulation.distributed_mass_bc import DistributedMassBC
from simscale_sdk_v1.models.simulation.elastic_support_bc import ElasticSupportBC
from simscale_sdk_v1.models.simulation.fixed_support_bc import FixedSupportBC
from simscale_sdk_v1.models.simulation.fixed_value_bc import FixedValueBC
from simscale_sdk_v1.models.simulation.force_load_bc import ForceLoadBC
from simscale_sdk_v1.models.simulation.nodal_load_bc import NodalLoadBC
from simscale_sdk_v1.models.simulation.point_mass_bc import PointMassBC
from simscale_sdk_v1.models.simulation.pressure_bc import PressureBC
from simscale_sdk_v1.models.simulation.remote_displacement_load_bc import RemoteDisplacementLoadBC
from simscale_sdk_v1.models.simulation.remote_force_load_bc import RemoteForceLoadBC
from simscale_sdk_v1.models.simulation.surface_load_bc import SurfaceLoadBC
from simscale_sdk_v1.models.simulation.symmetry_plane_bc import SymmetryPlaneBC
from simscale_sdk_v1.models.simulation.volume_load_bc import VolumeLoadBC

_ONE_OF__HARMONIC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS: dict[str, type] = {
    "BASE_EXCITATION": BaseExcitationBC,
    "BOLT_PRELOAD": BoltPreloadBC,
    "ELASTIC_SUPPORT": ElasticSupportBC,
    "FIXED_SUPPORT": FixedSupportBC,
    "FIXED_VALUE": FixedValueBC,
    "POINT_MASS": PointMassBC,
    "DISTRIBUTED_MASS": DistributedMassBC,
    "REMOTE_DISPLACEMENT_LOAD": RemoteDisplacementLoadBC,
    "SYMMETRY_PLANE": SymmetryPlaneBC,
    "CENTRIFUGAL_FORCE": CentrifugalForceBC,
    "FORCE_LOAD": ForceLoadBC,
    "NODAL_LOAD": NodalLoadBC,
    "PRESSURE": PressureBC,
    "REMOTE_FORCE_LOAD": RemoteForceLoadBC,
    "SURFACE_LOAD": SurfaceLoadBC,
    "VOLUME_LOAD": VolumeLoadBC,
}

OneOf_HarmonicAnalysisBoundaryConditions = Annotated[
    Union[
        BaseExcitationBC,
        BoltPreloadBC,
        ElasticSupportBC,
        FixedSupportBC,
        FixedValueBC,
        PointMassBC,
        DistributedMassBC,
        RemoteDisplacementLoadBC,
        SymmetryPlaneBC,
        CentrifugalForceBC,
        ForceLoadBC,
        NodalLoadBC,
        PressureBC,
        RemoteForceLoadBC,
        SurfaceLoadBC,
        VolumeLoadBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HARMONIC_ANALYSIS_BOUNDARY_CONDITIONS_VARIANTS,
        )
    ),
]
