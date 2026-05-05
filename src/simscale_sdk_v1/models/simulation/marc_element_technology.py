from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MarcElementTechnology(SimScaleModel):
    mesh_order: Literal["FIRST", "SECOND"] | None = Field(
        validation_alias="meshOrder",
        serialization_alias="meshOrder",
        default="FIRST",
        description="Select the finite element order to be used for the mesh. Typically, a first-order mesh is sufficient for this analysis type. It utilizes advanced element formulations that prevent locking effects and poor bending behavior. In general it is advised to rather increase the mesh resolution instead of switching to second order elements for more accurate stress results.First order: Elements use linear interpolation between corner nodes, providing high computational efficiency and lower memory consumption. They are best suited for large models where complex contact situations appear and capturing stress gradients with highest precision is not the primary requirement.Second order: Elements include additional mid-side nodes to support quadratic displacement functions, improving accuracy for curved surfaces and bending-dominated loading. Solving complex contact problems might be less robust with second order elements.Note: Once the value for the mesh order is changed, an existing mesh needs to be re-computed before running the analysis, otherwise the simulation will fail with an element order mismatch error.",
    )
