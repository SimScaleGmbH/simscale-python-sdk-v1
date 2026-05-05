from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_connector_settings import AdvancedConnectorSettings
from simscale_sdk_v1.models.simulation.pin_kinematic_behavior import PinKinematicBehavior
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PinConnector(SimScaleModel):
    """Connect multiple bodies via a virtual pin Usage: Define a separate pin connector item for each virtual pinAssign only cylindrical surfacesBehavior:Option to connect bodies to bodies or bodies to the ground via virtual pinsBodies freely rotate relative to one another about the virtual pin axisUsers have full control over axial translation and rotation of the connection with the ability to define torsional and axial spring stiffness"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PIN_CONNECTOR",
        description="Connect multiple bodies via a virtual pin Usage: Define a separate pin connector item for each virtual pinAssign only cylindrical surfacesBehavior:Option to connect bodies to bodies or bodies to the ground via virtual pinsBodies freely rotate relative to one another about the virtual pin axisUsers have full control over axial translation and rotation of the connection with the ability to define torsional and axial spring stiffness  Schema name: PinConnector",
    )
    name: str | None = Field(default=None)
    interaction: Literal["BODY_TO_BODY", "BODY_TO_GROUND"] | None = Field(
        default="BODY_TO_BODY",
        description="Select an interaction optionBody to body - Two or more bodies may be connected to each other via a single virtual pin. The pin will move with the bodies.Body to ground - Two or more bodies may be connected to the ground via a single virtual pin. The pin remains stationary.",
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
