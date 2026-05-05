from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation_spec import SimulationSpec
from simscale_sdk_v1.models.tables import Tables


class MaterialUpdateResponse(SimScaleModel):
    """Material update response schema"""

    spec: SimulationSpec
    tables: Tables
