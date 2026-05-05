from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_connection_group_connections import (
    OneOf_MarcConnectionGroupConnections,
)


class MarcConnectionGroup(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONTACT",
        description="Schema name: MarcConnectionGroup",
    )
    friction: Literal["NO_FRICTION", "COULOMB_BILINEAR"] | None = Field(
        default="COULOMB_BILINEAR",
        description="Define how tangential forces are handled when surfaces slide against each other.No Friction: Surfaces slide freely without resistance. Use this to simplify models where friction is negligible.Coulomb - Bilinear: Surfaces resist sliding based on the normal force and the friction coefficient. This model uses a regularized &quot;bilinear&quot; transition to smooth the change from sticking to sliding, providing better numerical stability in nonlinear analyses compared to a rigid stick-slip model.",
    )
    contact_formulation: Literal["ONE_SIDED", "DOUBLE_SIDED"] | None = Field(
        validation_alias="contactFormulation",
        serialization_alias="contactFormulation",
        default="DOUBLE_SIDED",
        description="Define how to search for and enforce contact constraints between contacting bodies:Double-sided: The solver checks for penetration from Part A into Part B AND Part B into Part A. This is the most accurate method, especially for complex geometries as it minimizes contact penetrations. With this setting the &quot;Hybrid&quot; contact formulation of Marc is used.One-sided: The solver only checks if nodes of the &quot;Source&quot; surface penetrate the &quot;Target&quot; surface. The choice of Source and Master is done automatically by the solver. With this setting the &quot;Standard&quot; contact formulation of Marc is used. With this setting some small contact penetrations are expected. Refine the mesh to reduce contact penetrations.",
    )
    separation_control: Literal["AUTOMATIC", "FORCE", "STRESS"] | None = Field(
        validation_alias="separationControl",
        serialization_alias="separationControl",
        default="AUTOMATIC",
        description="Define the criteria used to determine when two surfaces in contact should be allowed to pull apart.Automatic: The solver selects the best choice between force and stress criteria, based on the mesh order and contact formulation.Force: Separation is based on the nodal contact forces.Stress: Separation is triggered when the contact stress (pressure) drops below a specific threshold (close to zero). This is the preferred method as it is less mesh dependent than the force criterion.",
    )
    connections: list[OneOf_MarcConnectionGroupConnections] | None = Field(default=None)
