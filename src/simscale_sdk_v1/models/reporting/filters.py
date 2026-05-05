from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.cutting_plane import CuttingPlane
from simscale_sdk_v1.models.reporting.displacement import Displacement
from simscale_sdk_v1.models.reporting.iso_surface import IsoSurface
from simscale_sdk_v1.models.reporting.iso_volume import IsoVolume
from simscale_sdk_v1.models.reporting.particle_trace import ParticleTrace


class Filters(SimScaleModel):
    cutting_planes: list[CuttingPlane] | None = Field(
        validation_alias="cuttingPlanes", serialization_alias="cuttingPlanes", default=None
    )
    iso_surfaces: list[IsoSurface] | None = Field(
        validation_alias="isoSurfaces", serialization_alias="isoSurfaces", default=None
    )
    iso_volumes: list[IsoVolume] | None = Field(
        validation_alias="isoVolumes", serialization_alias="isoVolumes", default=None
    )
    displacement: Displacement | None = Field(default=None)
    particle_traces: list[ParticleTrace] | None = Field(
        validation_alias="particleTraces", serialization_alias="particleTraces", default=None
    )
