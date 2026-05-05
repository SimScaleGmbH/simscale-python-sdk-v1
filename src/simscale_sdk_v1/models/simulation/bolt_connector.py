from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_connector_settings import AdvancedConnectorSettings
from simscale_sdk_v1.models.simulation.bolt_mechanical_properties import BoltMechanicalProperties
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.force_preload import ForcePreload
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class BoltConnector(SimScaleModel):
    """Connect multiple bodies via a virtual bolt Usage: Define a separate bolt connector item for each virtual boltAssign entities must be coaxialBehavior:Bolt connectors mimic physical bolts using beam formulations. Relative translations and rotations of the connected entities are computed based on the defined bolt mechanical propertiesAbility to apply preload"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BOLT_CONNECTOR",
        description="Connect multiple bodies via a virtual bolt Usage: Define a separate bolt connector item for each virtual boltAssign entities must be coaxialBehavior:Bolt connectors mimic physical bolts using beam formulations. Relative translations and rotations of the connected entities are computed based on the defined bolt mechanical propertiesAbility to apply preload  Schema name: BoltConnector",
    )
    name: str | None = Field(default=None)
    bolt_type: Literal["BOLT_AND_NUT", "SCREW"] | None = Field(
        validation_alias="boltType",
        serialization_alias="boltType",
        default="BOLT_AND_NUT",
        description="Select your desired type of fastenerBolt and nut - a virtual connection between a bolt head and nut locationScrew - a virtual connection between a screw head location and a cylindrical surface representing a threaded section",
    )
    shank_diameter: Dimensional_Length | None = Field(
        validation_alias="shankDiameter", serialization_alias="shankDiameter", default=None
    )
    mechanical_properties: BoltMechanicalProperties | None = Field(
        validation_alias="mechanicalProperties", serialization_alias="mechanicalProperties", default=None
    )
    enable_bolt_preload: bool | None = Field(
        validation_alias="enableBoltPreload",
        serialization_alias="enableBoltPreload",
        default=False,
        description="Enable the definition of pretension within the virtual bolt.",
    )
    preload: ForcePreload | None = Field(default=None)
    advanced_bolt_settings: AdvancedConnectorSettings | None = Field(
        validation_alias="advancedBoltSettings", serialization_alias="advancedBoltSettings", default=None
    )
    master_topological_reference: TopologicalReference | None = Field(
        validation_alias="masterTopologicalReference", serialization_alias="masterTopologicalReference", default=None
    )
    slave_topological_reference: TopologicalReference | None = Field(
        validation_alias="slaveTopologicalReference", serialization_alias="slaveTopologicalReference", default=None
    )
