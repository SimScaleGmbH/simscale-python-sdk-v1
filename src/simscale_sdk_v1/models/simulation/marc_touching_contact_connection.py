from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.interference_fit import InterferenceFit
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class MarcTouchingContactConnection(SimScaleModel):
    """Define the physical nature of the connection between bodies.Glued: Parts are permanently bonded. No sliding or separation is allowed. Interfaces are treated as a continuous material transition.Note: Parts that are initially separated but come into contact during deformation will also be glued together locally once contact is established.Touching: Parts can slide and separate but cannot penetrate each other. Friction coefficients apply here.Glued + Touching: Use this for bodies which have both contact areas which behave glued and others which should be modeled as touching. Use the &quot;touching faces&quot; to define faces which should exhibit a &quot;touching&quot; behavior during contact.Note: Self-contact can be modeled by assigning a single volume to a contact definition."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOUCHING",
        description="Define the physical nature of the connection between bodies.Glued: Parts are permanently bonded. No sliding or separation is allowed. Interfaces are treated as a continuous material transition.Note: Parts that are initially separated but come into contact during deformation will also be glued together locally once contact is established.Touching: Parts can slide and separate but cannot penetrate each other. Friction coefficients apply here.Glued + Touching: Use this for bodies which have both contact areas which behave glued and others which should be modeled as touching. Use the &quot;touching faces&quot; to define faces which should exhibit a &quot;touching&quot; behavior during contact.Note: Self-contact can be modeled by assigning a single volume to a contact definition.  Schema name: MarcTouchingContactConnection",
    )
    name: str | None = Field(default=None)
    friction_coefficient: float | None = Field(
        validation_alias="frictionCoefficient",
        serialization_alias="frictionCoefficient",
        default=0.0,
        description="The Friction coefficient (&mu;) defines the proportionality between the normal contact force and the maximum allowable tangential resistance at the interface. A value of 0 represents a frictionless (lubricated) surface, while higher values increase the resistance to relative sliding between the two parts. For most metal-to-metal or metal-to-plastic contacts, values typically range between 0.1 and 0.4.",
    )
    interference_fit: InterferenceFit | None = Field(
        validation_alias="interferenceFit", serialization_alias="interferenceFit", default=None
    )
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    contact_bodies: TopologicalReference | None = Field(
        validation_alias="contactBodies", serialization_alias="contactBodies", default=None
    )
