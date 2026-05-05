from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ManualMeshGrading(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL",
        description="Schema name: ManualMeshGrading",
    )
    number_of_segments_per_edge: float | None = Field(
        validation_alias="numberOfSegmentsPerEdge",
        serialization_alias="numberOfSegmentsPerEdge",
        default=0.5,
        description="This value defines the minimum number of elements along a geometry edge.",
    )
    number_of_segments_per_radius: float | None = Field(
        validation_alias="numberOfSegmentsPerRadius",
        serialization_alias="numberOfSegmentsPerRadius",
        default=1.5,
        description="This value defines the minimum number of elements along a geometry radius.",
    )
    growth_rate: float | None = Field(
        validation_alias="growthRate",
        serialization_alias="growthRate",
        default=0.5,
        description="The growth rate determines how large the allowed difference in element size between neighbouring elements is. For example a value of 0.2 allows the edges of neighbouring elements to differ by 20%.If a large value is chosen, features requiring a finer mesh, like holes or fillets, will have a very local influence on the element size whereas for a small mesh grading those features will influence the element sizes in a wider area around them.Choosing a smaller value will thus lead to a higher number of elements but also result in a better overall mesh quality. The figure shows meshes for growth rate 2 (left) and 0.2 (right).",
    )
