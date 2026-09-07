from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField


class OutOfRangeColorOverride(SimScaleModel):
    """Out-of-range colors apply to an individual scalar, overriding what the state saved for it (including states/views with out-of-range colors switched off). This override requires the target field name. The colors are a per-scalar setting, a state can carry settings for several scalars. The target scalar can be one that has been applied to the model itself, globally, or one that was applied on a cutting plane, isosurface, isovolume or particle-trace. The override is considered valid only if the target scalar is in fact applied to either the model or a filter in the state/view, otherwise it will be rejected. This applies to automatic, manual and default states/vies."""

    scalar_field: ScalarField = Field(validation_alias="scalarField", serialization_alias="scalarField")
    below_range_color: Color | None = Field(
        validation_alias="belowRangeColor", serialization_alias="belowRangeColor", default=None
    )
    above_range_color: Color | None = Field(
        validation_alias="aboveRangeColor", serialization_alias="aboveRangeColor", default=None
    )
