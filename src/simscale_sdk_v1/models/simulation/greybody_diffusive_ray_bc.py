from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class GreybodyDiffusiveRayBC(SimScaleModel):
    """Radiative behaviour of the wall. The Kirchhoff's law of thermal radiation is applied in all options. This means that the absorptivity of the surface is equal to its emissivity.  Opaque is applied to surfaces with transmissivity equal to 0. The radiation that hits the surface will be absorbed and reflected, but not transmitted, e.g.: brick or concrete walls.Transparent is applied to surfaces with transmissivity equal to 1. The radiation that hits the surface will be fully transmitted to the other side, e.g.: inlets, outlets or regular windows.Semi-transparent is applied to non-fully transparent surfaces. The radiation that hits the surface will be absorbed, reflected and transmitted, e.g. some stained glass windows."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GREYBODY_DIFFUSIVE_RAY",
        description="Radiative behaviour of the wall. The Kirchhoff's law of thermal radiation is applied in all options. This means that the absorptivity of the surface is equal to its emissivity.  Opaque is applied to surfaces with transmissivity equal to 0. The radiation that hits the surface will be absorbed and reflected, but not transmitted, e.g.: brick or concrete walls.Transparent is applied to surfaces with transmissivity equal to 1. The radiation that hits the surface will be fully transmitted to the other side, e.g.: inlets, outlets or regular windows.Semi-transparent is applied to non-fully transparent surfaces. The radiation that hits the surface will be absorbed, reflected and transmitted, e.g. some stained glass windows.  Schema name: GreybodyDiffusiveRayBC",
    )
    emissivity: float | None = Field(default=0.9)
    farfield_black_body_temperature: Dimensional_Temperature | None = Field(
        validation_alias="farfieldBlackBodyTemperature",
        serialization_alias="farfieldBlackBodyTemperature",
        default=None,
    )
