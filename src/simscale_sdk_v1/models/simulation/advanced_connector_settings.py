from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AdvancedConnectorSettings(SimScaleModel):
    assigned_face_behavior: Literal["DEFORMABLE", "UNDEFORMABLE"] | None = Field(
        validation_alias="assignedFaceBehavior",
        serialization_alias="assignedFaceBehavior",
        default="DEFORMABLE",
        description="Choose the deformation behavior of the assigned entity. If deformable is selected, the entity is allowed to deform without applying additional stiffness, selecting undeformable leads to a rigid entity. Learn more",
    )
