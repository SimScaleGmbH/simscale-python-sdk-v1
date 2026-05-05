from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.h_const_thermo import HConstThermo
from simscale_sdk_v1.models.simulation.one_of__const_an_iso_transport_orientation import (
    OneOf_ConstAnIsoTransportOrientation,
)
from simscale_sdk_v1.models.simulation.orthotropic_conductivity import OrthotropicConductivity


class ConstAnIsoTransport(SimScaleModel):
    """The thermal conductivity of a material is a measure of its ability to conduct heat.Isotropic: the thermal conductivity &kappa; is the same in all directions.Orthotropic: the thermal conductivity is unique and independent in three orthogonal directions. It is defined by &kappa;x, &kappa;y, and &kappa;z.Cross-plane orthotropic: it is defined by an in-plane conductivity, which is an isotropic conductivity on a given plane, and a cross-plane&nbsp;conductivity, which acts in the direction normal to the aforementioned plane."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONST_AN_ISO",
        description="The thermal conductivity of a material is a measure of its ability to conduct heat.Isotropic: the thermal conductivity &kappa; is the same in all directions.Orthotropic: the thermal conductivity is unique and independent in three orthogonal directions. It is defined by &kappa;x, &kappa;y, and &kappa;z.Cross-plane orthotropic: it is defined by an in-plane conductivity, which is an isotropic conductivity on a given plane, and a cross-plane&nbsp;conductivity, which acts in the direction normal to the aforementioned plane.  Schema name: ConstAnIsoTransport",
    )
    conductivity: OrthotropicConductivity | None = Field(default=None)
    orientation: OneOf_ConstAnIsoTransportOrientation | None = Field(default=None)
    thermo: HConstThermo | None = Field(default=None)
