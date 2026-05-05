from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__contact_resistance import Dimensional_ContactResistance
from simscale_sdk_v1.models.simulation.dimensional__power import Dimensional_Power
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class StarThermalResistanceNetwork(SimScaleModel):
    """A Thermal Resistance Network can be used to approximate the effect of heat sources and heat transfer from that source to the surrounding domain without resolving the source geometry.  Select the top face of the body you want to assign. The models for Thermal resistance network are as follows:Star Network Resistance Model: defines a thermal resistance network consisting out of a top, a board, a board to interface and four side resistances. A power source is assigned to the body.Two resistor Model: defines a thermal resistance network consisting out of a top, a board and a board to interface resistance. A power source is assigned to the body.  Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STAR_NETWORK",
        description="A Thermal Resistance Network can be used to approximate the effect of heat sources and heat transfer from that source to the surrounding domain without resolving the source geometry.  Select the top face of the body you want to assign. The models for Thermal resistance network are as follows:Star Network Resistance Model: defines a thermal resistance network consisting out of a top, a board, a board to interface and four side resistances. A power source is assigned to the body.Two resistor Model: defines a thermal resistance network consisting out of a top, a board and a board to interface resistance. A power source is assigned to the body.  Learn more.  Schema name: StarThermalResistanceNetwork",
    )
    name: str | None = Field(default=None)
    resistance_top: Dimensional_ContactResistance | None = Field(
        validation_alias="resistanceTop", serialization_alias="resistanceTop", default=None
    )
    resistance_bottom: Dimensional_ContactResistance | None = Field(
        validation_alias="resistanceBottom", serialization_alias="resistanceBottom", default=None
    )
    resistance_sides: Dimensional_ContactResistance | None = Field(
        validation_alias="resistanceSides", serialization_alias="resistanceSides", default=None
    )
    resistance_interface: Dimensional_ContactResistance | None = Field(
        validation_alias="resistanceInterface", serialization_alias="resistanceInterface", default=None
    )
    network_power: Dimensional_Power | None = Field(
        validation_alias="networkPower", serialization_alias="networkPower", default=None
    )
    emissivity: float | None = Field(default=0.9)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
