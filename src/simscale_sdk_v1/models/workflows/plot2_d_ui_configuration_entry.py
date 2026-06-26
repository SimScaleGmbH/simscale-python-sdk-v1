from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class Plot2DUiConfigurationEntry(SimScaleModel):
    configuration_entry_type: str
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    data_series: Any | None = Field(
        validation_alias="dataSeries",
        serialization_alias="dataSeries",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
    groups: Any | None = Field(default=None, description="Value model for a list of values. Resolves to a JSON array.")
    name: Any | None = Field(default=None, description="Value model for a string value. Resolves to a text JSON node.")
    xaxis_label: Any | None = Field(
        validation_alias="xaxisLabel",
        serialization_alias="xaxisLabel",
        default=None,
        description="Value model for a string value. Resolves to a text JSON node.",
    )
    xaxis_scale: Any | None = Field(
        validation_alias="xaxisScale",
        serialization_alias="xaxisScale",
        default=None,
        description="Value model for an enum value. Resolves to a text JSON node.",
    )
    yaxis_label: Any | None = Field(
        validation_alias="yaxisLabel",
        serialization_alias="yaxisLabel",
        default=None,
        description="Value model for a string value. Resolves to a text JSON node.",
    )
    yaxis_scale: Any | None = Field(
        validation_alias="yaxisScale",
        serialization_alias="yaxisScale",
        default=None,
        description="Value model for an enum value. Resolves to a text JSON node.",
    )
