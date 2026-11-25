from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AdvancedConnectorSettings(SimScaleModel):
    assigned_face_behavior: Literal["DEFORMABLE", "UNDEFORMABLE"] | None = Field(
        validation_alias="assignedFaceBehavior",
        serialization_alias="assignedFaceBehavior",
        default="DEFORMABLE",
        description="How the assigned faces are tied to the connector:Deformable (RBE3): the faces can deform, e.g. a hole can ovalize. The connection adds no stiffness.Rigid (RBE2): the faces move as one rigid body and keep their shape. The joint is stiffer, and stresses can peak at the face edges.Note: a face can be in only one Rigid (RBE2) connection. Do not also assign it to another rigid connector, remote force, remote displacement or point mass. Learn more",
    )
