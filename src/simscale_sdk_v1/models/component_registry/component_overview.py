from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ComponentOverview(SimScaleModel):
    """Read projection of a component, enriched with the display name taken from the latest non-archived version. Returned by endpoints that exist to display components (the listing endpoint and the single-component fetch); write/state-transition endpoints return `ComponentMetadata`."""

    component_reference: str | None = Field(
        validation_alias="componentReference",
        serialization_alias="componentReference",
        default=None,
        description="Reference to a component.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  The fully qualified reference of a component follows the following syntax: `[component_group]:[component]`.",
    )
    component_type: (
        Literal["DATA_TYPE", "METHOD", "WORKFLOW_TYPE", "PHYSICS_AI_MODEL", "ENGINEERING_AI_AGENT"] | None
    ) = Field(validation_alias="componentType", serialization_alias="componentType", default=None)
    name: str | None = Field(default=None)
    state: Literal["ACTIVE", "ARCHIVED"] | None = Field(default=None, description="Possible states of a component.")
