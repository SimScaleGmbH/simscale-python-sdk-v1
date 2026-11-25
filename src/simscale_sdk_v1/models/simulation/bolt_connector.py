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
    """Connects parts through a virtual bolt, so the bolt and nut are not part of the CAD model. Define one bolt connector per bolt.Assign, all centred on one axis:Bolt head assignment: the faces or edges where the head sits, all on one partNut assignment: the faces or edges where the nut sits, all on one part (for a Screw, the threaded hole instead, see Bolt type)The virtual bolt is a beam between the centres of the two assignments, with the Shank diameter and Mechanical properties you enter. It can carry a preload. Learn more"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BOLT_CONNECTOR",
        description="Connects parts through a virtual bolt, so the bolt and nut are not part of the CAD model. Define one bolt connector per bolt.Assign, all centred on one axis:Bolt head assignment: the faces or edges where the head sits, all on one partNut assignment: the faces or edges where the nut sits, all on one part (for a Screw, the threaded hole instead, see Bolt type)The virtual bolt is a beam between the centres of the two assignments, with the Shank diameter and Mechanical properties you enter. It can carry a preload. Learn more  Schema name: BoltConnector",
    )
    name: str | None = Field(default=None)
    bolt_type: Literal["BOLT_AND_NUT", "SCREW"] | None = Field(
        validation_alias="boltType",
        serialization_alias="boltType",
        default="BOLT_AND_NUT",
        description="Select the type of fastener:Bolt and nut: the bolt goes through all parts. Assign where the head sits and where the nut sits.Screw: the screw ends in a threaded hole. Assign where the head sits and, as Threaded section assignment, the cylindrical face of the threaded hole.",
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
        description="Tightens the virtual bolt with a Pretension force before the loads are applied.",
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
