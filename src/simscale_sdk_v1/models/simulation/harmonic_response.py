from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.mumps_solver import MUMPSSolver


class HarmonicResponse(SimScaleModel):
    solver: MUMPSSolver | None = Field(default=None)
