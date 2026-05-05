from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_xmax import OneOf_FlowDomainBoundariesXMAX
from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_xmin import OneOf_FlowDomainBoundariesXMIN
from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_ymax import OneOf_FlowDomainBoundariesYMAX
from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_ymin import OneOf_FlowDomainBoundariesYMIN
from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_zmax import OneOf_FlowDomainBoundariesZMAX
from simscale_sdk_v1.models.simulation.one_of__flow_domain_boundaries_zmin import OneOf_FlowDomainBoundariesZMIN


class FlowDomainBoundaries(SimScaleModel):
    xmin: OneOf_FlowDomainBoundariesXMIN | None = Field(
        validation_alias="XMIN", serialization_alias="XMIN", default=None
    )
    xmax: OneOf_FlowDomainBoundariesXMAX | None = Field(
        validation_alias="XMAX", serialization_alias="XMAX", default=None
    )
    ymin: OneOf_FlowDomainBoundariesYMIN | None = Field(
        validation_alias="YMIN", serialization_alias="YMIN", default=None
    )
    ymax: OneOf_FlowDomainBoundariesYMAX | None = Field(
        validation_alias="YMAX", serialization_alias="YMAX", default=None
    )
    zmin: OneOf_FlowDomainBoundariesZMIN | None = Field(
        validation_alias="ZMIN", serialization_alias="ZMIN", default=None
    )
    zmax: OneOf_FlowDomainBoundariesZMAX | None = Field(
        validation_alias="ZMAX", serialization_alias="ZMAX", default=None
    )
