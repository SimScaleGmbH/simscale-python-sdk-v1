from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.custom_comfort_criterion_result_control import (
    CustomComfortCriterionResultControl,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_field_calculations import (
    OneOf_FluidResultControlsFieldCalculations,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_forces_moments import (
    OneOf_FluidResultControlsForcesMoments,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_result_controls_surface_data import (
    OneOf_FluidResultControlsSurfaceData,
)
from simscale_sdk_v1.models.simulation.probe_points_result_control import ProbePointsResultControl
from simscale_sdk_v1.models.simulation.scalar_transport_result_control import ScalarTransportResultControl
from simscale_sdk_v1.models.simulation.snapshot_result_control import SnapshotResultControl
from simscale_sdk_v1.models.simulation.statistical_averaging_result_control_v2 import (
    StatisticalAveragingResultControlV2,
)
from simscale_sdk_v1.models.simulation.transient_result_control import TransientResultControl


class FluidResultControls(SimScaleModel):
    custom_comfort_criteria: list[CustomComfortCriterionResultControl] | None = Field(
        validation_alias="customComfortCriteria", serialization_alias="customComfortCriteria", default=None
    )
    forces_moments: list[OneOf_FluidResultControlsForcesMoments] | None = Field(
        validation_alias="forcesMoments", serialization_alias="forcesMoments", default=None
    )
    surface_data: list[OneOf_FluidResultControlsSurfaceData] | None = Field(
        validation_alias="surfaceData", serialization_alias="surfaceData", default=None
    )
    scalar_transport: list[ScalarTransportResultControl] | None = Field(
        validation_alias="scalarTransport", serialization_alias="scalarTransport", default=None
    )
    probe_points: list[ProbePointsResultControl] | None = Field(
        validation_alias="probePoints", serialization_alias="probePoints", default=None
    )
    field_calculations: list[OneOf_FluidResultControlsFieldCalculations] | None = Field(
        validation_alias="fieldCalculations", serialization_alias="fieldCalculations", default=None
    )
    transient_result_control: TransientResultControl | None = Field(
        validation_alias="transientResultControl", serialization_alias="transientResultControl", default=None
    )
    statistical_averaging_result_control: StatisticalAveragingResultControlV2 | None = Field(
        validation_alias="statisticalAveragingResultControl",
        serialization_alias="statisticalAveragingResultControl",
        default=None,
    )
    snapshot_result_control: SnapshotResultControl | None = Field(
        validation_alias="snapshotResultControl", serialization_alias="snapshotResultControl", default=None
    )
