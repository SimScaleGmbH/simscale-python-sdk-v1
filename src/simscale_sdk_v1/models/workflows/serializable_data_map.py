from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.parameter_value_combination import ParameterValueCombination


class SerializableDataMap(SimScaleModel):
    """Data map provides the mapping of each data - according to the data interface of a method or a workflow - and each parameter value combination to the data identifiers."""

    data_by_name_and_parameter_value_combination_id: dict[str, dict[str, str]] | None = Field(
        validation_alias="dataByNameAndParameterValueCombinationId",
        serialization_alias="dataByNameAndParameterValueCombinationId",
        default=None,
    )
    parameter_value_combinations_by_id: dict[str, ParameterValueCombination] | None = Field(
        validation_alias="parameterValueCombinationsById",
        serialization_alias="parameterValueCombinationsById",
        default=None,
    )
