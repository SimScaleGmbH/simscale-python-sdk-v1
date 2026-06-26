from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.data_reference import DataReference


class DataMappingEntry(SimScaleModel):
    data_reference: DataReference | None = Field(
        validation_alias="dataReference", serialization_alias="dataReference", default=None
    )
    operation_data_name: str | None = Field(
        validation_alias="operationDataName", serialization_alias="operationDataName", default=None
    )
    parameter_name_mapping: dict[str, str] | None = Field(
        validation_alias="parameterNameMapping", serialization_alias="parameterNameMapping", default=None
    )
