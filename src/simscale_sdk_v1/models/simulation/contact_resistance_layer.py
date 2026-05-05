from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__contact_resistance_layer_interface_thermal import (
    OneOf_ContactResistanceLayerInterfaceThermal,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ContactResistanceLayer(SimScaleModel):
    """Choose the type of the contact resistance:To specify presence of thin layers with known thermal conductivity or/and electric resistivity and thickness, choose Thin layer resistance.If the thermal/electric contact resistance is known (e.g. due to an imperfectly matching interface, choose Contact resistance. The resistance can be defined as surface-dependent or not, i.e. total or specific. To make a resistance inactive, set it to 0. Enter a high value to make it an isolator.Conversely, if the thermal/electric contact conductance is known, choose Specific conductanceLearn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONTACT_RESISTANCE_LAYER",
        description="Choose the type of the contact resistance:To specify presence of thin layers with known thermal conductivity or/and electric resistivity and thickness, choose Thin layer resistance.If the thermal/electric contact resistance is known (e.g. due to an imperfectly matching interface, choose Contact resistance. The resistance can be defined as surface-dependent or not, i.e. total or specific. To make a resistance inactive, set it to 0. Enter a high value to make it an isolator.Conversely, if the thermal/electric contact conductance is known, choose Specific conductanceLearn more.  Schema name: ContactResistanceLayer",
    )
    name: str | None = Field(default=None)
    interface_thermal: OneOf_ContactResistanceLayerInterfaceThermal | None = Field(
        validation_alias="interfaceThermal", serialization_alias="interfaceThermal", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
