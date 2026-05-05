from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FixedSubdivision(SimScaleModel):
    num_subdivisions: int | None = Field(
        validation_alias="numSubdivisions",
        serialization_alias="numSubdivisions",
        default=4,
        description="Define the number of equal subdivisions of a time step in case of an adaptation event.",
    )
    max_subdivision_depth: int | None = Field(
        validation_alias="maxSubdivisionDepth",
        serialization_alias="maxSubdivisionDepth",
        default=3,
        description="Define maximum depth of the timestep subdivisions. If this value is exceeded the computation will stop. Example: If this value is set to 3, the number of subdivisions to 2 and the initial time step length is set to 1 sec, than the maximum depth is reached after 3 consecutive subdivisions (e.g. a time step of 1/8 sec based on 1.(1/2)3).",
    )
