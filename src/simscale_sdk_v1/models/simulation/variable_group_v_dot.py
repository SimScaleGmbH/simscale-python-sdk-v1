from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__volumetric_flow_rate import Unit_VolumetricFlowRate


class VariableGroup_V_DOT(SimScaleModel):
    v_dot: Unit_VolumetricFlowRate | None = Field(validation_alias="V_DOT", serialization_alias="V_DOT", default=None)
