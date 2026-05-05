from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.opacity import Opacity
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.vector_field import VectorField


class IsoSurface(SimScaleModel):
    iso_scalar: ScalarField | None = Field(validation_alias="isoScalar", serialization_alias="isoScalar", default=None)
    iso_value: float | None = Field(
        validation_alias="isoValue",
        serialization_alias="isoValue",
        default=None,
        description="The iso scalar value. Should be within the selected scalar range. Default value is the average between the min and max in the range.",
    )
    scalar_field: ScalarField | None = Field(
        validation_alias="scalarField", serialization_alias="scalarField", default=None
    )
    solid_color: Color | None = Field(validation_alias="solidColor", serialization_alias="solidColor", default=None)
    vector_field: VectorField | None = Field(
        validation_alias="vectorField", serialization_alias="vectorField", default=None
    )
    opacity: Opacity | None = Field(default=None)
