from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class BearingLoadDistributionMarc(SimScaleModel):
    angle: float | None = Field(
        default=180,
        description="Total angle of the cylindrical face over which the load is spread. The sector is centred symmetrically on the force direction (120° = ±60°).&lt; 180°: positive clearance (loose fit)180°: half of the face in contact (default)&gt; 180°: negative clearance / interference fit, up to 360°",
    )
    profile: Literal["SINUSOIDAL", "PARABOLIC", "CUSTOM"] | None = Field(
        default="SINUSOIDAL",
        description="How the load intensity varies across the loaded sector. The peak is at the force direction and the nodal forces always sum to the force.Sinusoidal: cosine-shaped, drops smoothly to zero at the sector edges (default). Force as constant, table or formula of time.Parabolic: fuller distribution, higher load near the edges. Force as constant, table or formula of time.Custom: define the force with a formula of the angle θ and time t. θ is in radians, from −Angle/2 to +Angle/2, and is zero at the centre of the sector. It grows counterclockwise seen from the tip of the cylinder axis, which points along the global axis it is closest to (+X, +Y or +Z). The sense matters only for a profile that is not symmetric in θ. Table input is not available.",
    )
    orientation: Literal["RADIAL", "PARALLEL"] | None = Field(
        default="RADIAL",
        description="Direction of the forces applied at each node of the loaded sector. Both options produce the same resultant.Radial (default): normal to the surface, contact-like.Parallel: parallel to the force.Shown for a force along +X, angle 120°, sinusoidal profile.",
    )
    distribution: Literal["OUTWARD", "INWARD"] | None = Field(
        default="OUTWARD",
        description="Which side of the face is loaded and whether forces push away from or toward the cylinder axis. Choose based on which part you modelled.Outward (default): bore loaded by a shaft.Inward: journal loaded by a housing.Shown for a force along +X (blue). The loaded sector and nodal forces are in orange.",
    )
