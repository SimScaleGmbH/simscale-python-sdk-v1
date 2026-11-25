from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_connector_settings import AdvancedConnectorSettings
from simscale_sdk_v1.models.simulation.pin_kinematic_behavior import PinKinematicBehavior
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PinConnector(SimScaleModel):
    """Connects parts through a virtual pin, so the pin itself is not modelled. Define one pin connector per pin.Assign the cylindrical hole faces of all parts the pin goes through:all faces on one common axis: no flat faces, no holes of another pineach face in one connector onlyBehavior: the parts turn about the pin axis but cannot tilt against each other. The virtual pin is rigid in bending and has no material or diameter. Set rotation and sliding under Kinematic behavior. Learn more"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PIN_CONNECTOR",
        description="Connects parts through a virtual pin, so the pin itself is not modelled. Define one pin connector per pin.Assign the cylindrical hole faces of all parts the pin goes through:all faces on one common axis: no flat faces, no holes of another pineach face in one connector onlyBehavior: the parts turn about the pin axis but cannot tilt against each other. The virtual pin is rigid in bending and has no material or diameter. Set rotation and sliding under Kinematic behavior. Learn more  Schema name: PinConnector",
    )
    name: str | None = Field(default=None)
    interaction: Literal["BODY_TO_BODY", "BODY_TO_GROUND"] | None = Field(
        default="BODY_TO_BODY",
        description="Choose what the pin connects:Body to body: two or more parts are connected to each other. The pin moves with the parts.Body to ground: one or more parts are connected to a pin that is fixed in space, like a hinge support.",
    )
    kinematic_behavior: PinKinematicBehavior | None = Field(
        validation_alias="kinematicBehavior", serialization_alias="kinematicBehavior", default=None
    )
    advanced_pin_settings: AdvancedConnectorSettings | None = Field(
        validation_alias="advancedPinSettings", serialization_alias="advancedPinSettings", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
